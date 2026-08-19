import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5ElaWidgetTools import *
from _res import *
from ExamplePage.T_Home import *
from ExamplePage.T_Icon import *
from ExamplePage.T_BaseComponents import *
from ExamplePage.T_Navigation import *
from ExamplePage.T_Popup import *
from ExamplePage.T_Card import *
from ExamplePage.T_ListView import *
from ExamplePage.T_TableView import *
from ExamplePage.T_TreeView import *
from ExamplePage.T_Setting import *
from ExamplePage.T_About import *
from ExamplePage.T_LogWidget import *
from ExamplePage.T_UpdateWidget import *
if sys.platform == "win32":
    from ExamplePage.T_ElaScreen import *


class MainWindow(ElaWindow):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.initWindow()
        self.initEdgeLayout()
        self.initContent()

        # 拦截默认关闭事件
        self._closeDialog = ElaContentDialog(self)
        self._closeDialog.rightButtonClicked.connect(self.close)
        self._closeDialog.middleButtonClicked.connect(
            lambda: (self._closeDialog.close(), self.showMinimized())
        )
        self.setIsDefaultClosed(False)
        self.closeButtonClicked.connect(lambda: self._closeDialog.exec())

        self.moveToCenter()

    def initWindow(self):
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setWindowIcon(QIcon(placeholderPixmap(64, 64)))
        self.resize(1200, 740)
        self.setUserInfoCardPixmap(QPixmap(placeholderPixmap(64, 64)))
        self.setUserInfoCardTitle("Ela Tool")
        self.setUserInfoCardSubTitle("Liniyous@gmail.com")
        self.setWindowTitle("ElaWidgetTool")

        centralStack = ElaText("这是一个主窗口堆栈页面", self)
        centralStack.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        centralStack.setTextPixelSize(32)
        centralStack.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.addCentralWidget(centralStack)

        # 窗口绘制模式（占位 pixmap，无图片资源；movie 无文件故跳过）
        self.setWindowPixmap(ElaThemeType.ThemeMode.Light, QPixmap(placeholderPixmap(64, 64)))
        self.setWindowPixmap(ElaThemeType.ThemeMode.Dark, QPixmap(placeholderPixmap(64, 64)))

        # 自定义 AppBar 菜单
        appBarMenu = ElaMenu(self)
        appBarMenu.setMenuItemHeight(27)
        appBarMenu.addAction("跳转到一级主要堆栈").triggered.connect(lambda: self.setCurrentStackIndex(0))
        appBarMenu.addAction("跳转到二级主要堆栈").triggered.connect(lambda: self.setCurrentStackIndex(1))
        appBarMenu.addAction("更改页面切换特效(Scale)").triggered.connect(
            lambda: self.setStackSwitchMode(ElaWindowType.StackSwitchMode.Scale)
        )
        appBarMenu.addElaIconAction(ElaIconType.IconName.GearComplex, "自定义主窗口设置").triggered.connect(
            lambda: self.navigation(self._settingKey)
        )
        appBarMenu.addSeparator()
        appBarMenu.addElaIconAction(ElaIconType.IconName.MoonStars, "更改项目主题").triggered.connect(
            lambda: eTheme.setThemeMode(
                ElaThemeType.ThemeMode.Dark
                if eTheme.getThemeMode() == ElaThemeType.ThemeMode.Light
                else ElaThemeType.ThemeMode.Light
            )
        )
        appBarMenu.addAction("使用原生菜单").triggered.connect(lambda: self.setCustomMenu(None))
        self.setCustomMenu(appBarMenu)

        # 堆栈独立自定义窗口
        centralCustomWidget = QWidget(self)
        centralCustomWidgetLayout = QHBoxLayout(centralCustomWidget)
        centralCustomWidgetLayout.setContentsMargins(13, 15, 9, 6)

        leftButton = ElaToolButton(self)
        leftButton.setElaIcon(ElaIconType.IconName.AngleLeft)
        leftButton.setEnabled(False)
        leftButton.clicked.connect(lambda: ElaActionCommander.getInstance().undoCommand("ElaWidgetToolsAction"))

        rightButton = ElaToolButton(self)
        rightButton.setElaIcon(ElaIconType.IconName.AngleRight)
        rightButton.setEnabled(False)
        rightButton.clicked.connect(lambda: ElaActionCommander.getInstance().redoCommand("ElaWidgetToolsAction"))

        def __onCommanderStateChanged(domainName: str, state: ElaActionCommanderType.CommanderState):
            if domainName != "ElaWidgetToolsAction":
                return
            if state == ElaActionCommanderType.CommanderState.UndoValid:
                leftButton.setEnabled(True)
            elif state == ElaActionCommanderType.CommanderState.UndoInvalid:
                leftButton.setEnabled(False)
            elif state == ElaActionCommanderType.CommanderState.RedoValid:
                rightButton.setEnabled(True)
            elif state == ElaActionCommanderType.CommanderState.RedoInvalid:
                rightButton.setEnabled(False)

        ElaActionCommander.getInstance().commanderStateChanged.connect(__onCommanderStateChanged)

        # SuggestBox：绑定 pyi 不完整，部分 API 可能缺失，整体兜底以免阻断启动
        self._windowSuggestBox = None
        try:
            self._windowSuggestBox = ElaSuggestBox(self)
            self._windowSuggestBox.setFixedHeight(32)
            self._windowSuggestBox.setPlaceholderText("搜索关键字")

            def __onSuggestionClicked(suggestData):
                try:
                    self.navigation(suggestData.getSuggestData().get("ElaPageKey"))
                except Exception:
                    pass

            self._windowSuggestBox.suggestionClicked.connect(__onSuggestionClicked)
        except Exception:
            self._windowSuggestBox = None

        progressBusyRingText = ElaText("系统运行中", self)
        progressBusyRingText.setIsWrapAnywhere(False)
        progressBusyRingText.setTextPixelSize(15)

        progressBusyRing = ElaProgressRing(self)
        progressBusyRing.setBusyingWidth(4)
        progressBusyRing.setFixedSize(28, 28)
        progressBusyRing.setIsBusying(True)

        centralCustomWidgetLayout.addWidget(leftButton)
        centralCustomWidgetLayout.addWidget(rightButton)
        if self._windowSuggestBox is not None:
            centralCustomWidgetLayout.addWidget(self._windowSuggestBox)
        centralCustomWidgetLayout.addStretch()
        centralCustomWidgetLayout.addWidget(progressBusyRingText)
        centralCustomWidgetLayout.addWidget(progressBusyRing)
        self.setCentralCustomWidget(centralCustomWidget)

    def initEdgeLayout(self):
        # 菜单栏
        menuBar = ElaMenuBar(self)
        menuBar.setFixedHeight(30)
        customWidget = QWidget(self)
        customWidget.setFixedWidth(500)
        customLayout = QVBoxLayout(customWidget)
        customLayout.setContentsMargins(0, 0, 0, 0)
        customLayout.addWidget(menuBar)
        customLayout.addStretch()
        self.setCustomWidget(ElaAppBarType.CustomArea.MiddleArea, customWidget)

        menuBar.addElaIconAction(ElaIconType.IconName.AtomSimple, "动作菜单")
        iconMenu = menuBar.addMenu(ElaIconType.IconName.Aperture, "图标菜单")
        iconMenu.setMenuItemHeight(27)
        iconMenu.addElaIconAction(ElaIconType.IconName.BoxCheck, "排序方式", QKeySequence.StandardKey.SelectAll)
        iconMenu.addElaIconAction(ElaIconType.IconName.Copy, "复制")
        iconMenu.addElaIconAction(ElaIconType.IconName.MagnifyingGlassPlus, "显示设置")
        iconMenu.addSeparator()
        iconMenu.addElaIconAction(ElaIconType.IconName.ArrowRotateRight, "刷新")
        iconMenu.addElaIconAction(ElaIconType.IconName.ArrowRotateLeft, "撤销")
        menuBar.addSeparator()

        shortCutMenu = ElaMenu("快捷菜单(&A)", self)
        shortCutMenu.setMenuItemHeight(27)
        shortCutMenu.addElaIconAction(ElaIconType.IconName.BoxCheck, "排序方式", QKeySequence.StandardKey.Find)
        shortCutMenu.addElaIconAction(ElaIconType.IconName.Copy, "复制")
        shortCutMenu.addElaIconAction(ElaIconType.IconName.MagnifyingGlassPlus, "显示设置")
        shortCutMenu.addSeparator()
        shortCutMenu.addElaIconAction(ElaIconType.IconName.ArrowRotateRight, "刷新")
        shortCutMenu.addElaIconAction(ElaIconType.IconName.ArrowRotateLeft, "撤销")
        menuBar.addMenu(shortCutMenu)

        for title in ["样例菜单(&B)", "样例菜单(&C)", "样例菜单(&E)", "样例菜单(&F)", "样例菜单(&G)"]:
            menuBar.addMenu(title).addElaIconAction(ElaIconType.IconName.ArrowRotateRight, "样例选项")

        # 工具栏
        toolBar = ElaToolBar("工具栏", self)
        toolBar.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea | Qt.ToolBarArea.BottomToolBarArea)
        toolBar.setToolBarSpacing(3)
        toolBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        toolBar.setIconSize(QSize(25, 25))
        for icon in [
            ElaIconType.IconName.BadgeCheck,
            ElaIconType.IconName.ChartUser,
        ]:
            tb = ElaToolButton(self)
            tb.setElaIcon(icon)
            toolBar.addWidget(tb)
        toolBar.addSeparator()
        tb = ElaToolButton(self)
        tb.setElaIcon(ElaIconType.IconName.Bluetooth)
        tb.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        tb.setText("Bluetooth")
        toolBar.addWidget(tb)
        tb = ElaToolButton(self)
        tb.setElaIcon(ElaIconType.IconName.BringFront)
        toolBar.addWidget(tb)
        toolBar.addSeparator()
        for icon in [
            ElaIconType.IconName.ChartSimple,
            ElaIconType.IconName.FaceClouds,
            ElaIconType.IconName.Aperture,
            ElaIconType.IconName.ChartMixed,
            ElaIconType.IconName.Coins,
        ]:
            t = ElaToolButton(self)
            t.setElaIcon(icon)
            toolBar.addWidget(t)
        tb = ElaToolButton(self)
        tb.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        tb.setElaIcon(ElaIconType.IconName.AlarmPlus)
        tb.setText("AlarmPlus")
        toolBar.addWidget(tb)
        tb = ElaToolButton(self)
        tb.setElaIcon(ElaIconType.IconName.Crown)
        toolBar.addWidget(tb)

        progressBar = ElaProgressBar(self)
        progressBar.setMinimum(0)
        progressBar.setMaximum(0)
        progressBar.setFixedWidth(350)
        toolBar.addWidget(progressBar)

        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolBar)

        # 停靠窗口
        logDockWidget = ElaDockWidget("日志信息", self)
        logDockWidget.setWidget(T_LogWidget(self))
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, logDockWidget)
        self.resizeDocks([logDockWidget], [200], Qt.Orientation.Horizontal)

        updateDockWidget = ElaDockWidget("更新内容", self)
        updateDockWidget.setWidget(T_UpdateWidget(self))
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, updateDockWidget)
        self.resizeDocks([updateDockWidget], [200], Qt.Orientation.Horizontal)

        # 状态栏
        statusBar = ElaStatusBar(self)
        statusText = ElaText("初始化成功！", self)
        statusText.setTextPixelSize(14)
        statusBar.addWidget(statusText)
        self.setStatusBar(statusBar)

    def initContent(self):
        self._homePage = T_Home(self)
        self._elaScreenPage = None
        if sys.platform == "win32" and T_ElaScreen is not None:
            self._elaScreenPage = T_ElaScreen(self)
        self._iconPage = T_Icon(self)
        self._baseComponentsPage = T_BaseComponents(self)
        self._navigationPage = T_Navigation(self)
        self._popupPage = T_Popup(self)
        self._cardPage = T_Card(self)
        self._listViewPage = T_ListView(self)
        self._tableViewPage = T_TableView(self)
        self._treeViewPage = T_TreeView(self)
        self._settingPage = T_Setting(self)

        self.addPageNode("HOME", self._homePage, ElaIconType.IconName.House)

        self._elaDxgiKey = None
        if sys.platform == "win32" and self._elaScreenPage is not None:
            _, self._elaDxgiKey = self.addExpanderNode("ElaDxgi", ElaIconType.IconName.TvMusic)
            self.addCategoryNode("Windows-DXGI", self._elaDxgiKey)
            self.addPageNodeKeyPoints(
                "ElaScreen", self._elaScreenPage, self._elaDxgiKey, 3, ElaIconType.IconName.ObjectGroup
            )

        self.addCategoryNode("Controls")
        self.addPageNode("ElaBaseComponents", self._baseComponentsPage, ElaIconType.IconName.CabinetFiling)

        _, _viewKey = self.addExpanderNode("ElaView", ElaIconType.IconName.CameraViewfinder)
        self.addCategoryNode("View Content", _viewKey)
        self.addPageNodeKeyPoints("ElaListView", self._listViewPage, _viewKey, 9, ElaIconType.IconName.List)
        self.addPageNode("ElaTableView", self._tableViewPage, _viewKey, ElaIconType.IconName.Table)
        self.addPageNode("ElaTreeView", self._treeViewPage, _viewKey, ElaIconType.IconName.ListTree)
        self.expandNavigationNode(_viewKey)

        self.addPageNode("ElaCard", self._cardPage, ElaIconType.IconName.Cards)

        self.addCategoryNode("Custom")
        self.addPageNode("ElaNavigation", self._navigationPage, ElaIconType.IconName.LocationArrow)
        self.addPageNode("ElaPopup", self._popupPage, ElaIconType.IconName.Envelope)
        self.addPageNodeKeyPoints("ElaIcon", self._iconPage, 99, ElaIconType.IconName.FontCase)

        _, testKey_1 = self.addExpanderNode("TEST_EXPAND_NODE1", ElaIconType.IconName.Acorn)
        _, testKey_2 = self.addExpanderNode("TEST_EXPAND_NODE2", testKey_1, ElaIconType.IconName.Acorn)
        self.addPageNode("TEST_NODE3", QWidget(self), testKey_2, ElaIconType.IconName.Acorn)
        for i in range(10):
            self.addExpanderNode(f"TEST_EXPAND_NODE{i + 4}", testKey_2, ElaIconType.IconName.Acorn)
        self.addExpanderNode("TEST_EXPAND_NODE14", ElaIconType.IconName.Acorn)
        self.addExpanderNode("TEST_EXPAND_NODE5", ElaIconType.IconName.Acorn)
        self.addExpanderNode("TEST_EXPAND_NODE16", ElaIconType.IconName.Acorn)

        _, self._aboutKey = self.addFooterNode("About", None, 0, ElaIconType.IconName.User)
        self._aboutPage = T_About()
        self._aboutPage.hide()

        def __onNavigationNodeClicked(nodeType: ElaNavigationType.NavigationNodeType, nodeKey: str):
            if self._aboutKey == nodeKey:
                self._aboutPage.setFixedSize(400, 400)
                self._aboutPage.moveToCenter()
                self._aboutPage.show()

        self.navigationNodeClicked.connect(__onNavigationNodeClicked)

        _, self._settingKey = self.addFooterNode("Setting", self._settingPage, 0, ElaIconType.IconName.GearComplex)

        self.userInfoCardClicked.connect(lambda: self.navigation(self._homePage.property("ElaPageKey")))

        if sys.platform == "win32" and self._elaScreenPage is not None:
            self._homePage.elaScreenNavigation.connect(
                lambda: self.navigation(self._elaScreenPage.property("ElaPageKey"))
            )
        self._homePage.elaBaseComponentNavigation.connect(
            lambda: self.navigation(self._baseComponentsPage.property("ElaPageKey"))
        )
        self._homePage.elaIconNavigation.connect(
            lambda: self.navigation(self._iconPage.property("ElaPageKey"))
        )
        self._homePage.elaCardNavigation.connect(
            lambda: self.navigation(self._cardPage.property("ElaPageKey"))
        )

        if self._windowSuggestBox is not None:
            try:
                self._windowSuggestBox.addSuggestion(self.getNavigationSuggestDataList())
            except Exception:
                pass

    def mouseReleaseEvent(self, event):
        if self.getCurrentNavigationIndex() != 2:
            if event.button() == Qt.MouseButton.BackButton:
                self.setCurrentStackIndex(0)
            elif event.button() == Qt.MouseButton.ForwardButton:
                self.setCurrentStackIndex(1)
        super().mouseReleaseEvent(event)
