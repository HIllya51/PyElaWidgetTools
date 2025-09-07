import re, os

asQt5 = True
asSide6 = False

os.chdir(os.path.dirname(os.path.abspath(__file__)))

for _d, _, _fs in os.walk("."):
    for _f in _fs:
        if _f == "beforemain.py":
            continue
        if _f.endswith(".py"):
            with open(_d + "/" + _f, "r", encoding="utf8") as ff:
                s = ff.read()

            with open(_d + "/" + _f, "w", encoding="utf8") as ff:

                if asSide6:
                    s = re.sub("PyQt[56]", "PySide6", s)
                    s = re.sub("PyQt[56]ElaWidgetTools", "PySide6ElaWidgetTools", s)
                    s = re.sub("addPageNodeKeyPoints", "addPageNode", s)  # 不可逆
                else:
                    s = re.sub("PySide6", "PyQt5", s)
                    s = re.sub("PySide6ElaWidgetTools", "PyQt5ElaWidgetTools", s)
                    if asQt5:
                        s = s.replace("PyQt6", "PyQt5").replace(
                            "PyQt6ElaWidgetTools", "PyQt5ElaWidgetTools"
                        )
                    else:
                        s = s.replace("PyQt5", "PyQt6").replace(
                            "PyQt5ElaWidgetTools", "PyQt6ElaWidgetTools"
                        )

                ff.write(s)


from main import *
