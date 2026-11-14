from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_Navigation(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("导航与标签")
        self.createCustomWidget("通过路径、分类与标签组织内容，点击控件查看当前导航位置。", "导航与标签")
        mainLayout = self.createPageLayout()

        # 路径导航 · ElaBreadcrumbBar
        breadcrumbSection = self.addExampleSection(
            mainLayout, "路径导航 · ElaBreadcrumbBar", "点击上级路径返回，使用还原按钮重新展示完整路径。"
        )
        path = ["工作空间", "设计系统", "组件库", "导航组件"]
        self._breadcrumbBar = ElaBreadcrumbBar(self)
        self._breadcrumbBar.setBreadcrumbList(path)
        resetButton = ElaPushButton("还原路径", self)
        resetButton.setFixedWidth(100)
        breadcrumbResultText = ElaText("当前位置：导航组件", self)

        def _onResetClicked():
            self._breadcrumbBar.setBreadcrumbList(path)
            breadcrumbResultText.setText("当前位置：导航组件")

        resetButton.clicked.connect(_onResetClicked)

        def _onBreadcrumbClicked(value, _paths):
            breadcrumbResultText.setText("当前位置：" + value)

        self._breadcrumbBar.breadcrumbClicked.connect(_onBreadcrumbClicked)
        breadcrumbSection.addWidget(self._breadcrumbBar)
        breadcrumbActionLayout = QHBoxLayout()
        breadcrumbActionLayout.addWidget(breadcrumbResultText, 1)
        breadcrumbActionLayout.addWidget(resetButton)
        breadcrumbSection.addLayout(breadcrumbActionLayout)

        # 分类切换 · ElaPivot
        pivotSection = self.addExampleSection(
            mainLayout, "分类切换 · ElaPivot", "点击分类，观察选中标记和内容的联动。"
        )
        self._pivot = ElaPivot(self)
        self._pivot.setPivotSpacing(18)
        self._pivot.setMarkWidth(28)
        categories = ["概览", "设计", "开发", "发布"]
        for title in categories:
            self._pivot.appendPivot(title)
        self._pivot.setCurrentIndex(0)
        pivotResultText = ElaText("概览：查看项目进度与最近活动。", self)
        descriptions = [
            "概览：查看项目进度与最近活动。",
            "设计：整理视觉规范和交互说明。",
            "开发：浏览组件实现与接口。",
            "发布：检查版本信息与交付清单。",
        ]

        def _onPivotClicked(index):
            if 0 <= index < len(descriptions):
                pivotResultText.setText(descriptions[index])

        self._pivot.pivotClicked.connect(_onPivotClicked)
        pivotSection.addWidget(self._pivot)
        pivotSection.addWidget(pivotResultText)

        # 多文档标签 · ElaTabWidget
        tabSection = self.addExampleSection(
            mainLayout, "多文档标签 · ElaTabWidget", "切换、拖动或关闭标签；右键可固定标签，也可以新增一个页面。"
        )
        addButton = ElaPushButton("新增标签", self)
        self._tabWidget = ElaTabWidget(self)
        self._tabWidget.setFixedHeight(280)
        self._tabWidget.setIsTabTransparent(True)
        self._tabWidget.setIsTabWidthAdaptive(True)
        # 页面控件需保持强引用（见 T_Card 的说明：旧 wheel 未转移所有权）
        self._tabPages = []
        for title in ["项目概览", "界面设计", "开发记录"]:
            pageText = ElaText(title + "\n\n这是一个可以独立切换的文档页面", self)
            pageText.setTextPixelSize(18)
            pageText.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self._tabPages.append(pageText)
            self._tabWidget.addTab(pageText, title)

        def _onAddClicked():
            title = "新文档 {}".format(self._tabWidget.count() + 1)
            pageText = ElaText(title, self)
            pageText.setTextPixelSize(18)
            pageText.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self._tabPages.append(pageText)
            self._tabWidget.setCurrentIndex(self._tabWidget.addTab(pageText, title))

        addButton.clicked.connect(_onAddClicked)

        def _onTabCloseRequested(index):
            page = self._tabWidget.widget(index)
            self._tabWidget.removeTab(index)
            page.deleteLater()

        self._tabWidget.tabCloseRequested.connect(_onTabCloseRequested)

        def _onTabContextMenuRequested(index, position):
            menu = ElaMenu(self)
            isPinned = self._tabWidget.getIsTabPinned(index)

            def _onTogglePinned():
                self._tabWidget.setIsTabPinned(index, not isPinned)

            menu.addAction("取消固定" if isPinned else "固定标签").triggered.connect(_onTogglePinned)
            menu.exec(position)
            # 对应 C++ 的栈上菜单：用完即毁，避免挂在页面下累积
            menu.deleteLater()

        self._tabWidget.tabContextMenuRequested.connect(_onTabContextMenuRequested)
        tabSection.addWidget(addButton, 0, Qt.AlignmentFlag.AlignLeft)
        tabSection.addWidget(self._tabWidget)
