from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_UpdateWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 260)
        mainLayout = QVBoxLayout(self)
        mainLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        mainLayout.setContentsMargins(5, 10, 5, 5)
        mainLayout.setSpacing(4)
        updateTitle = ElaText("2026-8-14更新", 15, self)
        update1 = ElaText("1、新增ElaRibbon组件", 13, self)
        update2 = ElaText("2、ElaTabWidget等组件体验优化", 13, self)
        update3 = ElaText("3、无边框窗口动画效果优化", 13, self)
        update4 = ElaText("4、组件库整体API及规范优化", 13, self)
        update5 = ElaText("5、QQ交流群: 850243692", 13, self)
        update1.setIsWrapAnywhere(True)
        update2.setIsWrapAnywhere(True)
        update3.setIsWrapAnywhere(True)
        update4.setIsWrapAnywhere(True)

        mainLayout.addWidget(updateTitle)
        mainLayout.addWidget(update1)
        mainLayout.addWidget(update2)
        mainLayout.addWidget(update3)
        mainLayout.addWidget(update4)
        mainLayout.addWidget(update5)
        mainLayout.addStretch()
