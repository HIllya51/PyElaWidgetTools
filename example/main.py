import sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5ElaWidgetTools import *
from mainwindow import *

try:
    QT_VERSION_STR
except:
    QT_VERSION_STR = "6.8.3"

if QT_VERSION_STR < "6.0.0":
    QGuiApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
    if QT_VERSION_STR >= "5.14.0":
        QGuiApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
        QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
        )

app = QApplication(sys.argv)
eApp.init()
w = MainWindow()
w.show()
app.exec()
