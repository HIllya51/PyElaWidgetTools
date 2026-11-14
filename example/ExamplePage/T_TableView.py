from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *
from ModelView.T_TableViewModel import *


class T_TableView(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("表格视图")
        self.createCustomWidget("在多列数据中搜索、排序与选择，拖动表头边界可调整列宽。", "表格视图")
        mainLayout = self.createPageLayout()
        section = self.addExampleSection(
            mainLayout, "音乐资料库 · ElaTableView", "输入歌名、歌手或专辑筛选，点击列标题切换排序。"
        )
        searchEdit = ElaLineEdit(self)
        searchEdit.setFixedWidth(280)
        searchEdit.setPlaceholderText("搜索歌名、歌手或专辑")
        searchEdit.setClearButtonEnabled(True)
        alternatingCheckBox = ElaCheckBox("交替行背景", self)
        alternatingCheckBox.setFixedHeight(searchEdit.height())
        alternatingCheckBox.setChecked(True)
        optionsLayout = ElaFlowLayout(0, 20, 12)
        optionsLayout.addWidget(searchEdit)
        optionsLayout.addWidget(alternatingCheckBox)

        self._tableView = ElaTableView(self)
        libraryModel = T_TableViewModel(self)
        filterModel = T_MusicFilterModel(self)
        filterModel.setSourceModel(libraryModel)
        filterModel.setFilterKeyColumn(-1)
        filterModel.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self._tableView.setModel(filterModel)
        self._tableView.setAlternatingRowColors(True)
        # 初始保持源模型顺序 点击表头后再按对应列排序
        self._tableView.horizontalHeader().setSortIndicator(-1, Qt.SortOrder.AscendingOrder)
        self._tableView.setSortingEnabled(True)
        self._tableView.setIconSize(QSize(32, 32))
        self._tableView.verticalHeader().hide()
        self._tableView.verticalHeader().setDefaultSectionSize(44)
        self._tableView.horizontalHeader().setMinimumSectionSize(48)
        self._tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self._tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self._tableView.setColumnWidth(0, 52)
        self._tableView.setColumnWidth(2, 130)
        self._tableView.setColumnWidth(3, 150)
        self._tableView.setColumnWidth(4, 68)
        self._tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self._tableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self._tableView.setFixedHeight(380)
        resultText = ElaText("点击一行查看选择结果", self)
        resultText.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)

        def _onCurrentRowChanged(current, _previous):
            resultText.setText(
                "当前选择：{} · {}".format(
                    current.sibling(current.row(), 1).data(),
                    current.sibling(current.row(), 2).data(),
                )
                if current.isValid()
                else "点击一行查看选择结果"
            )

        searchEdit.textChanged.connect(filterModel.setFilterFixedString)
        alternatingCheckBox.toggled.connect(self._tableView.setAlternatingRowColors)
        self._tableView.selectionModel().currentRowChanged.connect(_onCurrentRowChanged)
        section.addLayout(optionsLayout)
        section.addWidget(self._tableView)
        section.addWidget(resultText)
