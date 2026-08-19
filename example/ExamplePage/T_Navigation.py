from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *
from _res import *


class T_Navigation(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaNavigation")

        self.createCustomWidget("一些导航组件被放置于此，可在此界面体验其效果并按需添加进项目中")

        # ElaBreadcrumbBar
        breadcrumbBarText = ElaText("ElaBreadcrumbBar", self)
        breadcrumbBarText.setTextPixelSize(18)
        self._breadcrumbBar = ElaBreadcrumbBar(self)
        breadcrumbBarList = []
        for i in range(20):
            breadcrumbBarList.append("Item{}".format(i + 1))
        self._breadcrumbBar.setBreadcrumbList(breadcrumbBarList)

        resetButton = ElaPushButton("还原", self)
        resetButton.setFixedSize(60, 32)
        resetButton.clicked.connect(
            lambda: self._breadcrumbBar.setBreadcrumbList(breadcrumbBarList)
        )

        breadcrumbBarTextLayout = QHBoxLayout()
        breadcrumbBarTextLayout.addWidget(breadcrumbBarText)
        breadcrumbBarTextLayout.addSpacing(15)
        breadcrumbBarTextLayout.addWidget(resetButton)
        breadcrumbBarTextLayout.addStretch()

        breadcrumbBarArea = ElaScrollPageArea(self)
        breadcrumbBarLayout = QVBoxLayout(breadcrumbBarArea)
        breadcrumbBarLayout.addWidget(self._breadcrumbBar)

        # ElaPivot
        pivotText = ElaText("ElaPivot", self)
        pivotText.setTextPixelSize(18)
        self._pivot = ElaPivot(self)
        self._pivot.setPivotSpacing(8)
        self._pivot.setMarkWidth(75)
        self._pivot.appendPivot("本地歌曲")
        self._pivot.appendPivot("下载歌曲")
        self._pivot.appendPivot("下载视频")
        self._pivot.appendPivot("正在下载")
        self._pivot.appendPivot("本地歌曲")
        self._pivot.appendPivot("下载歌曲")
        self._pivot.appendPivot("下载视频")
        self._pivot.appendPivot("正在下载")
        self._pivot.appendPivot("本地歌曲")
        self._pivot.appendPivot("下载歌曲")
        self._pivot.appendPivot("下载视频")
        self._pivot.appendPivot("正在下载")
        self._pivot.setCurrentIndex(0)

        pivotArea = ElaScrollPageArea(self)
        pivotLayout = QVBoxLayout(pivotArea)
        pivotLayout.addWidget(self._pivot)

        # ElaTabWidget
        tabWidgetText = ElaText("ElaTabWidget", self)
        tabWidgetText.setTextPixelSize(18)
        self._tabWidget = ElaTabWidget(self)
        self._tabWidget.setFixedHeight(600)
        self._tabWidget.setIsTabTransparent(True)
        page1 = ElaText("新标签页", self)
        page1.setTextPixelSize(32)
        page1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._tabWidget.addTab(page1, QIcon(placeholderPixmap(38, 38)), "新标签页")
        for i in range(5):
            page = ElaText("新标签页{}".format(i), self)
            page.setTextPixelSize(32)
            page.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self._tabWidget.addTab(page, "新标签页{}".format(i))

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
        centerVLayout.addWidget(self._tabWidget)
        centerVLayout.addStretch()
        self.addCentralWidget(centralWidget, True, False, 0)
