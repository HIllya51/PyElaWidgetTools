import sys, os

asQt5 = True

os.chdir(os.path.dirname(os.path.abspath(__file__)))

for _d, _, _fs in os.walk("."):
    for _f in _fs:
        if _f == "beforemain.py":
            continue
        if _f.endswith(".py"):
            with open(_d + "/" + _f, "r", encoding="utf8") as ff:
                s = ff.read()

            with open(_d + "/" + _f, "w", encoding="utf8") as ff:
                if asQt5:
                    ff.write(
                        s.replace("PyQt6", "PyQt5").replace(
                            "PyQt6ElaWidgetTools", "PyQt5ElaWidgetTools"
                        )
                    )
                else:
                    ff.write(
                        s.replace("PyQt5", "PyQt6").replace(
                            "PyQt5ElaWidgetTools", "PyQt6ElaWidgetTools"
                        )
                    )

from main import *