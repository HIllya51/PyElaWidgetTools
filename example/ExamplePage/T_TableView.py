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

        self.createCustomWidget(
            "表格视图被放置于此，可在此界面体验其效果并按需添加进项目中"
        )

        tableText = ElaText("ElaTableView", self)
        tableText.setTextPixelSize(18)
        _tableView = ElaTableView(self)

        tableHeaderFont = _tableView.horizontalHeader().font()
        tableHeaderFont.setPixelSize(16)
        _tableView.horizontalHeader().setFont(tableHeaderFont)
        _tableView.setModel(T_TableViewModel(self))
        _tableView.setAlternatingRowColors(True)
        _tableView.setIconSize(QSize(38, 38))
        _tableView.verticalHeader().setHidden(True)
        _tableView.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Interactive
        )
        _tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        _tableView.horizontalHeader().setMinimumSectionSize(60)
        _tableView.verticalHeader().setMinimumSectionSize(46)
        _tableView.setFixedHeight(450)

        def __():
            _tableView.setColumnWidth(0, 60)
            _tableView.setColumnWidth(1, 205)
            _tableView.setColumnWidth(2, 170)
            _tableView.setColumnWidth(3, 150)
            _tableView.setColumnWidth(4, 60)

        _tableView.tableViewShow.connect(__)
        tableViewLayout = QHBoxLayout()
        tableViewLayout.setContentsMargins(0, 0, 10, 0)
        tableViewLayout.addWidget(_tableView)

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaView")
        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setContentsMargins(0, 0, 0, 0)
        centerVLayout.addWidget(tableText)
        centerVLayout.addSpacing(10)
        centerVLayout.addLayout(tableViewLayout)
        centerVLayout.addStretch()
        self.addCentralWidget(centralWidget, True, False, 0)
