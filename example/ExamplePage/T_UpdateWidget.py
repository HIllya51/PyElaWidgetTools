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
        updateTitle = ElaText("2025-5-25更新", 15, self)
        update1 = ElaText("1、适配原生Mica、Mica-Alt、Acrylic、Dwm-Blur模式", 13, self)
        update2 = ElaText("2、优化列表组件的视觉效果", 13, self)
        update3 = ElaText("3、修正ElaComboBox可编辑模式下不正确的显示状态", 13, self)
        update4 = ElaText("4、新增ElaProgressRing环形进度条组件", 13, self)
        update5 = ElaText("4、QQ交流群: 850243692", 13, self)
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
