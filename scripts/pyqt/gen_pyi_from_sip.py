import re, sys
from pathlib import Path
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# --- Type Mapping (C++ to Python) ---
# This can be expanded
TYPE_MAP = {
    "void": "None",
    "QString": "str",
    "bool": "bool",
    "int": "int",
    "double": "float",
    "QWidget*": "QWidget",
    "QMainWindow*": "QMainWindow",
    "QPixmap": "QPixmap",
    # Add more mappings as needed
    # For namespace::type, we'll try to convert :: to .
}


# --- Helper Functions ---
def sip_to_python_type(sip_type, current_namespace_context=None):
    sip_type = sip_type.strip()
    # Handle pointers and references by removing them for type hint
    sip_type = sip_type.replace("*", "").replace("&", "").strip()
    mapstring = {
        "const": "",
        "virtual": "",
        "Q_SLOT": "",
        "QStringList": "List[str]",
        "public:": "",
        "static": "",
        "QList<int>": "List[int]",
        "void": "None",
        "QString": "str",
        "qreal": "float",
        "quint32": "int",
        "quint16": "int",
        "uint": "int",
        "qintptr": "int",
        "QVariantMap": "map",
    }
    sip_type = " ".join(mapstring.get(_, _) for _ in sip_type.split(" "))
    if sip_type in TYPE_MAP:
        return TYPE_MAP[sip_type]

    # Handle Namespace::Type -> Namespace.Type
    if "::" in sip_type:
        parts = sip_type.split("::")
        # If the first part is a known namespace being processed,
        # it might be an inner type.
        # Otherwise, assume it's a fully qualified type.
        return ".".join(parts)

    # If it's a known Qt class without module, add it
    qt_classes = [
        "QWidget",
        "QMainWindow",
        "QPixmap",
        "QFlags",
    ]  # Add more common Qt classes
    if sip_type in qt_classes:
        return sip_type  # Assumes it's imported

    # Default: use the type as is, or Any if unsure
    return sip_type  # Could be 'Any' as a fallback: 'typing.Any'


def parse_parameters(param_str, current_namespace_context):
    params = []
    py_params = []
    out_params_types = []

    if not param_str.strip():
        return [], []

    param_list = list(_.strip() for _ in param_str.split(","))
    # print(param_list)
    for p_full in param_list:
        p_full = p_full.strip()
        is_out_param = "/Out/" in p_full
        p_full = p_full.replace("/Out/", "").strip()

        _, default_value = (p_full + "=").split("=")[:2]
        default_value = default_value.strip()
        _ = _.strip()
        param_type_str = " ".join(_.split(" ")[:-1])
        param_name = _.split(" ")[-1]

        # param_type_str, param_name, default_value = match.groups()

        py_type = sip_to_python_type(param_type_str, current_namespace_context)

        if is_out_param:
            out_params_types.append(py_type)
        else:
            param_def = f"{param_name}: {py_type}"
            if default_value:
                # Try to pythonify default value (e.g. ElaIconType::None -> ElaIconType.IconName.None)
                # This is heuristic. Assumes EnumName::Member maps to EnumName.Member
                # And that 'None' is a member name if path is ElaIconType::None.
                # A more robust way would be to know ElaIconType is a namespace and 'None' is in IconName enum.
                # For now, just replace :: with .
                default_value = default_value.replace("::", ".")
                if default_value == "nullptr":
                    default_value = "None"
                if default_value == "true":
                    default_value = "True"
                if default_value == "false":
                    default_value = "False"

                param_def += f" = {default_value}"
            py_params.append(param_def)
    # print(py_params, out_params_types)
    return py_params, out_params_types


