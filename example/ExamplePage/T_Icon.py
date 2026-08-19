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
        # 预览窗口标题
        self.setWindowTitle("ElaIcon")
        # 顶部元素
        self.createCustomWidget("一堆常用图标被放置于此，左键单击以复制其枚举")

        centralWidget = QWidget(self)
        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setContentsMargins(0, 0, 5, 0)
        centralWidget.setWindowTitle("ElaIcon")

        # ListView
        self._iconView = ElaListView(self)
        self._iconView.setIsTransparent(True)
        self._iconView.setFlow(QListView.Flow.LeftToRight)
        self._iconView.setViewMode(QListView.ViewMode.IconMode)
        self._iconView.setResizeMode(QListView.ResizeMode.Adjust)

        def _clicked(index):
            iconName = self._iconModel.getIconNameFromModelIndex(index)
            if not iconName:
                return
            QGuiApplication.clipboard().setText(iconName)
            ElaMessageBar.success(
                ElaMessageBarType.PositionPolicy.Top,
                "复制完成",
                iconName + "已被复制到剪贴板",
                1000,
                self,
            )

        self._iconView.clicked.connect(_clicked)

        self._iconModel = T_IconModel(self)
        self._iconDelegate = T_IconDelegate(self)
        self._iconView.setModel(self._iconModel)
        self._iconView.setItemDelegate(self._iconDelegate)
        self._iconView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self._searchEdit = ElaLineEdit(self)
        self._searchEdit.setPlaceholderText("搜索图标")
        self._searchEdit.setFixedSize(300, 35)
        self._searchEdit.textEdited.connect(self.onSearchEditTextEdit)
        self._searchEdit.focusIn.connect(self.onSearchEditTextEdit)

        centerVLayout.addSpacing(13)
        centerVLayout.addWidget(self._searchEdit)
        centerVLayout.addWidget(self._iconView)
        self.addCentralWidget(centralWidget, True, True, 0)

    def onSearchEditTextEdit(self, searchText):
        if not searchText:
            self._iconModel.setIsSearchMode(False)
            self._iconModel.setSearchKeyList([])
            self._iconView.clearSelection()
            self._iconView.viewport().update()
            return
        searchKeyList = []
        for key in self._iconModel.getAllIconNames():
            if searchText.lower() in key.lower():
                searchKeyList.append(key)
        self._iconModel.setIsSearchMode(True)
        self._iconModel.setSearchKeyList(searchKeyList)
        self._iconView.clearSelection()
        self._iconView.scrollTo(self._iconModel.index(0, 0))
        self._iconView.viewport().update()
