from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *

class T_Icon(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaIcon");
        
        self.createCustomWidget("一堆常用图标被放置于此，左键单击以复制其枚举");

        _metaEnum = QMetaEnum()#<ElaIconType::IconName>();
        centralWidget = QWidget(self);
        centerVLayout = QVBoxLayout(centralWidget);
        centerVLayout.setContentsMargins(0, 0, 5, 0);
        centralWidget.setWindowTitle("ElaIcon");
        
        _iconView = ElaListView(self);
        _iconView.setIsTransparent(True);
        _iconView.setFlow(QListView.Flow.LeftToRight);
        _iconView.setViewMode(QListView.ViewMode.IconMode);
        _iconView.setResizeMode(QListView.ResizeMode.Adjust);
    #     def __(index:QModelIndex):
    #         iconName = _iconModel.getIconNameFromModelIndex(index);
    #         if (iconName.isEmpty())
    #         {
    #             return;
    #         }
    #         qApp.clipboard().setText(iconName);
    #         ElaMessageBar::success(ElaMessageBarType::Top, "复制完成", iconName + "已被复制到剪贴板", 1000, self);
    #     _iconView.clicked.connect(__)
    #     connect(_iconView, &ElaListView::clicked, self, [=](const QModelIndex& index) {
    #         QString iconName = _iconModel.getIconNameFromModelIndex(index);
    #         if (iconName.isEmpty())
    #         {
    #             return;
    #         }
    #         qApp.clipboard().setText(iconName);
    #         ElaMessageBar::success(ElaMessageBarType::Top, "复制完成", iconName + "已被复制到剪贴板", 1000, self);
    #     });
    #     _iconModel = T_IconModel(self);
    #     _iconDelegate = T_IconDelegate(self);
    #     _iconView.setModel(_iconModel);
    #     _iconView.setItemDelegate(_iconDelegate);
    #     _iconView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff);

        _searchEdit = ElaLineEdit(self);
        _searchEdit.setPlaceholderText("搜索图标");
        _searchEdit.setFixedSize(300, 35);
        
        #connect(_searchEdit, &ElaLineEdit::textEdited, self, &T_Icon::onSearchEditTextEdit);
       # connect(_searchEdit, &ElaLineEdit::focusIn, self, &T_Icon::onSearchEditTextEdit);

        centerVLayout.addSpacing(13);
        centerVLayout.addWidget(_searchEdit);
        centerVLayout.addWidget(_iconView);
        self.addCentralWidget(centralWidget, True, True, 0);