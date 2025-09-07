import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


eladir = "../../ElaWidgetTools/ElaWidgetTools"


import re


def gen_defs():

    with open(eladir + "/ElaDef.h", "r", encoding="utf8") as ff:
        header_content = ff.read()
    sip_output = []

    # Regex to find the Q_BEGIN_ENUM_CREATE blocks
    # It captures the "ClassName" (e.g., ElaApplicationType)
    # and the content within that block.
    block_pattern = re.compile(
        r"Q_BEGIN_ENUM_CREATE\s*\(\s*(\w+)\s*\)\s*(.*?)\s*Q_END_ENUM_CREATE\s*\(\s*\1\s*\)",
        re.DOTALL,
    )

    # Regex to find enums within a block
    # Captures EnumName and its members
    enum_pattern = re.compile(
        r"enum\s+(\w+)\s*\{(.*?)\};.*?Q_ENUM_CREATE\s*\(\s*\1\s*\)", re.DOTALL
    )
    # For Qt5 < 5.14 compatibility where Q_ENUM_CREATE might be Q_ENUM
    # This is already handled by the Q_ENUM_CREATE in the regex, but good to keep in mind.

    # Regex to find Q_DECLARE_FLAGS
    # Captures FlagsName and the EnumName it's based on
    qflags_pattern = re.compile(
        r"Q_DECLARE_FLAGS\s*\(\s*(\w+)\s*,\s*(\w+(?:::\w+)?)\s*\)"
    )
    flags = {}

    for block_match in block_pattern.finditer(header_content):
        class_name = block_match.group(1)
        block_content = block_match.group(2)
        if class_name == "CLASS":
            continue
        enums = []
        for enum_match in enum_pattern.finditer(block_content):
            enum_name = enum_match.group(1)
            enums.append(enum_name)
        sip_output.append((class_name, enums))
        # Find Q_DECLARE_FLAGS within this block
        # Note: Q_DECLARE_FLAGS might refer to an enum defined inside this "class_name"
        # or potentially a globally defined one (though not in this Def.h structure)
        for qflags_match in qflags_pattern.finditer(block_content):
            flags_name = qflags_match.group(1)
            base_enum_full_name = qflags_match.group(
                2
            )  # e.g., ButtonType or SomeOtherNamespace::ButtonType

            # We need to ensure the base_enum_full_name is correctly referenced.
            # If it's just "ButtonType", SIP assumes it's in the current scope (namespace class_name)
            # If it's "ElaAppBarType::ButtonType", SIP needs to know "ElaAppBarType" first.
            # The current structure implies base_enum_full_name will be just the EnumName.
            base_enum_name_simple = base_enum_full_name.split("::")[-1]

            flags[base_enum_name_simple] = flags_name

    output = ""
    for namespace, enums in sip_output:
        output += f'<namespace-type name="{namespace}">'
        for em in enums:
            if em in flags:
                output += f'<enum-type name="{em}" flags="{flags[em]}"/>'
            else:
                output += f'<enum-type name="{em}" />'

        output += "</namespace-type>"

    return output


xmlinternal = gen_defs()
xmlbase = """<?xml version="1.0"?>
<typesystem package="ElaWidgetTools">
    <load-typesystem name="typesystem_widgets.xml" generate="no"/>
    <load-typesystem name="typesystem_gui.xml" generate="no"/>

{internal}

</typesystem>"""
with open("bindings.xml", "w", encoding="utf8") as ff:
    ff.write(xmlbase.format(internal=xmlinternal))


wrapperbase = """
#ifndef MY_WRAPPER_H
#define MY_WRAPPER_H

// Hmm, weird hack to allow for static asserts with offsetof
#define _CRT_USE_BUILTIN_OFFSETOF

{internal}

#endif
"""

H_internal = """ #include <ElaDef.h> """
with open("wrapper.hpp", "w", encoding="utf8") as ff:
    ff.write(wrapperbase.format(internal=H_internal))
