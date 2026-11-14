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
        updateTitle = ElaText("2026-11-14 更新汇总", 15, self)
        update1 = ElaText("1、优化控件配色与焦点动画，改善主题切换及交互反馈。", 13, self)
        update2 = ElaText("2、完善下拉框与菜单展开效果，优化弹出定位及圆角阴影。", 13, self)
        update3 = ElaText("3、改进抽屉展开与收回动画，完善内容适配及标题交互。", 13, self)
        update4 = ElaText("4、优化日历切换与日期显示，完善列表样式及表格排序。", 13, self)
        update1.setIsWrapAnywhere(True)
        update2.setIsWrapAnywhere(True)
        update3.setIsWrapAnywhere(True)
        update4.setIsWrapAnywhere(True)

        mainLayout.addWidget(updateTitle)
        mainLayout.addWidget(update1)
        mainLayout.addWidget(update2)
        mainLayout.addWidget(update3)
        mainLayout.addWidget(update4)
        mainLayout.addStretch()
