import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_Setting(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        window = parent if isinstance(parent, ElaWindow) else None
        self.setWindowTitle("设置")
        self.createCustomWidget("调整展示程序的外观、导航与交互效果，设置会即时应用。", "设置")
        mainLayout = self.createPageLayout()

        # 外观
        appearanceSection = self.addExampleSection(
            mainLayout, "外观", "背景绘制与窗口材质可分别调整，系统材质效果取决于平台支持。"
        )
        self._themeComboBox = ElaComboBox(self)
        self._themeComboBox.setFixedWidth(200)
        self._themeComboBox.addItems(["浅色", "深色"])
        self._themeComboBox.setCurrentIndex(int(eTheme.getThemeMode()))

        def _onThemeChanged(index):
            eTheme.setThemeMode(
                ElaThemeType.ThemeMode.Light if index == 0 else ElaThemeType.ThemeMode.Dark
            )

        self._themeComboBox.currentIndexChanged.connect(_onThemeChanged)

        def _onThemeModeChanged(mode):
            self._themeComboBox.blockSignals(True)
            self._themeComboBox.setCurrentIndex(int(mode))
            self._themeComboBox.blockSignals(False)

        eTheme.themeModeChanged.connect(_onThemeModeChanged)
        appearanceSection.addWidget(
            self.createSettingRow("明暗主题", "为整个展示程序切换主题", self._themeComboBox)
        )

        paintComboBox = ElaComboBox(self)
        paintComboBox.setFixedWidth(200)
        paintComboBox.addItems(["纯色背景", "静态图片", "动态图片"])
        paintComboBox.setEnabled(window is not None)
        if window is not None:
            paintComboBox.setCurrentIndex(int(window.getWindowPaintMode()))

            def _onPaintChanged(index):
                window.setWindowPaintMode(ElaWindowType.PaintMode(index))

            paintComboBox.currentIndexChanged.connect(_onPaintChanged)

            def _onWindowPaintModeChanged():
                paintComboBox.blockSignals(True)
                paintComboBox.setCurrentIndex(int(window.getWindowPaintMode()))
                paintComboBox.blockSignals(False)

            window.pWindowPaintModeChanged.connect(_onWindowPaintModeChanged)
        appearanceSection.addWidget(
            self.createSettingRow("窗口背景", "在普通背景、图片和动图之间切换", paintComboBox)
        )

        materialComboBox = ElaComboBox(self)
        materialComboBox.setFixedWidth(200)
        materialComboBox.addItems(["默认材质", "Ela 云母"])
        if sys.platform == "win32":
            materialComboBox.addItems(["系统云母", "替代云母", "亚克力", "窗口模糊"])
        materialComboBox.setCurrentIndex(int(eApp.getWindowDisplayMode()))

        def _onMaterialChanged(index):
            eApp.setWindowDisplayMode(ElaApplicationType.WindowDisplayMode(index))

        materialComboBox.currentIndexChanged.connect(_onMaterialChanged)

        def _onWindowDisplayModeChanged():
            materialComboBox.blockSignals(True)
            materialComboBox.setCurrentIndex(int(eApp.getWindowDisplayMode()))
            materialComboBox.blockSignals(False)

        eApp.pWindowDisplayModeChanged.connect(_onWindowDisplayModeChanged)
        appearanceSection.addWidget(
            self.createSettingRow("窗口材质", "选择应用背景的材质效果", materialComboBox)
        )

        # 导航与页面
        navigationSection = self.addExampleSection(
            mainLayout, "导航与页面", "控制侧边栏的展开方式和页面切换动画。"
        )
        navigationComboBox = ElaComboBox(self)
        navigationComboBox.setFixedWidth(200)
        navigationComboBox.addItems(["自动适应", "最小化", "紧凑", "完整展开"])
        navigationComboBox.setEnabled(window is not None)
        transitionComboBox = ElaComboBox(self)
        transitionComboBox.setFixedWidth(200)
        transitionComboBox.addItems(["无动画", "滑入", "缩放", "翻转", "模糊"])
        transitionComboBox.setEnabled(window is not None)
        if window is not None:
            navigationComboBox.setCurrentIndex(int(window.getNavigationBarDisplayMode()))
            transitionComboBox.setCurrentIndex(int(window.getStackSwitchMode()))

            def _onNavigationModeChanged(index):
                window.setNavigationBarDisplayMode(
                    ElaNavigationType.NavigationDisplayMode(index)
                )

            def _onTransitionChanged(index):
                window.setStackSwitchMode(ElaWindowType.StackSwitchMode(index))

            navigationComboBox.currentIndexChanged.connect(_onNavigationModeChanged)
            transitionComboBox.currentIndexChanged.connect(_onTransitionChanged)

            def _onNavigationBarDisplayModeChanged():
                navigationComboBox.blockSignals(True)
                navigationComboBox.setCurrentIndex(int(window.getNavigationBarDisplayMode()))
                navigationComboBox.blockSignals(False)

            def _onStackSwitchModeChanged():
                transitionComboBox.blockSignals(True)
                transitionComboBox.setCurrentIndex(int(window.getStackSwitchMode()))
                transitionComboBox.blockSignals(False)

            window.pNavigationBarDisplayModeChanged.connect(_onNavigationBarDisplayModeChanged)
            window.pStackSwitchModeChanged.connect(_onStackSwitchModeChanged)
        self._userCardSwitchButton = ElaToggleSwitch(self)
        self._userCardSwitchButton.setIsToggled(True)
        self._userCardSwitchButton.setEnabled(window is not None)
        if window is not None:
            self._userCardSwitchButton.toggled.connect(window.setUserInfoCardVisible)
        navigationSection.addWidget(
            self.createSettingRow("导航栏模式", "让侧边栏适应当前窗口宽度", navigationComboBox)
        )
        navigationSection.addWidget(
            self.createSettingRow("页面切换", "选择页面之间的过渡方式", transitionComboBox)
        )
        navigationSection.addWidget(
            self.createSettingRow("显示用户卡片", "显示导航栏顶部的用户信息", self._userCardSwitchButton)
        )

        # 应用
        applicationSection = self.addExampleSection(mainLayout, "应用", "控制展示程序的日志记录。")
        self._logSwitchButton = ElaToggleSwitch(self)

        def _onLogToggled(checked):
            ElaLog.getInstance().initMessageLog(checked)
            print("日志已启用!" if checked else "日志已关闭!")

        self._logSwitchButton.toggled.connect(_onLogToggled)
        applicationSection.addWidget(
            self.createSettingRow("启用日志功能", "日志会显示在日志面板并写入文件", self._logSwitchButton)
        )
