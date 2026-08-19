from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *
from ModelView.T_TableViewModel import *


class T_TableView(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaTableView")

        self.createCustomWidget("表格视图被放置于此，可在此界面体验其效果并按需添加进项目中")

        tableText = ElaText("ElaTableView", self)
        tableText.setTextPixelSize(18)
        self._tableView = ElaTableView(self)
        tableHeaderFont = self._tableView.horizontalHeader().font()
        tableHeaderFont.setPixelSize(16)
        self._tableView.horizontalHeader().setFont(tableHeaderFont)
        self._tableView.setModel(T_TableViewModel(self))
        self._tableView.setAlternatingRowColors(True)
        self._tableView.setIconSize(QSize(38, 38))
        self._tableView.verticalHeader().setHidden(True)
        self._tableView.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Interactive
        )
        self._tableView.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self._tableView.horizontalHeader().setMinimumSectionSize(60)
        self._tableView.verticalHeader().setMinimumSectionSize(46)
        self._tableView.setFixedHeight(450)
        self._tableView.tableViewShow.connect(self._onTableViewShow)
        tableViewLayout = QHBoxLayout()
        tableViewLayout.setContentsMargins(0, 0, 10, 0)
        tableViewLayout.addWidget(self._tableView)

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaView")
        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setContentsMargins(0, 0, 0, 0)
        centerVLayout.addWidget(tableText)
        centerVLayout.addSpacing(10)
        centerVLayout.addLayout(tableViewLayout)
        centerVLayout.addStretch()
        self.addCentralWidget(centralWidget, True, False, 0)

    def _onTableViewShow(self):
        self._tableView.setColumnWidth(0, 60)
        self._tableView.setColumnWidth(1, 205)
        self._tableView.setColumnWidth(2, 170)
        self._tableView.setColumnWidth(3, 150)
        self._tableView.setColumnWidth(4, 60)
