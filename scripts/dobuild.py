import sys, os, subprocess, shutil

print(sys.platform)
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


# 准备环境
if sys.platform == "win32":
    pyPathEx = f"C:/hostedtoolcache/windows/Python/3.12.10/x64/python.exe"
    pyDir = f"C:/hostedtoolcache/windows/Python/{pythonversion}/{arch}"
    pyPath = f"{pyDir}/python.exe"
    qtarchdir = qtarch[qtarch.find("_") + 1 :]
    Qtinstallpath = f"D:/a/PyElaWidgetTools/Qt/{qtversion}/{qtarchdir}"
    qmake = f"{Qtinstallpath}/bin/qmake.exe"
    sipbuild = f"{pyDir}/Scripts/sip-build"
elif sys.platform == "linux":
    pyPathEx = f"/opt/hostedtoolcache/Python/3.12.10/x64/bin/python"
    pyDir = f"/opt/hostedtoolcache/Python/{pythonversion}/{arch}/bin"
    pyPath = f"{pyDir}/python"
    Qtinstallpath = f"/home/runner/work/PyElaWidgetTools/Qt/{qtversion}/{qtarch}"
    qmake = f"{Qtinstallpath}/bin/qmake"
    sipbuild = f"{pyDir}/sip-build"


subprocess.run(f"{pyPath} -m pip install --upgrade pip", shell=True)
if binding.lower().startswith("pyqt"):
    if qtversion.startswith("6"):
        subprocess.run(
            f"{pyPath} -m pip install pyqt6==6.6 PyQt-builder sip", shell=True
        )
    else:
        subprocess.run(
            f"{pyPath} -m pip install pyqt5==5.15.9 PyQt-builder==1.15 sip==6.7",
            shell=True,
        )
elif binding.lower().startswith("pyside"):
    subprocess.run(
        f"{pyPath} -m pip install pyside6=={qtversion} shiboken6=={qtversion} shiboken6_generator=={qtversion}",
        shell=True,
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
    "../ElaWidgetTools/ElaWidgetTools/CMakeLists.txt",
    lambda cml: cml.replace("qt_add_library", "add_library"),  # qt6.8以上
)
__parsefile(
    "../ElaWidgetTools/ElaWidgetTools/ElaProperty.h",
    lambda cml: cml.replace(
        "Q_DECL_EXPORT",
        "",
    ).replace("Q_DECL_IMPORT", ""),
)
if sys.platform == "win32":
    archA = ("win32", "x64")[arch == "x64"]
    flags = f'-G "Visual Studio 17 2022" -A {archA} -T host={arch}'
else:
    flags = ""
subprocess.run(
    f"cmake -DELAWIDGETTOOLS_BUILD_STATIC_LIB=ON ../ElaWidgetTools/CMakeLists.txt {flags}",
    shell=True,
)
subprocess.run(
    f"cmake --build ./ --config Release -j {os.cpu_count()}",
    shell=True,
)
if binding.lower().startswith("pyqt"):
    os.chdir("pyqt")
    os.mkdir("sip")
    subprocess.run(f"python gen_Def.sip.py", shell=True)
    subprocess.run(
        f'python gen_widgets.py {int(qtversion.startswith("5"))}', shell=True
    )
    subprocess.run(
        f'python gen_pyi_from_sip.py {int(qtversion.startswith("5"))}', shell=True
    )
    subprocess.run(f"{pyPath} sip_code_fix.py", shell=True)
    if sys.platform == "win32":
        __parsefile(
            "pyproject.toml",
            lambda c: c.replace(
                '[ "ElaWidgetTools" ]',
                '[ "ElaWidgetTools","D3D11", "DXGI", "kernel32" ,"user32", "gdi32", "winspool" ,"comdlg32", "advapi32", "shell32", "ole32", "oleaut32", "uuid", "odbc32", "odbccp32"]',
            ),
        )
    subprocess.run(f"{sipbuild} --verbose --qmake {qmake}", shell=True)
    for _dir, _, _fs in os.walk(r"."):
        for _f in _fs:
            print(_dir, _f)
    os.chdir("..")
    os.mkdir("objects")
    shutil.copy("pyqt/build/ElaWidgetTools/ElaWidgetTools.pyd", "objects")
    shutil.copy("pyqt/ElaWidgetTools.pyi", "objects")
    shutil.copytree("pyqt/sip", "objects/sip")

elif binding.lower().startswith("pyside"):
    cwd = os.getcwd()
    # 使用pyqt的东西来生成pyi，shiboken自带的谜之不管用
    os.chdir("pyqt")
    os.mkdir("sip")
    subprocess.run(f"python gen_Def.sip.py", shell=True)
    subprocess.run(
        f'python gen_widgets.py {int(qtversion.startswith("5"))}', shell=True
    )
    subprocess.run(
        f'python gen_pyi_from_sip.py {int(qtversion.startswith("5"))}', shell=True
    )
    __parsefile(
        "ElaWidgetTools.pyi",
        lambda c: c.replace("PyQt6", "PySide6").replace("pyqtSignal", "Signal"),
    )
    pyipath = os.getcwd()
    os.chdir(cwd)
    os.chdir("pyside6")

    subprocess.run(
        f'python gen_xml.py {os.path.abspath("../../ElaWidgetTools/ElaWidgetTools").replace("\\", "/")} {Qtinstallpath} {pyDir}',
        shell=True,
    )

    subprocess.run(
        f'cmake -DMY_QT_INSTALL={Qtinstallpath} -DMY_PYTHON_INSTALL_PATH={pyDir} -DELA_LIB_PATH={os.path.abspath("../ElaWidgetTools/Release/ElaWidgetTools.lib").replace("\\", "/")} -DELA_INCLUDE_PATH={os.path.abspath("../../ElaWidgetTools/ElaWidgetTools").replace("\\", "/")} ./CMakeLists.txt {flags}',
        shell=True,
    )
    subprocess.run(
        f"cmake --build ./ --config Release -j {os.cpu_count()}",
        shell=True,
    )

    os.chdir("..")
    os.mkdir("objects")
    shutil.copy("pyside6/Release/ElaWidgetTools.pyd", "objects")
    shutil.copy(pyipath + "/ElaWidgetTools.pyi", "objects")

dirname = f"{binding}ElaWidgetTools"
os.mkdir(f"wheel/{dirname}")
shutil.copy("objects/ElaWidgetTools.pyd", f"wheel/{dirname}")
shutil.copy("objects/ElaWidgetTools.pyi", f"wheel/{dirname}")

with open("wheel/__init__.py", "r") as ff:
    init = ff.read()
with open(f"wheel/{dirname}/__init__.py", "w") as ff:
    ff.write(f"from {binding} import QtCore, QtWidgets, QtGui\n" + init)

#
os.chdir("wheel")
subprocess.run(f"{pyPathEx} -m pip install setuptools wheel", shell=True)

req = ""
if binding.lower().startswith("pyside"):
    req = f"PySide6=={qtversion}"
subprocess.run(
    f"{pyPathEx} setup.py bdist_wheel {req} {('64','32')[arch == 'x86']} {binding}",
    shell=True,
)
os.chdir("..")

shutil.copytree("wheel/dist", "objects/wheel")

for f in os.listdir("objects/wheel"):
    shutil.move("objects/wheel/" + f, "objects/wheel/" + f.lower())
