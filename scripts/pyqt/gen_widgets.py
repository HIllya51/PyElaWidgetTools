import sys, os, re

os.chdir(os.path.dirname(os.path.abspath(__file__)))
forQt5 = len(sys.argv) >= 2 and int(sys.argv[1])

eladir = "../../ElaWidgetTools/ElaWidgetTools"


def parse_parameters(param_str):
    params = []
    if not param_str.strip():
        return params

    # This is a simplified parser. C++ parameter parsing can be complex.
    # It handles basic cases like "type name", "type name = default_value"
    # It does NOT handle function pointers, complex templates well without more rules.
    # Split by comma, but be careful about commas in template arguments or default values
    # This regex tries to split by comma not inside parentheses (for default args like constructors)
    # or angle brackets (for templates)
    raw_params = re.split(r",(?![^<]*>)(?![^\(]*\))", param_str)

    for p_orig in raw_params:
        p = p_orig.strip()
        if not p:
            continue

        default_value = None
        if "=" in p:
            param_def, default_value_str = p.split("=", 1)
            param_def = param_def.strip()
            default_value = default_value_str.strip()
        else:
            param_def = p

        # Try to get type and name (handles pointers and references somewhat)
        # Order of matching matters: *& (ref to pointer) then * then &
        match_ref_ptr = re.match(
            r"(.+?\S)\s*([*&])\s*([*&]?)\s*(\w+)$", param_def
        )  # e.g. const QString & name
        match_ptr_ref = re.match(
            r"(.+?\S)\s*([*&])\s*(\w+)$", param_def
        )  # e.g. QWidget * parent
        match_simple = re.match(r"(.+?\S)\s+(\w+)$", param_def)  # e.g. int value

        param_type = ""
        param_name = ""

        if match_ref_ptr:
            param_type = f"{match_ref_ptr.group(1).strip()} {match_ref_ptr.group(2)}{match_ref_ptr.group(3)}".strip()
            param_name = match_ref_ptr.group(4)
        elif match_ptr_ref:
            param_type = (
                f"{match_ptr_ref.group(1).strip()} {match_ptr_ref.group(2)}".strip()
            )
            param_name = match_ptr_ref.group(3)
        elif match_simple:
            param_type = match_simple.group(1).strip()
            param_name = match_simple.group(2)
        else:  # Fallback for simple type without name (unlikely in methods) or very complex
            param_type = param_def.strip()  # Might be just the type for unnamed params
            param_name = f"arg{len(params) + 1}"  # Placeholder name

        sip_param_type = param_type

        # Heuristic for /TransferThisPointer/ for QWidget* parent
        transfer_this = (
            "/TransferThisPointer/"
            if "QWidget*" in param_type and "parent" in param_name.lower()
            else ""
        )

        # Handle out-parameters (like QString& key)
        if param_type.endswith("&") and not param_type.startswith("const"):
            annotation = "/Out/"
            # For QString&, SIP often uses /PyName=.../ to return it as a tuple element
            # params.append(f"{sip_param_type} {param_name} {annotation} /PyName={param_name}_out/")
            # Simpler: just mark as /Out/ and SIP will handle it as a modifiable argument
            params.append(
                f"{sip_param_type} {param_name} {annotation} {transfer_this}".strip()
            )
        else:
            param_list_entry = f"{sip_param_type} {param_name} {transfer_this}".strip()
            if default_value is not None:
                # SIP default values often need to be C++ literals
                param_list_entry += f" = {default_value}"
            params.append(param_list_entry)
    return params


