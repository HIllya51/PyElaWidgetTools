from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5ElaWidgetTools import *
from ExamplePage.T_Icon import *
from ExamplePage.T_BaseComponents import *
from ExamplePage.T_About import *


class MainWindow(ElaWindow):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.initWindow()
        self.initEdgeLayout()
        self.initContent()
        _closeDialog = ElaContentDialog(self)
        _closeDialog.rightButtonClicked.connect(self.closeWindow)
        _closeDialog.middleButtonClicked.connect(
            lambda: (_closeDialog.close(), self.showMinimized())
        )
        self.setIsDefaultClosed(False)
        self.closeButtonClicked.connect(lambda: _closeDialog.exec())
        self.moveToCenter()

    def initWindow(self):
        self.setWindowIcon(QIcon(r"C:\Users\11737\Pictures\冥契\過去未来1.jpg"))
        self.resize(1200, 740)
        # // ElaLog::getInstance().initMessageLog(true);
        # // eTheme.setThemeMode(ElaThemeType::Dark);
        # // setIsNavigationBarEnable(false);
        # // setNavigationBarDisplayMode(ElaNavigationType::Compact);
        # // setWindowButtonFlag(ElaAppBarType::MinimizeButtonHint, false);
        self.setUserInfoCardPixmap(
            QPixmap(r"C:\Users\11737\Pictures\冥契\過去未来1.jpg")
        )
        self.setUserInfoCardTitle("Fuck")
        self.setUserInfoCardSubTitle("Fuck@Fuck.com")
        self.setWindowTitle("Fuck")

    def initEdgeLayout(self):

        menuBar = ElaMenuBar(self)
        menuBar.setFixedHeight(30)
        customWidget = QWidget(self)
        customLayout = QVBoxLayout(customWidget)
        customLayout.setContentsMargins(0, 0, 0, 0)
        customLayout.addWidget(menuBar)
        customLayout.addStretch()
        self.setCustomWidget(ElaAppBarType.CustomArea.MiddleArea, customWidget)
        self.setCustomWidgetMaximumWidth(500)

        menuBar.addElaIconAction(ElaIconType.IconName.AtomSimple, "动作菜单")
        iconMenu = menuBar.addMenu(ElaIconType.IconName.Aperture, "图标菜单")
        iconMenu.setMenuItemHeight(27)
        iconMenu.addElaIconAction(
            ElaIconType.IconName.BoxCheck,
            "排序方式",
            QKeySequence.StandardKey.SelectAll,
        )
        iconMenu.addElaIconAction(ElaIconType.IconName.Copy, "复制")
        iconMenu.addElaIconAction(ElaIconType.IconName.MagnifyingGlassPlus, "显示设置")
        iconMenu.addSeparator()
        iconMenu.addElaIconAction(ElaIconType.IconName.ArrowRotateRight, "刷新")
        iconMenu.addElaIconAction(ElaIconType.IconName.ArrowRotateLeft, "撤销")
        menuBar.addSeparator()
        shortCutMenu = ElaMenu("快捷菜单(&A)", self)
        shortCutMenu.setMenuItemHeight(27)
        shortCutMenu.addElaIconAction(
            ElaIconType.IconName.BoxCheck, "排序方式", QKeySequence.StandardKey.Find
        )
        shortCutMenu.addElaIconAction(ElaIconType.IconName.Copy, "复制")
        shortCutMenu.addElaIconAction(
            ElaIconType.IconName.MagnifyingGlassPlus, "显示设置"
        )
        shortCutMenu.addSeparator()
        shortCutMenu.addElaIconAction(ElaIconType.IconName.ArrowRotateRight, "刷新")
        shortCutMenu.addElaIconAction(ElaIconType.IconName.ArrowRotateLeft, "撤销")
        menuBar.addMenu(shortCutMenu)

        menuBar.addMenu("样例菜单(&B)").addElaIconAction(
            ElaIconType.IconName.ArrowRotateRight, "样例选项"
        )
        menuBar.addMenu("样例菜单(&C)").addElaIconAction(
            ElaIconType.IconName.ArrowRotateRight, "样例选项"
        )
        menuBar.addMenu("样例菜单(&E)").addElaIconAction(
            ElaIconType.IconName.ArrowRotateRight, "样例选项"
        )
        menuBar.addMenu("样例菜单(&F)").addElaIconAction(
            ElaIconType.IconName.ArrowRotateRight, "样例选项"
        )
        menuBar.addMenu("样例菜单(&G)").addElaIconAction(
            ElaIconType.IconName.ArrowRotateRight, "样例选项"
        )

        toolBar = ElaToolBar("工具栏", self)
        toolBar.setAllowedAreas(
            Qt.ToolBarArea.TopToolBarArea | Qt.ToolBarArea.BottomToolBarArea
        )
        toolBar.setToolBarSpacing(3)
        toolBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        toolBar.setIconSize(QSize(25, 25))
        toolButton1 = ElaToolButton(self)
        toolButton1.setElaIcon(ElaIconType.IconName.BadgeCheck)
        toolBar.addWidget(toolButton1)
        toolButton2 = ElaToolButton(self)
        toolButton2.setElaIcon(ElaIconType.IconName.ChartUser)
        toolBar.addWidget(toolButton2)
        toolBar.addSeparator()
        toolButton3 = ElaToolButton(self)
        toolButton3.setElaIcon(ElaIconType.IconName.Bluetooth)
        toolButton3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolButton3.setText("Bluetooth")
        toolBar.addWidget(toolButton3)
        toolButton4 = ElaToolButton(self)
        toolButton4.setElaIcon(ElaIconType.IconName.BringFront)
        toolBar.addWidget(toolButton4)
        toolBar.addSeparator()
        toolButton5 = ElaToolButton(self)
        toolButton5.setElaIcon(ElaIconType.IconName.ChartSimple)
        toolBar.addWidget(toolButton5)
        toolButton6 = ElaToolButton(self)
        toolButton6.setElaIcon(ElaIconType.IconName.FaceClouds)
        toolBar.addWidget(toolButton6)
        toolButton8 = ElaToolButton(self)
        toolButton8.setElaIcon(ElaIconType.IconName.Aperture)
        toolBar.addWidget(toolButton8)
        toolButton9 = ElaToolButton(self)
        toolButton9.setElaIcon(ElaIconType.IconName.ChartMixed)
        toolBar.addWidget(toolButton9)
        toolButton10 = ElaToolButton(self)
        toolButton10.setElaIcon(ElaIconType.IconName.Coins)
        toolBar.addWidget(toolButton10)
        toolButton11 = ElaToolButton(self)
        toolButton11.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolButton11.setElaIcon(ElaIconType.IconName.AlarmPlus)
        toolButton11.setText("AlarmPlus")
        toolBar.addWidget(toolButton11)
        toolButton12 = ElaToolButton(self)
        toolButton12.setElaIcon(ElaIconType.IconName.Crown)
        toolBar.addWidget(toolButton12)
        test = QAction(self)
        test.setMenu(QMenu(self))

        progressBar = ElaProgressBar(self)
        progressBar.setMinimum(0)
        progressBar.setMaximum(0)
        progressBar.setFixedWidth(350)
        toolBar.addWidget(progressBar)

        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolBar)

        logDockWidget = ElaDockWidget("日志信息", self)
        logDockWidget.setWidget(QWidget(self))  # T_LogWidget(self));
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, logDockWidget)
        self.resizeDocks([logDockWidget], [200], Qt.Orientation.Horizontal)

        updateDockWidget = ElaDockWidget("更新内容", self)
        updateDockWidget.setWidget(QWidget(self))  # T_UpdateWidget(self));
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, updateDockWidget)
        self.resizeDocks([updateDockWidget], [200], Qt.Orientation.Horizontal)

        statusBar = ElaStatusBar(self)
        statusText = ElaText("初始化成功！", self)
        statusText.setTextPixelSize(14)
        statusBar.addWidget(statusText)
        self.setStatusBar(statusBar)

    def initContent(self):
        self._homePage = QWidget()  # T_Home(self);
        self._elaScreenPage = QWidget()  # T_ElaScreen(self);
        self._iconPage = T_Icon(self);
        self._baseComponentsPage = T_BaseComponents(self);
        self._graphicsPage = QWidget()  # T_Graphics(self);
        self._navigationPage = QWidget()  # T_Navigation(self);
        self._popupPage = QWidget()  # T_Popup(self);
        self._cardPage = QWidget()  # T_Card(self);
        self._listViewPage = QWidget()  # T_ListView(self);
        self._tableViewPage = QWidget()  # T_TableView(self);
        self._treeViewPage = QWidget()  # T_TreeView(self);
        self._settingPage = QWidget()  # T_Setting(self);

        self.addPageNode("HOME", self._homePage, ElaIconType.IconName.House)
        # ifdef Q_OS_WIN
        _, testKey_1 = self.addExpanderNode("ElaDxgi", ElaIconType.IconName.TvMusic)
        self.addPageNodeKeyPoints(
            "ElaScreen", self._elaScreenPage, 3, ElaIconType.IconName.ObjectGroup
        )
        # endif
        self.addPageNode(
            "ElaBaseComponents",
            self._baseComponentsPage,
            ElaIconType.IconName.CabinetFiling,
        )

        _, _viewKey = self.addExpanderNode(
            "ElaView", ElaIconType.IconName.CameraViewfinder
        )
        self.addPageNodeKeyPoints(
            "ElaListView", self._listViewPage, _viewKey, 9, ElaIconType.IconName.List
        )
        self.addPageNode(
            "ElaTableView", self._tableViewPage, _viewKey, ElaIconType.IconName.Table
        )
        self.addPageNode(
            "ElaTreeView", self._treeViewPage, _viewKey, ElaIconType.IconName.ListTree
        )
        self.expandNavigationNode(_viewKey)

        self.addPageNodeKeyPoints(
            "ElaGraphics", self._graphicsPage, 9, ElaIconType.IconName.Paintbrush
        )
        self.addPageNode("ElaCard", self._cardPage, ElaIconType.IconName.Cards)
        self.addPageNode(
            "ElaNavigation", self._navigationPage, ElaIconType.IconName.LocationArrow
        )
        self.addPageNode("ElaPopup", self._popupPage, ElaIconType.IconName.Envelope)
        self.addPageNodeKeyPoints("ElaIcon", self._iconPage, 99, ElaIconType.IconName.FontCase)
        _, testKey_2 = self.addExpanderNode("TEST4", ElaIconType.IconName.Acorn)
        _, testKey_1 = self.addExpanderNode(
            "TEST5", testKey_2, ElaIconType.IconName.Acorn
        )
        self.addPageNode(
            "Third Level", QWidget(self), testKey_1, ElaIconType.IconName.Acorn
        )
        _, testKey_1 = self.addExpanderNode(
            "TEST6", testKey_2, ElaIconType.IconName.Acorn
        )
        _, testKey_1 = self.addExpanderNode(
            "TEST7", testKey_2, ElaIconType.IconName.Acorn
        )
        _, testKey_1 = self.addExpanderNode(
            "TEST8", testKey_2, ElaIconType.IconName.Acorn
        )
        _, testKey_1 = self.addExpanderNode(
            "TEST9", testKey_2, ElaIconType.IconName.Acorn
        )
        _, testKey_1 = self.addExpanderNode(
            "TEST10", testKey_2, ElaIconType.IconName.Acorn
        )
        _, testKey_1 = self.addExpanderNode(
            "TEST11", testKey_2, ElaIconType.IconName.Acorn
        )
        _, testKey_1 = self.addExpanderNode(
            "TEST12", testKey_2, ElaIconType.IconName.Acorn
        )
        _, testKey_1 = self.addExpanderNode(
            "TEST13", testKey_2, ElaIconType.IconName.Acorn
        )
        _, testKey_1 = self.addExpanderNode(
            "TEST14", testKey_2, ElaIconType.IconName.Acorn
        )
        _, testKey_1 = self.addExpanderNode("TEST15", ElaIconType.IconName.Acorn)
        _, testKey_1 = self.addExpanderNode("TEST16", ElaIconType.IconName.Acorn)
        _, testKey_1 = self.addExpanderNode("TEST17", ElaIconType.IconName.Acorn)

        _, _aboutKey = self.addFooterNode("About", None, 0, ElaIconType.IconName.User)
        self._aboutPage = T_About()

        self._aboutPage.hide()

        def __(nodeType: ElaNavigationType.NavigationNodeType, nodeKey: str):
            if _aboutKey == nodeKey:
                self._aboutPage.setFixedSize(400, 400)
                # self._aboutPage.moveToCenter();
                self._aboutPage.show()

        self.navigationNodeClicked.connect(__)
        _, _settingKey = self.addFooterNode(
            "Setting", self._settingPage, 0, ElaIconType.IconName.GearComplex
        )
        self.userInfoCardClicked.connect(
            lambda: self.navigation(self._homePage.property("ElaPageKey"))
        )

    # #ifdef Q_OS_WIN
    #     connect(_homePage, &T_Home::elaScreenNavigation, self, [=]() {
    #         self.navigation(_elaScreenPage.property("ElaPageKey").toString());
    #     });
    # #endif
    #     connect(_homePage, &T_Home::elaBaseComponentNavigation, self, [=]() {
    #         self.navigation(_baseComponentsPage.property("ElaPageKey").toString());
    #     });
    #     connect(_homePage, &T_Home::elaSceneNavigation, self, [=]() {
    #         self.navigation(_graphicsPage.property("ElaPageKey").toString());
    #     });
    #     connect(_homePage, &T_Home::elaIconNavigation, self, [=]() {
    #         self.navigation(_iconPage.property("ElaPageKey").toString());
    #     });
    #     connect(_homePage, &T_Home::elaCardNavigation, self, [=]() {
    #         self.navigation(_cardPage.property("ElaPageKey").toString());
    #     });
    #     qDebug() << "已注册的事件列表" << ElaEventBus::getInstance().getRegisteredEventsName();
