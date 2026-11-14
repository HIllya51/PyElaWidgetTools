from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *
from ModelView.T_IconModel import *
from ModelView.T_IconDelegate import *


class T_Icon(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("图标资源")
        self.createCustomWidget("按英文名称搜索图标，点击图标复制对应的 ElaIconType 枚举。", "图标资源")
        mainLayout = self.createPageLayout()
        section = self.addExampleSection(
            mainLayout, "图标浏览器", "悬停可查看完整名称，支持大小写不敏感的关键字搜索。"
        )

        self._iconModel = T_IconModel(self)
        self._iconDelegate = T_IconDelegate(self)

        self._searchEdit = ElaLineEdit(self)
        self._searchEdit.setPlaceholderText("搜索图标，例如 Search、Folder、Arrow")
        self._searchEdit.setClearButtonEnabled(True)
        self._searchEdit.setMinimumWidth(120)
        self._searchEdit.setMaximumWidth(360)
        self._resultText = ElaText("{} 个图标".format(self._iconModel.rowCount()), self)
        self._resultText.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        searchLayout = QHBoxLayout()
        searchLayout.setSpacing(16)
        searchLayout.addWidget(self._searchEdit, 1)
        searchLayout.addWidget(self._resultText)

        self._iconView = ElaListView(self)
        self._iconView.setIsTransparent(True)
        self._iconView.setFlow(QListView.Flow.LeftToRight)
        self._iconView.setViewMode(QListView.ViewMode.IconMode)
        self._iconView.setResizeMode(QListView.ResizeMode.Adjust)
        self._iconView.setUniformItemSizes(True)
        self._iconView.setSpacing(4)
        self._iconView.setFixedHeight(420)
        self._iconView.setModel(self._iconModel)
        self._iconView.setItemDelegate(self._iconDelegate)
        self._iconView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._emptyText = ElaText("没有找到匹配的图标，请尝试其他关键字。", self)
        self._emptyText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._emptyText.setMinimumHeight(140)
        self._emptyText.hide()
        selectedText = ElaText("点击一个图标即可复制枚举名称", self)
        selectedText.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        selectedText.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)

        def _clicked(index):
            iconName = self._iconModel.getIconNameFromModelIndex(index)
            if iconName:
                QGuiApplication.clipboard().setText(iconName)
                selectedText.setText("已复制：" + iconName)

        self._iconView.clicked.connect(_clicked)
        self._searchEdit.textChanged.connect(self.onSearchEditTextEdit)
        section.addLayout(searchLayout)
        section.addWidget(self._iconView)
        section.addWidget(self._emptyText)
        section.addWidget(selectedText)

    def onSearchEditTextEdit(self, searchText):
        query = searchText.strip()
        names = []
        if query:
            for name in self._iconModel.getAllIconNames():
                if query.lower() in name.lower():
                    names.append(name)
        self._iconModel.setIsSearchMode(bool(query))
        self._iconModel.setSearchKeyList(names)
        self._iconView.clearSelection()
        self._iconView.scrollToTop()
        count = self._iconModel.rowCount()
        self._resultText.setText("{} 个图标".format(count))
        self._emptyText.setVisible(count == 0)
        self._iconView.setVisible(count > 0)
