import os, re, sys

print(sys.argv)
if len(sys.argv) > 1:
    ELA_INCLUDE_PATH = sys.argv[1]
    MY_QT_INSTALL = sys.argv[2]
    MY_PYTHON_INSTALL_PATH = sys.argv[3]
    MY_SITE_PACKAGES_PATH = sys.argv[4]
else:
    ELA_INCLUDE_PATH = (
        "C:/Users/11737/Documents/GitHub/PyElaWidgetTools/ElaWidgetTools/ElaWidgetTools"
    )
    MY_QT_INSTALL = "c:/tmp/6.6.2/msvc2019_64"
    MY_PYTHON_INSTALL_PATH = "C:/Users/11737/AppData/Local/Programs/Python/Python312"
    MY_SITE_PACKAGES_PATH = "C:/Users/11737/AppData/Local/Programs/Python/Python312/Lib/site-packages"
os.chdir(os.path.dirname(os.path.abspath(__file__)))

eladir = "../../ElaWidgetTools/ElaWidgetTools"

with open(eladir + "/ElaProperty.h", "r", encoding="utf8") as ff:
    pro = ff.read()
# 如果不这样改，信号会被识别成方法。
if not ("Q_SIGNALS:Q_SIGNAL" in pro):
    pro = re.sub(r"Q_SIGNAL(.*?)\\", r"Q_SIGNALS:Q_SIGNAL \1\\\npublic:\\", pro)

    with open(eladir + "/ElaProperty.h", "w", encoding="utf8") as ff:
        ff.write(pro)


def specialfuns(const=True):
    ___ = ""
    ___ += r"""<modify-function signature="addFooterNode(QString,QString&amp;,int,ElaIconType::IconName)const">
    <modify-argument index="2">
        <remove-argument/>
    </modify-argument>
    <inject-code class="target" position="beginning">
        QString footerKey;
        ElaNavigationType::NodeOperateReturnType cppRes =
            %CPPSELF.addFooterNode(%1, footerKey, %3, %4);

        PyObject* pyRes = Shiboken::Conversions::copyToPython(
            PepType_SETP(reinterpret_cast&lt;SbkEnumType *&gt;(Shiboken::Module::get(SbkElaWidgetToolsTypeStructs[SBK_ElaNavigationType_NodeOperateReturnType_IDX])))-&gt;converter,
            &amp;cppRes);

        PyObject* pyFooterKey = Shiboken::Conversions::copyToPython(
            SbkPySide6_QtCoreTypeConverters[SBK_QString_IDX],
            &amp;footerKey);

        return Py_BuildValue("(NN)", pyRes, pyFooterKey);
    </inject-code>
</modify-function>"""
    ___ += r"""<modify-function signature="addFooterNode(QString,QWidget*,QString&amp;,int,ElaIconType::IconName)const">
    <modify-argument index="3">
        <remove-argument/>
    </modify-argument>
    <inject-code class="target" position="beginning">
        QString footerKey;
        ElaNavigationType::NodeOperateReturnType cppRes =
            %CPPSELF.addFooterNode(%1, %2, footerKey, %4, %5);

        PyObject* pyRes = Shiboken::Conversions::copyToPython(
            PepType_SETP(reinterpret_cast&lt;SbkEnumType *&gt;(Shiboken::Module::get(SbkElaWidgetToolsTypeStructs[SBK_ElaNavigationType_NodeOperateReturnType_IDX])))-&gt;converter,
            &amp;cppRes);

        PyObject* pyFooterKey = Shiboken::Conversions::copyToPython(
            SbkPySide6_QtCoreTypeConverters[SBK_QString_IDX],
            &amp;footerKey);

        return Py_BuildValue("(NN)", pyRes, pyFooterKey);
    </inject-code>
</modify-function>"""
    ___ += r"""<modify-function signature="addExpanderNode(QString,QString&amp;,ElaIconType::IconName)const">
    <modify-argument index="2">
        <remove-argument/>
    </modify-argument>
    <inject-code class="target" position="beginning">
        QString footerKey;
        ElaNavigationType::NodeOperateReturnType cppRes =
            %CPPSELF.addExpanderNode(%1, footerKey, %3);

        PyObject* pyRes = Shiboken::Conversions::copyToPython(
            PepType_SETP(reinterpret_cast&lt;SbkEnumType *&gt;(Shiboken::Module::get(SbkElaWidgetToolsTypeStructs[SBK_ElaNavigationType_NodeOperateReturnType_IDX])))-&gt;converter,
            &amp;cppRes);

        PyObject* pyFooterKey = Shiboken::Conversions::copyToPython(
            SbkPySide6_QtCoreTypeConverters[SBK_QString_IDX],
            &amp;footerKey);

        return Py_BuildValue("(NN)", pyRes, pyFooterKey);
    </inject-code>
</modify-function>"""
    ___ += r"""<modify-function signature="addExpanderNode(QString,QString&amp;,QString,ElaIconType::IconName)const">
    <modify-argument index="2">
        <remove-argument/>
    </modify-argument>
    <inject-code class="target" position="beginning">
        QString footerKey;
        ElaNavigationType::NodeOperateReturnType cppRes =
            %CPPSELF.addExpanderNode(%1, footerKey, %3, %4);

        PyObject* pyRes = Shiboken::Conversions::copyToPython(
            PepType_SETP(reinterpret_cast&lt;SbkEnumType *&gt;(Shiboken::Module::get(SbkElaWidgetToolsTypeStructs[SBK_ElaNavigationType_NodeOperateReturnType_IDX])))-&gt;converter,
            &amp;cppRes);

        PyObject* pyFooterKey = Shiboken::Conversions::copyToPython(
            SbkPySide6_QtCoreTypeConverters[SBK_QString_IDX],
            &amp;footerKey);

        return Py_BuildValue("(NN)", pyRes, pyFooterKey);
    </inject-code>
</modify-function>"""

    # SIP没办法处理这4个重载，但SHIBOKEN可以。但为了统一，将SHIBOKEN也改名。
    ___ += r"""<modify-function signature="addPageNode(QString,QWidget*,int,ElaIconType::IconName)const" rename="addPageNodeKeyPoints"/>"""
    ___ += r"""<modify-function signature="addPageNode(QString,QWidget*,QString,int,ElaIconType::IconName)const" rename="addPageNodeKeyPoints"/>"""
    if not const:
        ___ = ___.replace("const", "")
    return ___


