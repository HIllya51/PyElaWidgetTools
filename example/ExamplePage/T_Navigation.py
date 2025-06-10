from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_Navigation(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("ElaNavigation")

        self.createCustomWidget(
            "一些导航组件被放置于此，可在此界面体验其效果并按需添加进项目中"
        )

        breadcrumbBarText = ElaText("ElaBreadcrumbBar", self)
        breadcrumbBarText.setTextPixelSize(18)
        _breadcrumbBar = ElaBreadcrumbBar(self)
        breadcrumbBarList = []
        for i in range(20):
            breadcrumbBarList.append("Item{}".format(i + 1))

        _breadcrumbBar.setBreadcrumbList(breadcrumbBarList)

        resetButton = ElaPushButton("还原", self)
        resetButton.setFixedSize(60, 32)
        resetButton.clicked.connect(
            lambda: _breadcrumbBar.setBreadcrumbList(breadcrumbBarList)
        )

        breadcrumbBarTextLayout = QHBoxLayout()
        breadcrumbBarTextLayout.addWidget(breadcrumbBarText)
        breadcrumbBarTextLayout.addSpacing(15)
        breadcrumbBarTextLayout.addWidget(resetButton)
        breadcrumbBarTextLayout.addStretch()

        breadcrumbBarArea = ElaScrollPageArea(self)
        breadcrumbBarLayout = QVBoxLayout(breadcrumbBarArea)
        breadcrumbBarLayout.addWidget(_breadcrumbBar)

        pivotText = ElaText("ElaPivot", self)
        pivotText.setTextPixelSize(18)
        _pivot = ElaPivot(self)
        _pivot.setPivotSpacing(8)
        _pivot.setMarkWidth(75)
        _pivot.appendPivot("本地歌曲")
        _pivot.appendPivot("下载歌曲")
        _pivot.appendPivot("下载视频")
        _pivot.appendPivot("正在下载")
        _pivot.setCurrentIndex(0)

        pivotArea = ElaScrollPageArea(self)
        pivotLayout = QVBoxLayout(pivotArea)
        pivotLayout.addWidget(_pivot)

        tabWidgetText = ElaText("ElaTabWidget", self)
        tabWidgetText.setTextPixelSize(18)
        _tabWidget = ElaTabWidget(self)
        _tabWidget.setFixedHeight(500)
        page1 = QLabel("新标签页1", self)
        page1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = page1.font()
        font.setPixelSize(32)
        page1.setFont(font)
        page2 = QLabel("新标签页2", self)
        page2.setFont(font)
        page2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        page3 = QLabel("新标签页3", self)
        page3.setFont(font)
        page3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        page4 = QLabel("新标签页4", self)
        page4.setFont(font)
        page4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _tabWidget.addTab(page1, QIcon(":/Resource/Image/Cirno.jpg"), "新标签页1")
        _tabWidget.addTab(page2, "新标签页2")
        _tabWidget.addTab(page3, "新标签页3")
        _tabWidget.addTab(page4, "新标签页4")
        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaNavigation")
        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setContentsMargins(0, 0, 0, 0)
        centerVLayout.addLayout(breadcrumbBarTextLayout)
        centerVLayout.addSpacing(10)
        centerVLayout.addWidget(breadcrumbBarArea)
        centerVLayout.addSpacing(15)
        centerVLayout.addWidget(pivotText)
        centerVLayout.addSpacing(10)
        centerVLayout.addWidget(pivotArea)
        centerVLayout.addSpacing(15)
        centerVLayout.addWidget(tabWidgetText)
        centerVLayout.addSpacing(10)
        centerVLayout.addWidget(_tabWidget)
        self.addCentralWidget(centralWidget, True, False, 0)