def generate_pyi(sip_content):
    pyi_lines = []

    # State variables
    current_indent = ""
    in_namespace = False
    current_namespace_name = None
    in_class = False
    current_class_name = None
    in_enum = False

    lines = sip_content.splitlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1

        if (
            not line
            or line.startswith("//")
            or line.startswith("%Import")
            or line.startswith("%Include")
        ):
            continue

        if line.startswith("%TypeHeaderCode"):
            while i < len(lines) and not lines[i].strip().startswith("%End"):
                i += 1
            if i < len(lines) and lines[i].strip().startswith("%End"):
                i += 1
            continue

        # Namespace
        match_namespace_start = re.match(r"namespace\s+(\w+)", line)
        if match_namespace_start:
            current_namespace_name = match_namespace_start.group(1)
            pyi_lines.append(f"{current_indent}class {current_namespace_name}:")
            current_indent += "    "
            in_namespace = True
            continue

        if line.startswith("}; // namespace") and in_namespace:
            current_indent = current_indent[:-4]
            pyi_lines.append("")  # Add a blank line after namespace
            in_namespace = False
            current_namespace_name = None
            continue

        # Enum
        match_enum_start = re.match(r"enum\s+(\w+)", line)
        if match_enum_start:
            enum_name = match_enum_start.group(1)
            pyi_lines.append(f"{current_indent}class {enum_name}(IntEnum):")
            current_indent += "    "
            in_enum = True
            continue

        if line.startswith("};") and in_enum:
            current_indent = current_indent[:-4]
            in_enum = False
            pyi_lines.append("")  # Add a blank line after enum
            continue

        if in_enum:
            # Enum members: Name = Value,
            enum_member_match = re.match(r"(\w+)\s*=\s*(0x[0-9a-fA-F]+|\d+)\s*,?", line)
            if enum_member_match:
                name, value = enum_member_match.groups()
                if name == "None":
                    name = "None_"
                pyi_lines.append(f"{current_indent}{name} = {value}")
            elif line.strip() and not line.startswith(
                "};"
            ):  # Handle member without explicit value (if SIP allows)
                if line.startswith("{"):
                    continue
                pyi_lines.append(
                    f"{current_indent}{line.split(',')[0].strip()} = ... # type: ignore # Auto-assigned value"
                )
            continue

        # Typedef
        # typedef QFlags<ElaAppBarType::ButtonType> ButtonFlags;
        match_typedef = re.match(r"typedef\s+QFlags<([\w:]+)>\s+(\w+);", line)
        if match_typedef:
            qflags_enum_type, alias_name = match_typedef.groups()
            python_enum_type = sip_to_python_type(
                qflags_enum_type, current_namespace_name
            )
            # For QFlags, the alias often refers to the enum type itself or int
            # If ButtonType is an IntFlag, then ButtonFlags = ButtonType is good.
            # For simplicity, we'll alias to the enum name.
            pyi_lines.append(
                f"{current_indent}{alias_name}: TypeAlias = {python_enum_type} # Or int"
            )
            continue

        # Class
        match_class_start = re.match(r"class\s+(\w+)\s*:\s*public\s+([\w:]+)", line)
        if match_class_start:
            current_class_name, base_class_sip = match_class_start.groups()
            base_class_py = sip_to_python_type(base_class_sip, current_namespace_name)

            pyi_lines.append(
                f"{current_indent}class {current_class_name}({base_class_py}):"
            )
            current_indent += "    "
            in_class = True
            continue
        else:
            match_class_start = re.match(r"class\s+(\w+)", line)
            if match_class_start:
                (current_class_name,) = match_class_start.groups()
                pyi_lines.append(f"{current_indent}class {current_class_name}:")
                current_indent += "    "
                in_class = True
                continue

        if line.startswith("};") and in_class:  # End of class
            current_indent = current_indent[:-4]
            pyi_lines.append("")  # Add a blank line after class
            in_class = False
            current_class_name = None
            continue
        if in_class:
            # Signals: public: Q_SIGNAL void signalName(args);
            # or Q_SIGNALS: Q_SIGNAL void signalName(args);
            if "Q_SIGNAL" in line:
                # Q_SIGNAL void pIsStayTopChanged();
                # Q_SIGNAL  void userInfoCardClicked();
                # Q_SIGNAL  void navigationNodeClicked(ElaNavigationType::NavigationNodeType nodeType, QString nodeKey);
                signal_match = re.match(
                    r"(?:public:\s*)?Q_SIGNAL\s+(?:void\s+)?(\w+)\s*\(([^)]*)\)\s*;",
                    line,
                )
                if not signal_match:  # Try alternative format if Q_SIGNALS block
                    signal_match_alt = re.match(
                        r"Q_SIGNAL\s+(?:void\s+)?(\w+)\s*\(([^)]*)\)\s*;", line
                    )
                    if signal_match_alt:
                        signal_match = signal_match_alt
                    else:  # Signal with no args
                        signal_match_no_args = re.match(
                            r"(?:public:\s*)?Q_SIGNAL\s+(?:void\s+)?(\w+)\s*;", line
                        )
                        if signal_match_no_args:
                            pyi_lines.append(
                                f"{current_indent}{signal_match_no_args.group(1)}: pyqtSignal()"
                            )
                            continue
                        signal_match_no_args_alt = re.match(
                            r"Q_SIGNAL\s+(?:void\s+)?(\w+)\s*;", line
                        )
                        if signal_match_no_args_alt:
                            pyi_lines.append(
                                f"{current_indent}{signal_match_no_args_alt.group(1)} = pyqtSignal()"
                            )
                            continue

                        print(f"Warning: Could not parse signal: {line}")
                        continue

                signal_name, signal_args_str = signal_match.groups()
                if signal_args_str.strip():
                    # Parse args for comment
                    # Example: ElaNavigationType::NavigationNodeType nodeType, QString nodeKey
                    args_list = []
                    raw_arg_list = [a.strip() for a in signal_args_str.split(",")]
                    for arg_item in raw_arg_list:
                        type_part = arg_item.rsplit(" ", 1)[0]  # type at the beginning
                        args_list.append(
                            sip_to_python_type(type_part, current_namespace_name)
                        )
                    pyi_lines.append(
                        f"{current_indent}{signal_name} = pyqtSignal({', '.join(args_list)})"
                    )
                else:
                    pyi_lines.append(f"{current_indent}{signal_name} = pyqtSignal()")
                continue
            # Constructor: explicit ClassName(QWidget * parent = nullptr);
            if line.startswith("explicit " + str(current_class_name)):
                ctor_match = re.match(r"explicit\s+\w+\s*\((.*)\)\s*;", line)
                if ctor_match:
                    params_str = ctor_match.group(1)
                    py_params, _ = parse_parameters(params_str, current_namespace_name)
                    pyi_lines.append(
                        f"{current_indent}def __init__(self, {', '.join(py_params)}) -> None:"
                    )
                    pyi_lines.append(f"{current_indent}    ...")
                continue

            # Destructor: ~ClassName();
            if line.startswith("~" + str(current_class_name)):
                pyi_lines.append(
                    f"{current_indent}def __del__(self) -> None:"
                )  # Optional for pyi
                pyi_lines.append(f"{current_indent}    ...")
                continue

            # Methods
            # ReturnType methodName(args) const /PyName=pyName/;
            # void setIsStayTop(bool IsStayTop);
            # bool getIsStayTop() const;
            # ElaNavigationType::NodeOperateReturnType addExpanderNode(QString expanderTitle, QString & expanderKey /Out/, ElaIconType::IconName awesome = ElaIconType::None) const ;
            method_match = re.match(
                r"([\w:*&\s]+?)\s+"  # Return type (can include *, &, ::)
                r"(\w+)\s*"  # Method name
                r"\(([^)]*)\)\s*"  # Parameters
                r"(const)?\s*"  # Optional const
                r"(?:/\s*PyName\s*=\s*(\w+)\s*/)?\s*;",  # Optional PyName
                line,
            )
            if method_match:
                (
                    ret_type_sip,
                    method_name_sip,
                    params_str,
                    is_const,
                    py_name_override,
                ) = method_match.groups()

                method_name_py = (
                    py_name_override if py_name_override else method_name_sip
                )

                py_params, out_param_types = parse_parameters(
                    params_str, current_namespace_name
                )
                ret_type_py = sip_to_python_type(ret_type_sip, current_namespace_name)

                if "static" in ret_type_sip:
                    pyi_lines.append("    @staticmethod")
                final_ret_type = ret_type_py
                if out_param_types:
                    if ret_type_py == "None":  # void function with /Out/ params
                        if len(out_param_types) == 1:
                            final_ret_type = out_param_types[0]
                        else:
                            final_ret_type = f"Tuple[{', '.join(out_param_types)}]"
                    else:  # function with return value AND /Out/ params
                        all_returns = [ret_type_py] + out_param_types
                        final_ret_type = f"Tuple[{', '.join(all_returns)}]"

                param_list_str = ", ".join(py_params)
                if param_list_str:
                    pyi_lines.append(
                        f"{current_indent}def {method_name_py}(self, {param_list_str}) -> {final_ret_type}:"
                    )
                else:
                    pyi_lines.append(
                        f"{current_indent}def {method_name_py}(self) -> {final_ret_type}:"
                    )
                pyi_lines.append(f"{current_indent}    ...")
                continue

        # Catch Q_SIGNALS: block start (often empty line after it)
        if line.strip() == "Q_SIGNALS:":
            continue  # The actual signals are parsed above

    # Prepend imports
    final_pyi_content = "\n".join(pyi_lines)
    return final_pyi_content


forQt5 = len(sys.argv) >= 2 and int(sys.argv[1])
pyqtVer = ["6", "5"][forQt5]
if __name__ == "__main__":
    # === 创建一些示例 SIP 文件用于测试 ===
    test_sip_dir = Path("sip")

    content = ""
    for sip_file in list(test_sip_dir.glob("*.sip")):
        pyi_output = generate_pyi(sip_file.read_text())
        content += pyi_output

    content = "\n".join(
        (
            "from typing import Any, List, Tuple, Callable, Optional, Union, TypeAlias",
            "from enum import IntEnum",  # Using IntEnum for all enums for simplicity
            # Common Qt imports - adjust for your binding (PyQt5, PyQt6, PySide2, PySide6)
            f"from PyQt{pyqtVer}.QtCore import *",  # pyqtSignal is often aliased to Signal
            f"from PyQt{pyqtVer}.QtGui import *",
            f"from PyQt{pyqtVer}.QtWidgets import *",
            "",
        )
    ) + content.replace(".None", ".None_")

    content = content.replace(" TabPosition", " QTabWidget.TabPosition")
    with open("ElaWidgetTools.pyi", "w", encoding="utf8") as ff:
        ff.write(content)