def generate_sip_for_class_2(header_content, filename=""):
    sip_lines = []

    is_singleton = "Q_SINGLETON_CREATE_H" in header_content

    # Extract class name (works for Q_OBJECT or plain classes)
    class_match = re.search(
        r"class\s+(?:ELA_EXPORT\s+)?(\w+)\s*(?::\s*public\s+[\w:]+)?", header_content
    )
    if not class_match:
        print(f"Error: Could not find class name in {filename}")
        return None
    class_name = class_match.group(1)

    # Determine base class if any
    base_class_match = re.search(
        r"class\s+(?:ELA_EXPORT\s+)?\w+\s*:\s*public\s+([\w:]+)", header_content
    )
    base_class_name = base_class_match.group(1) if base_class_match else None

    if base_class_name:
        sip_lines.append(f"class {class_name} : public {base_class_name}\n{{")
    else:
        sip_lines.append(f"class {class_name}\n{{")

    sip_lines.append("%TypeHeaderCode")
    sip_lines.append(f'#include "{os.path.basename(filename)}"')
    # If singleton implies a static getInstance(), its definition needs to be available
    # This is often in the .cpp file, but the header is enough for SIP declaration
    sip_lines.append("%End\n")

    if is_singleton:
        sip_lines.append("private:")  # Hide constructor for singletons
        sip_lines.append(
            f"    explicit {class_name}(); // Private constructor, not for Python use"
        )
        sip_lines.append(
            f"    ~ {class_name}(); // Private constructor, not for Python use"
        )
        sip_lines.append("")
        sip_lines.append("public:")
        # Assume getInstance() exists. Modify if your macro creates a different name.
        # The return type might be ElaIcon* or ElaIcon&.
        # If it's ElaIcon&, SIP might need / వ‌Reference/ or careful handling.
        # For ElaIcon*, SIP handles pointer ownership well if getInstance returns a persistent singleton.
        sip_lines.append(f"    static {class_name}* getInstance();")
        #  sip_lines.append(f"    %StaticMetatype") # Important for QObject-less singletons with static methods in Python
        sip_lines.append("")

    # --- Methods ---
    # Process content between class { ... };
    class_body_content_match = re.search(
        r"class\s+.*?\w+\s*\{([\s\S]*)\};", header_content, re.DOTALL
    )
    if not class_body_content_match:
        print(f"Error: Could not extract class body from {filename}")
        return None

    class_body_content = class_body_content_match.group(1)

    constructor_destructor_pattern = re.compile(
        r"^\s*(Q_INVOKABLE)?\s*(explicit\s+|virtual\s+)?\s*"
        r"(~?%s)\s*"  # Class name, possibly with ~
        r"\(([^)]*)\)\s*(override)?\s*;" % class_name,
        re.MULTILINE,
    )

    current_access = "private"  # Default in C++ if no specifier
    # Split by access specifiers
    sections = re.split(r"(public:|protected:|private:)", class_body_content)

    processed_methods_for_access_section = set()

    # Iterate through sections (specifier, code, specifier, code, ...)
    # Handle the case where the first block of code has no explicit specifier (defaults to private)
    if not sections[0].strip() and len(sections) > 1 and not sections[1].endswith(":"):
        first_block = sections[0]
        # process this first_block as private

    # Start iterating from the first actual specifier or the beginning if no specifiers found
    idx = 0
    if (
        not sections[0].strip() and len(sections) > 1 and sections[1].endswith(":")
    ):  # typical case
        idx = 1
    elif not sections[0].endswith(":"):  # Content before any explicit specifier
        # This content is considered private by default in C++
        # For ElaIcon, constructor/destructor are here
        code_block = sections[0]
        access_specifier_sip = "private:"  # It's private
        if (
            not is_singleton
        ):  # For non-singletons, private members are not usually bound
            pass  # sip_lines.append(access_specifier_sip)

        # Constructors/Destructors in this "default private" block
        for match in constructor_destructor_pattern.finditer(code_block):
            Q_INVOKABLE = ""  # match.group(1) or ""
            # For ElaIcon (singleton), these are private and we've handled the constructor above
            if is_singleton and match.group(3) == f"{class_name}":
                # sip_lines.append(f"  {class_name}(); // Already handled as private for singleton")
                processed_methods_for_access_section.add(
                    f"{Q_INVOKABLE} {match.group(3)}({match.group(4)})"
                )
                continue
            if is_singleton and match.group(3) == f"~{class_name}":
                # sip_lines.append(f"  ~{class_name}(); // Private destructor")
                processed_methods_for_access_section.add(
                    f"{match.group(3)}({match.group(4)})"
                )
                continue
            # ... (logic for non-singleton private constructors if needed)

        idx = 1  # Move to the next part which should be a specifier

    while idx < len(sections):
        current_access = sections[idx].strip()  # public:, protected:, private:
        sip_lines.append(current_access)
        processed_methods_for_access_section.clear()

        code_block = sections[idx + 1] if (idx + 1) < len(sections) else ""

        # Constructors/Destructors
        for match in constructor_destructor_pattern.finditer(code_block):
            method_key = f"{match.group(3)}({match.group(4)})"
            if method_key in processed_methods_for_access_section:
                continue
            processed_methods_for_access_section.add(method_key)

            if (
                is_singleton and match.group(3) == f"{class_name}"
            ):  # If somehow a public ctor in a singleton
                sip_lines.append(
                    f"  // Public constructor for singleton? Unusual. getInstance() is preferred."
                )
                continue  # getInstance is the way
            if is_singleton and match.group(3) == f"~{class_name}":
                sip_lines.append(f"  // Public destructor for singleton? Unusual.")
                continue

            explicit_kw = match.group(2) or ""
            name = match.group(3)  # ~ClassName or ClassName
            params_str = match.group(4)
            parsed_params = parse_parameters(params_str)
            sip_lines.append(f"  {explicit_kw}{name}({', '.join(parsed_params)});")

        # Regular methods
        # Using a simpler regex for methods within known access blocks
        method_pattern_simple = re.compile(
            r"^\s*(virtual\s+)?([\w\s:*&<>~]+?)\s+"  # virtual, return type
            r"(\b\w+)\s*"  # method name
            r"\(([^)]*)\)"  # parameters
            r"(\s*const)?(\s*override|\s*final|\s*=\s*0)?\s*;",
            re.MULTILINE,
        )
        for match in method_pattern_simple.finditer(code_block):
            method_name = match.group(3)
            params_str_for_key = match.group(4)
            method_key = f"{method_name}({params_str_for_key})"  # Create a key to avoid duplicates

            # Skip if it's a constructor/destructor already handled by the more specific pattern
            if method_name == class_name or method_name == f"~{class_name}":
                continue
            if method_key in processed_methods_for_access_section:
                continue
            processed_methods_for_access_section.add(method_key)

            virtual_kw = match.group(1) or ""
            return_type_raw = match.group(2).strip()
            params_str = match.group(4)
            const_kw = match.group(5) or ""

            sip_return_type = return_type_raw
            parsed_params = parse_parameters(params_str)

            sip_lines.append(
                f"  {virtual_kw}{sip_return_type} {method_name}({', '.join(parsed_params)}){const_kw};"
            )

        sip_lines.append("")
        idx += 2

    # --- Signals (if any, not in ElaIcon) ---
    # (Signal parsing logic from previous script can be added here if needed)

    sip_lines.append("};")
    return "\n".join(
        s for s in sip_lines if s.strip()
    )  # Remove empty lines from list before joining