def cast_h_to_sip(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    _ = re.findall(r"class ELA_EXPORT ([\w]*)", content)
    ___ = ""
    # 目前看起来，只有第一个类里面有signal，所以暂时懒得做更复杂的处理了。
    for __ in _:
        # ElaFlowLayout::itemAt
        # ElaFlowLayout::addItem
        ___ += f'<object-type name="{__}" >'
        if "ElaNavigationBar" in filename or "ElaWindow" in filename:
            ___ += specialfuns("ElaWindow" in filename)
        # if signals:
        #     for signal in signals:
        #         ___ += f'<function signature="{signal}()" signal="true" />'
        #     signals.clear()
        ___ += f"</object-type>"
    return ___


def gen_widgets(eladir: str):

    hs = []
    xmls = []
    for f in os.listdir(eladir):
        if f.startswith("ElaDef"):
            continue
        if f.startswith("ElaProperty"):
            continue
        if f.startswith("ElaSingleton"):
            continue
        if f.startswith("Ela") and f.endswith(".h"):
            xmls.append(cast_h_to_sip(eladir + "/" + f))
            hs.append(f"#include<{os.path.basename(f)}>")

    return "\n".join(xmls), "\n".join(hs)


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


xml, h = gen_widgets(eladir)
xmlinternal = gen_defs()
xmlbase = """<?xml version="1.0"?>
<typesystem package="ElaWidgetTools">
    <load-typesystem name="typesystem_widgets.xml" generate="no"/>
    <load-typesystem name="typesystem_gui.xml" generate="no"/>

{internal}

</typesystem>"""

xmlall = xmlbase.format(internal=xmlinternal + xml)


def maybeparse(xx: str):
    with open(
        f"{MY_SITE_PACKAGES_PATH}/PySide6/include/QtCore/pyside6_qtcore_python.h", "r"
    ) as ff:
        qtcore = ff.read()
        if not ("SBK_QString_IDX" in qtcore):
            xx = xx.replace("SBK_QLayoutItem_IDX", "SBK_QLAYOUTITEM_IDX")
            xx = xx.replace("SBK_QLayout_IDX", "SBK_QLAYOUT_IDX")
            xx = xx.replace("SBK_QString_IDX", "SBK_QSTRING_IDX")
            xx = xx.replace("SBK_QWidget_IDX", "SBK_QWIDGET_IDX")
            xx = xx.replace("Shiboken::Module::get", "")
            xx = xx.replace("SbkElaWidgetToolsTypeStructs", "SbkElaWidgetToolsTypes")
            xx = xx.replace(
                "SbkPySide6_QtWidgetsTypeStructs", "SbkPySide6_QtWidgetsTypes"
            )
            xx = xx.replace(
                "SBK_ElaNavigationType_NodeOperateReturnType_IDX",
                "SBK_ELANAVIGATIONTYPE_NODEOPERATERETURNTYPE_IDX",
            )
        return xx


with open("bindings.xml", "w", encoding="utf8") as ff:
    ff.write(maybeparse(xmlall))

with open("special.hpp", "r", encoding="utf8") as ff:
    special = ff.read()

with open("special.hpp", "w", encoding="utf8") as ff:
    ff.write(maybeparse(special))


wrapperbase = """
#ifndef MY_WRAPPER_H
#define MY_WRAPPER_H

// Hmm, weird hack to allow for static asserts with offsetof
#define _CRT_USE_BUILTIN_OFFSETOF

{internal}

#endif
"""

H_internal = """#include <ElaDef.h>"""
with open("wrapper.hpp", "w", encoding="utf8") as ff:
    ff.write(wrapperbase.format(internal=H_internal + "\n" + h))


sysinclude = ""
if "msvc2019" in MY_QT_INSTALL:
    # <=6.7必须使用msvc2019的头文件
    vspath = "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC"
    if not os.path.exists(vspath):
        vspath = (
            "C:/Program Files/Microsoft Visual Studio/2022/Enterprise/VC/Tools/MSVC"
        )
    print(os.listdir(vspath))
    for _ in os.listdir(vspath):
        if _.startswith("14.29"):
            msvc2019 = _
    sysinclude = vspath + "/" + msvc2019 + "/include"
    print(sysinclude)
    sysinclude = f'--system-include-paths="{sysinclude}"'

if sys.platform=='linux':
    inc='/usr/lib/gcc/x86_64-linux-gnu/14/include'
    if not os.path.exists(inc):
        inc='/usr/lib/gcc/x86_64-linux-gnu/11/include'
    __ = os.path.dirname(os.path.dirname(sys.executable))
    pyDir = __ + "/include/"+os.listdir(__ + "/include")[0]
    print(pyDir)
    sysinclude = f' -I{inc} -I{pyDir} '
os.system(
    f"""shiboken6 {sysinclude}
        --generator-set=shiboken
        --output-directory=OUTPUTDIR
        -I{ELA_INCLUDE_PATH}
        -I{MY_QT_INSTALL}/include -I{MY_QT_INSTALL}/include/QtCore -I{MY_QT_INSTALL}/include/QtGui -I{MY_QT_INSTALL}/include/QtWidgets
        --typesystem-paths={MY_SITE_PACKAGES_PATH}/PySide6/typesystems
        --enable-pyside-extensions
        --avoid-protected-hack
        wrapper.hpp
        bindings.xml""".replace(
        "\n", " "
    )
)

with open("OUTPUTDIR/ElaWidgetTools/elaflowlayout_wrapper.h", "r") as ff:
    __ = ff.read()
with open("OUTPUTDIR/ElaWidgetTools/elaflowlayout_wrapper.h", "w") as ff:
    ff.write(__ + '\n#include"special.hpp"')
