import sys, os, subprocess, shutil

print(sys.executable)
rootDir = os.path.dirname(__file__)
if not rootDir:
    rootDir = os.path.abspath(".")
else:
    rootDir = os.path.abspath(rootDir)
rootthisfiledir = rootDir
os.chdir(rootthisfiledir)

pythonversion = sys.argv[1]
qtarch = sys.argv[2]
qtversion = sys.argv[3]
arch = sys.argv[4]
binding = sys.argv[5]

qtarchdir = qtarch[qtarch.find("_") + 1 :]

# 准备环境
pyPathEx = f"C:\\hostedtoolcache\\windows\\Python\\3.12.10\\x64\\python.exe"
pyDir = f"C:\\hostedtoolcache\\windows\\Python\\{pythonversion}\\{arch}"
pyPath = f"{pyDir}\\python.exe"
subprocess.run(f"{pyPath} -m pip install --upgrade pip")
if binding.lower().startswith("pyqt"):
    if qtversion.startswith("6"):
        subprocess.run(f"{pyPath} -m pip install pyqt6==6.6 PyQt-builder sip")
    else:
        subprocess.run(
            f"{pyPath} -m pip install pyqt5==5.15.9 PyQt-builder==1.15 sip==6.7"
        )
elif binding.lower().startswith("pyside"):
    subprocess.run(
        f"{pyPath} -m pip install pyside6=={qtversion} shiboken6=={qtversion} shiboken6_generator=={qtversion}"
    )


# 编译ela
def __parsefile(fn, cb):
    with open(fn, "r", encoding="utf8") as ff:
        cml = ff.read()
    with open(fn, "w", encoding="utf8") as ff:
        ff.write(cb(cml))


__parsefile(
    "../ElaWidgetTools/CMakeLists.txt",
    lambda cml: cml.replace("add_subdirectory(ElaWidgetToolsExample)", ""),
)
__parsefile(
    r"..\ElaWidgetTools\ElaWidgetTools\CMakeLists.txt",
    lambda cml: cml.replace("qt_add_library", "add_library"),  # qt6.8以上
)
__parsefile(
    r"..\ElaWidgetTools\ElaWidgetTools\ElaProperty.h",
    lambda cml: cml.replace(
        "Q_DECL_EXPORT",
        "",
    ).replace("Q_DECL_IMPORT", ""),
)

archA = ("win32", "x64")[arch == "x64"]
subprocess.run(
    f'cmake -DELAWIDGETTOOLS_BUILD_STATIC_LIB=ON ../ElaWidgetTools/CMakeLists.txt -G "Visual Studio 17 2022" -A {archA} -T host={arch}'
)
subprocess.run(
    f"cmake --build ./ --config Release --target ALL_BUILD -j {os.cpu_count()}"
)
if binding.lower().startswith("pyqt"):
    os.chdir("pyqt")
    os.mkdir("sip")
    subprocess.run(f"python gen_Def.sip.py")
    subprocess.run(f'python gen_widgets.py {int(qtversion.startswith("5"))}')
    subprocess.run(f'python gen_pyi_from_sip.py {int(qtversion.startswith("5"))}')
    subprocess.run(f"{pyPath} sip_code_fix.py")
    subprocess.run(
        rf"{pyDir}\Scripts\sip-build --verbose --qmake D:\a\PyElaWidgetTools\Qt\{qtversion}\{qtarchdir}\bin\qmake.exe"
    )
    # for _dir, _, _fs in os.walk(r"."):
    #     for _f in _fs:
    #         print(_dir, _f)
    os.chdir("..")
    os.mkdir("objects")
    shutil.copy(r"pyqt\build\ElaWidgetTools\ElaWidgetTools.pyd", "objects")
    shutil.copy(r"pyqt\ElaWidgetTools.pyi", "objects")
    shutil.copytree(r"pyqt\sip", "objects/sip")

elif binding.lower().startswith("pyside"):
    cwd = os.getcwd()
    # 使用pyqt的东西来生成pyi，shiboken自带的谜之不管用
    os.chdir("pyqt")
    os.mkdir("sip")
    subprocess.run(f"python gen_Def.sip.py")
    subprocess.run(f'python gen_widgets.py {int(qtversion.startswith("5"))}')
    subprocess.run(f'python gen_pyi_from_sip.py {int(qtversion.startswith("5"))}')
    __parsefile(
        "ElaWidgetTools.pyi",
        lambda c: c.replace("PyQt6", "PySide6").replace("pyqtSignal", "Signal"),
    )
    pyipath = os.getcwd()
    os.chdir(cwd)
    os.chdir("pyside6")

    subprocess.run(
        f'python gen_xml.py {os.path.abspath("../../ElaWidgetTools/ElaWidgetTools").replace("\\", "/")} D:/a/PyElaWidgetTools/Qt/{qtversion}/{qtarchdir} {pyDir.replace("\\", "/")}'
    )

    archA = ("win32", "x64")[arch == "x64"]
    subprocess.run(
        f'cmake -DMY_QT_INSTALL=D:/a/PyElaWidgetTools/Qt/{qtversion}/{qtarchdir} -DMY_PYTHON_INSTALL_PATH={pyDir.replace("\\", "/")} -DELA_LIB_PATH={os.path.abspath("../ElaWidgetTools/Release/ElaWidgetTools.lib").replace("\\", "/")} -DELA_INCLUDE_PATH={os.path.abspath("../../ElaWidgetTools/ElaWidgetTools").replace("\\", "/")} ./CMakeLists.txt -G "Visual Studio 17 2022" -A {archA} -T host={arch}'
    )
    subprocess.run(
        f"cmake --build ./ --config Release --target ALL_BUILD -j {os.cpu_count()}"
    )

    os.chdir("..")
    os.mkdir("objects")
    shutil.copy(r"pyside6\Release\ElaWidgetTools.pyd", "objects")
    shutil.copy(pyipath + r"\ElaWidgetTools.pyi", "objects")

dirname = f"{binding}ElaWidgetTools"
os.mkdir(rf"wheel\{dirname}")
shutil.copy(r"objects\ElaWidgetTools.pyd", rf"wheel\{dirname}")
shutil.copy(r"objects\ElaWidgetTools.pyi", rf"wheel\{dirname}")

with open(r"wheel\__init__.py", "r") as ff:
    init = ff.read()
with open(rf"wheel\{dirname}\__init__.py", "w") as ff:
    ff.write(f"from {binding} import QtCore, QtWidgets, QtGui\n" + init)

#
os.chdir("wheel")
subprocess.run(f"{pyPathEx} -m pip install setuptools wheel")
subprocess.run(
    f"{pyPathEx} setup.py bdist_wheel {('64','32')[arch == 'x86']} {binding}"
)
os.chdir("..")

shutil.copytree("wheel/dist", "objects/wheel")

for f in os.listdir("objects/wheel"):
    shutil.move("objects/wheel/" + f, "objects/wheel/" + f.lower())