def generate_sip_for_class(header_content, filename):

    # Extract class name and base class
    class_match = re.findall(
        r"(class\s+ELA_EXPORT\s+?\w+\s*:\s*public\s+\w+[\s\S]*?\};)",
        header_content,
        re.MULTILINE,
    )
    if len(class_match) > 1:
        # print("class_match", class_match)
        return "\n".join(generate_sip_for_class__1(_, filename) for _ in class_match)
    return generate_sip_for_class__1(header_content, filename)


def generate_sip_for_class__1(header_content, filename=""):
    sip_lines = []
    classmethods = {}
    # Extract class name and base class
    class_match = re.search(
        r"class\s+(ELA_EXPORT\s+)?(\w+)\s*:\s*public\s+(\w+)", header_content
    )
    if not class_match:
        return generate_sip_for_class_2(header_content, filename=filename)

    class_name = class_match.group(2)
    base_class_name = class_match.group(3)
    sip_lines.append(f"class {class_name} : public {base_class_name}\n{{")
    sip_lines.append("%TypeHeaderCode")
    sip_lines.append(f'#include "ElaDef.h"')
    sip_lines.append(f'#include "{os.path.basename(filename)}"')
    sip_lines.append("%End\n")

    # --- Properties ---
    # Q_PROPERTY_CREATE_Q_H(type, Name)
    # Assumes getter: Name() or isName() for bool, Setter: setName(type)
    for pt in ("Q_PROPERTY_CREATE", "Q_PROPERTY_CREATE_Q_H"):
        prop_pattern = re.compile(rf"{pt}\((.*?),\s*(\w+)\)")
        has_public_section_for_props = False  # To add "public:" if props are first

        for match in prop_pattern.finditer(header_content):
            if not has_public_section_for_props:
                # Properties are usually public in SIP even if members are private
                # sip_lines.append("public:") # Not strictly needed for %Property
                has_public_section_for_props = True

            prop_type_raw = match.group(1).strip()
            prop_name = match.group(2)

            sip_prop_type = prop_type_raw

            # Determine getter/setter names based on convention
            getter_name = f"get{prop_name}"
            setter_name = f"set{prop_name}"

            # Check if these methods actually exist as public methods later
            # For now, assume they follow the macro's convention
            # sip_lines.append(f"  // Property: {prop_name}")
            # sip_lines.append(f"  %Property({sip_prop_type} {prop_name.lower()} READ {getter_name} WRITE {setter_name})\n")
            sip_lines.append(f"public: Q_SIGNAL void p{prop_name}Changed();")
            sip_lines.append(
                f"  void {setter_name}({(prop_type_raw)} {prop_name});"
            )  # Use input version of type
            sip_lines.append(
                f"  {(prop_type_raw)} {getter_name}() const;"
            )  # Use return version

    # --- Methods ---
    # This regex is a starting point and might need refinement for complex signatures
    # It looks for lines that look like method declarations.
    # Covers: optional virtual, return_type, ClassName::(optional), method_name, (params), optional const, optional override/final
    # It tries to capture sections: public, protected, private
    current_access = "public"  # Default, Qt classes often start with public

    # Split by access specifiers to process methods within each
    # Simplification: Assumes methods are declared after Q_OBJECT, Q_Q_CREATE etc.
    # and before signals.

    # Find the content between "public:" / "protected:" / "private:" and "Q_SIGNALS:" or end of class "};"
    class_body_match = re.search(
        r"class\s+ELA_EXPORT\s+\w+\s*:\s*public\s+\w+\s*\{(.*?)(\};)",
        header_content,
        re.DOTALL,
    )
    if "Q_SINGLETON_CREATE_H" in header_content:
        sip_lines.append(f"public: static {class_name}* getInstance();")
    if class_body_match:
        body_content = class_body_match.group(1)
        body_content = "private:" + body_content
        # Method pattern: (virtual)? (return_type) (method_name) ((params)) (const)? (override|final|=0)? ;
        method_pattern = re.compile(
            r"^\s*(virtual\s+)?([\w\s:*&<>~]+?)\s+"  # virtual, return type (can be complex)
            r"(\b\w+)\s*"  # method name
            r"\(([^)]*)\)"  # parameters
            r"(\s*const)?(\s*override|\s*final|\s*=\s*0)?\s*;",  # const, override, final, pure virtual
            re.MULTILINE,
        )

        # Constructor pattern
        constructor_pattern = re.compile(
            r"^\s*(Q_INVOKABLE)?\s*(explicit\s+)?%s\s*\((.*)\)\s*(?:override)?\s*;"
            % class_name,  # Constructor specific to class_name
            re.MULTILINE,
        )
        # Destructor pattern
        destructor_pattern = re.compile(
            r"^\s*(virtual\s+)?~%s\s*\(([^)]*)\)\s*(override)?\s*;" % class_name,
            re.MULTILINE,
        )

        access_sections = re.split(r"(public:|protected:|private:)", body_content)

        active_access_specifier = (
            "private"  # Default if no specifier found before methods
        )
        # This can be improved by looking for the first one.

        for i in range(1, len(access_sections), 2):
            specifier = access_sections[i].strip()
            code_block = access_sections[i + 1]
            if not code_block.strip():
                continue

            sip_lines.append(f"{specifier}")  # public:, protected:, private:

            # Constructors
            for match in constructor_pattern.finditer(code_block):
                Q_INVOKABLE = ""  # match.group(1) or ""
                explicit_kw = match.group(2) or ""
                params_str = match.group(3)
                parsed_params = parse_parameters(params_str)
                sip_lines.append(
                    f"  {Q_INVOKABLE} {explicit_kw}{class_name}({', '.join(parsed_params)});"
                )

            # Destructor
            for match in destructor_pattern.finditer(code_block):
                virtual_kw = match.group(1) or ""
                # params_str = match.group(2) # Destructors usually have no params
                sip_lines.append(f"  {virtual_kw}~{class_name}();")

            # Regular methods
            for match in method_pattern.finditer(code_block):
                # Skip if it's a constructor/destructor already handled
                if match.group(3) == class_name or match.group(3) == f"~{class_name}":
                    continue

                virtual_kw = match.group(1) or ""
                return_type_raw = match.group(2).strip()
                if (not return_type_raw.strip()) or (return_type_raw == "Q_OBJECT"):
                    continue
                method_name = match.group(3)
                params_str = match.group(4)
                const_kw = match.group(5) or ""
                override_final_kw = (
                    match.group(6) or ""
                )  # We don't typically put override/final in SIP

                # Skip property getters/setters if we already generated them via %Property
                # (This is a basic check, might need refinement)
                is_prop_accessor = False
                for prop_match_again in prop_pattern.finditer(header_content):
                    prop_type_check = prop_match_again.group(1).strip()
                    prop_name_check = prop_match_again.group(2)
                    getter_check = (
                        f"is{prop_name_check}"
                        if prop_type_check == "bool"
                        else prop_name_check
                    )
                    setter_check = f"set{prop_name_check}"
                    if method_name == getter_check or method_name == setter_check:
                        is_prop_accessor = True
                        break
                if is_prop_accessor and any(
                    f"%Property({prop_name_check.lower()}" in line for line in sip_lines
                ):
                    # This method is likely a getter/setter for an already defined %Property
                    # Check if the declaration for it was already added above the %Property line.
                    # If a %Property exists, we assume its getter/setter are also declared for SIP
                    # and we don't need to declare them again here unless they are virtual and overridable.
                    # For simplicity here, if it's part of a property, we skip adding it again as a plain method.
                    # If it needs to be overridable and is protected/public virtual, it should be added.
                    # The Q_PROPERTY_CREATE_Q_H likely makes them public.
                    if (
                        "virtual" not in virtual_kw and specifier == "public:"
                    ):  # if its a public non-virtual accessor of a property
                        continue

                sip_return_type = return_type_raw
                parsed_params = parse_parameters(params_str)
                PyName = ""
                if ("takeOverNativeEvent" == method_name) and (sys.platform != "win32"):
                    continue
                elif method_name == "addPageNode" and "keyPoints" in params_str:
                    print(match.groups())
                    PyName = f"/PyName={method_name}KeyPoints/"
                else:
                    classmethods[method_name] = 1
                method_line = f"  {virtual_kw}{sip_return_type} {method_name}({', '.join(parsed_params)}){const_kw} {PyName};"

                # Handle known out parameters like QString& for keys
                # Example: ElaNavigationType::NodeOperateReturnType addExpanderNode(QString expanderTitle, QString& expanderKey, ...)
                # The parse_parameters function now adds /Out/.
                # If a method returns a type AND has /Out/ params, Python might see a tuple.
                # SIP handles this, e.g., (return_value, out_param1, out_param2)

                sip_lines.append(method_line)
            sip_lines.append("")

    sip_lines.append("};")
    return "\n".join(sip_lines)


