from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *
from _res import *


class T_Home(T_BasePage):
    elaScreenNavigation = pyqtSignal()
    elaBaseComponentNavigation = pyqtSignal()
    elaSceneNavigation = pyqtSignal()
    elaCardNavigation = pyqtSignal()
    elaIconNavigation = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # 预览窗口标题
        self.setWindowTitle("Home")

        self.setTitleVisible(False)
        self.setContentsMargins(2, 2, 0, 0)

        # 标题卡片区域
        desText = ElaText("FluentUI For QWidget", self)
        desText.setTextPixelSize(18)
        titleText = ElaText("ElaWidgetTools", self)
        titleText.setTextPixelSize(35)

        titleLayout = QVBoxLayout()
        titleLayout.setContentsMargins(30, 10, 0, 0)
        titleLayout.addWidget(desText)
        titleLayout.addWidget(titleText)

        backgroundCard = ElaImageCard(self)
        backgroundCard.setBorderRadius(10)
        backgroundCard.setFixedHeight(340)
        backgroundCard.setCardImage(placeholderImage(800, 340))

        urlCard1 = ElaAcrylicUrlCard(self)
        urlCard1.setCardPixmapSize(QSize(62, 62))
        urlCard1.setFixedSize(195, 225)
        urlCard1.setTitlePixelSize(17)
        urlCard1.setTitleSpacing(25)
        urlCard1.setSubTitleSpacing(13)
        urlCard1.setUrl("https://github.com/Liniyous/ElaWidgetTools")
        urlCard1.setCardPixmap(placeholderPixmap(62, 62))
        urlCard1.setTitle("ElaTool Github")
        urlCard1.setSubTitle("Use ElaWidgetTools To Create A Cool Project")
        urlCard1ToolTip = ElaToolTip(urlCard1)
        urlCard1ToolTip.setToolTip("https://github.com/Liniyous/ElaWidgetTools")

        urlCard2 = ElaAcrylicUrlCard(self)
        urlCard2.setCardPixmapSize(QSize(62, 62))
        urlCard2.setFixedSize(195, 225)
        urlCard2.setTitlePixelSize(17)
        urlCard2.setTitleSpacing(25)
        urlCard2.setSubTitleSpacing(13)
        urlCard2.setUrl("https://space.bilibili.com/21256707")
        urlCard2.setCardPixmap(placeholderPixmap(62, 62))
        urlCard2.setTitle("ElaWidgetTool")
        urlCard2.setSubTitle("80985@qq.com")

        cardScrollArea = ElaScrollArea(self)
        cardScrollArea.setWidgetResizable(True)
        cardScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        cardScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        cardScrollArea.setIsGrabGesture(True, 0)
        cardScrollArea.setIsOverShoot(Qt.Orientation.Horizontal, True)
        cardScrollAreaWidget = QWidget(self)
        cardScrollAreaWidget.setStyleSheet("background-color:transparent;")
        cardScrollArea.setWidget(cardScrollAreaWidget)
        urlCardLayout = QHBoxLayout()
        urlCardLayout.setSpacing(15)
        urlCardLayout.setContentsMargins(30, 0, 0, 6)
        urlCardLayout.addWidget(urlCard1)
        urlCardLayout.addWidget(urlCard2)
        urlCardLayout.addStretch()
        cardScrollAreaWidgetLayout = QVBoxLayout(cardScrollAreaWidget)
        cardScrollAreaWidgetLayout.setContentsMargins(0, 0, 0, 0)
        cardScrollAreaWidgetLayout.addStretch()
        cardScrollAreaWidgetLayout.addLayout(urlCardLayout)

        backgroundLayout = QVBoxLayout(backgroundCard)
        backgroundLayout.setContentsMargins(0, 0, 0, 0)
        backgroundLayout.addLayout(titleLayout)
        backgroundLayout.addWidget(cardScrollArea)

        # 推荐卡片
        flowText = ElaText("热门免费应用", self)
        flowText.setTextPixelSize(20)
        flowTextLayout = QHBoxLayout()
        flowTextLayout.setContentsMargins(33, 0, 0, 0)
        flowTextLayout.addWidget(flowText)

        # ElaFlowLayout
        homeCard = ElaPopularCard(self)
        homeCard.popularCardButtonClicked.connect(
            lambda: QDesktopServices.openUrl(
                QUrl("https://github.com/Liniyous/ElaWidgetTools")
            )
        )
        homeCard.setCardPixmap(placeholderPixmap(120, 120))
        homeCard.setTitle("ElaWidgetTool")
        homeCard.setSubTitle("5.0⭐ 实用程序与工具")
        homeCard.setInteractiveTips("免费下载")
        homeCard.setDetailedText(
            "ElaWidgetTools致力于为QWidget用户提供一站式的外观和实用功能解决方案,只需数十MB内存和极少CPU占用以支持高效而美观的界面开发"
        )
        homeCard.setCardFloatPixmap(placeholderPixmap(32, 32))

        homeCard1 = ElaPopularCard(self)
        homeCard1.popularCardButtonClicked.connect(self.elaScreenNavigation)
        homeCard1.setTitle("ElaScreen")
        homeCard1.setSubTitle("5.0⭐ 实用程序与工具")
        homeCard1.setCardPixmap(placeholderPixmap(120, 120))
        homeCard1.setInteractiveTips("免费使用")
        homeCard1.setDetailedText(
            "使用ElaDxgiManager获取屏幕的实时数据，以QImage的形式处理数据，支持切换采集设备和输出设备。"
        )
        homeCard1.setCardFloatPixmap(placeholderPixmap(32, 32))

        homeCard2 = ElaPopularCard(self)
        homeCard2.popularCardButtonClicked.connect(self.elaSceneNavigation)
        homeCard2.setTitle("ElaScene")
        homeCard2.setSubTitle("5.0⭐ 实用程序与工具")
        homeCard2.setCardPixmap(placeholderPixmap(120, 120))
        homeCard2.setInteractiveTips("免费使用")
        homeCard2.setDetailedText(
            "使用ElaScene封装的高集成度API进行快速拓扑绘图开发，对基于连接的网络拓扑特化处理。"
        )
        homeCard2.setCardFloatPixmap(placeholderPixmap(32, 32))

        homeCard3 = ElaPopularCard(self)
        homeCard3.popularCardButtonClicked.connect(self.elaBaseComponentNavigation)
        homeCard3.setTitle("ElaBaseComponent")
        homeCard3.setSubTitle("5.0⭐ 实用程序与工具")
        homeCard3.setCardPixmap(placeholderPixmap(120, 120))
        homeCard3.setInteractiveTips("免费使用")
        homeCard3.setDetailedText(
            "添加ElaBaseComponent页面中的基础组件到你的项目中以进行快捷开发，使用方便，结构整洁，API规范"
        )
        homeCard3.setCardFloatPixmap(placeholderPixmap(32, 32))

        homeCard4 = ElaPopularCard(self)
        homeCard4.popularCardButtonClicked.connect(self.elaCardNavigation)
        homeCard4.setTitle("ElaCard")
        homeCard4.setSubTitle("5.0⭐ 实用程序与工具")
        homeCard4.setCardPixmap(placeholderPixmap(120, 120))
        homeCard4.setInteractiveTips("免费使用")
        homeCard4.setDetailedText(
            "使用ElaCard系列组件，包括促销卡片和促销卡片视窗来快速建立循环动画。"
        )
        homeCard4.setCardFloatPixmap(placeholderPixmap(32, 32))

        homeCard5 = ElaPopularCard(self)
        homeCard5.popularCardButtonClicked.connect(self.elaIconNavigation)
        homeCard5.setTitle("ElaIcon")
        homeCard5.setSubTitle("5.0⭐ 实用程序与工具")
        homeCard5.setCardPixmap(placeholderPixmap(120, 120))
        homeCard5.setInteractiveTips("免费使用")
        homeCard5.setDetailedText(
            "在该界面快速挑选你喜欢的图标应用到项目中，以枚举的形式使用它"
        )
        homeCard5.setCardFloatPixmap(placeholderPixmap(32, 32))

        flowLayout = ElaFlowLayout(0, 5, 5)
        flowLayout.setContentsMargins(30, 0, 0, 0)
        flowLayout.setIsAnimation(True)
        flowLayout.addWidget(homeCard)
        flowLayout.addWidget(homeCard1)
        flowLayout.addWidget(homeCard2)
        flowLayout.addWidget(homeCard3)
        flowLayout.addWidget(homeCard4)
        flowLayout.addWidget(homeCard5)

        # 菜单
        self._homeMenu = ElaMenu(self)
        checkMenu = self._homeMenu.addMenu(ElaIconType.IconName.Cubes, "查看")
        checkMenu.addAction("查看1")
        checkMenu.addAction("查看2")
        checkMenu.addAction("查看3")
        checkMenu.addAction("查看4")

        checkMenu1 = self._homeMenu.addMenu(ElaIconType.IconName.Cubes, "查看")
        checkMenu1.addAction("查看1")
        checkMenu1.addAction("查看2")
        checkMenu1.addAction("查看3")
        checkMenu1.addAction("查看4")

        checkMenu2 = checkMenu.addMenu(ElaIconType.IconName.Cubes, "查看")
        checkMenu2.addAction("查看1")
        checkMenu2.addAction("查看2")
        checkMenu2.addAction("查看3")
        checkMenu2.addAction("查看4")

        # QKeySequence key = QKeySequence(Qt::CTRL | Qt::Key_S);

        self._homeMenu.addSeparator()
        self._homeMenu.addElaIconAction(
            ElaIconType.IconName.BoxCheck, "排序方式", QKeySequence.StandardKey.Save
        )
        self._homeMenu.addElaIconAction(ElaIconType.IconName.ArrowRotateRight, "刷新")
        action = self._homeMenu.addElaIconAction(
            ElaIconType.IconName.ArrowRotateLeft, "撤销"
        )
        action.triggered.connect(
            lambda: ElaActionCommander.getInstance().undoCommand("ElaWidgetToolsAction")
        )

        self._homeMenu.addElaIconAction(ElaIconType.IconName.Copy, "复制")
        self._homeMenu.addElaIconAction(
            ElaIconType.IconName.MagnifyingGlassPlus, "显示设置"
        )

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("Home")
        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setSpacing(0)
        centerVLayout.setContentsMargins(0, 0, 0, 0)
        centerVLayout.addWidget(backgroundCard)
        centerVLayout.addSpacing(20)
        centerVLayout.addLayout(flowTextLayout)
        centerVLayout.addSpacing(10)
        centerVLayout.addLayout(flowLayout)
        centerVLayout.addStretch()
        self.addCentralWidget(centralWidget)

        # 初始化提示
        ElaMessageBar.success(
            ElaMessageBarType.PositionPolicy.BottomRight,
            "Success",
            "初始化成功!",
            2000,
        )
        print("初始化成功")

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.RightButton:
            try:
                pos = event.globalPosition().toPoint()
            except AttributeError:
                pos = event.globalPos()
            self._homeMenu.popup(pos)
        super().mouseReleaseEvent(event)
