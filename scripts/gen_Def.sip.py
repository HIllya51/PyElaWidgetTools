import sys, os, ctypes

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open(r"./ElaWidgetTools/ElaWidgetTools\ElaDef.h", "r", encoding="utf8") as ff:
    content = ff.read()

import re
import sys


def parse_def_h_to_sip(header_content):
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

    # Regex to parse individual enum members
    # Captures MemberName and its Value. Handles comments.
    member_pattern = re.compile(
        r"^\s*(\w+)\s*=\s*([^,/]+?)\s*(?:,//.*|/\*.*?\*/|,|\s)*$", re.MULTILINE
    )

    for block_match in block_pattern.finditer(header_content):
        class_name = block_match.group(1)
        block_content = block_match.group(2)
        if class_name == "CLASS":
            continue
        sip_output.append(f"namespace {class_name}\n{{")
        sip_output.append(
            """
%TypeHeaderCode
#include "ElaDef.h"
%End
"""
        )

        # Find enums within this block
        for enum_match in enum_pattern.finditer(block_content):
            enum_name = enum_match.group(1)
            members_str = enum_match.group(2)

            # Handle conditional compilation for members (simplified: include all)
            # A more sophisticated parser might try to evaluate these.
            # For now, we'll just clean them up a bit for parsing.
            members_str = re.sub(r"#if\s+defined\([^)]+\)", "", members_str)
            members_str = re.sub(r"#endif", "", members_str)

            sip_output.append(f"    enum {enum_name}")#(f"    enum {enum_name} /PyName={enum_name}/")
            sip_output.append("    {")

            found_members = []
            for member_line in members_str.splitlines():
                member_line = member_line.strip()
                if not member_line or member_line.startswith("//"):
                    continue

                # Try to match with value
                m = member_pattern.match(member_line)
                if m:
                    member_name = m.group(1)
                    member_value = m.group(2).strip()
                    sip_output.append(f"        {member_name} = {member_value},")
                    found_members.append(member_name)
                elif member_line and not member_line.endswith(
                    ","
                ):  # Handle valueless last member
                    # This case is less common with explicit values but good to consider
                    # For this file, all members have values.
                    member_name_only = member_line.split("=")[0].strip()
                    if member_name_only and member_name_only not in found_members:
                        sip_output.append(f"        {member_name_only},")
                        found_members.append(member_name_only)
                elif member_line.endswith(","):  # Handle valueless member with comma
                    member_name_only = member_line.split("=")[0].strip().rstrip(",")
                    if member_name_only and member_name_only not in found_members:
                        sip_output.append(f"        {member_name_only},")
                        found_members.append(member_name_only)

            # Remove trailing comma from the last member if any
            if sip_output[-1].endswith(","):
                sip_output[-1] = sip_output[-1][:-1]
            sip_output.append("    };")
            sip_output.append("")  # Newline for readability

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

            sip_output.append(f"    typedef QFlags<{class_name}::{base_enum_name_simple}> {flags_name};")
            sip_output.append("")  # Newline

        sip_output.append(f"}}; // namespace {class_name}")
        sip_output.append("")  # Newline

    # Handle Q_DECLARE_OPERATORS_FOR_FLAGS - SIP usually handles this if %QFlags is defined
    # We can add comments or specific directives if needed, but often not required.
    # Example:
    # for op_match in re.finditer(r"Q_DECLARE_OPERATORS_FOR_FLAGS\s*\(([\w:]+)\)", header_content):
    #     flags_type_full_name = op_match.group(1)
    #     sip_output.append(f"// Operators for {flags_type_full_name} should be automatically handled by SIP")
    #     sip_output.append("")

    return "\n".join(sip_output)


sip = parse_def_h_to_sip(content)
with open("sip/ElaDef.sip", "w", encoding="utf8") as ff:
    ff.write('''%Import QtCore/QtCoremod.sip\n''')
    ff.write(sip)
