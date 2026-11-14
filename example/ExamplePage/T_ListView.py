from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *
from ModelView.T_ListViewModel import *


class T_ListView(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("列表视图")
        self.createCustomWidget("搜索列表内容，尝试单选、多选以及不同的行背景。", "列表视图")
        mainLayout = self.createPageLayout()
        section = self.addExampleSection(
            mainLayout, "资源列表 · ElaListView", "启用多选后，可使用 Ctrl 或 Shift 连续选择多个条目。"
        )
        searchEdit = ElaLineEdit(self)
        searchEdit.setFixedWidth(260)
        searchEdit.setPlaceholderText("搜索资源名称")
        searchEdit.setClearButtonEnabled(True)
        multiCheckBox = ElaCheckBox("允许多选", self)
        multiCheckBox.setFixedHeight(searchEdit.height())
        alternatingCheckBox = ElaCheckBox("交替行背景", self)
        alternatingCheckBox.setFixedHeight(searchEdit.height())
        optionsLayout = ElaFlowLayout(0, 20, 12)
        optionsLayout.addWidget(searchEdit)
        optionsLayout.addWidget(multiCheckBox)
        optionsLayout.addWidget(alternatingCheckBox)

        self._listView = ElaListView(self)
        self._listView.setFixedHeight(350)
        self._listView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        resourceModel = T_ListViewModel(self)
        filterModel = QSortFilterProxyModel(self)
        filterModel.setSourceModel(resourceModel)
        filterModel.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self._listView.setModel(filterModel)
        resultText = ElaText("选择结果：尚未选择", self)

        def _onMultiToggled(checked):
            self._listView.clearSelection()
            self._listView.setSelectionMode(
                QAbstractItemView.SelectionMode.ExtendedSelection
                if checked
                else QAbstractItemView.SelectionMode.SingleSelection
            )

        searchEdit.textChanged.connect(filterModel.setFilterFixedString)
        multiCheckBox.toggled.connect(_onMultiToggled)
        alternatingCheckBox.toggled.connect(self._listView.setAlternatingRowColors)

        def _onSelectionChanged():
            indexes = self._listView.selectionModel().selectedIndexes()
            resultText.setText(
                "选择结果：尚未选择"
                if not indexes
                else "已选 {} 项 · {}".format(len(indexes), indexes[0].data())
            )

        self._listView.selectionModel().selectionChanged.connect(_onSelectionChanged)
        resultText.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        section.addLayout(optionsLayout)
        section.addWidget(self._listView)
        section.addWidget(resultText)
