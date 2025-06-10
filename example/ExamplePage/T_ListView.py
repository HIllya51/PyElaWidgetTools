from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *
from ModelView.T_ListViewModel import *


class T_ListView(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaListView")

        self.createCustomWidget(
            "列表视图被放置于此，可在此界面体验其效果并按需添加进项目中"
        )

        listText = ElaText("ElaListView", self)
        listText.setTextPixelSize(18)
        _listView = ElaListView(self)
        _listView.setFixedHeight(450)
        _listView.setModel(T_ListViewModel(self))
        listViewFloatScrollBar = ElaScrollBar(_listView.verticalScrollBar(), _listView)
        listViewFloatScrollBar.setIsAnimation(True)
        listViewLayout = QHBoxLayout()
        listViewLayout.setContentsMargins(0, 0, 10, 0)
        listViewLayout.addWidget(_listView)

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaView")
        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setContentsMargins(0, 0, 0, 0)
        centerVLayout.addWidget(listText)
        centerVLayout.addSpacing(10)
        centerVLayout.addLayout(listViewLayout)
        centerVLayout.addStretch()
        self.addCentralWidget(centralWidget, True, False, 0)