def parseshitelasuggestbox(content):

    x = re.search(r"struct ELA_EXPORT SuggestData \{[\s\S]*?\};", content)

    klass = content.find("class")
    content = content.replace(x.group(), "")
    content = content[:klass] + x.group() + "\n" + content[klass:]
    return content


def parseshitelasuggestbox2(sip_class_def: str):
    extra = r"""struct SuggestData {
    public:
        explicit SuggestData();
        explicit SuggestData(ElaIconType::IconName icon, const QString& suggestText, const QVariantMap& suggestData = {});
        ~SuggestData();
    };"""

    idx = sip_class_def.rfind("public:\n") + 8
    sip_class_def = sip_class_def[:idx] + "\n" + extra + "\n" + sip_class_def[idx:]
    return sip_class_def


def cast_h_to_sip(filename):
    filename = os.path.splitext(os.path.basename(filename))[0]
    input_header_file = f"{eladir}/{filename}.h"
    output_sip_file = f"sip/{filename}.sip"

    with open(input_header_file, "r", encoding="utf-8") as f:
        content = f.read()
    if filename == "ElaSuggestBox":
        content = parseshitelasuggestbox(content)

    # A common pattern is to have a main .sip file that includes others.
    # This script generates the content for a single class.
    # You'd typically wrap this with %Module, %Import, etc.
    content = content.replace(
        "Q_TAKEOVER_NATIVEEVENT_H",
        f"virtual bool nativeEvent(const QByteArray& eventType, void* message, {('qintptr','long')[forQt5]}* result) override;",
    )
    sip_class_def = generate_sip_for_class(content, input_header_file)

    if not sip_class_def:
        return

    if filename == "ElaSuggestBox":
        sip_class_def = parseshitelasuggestbox2(sip_class_def)

    full_sip_content = []
    # Add necessary imports based on base class and parameter types
    # This is a basic set, might need to be smarter
    full_sip_content.append("%Import QtCore/QtCoremod.sip")
    full_sip_content.append("%Import QtGui/QtGuimod.sip")
    full_sip_content.append("%Import QtWidgets/QtWidgetsmod.sip")
    full_sip_content.append("")
    full_sip_content.append(sip_class_def)
    final_output = "\n".join(full_sip_content)
    ls = final_output.splitlines()
    #ls = [_ for _ in ls if "QVector" not in _]  # 不支持的类型转换
    ls = [_ for _ in ls if "QList<QVariantMap>" not in _]  # 不支持的类型转换
    bad = ("long *", "qintptr *")[forQt5]
    ls = [_ for _ in ls if bad not in _]  # 这个是Qt5的条件编译，Qt6的话要删掉另一条

    final_output = "\n".join(ls)

    with open(output_sip_file, "w", encoding="utf-8") as f:
        f.write(final_output)


allfiles = []

for f in os.listdir(eladir):
    if f.startswith("ElaDef"):
        continue
    if f.startswith("ElaProperty"):
        continue
    if f.startswith("ElaSingleton"):
        continue
    if f.startswith("ElaDxgiManager") and (sys.platform != "win32"):
        continue
    if f.startswith("Ela") and f.endswith(".h"):
        cast_h_to_sip(f)
        allfiles.append(f"%Include {os.path.basename(f).split('.')[0]}.sip")

with open("sip/ElaWidgetTools.sip", "w", encoding="utf-8") as f:
    __ = "\n".join(allfiles)
    f.write(
        rf"""%Module(name=ElaWidgetTools, use_limited_api=True)

%Include ElaDef.sip
{__}

"""
    )
