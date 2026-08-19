from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_Setting(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 预览窗口标题
        window = self.window()
        self.setWindowTitle("Setting")

        themeText = ElaText("主题设置", self)
        themeText.setWordWrap(False)
        themeText.setTextPixelSize(18)

        self._themeComboBox = ElaComboBox(self)
        self._themeComboBox.addItem("日间模式")
        self._themeComboBox.addItem("夜间模式")
        themeSwitchArea = ElaScrollPageArea(self)
        themeSwitchLayout = QHBoxLayout(themeSwitchArea)
        themeSwitchText = ElaText("主题切换", self)
        themeSwitchText.setWordWrap(False)
        themeSwitchText.setTextPixelSize(15)
        themeSwitchLayout.addWidget(themeSwitchText)
        themeSwitchLayout.addStretch()
        themeSwitchLayout.addWidget(self._themeComboBox)
        self._themeComboBox.currentIndexChanged.connect(
            lambda index: (
                eTheme.setThemeMode(ElaThemeType.ThemeMode.Light)
                if index == 0
                else eTheme.setThemeMode(ElaThemeType.ThemeMode.Dark)
            )
        )

        def __themeModeChanged(themeMode: ElaThemeType.ThemeMode):
            self._themeComboBox.blockSignals(True)
            if themeMode == ElaThemeType.ThemeMode.Light:
                self._themeComboBox.setCurrentIndex(0)
            else:
                self._themeComboBox.setCurrentIndex(1)
            self._themeComboBox.blockSignals(False)

        eTheme.themeModeChanged.connect(__themeModeChanged)

        windowPaintText = ElaText("主窗口绘制设置", self)
        windowPaintText.setWordWrap(False)
        windowPaintText.setTextPixelSize(15)

        self._windowNormalButton = ElaRadioButton("Normal", self)
        self._windowNormalButton.setChecked(True)
        self._windowPixmapButton = ElaRadioButton("Pixmap", self)
        self._windowMovieButton = ElaRadioButton("Movie", self)

        windowPaintButtonGroup = QButtonGroup(self)
        windowPaintButtonGroup.addButton(self._windowNormalButton, 0)
        windowPaintButtonGroup.addButton(self._windowPixmapButton, 1)
        windowPaintButtonGroup.addButton(self._windowMovieButton, 2)
        windowPaintModes = [
            ElaWindowType.PaintMode.Normal,
            ElaWindowType.PaintMode.Pixmap,
            ElaWindowType.PaintMode.Movie,
        ]
        windowPaintButtonGroup.buttonToggled.connect(
            lambda button, isToggled: (
                window.setWindowPaintMode(
                    windowPaintModes[windowPaintButtonGroup.id(button)]
                )
                if isToggled
                else None
            )
        )

        def __pWindowPaintModeChanged():
            button = windowPaintButtonGroup.button(window.getWindowPaintMode())
            elaRadioButton = button
            if elaRadioButton:
                elaRadioButton.setChecked(True)

        window.pWindowPaintModeChanged.connect(__pWindowPaintModeChanged)

        windowPaintModeArea = ElaScrollPageArea(self)
        windowPaintModeLayout = QHBoxLayout(windowPaintModeArea)
        windowPaintModeLayout.addWidget(windowPaintText)
        windowPaintModeLayout.addStretch()
        windowPaintModeLayout.addWidget(self._windowNormalButton)
        windowPaintModeLayout.addWidget(self._windowPixmapButton)
        windowPaintModeLayout.addWidget(self._windowMovieButton)

        helperText = ElaText("应用程序设置", self)
        helperText.setWordWrap(False)
        helperText.setTextPixelSize(18)

        micaSwitchText = ElaText("窗口效果", self)
        micaSwitchText.setWordWrap(False)
        micaSwitchText.setTextPixelSize(15)
        self._normalButton = ElaRadioButton("Normal", self)
        self._elaMicaButton = ElaRadioButton("ElaMica", self)
        # ifdef Q_OS_WIN
        self._micaButton = ElaRadioButton("Mica", self)
        self._micaAltButton = ElaRadioButton("Mica-Alt", self)
        self._acrylicButton = ElaRadioButton("Acrylic", self)
        self._dwmBlurnormalButton = ElaRadioButton("Dwm-Blur", self)
        # endif
        self._normalButton.setChecked(True)
        displayButtonGroup = QButtonGroup(self)
        displayButtonGroup.addButton(self._normalButton, 0)
        displayButtonGroup.addButton(self._elaMicaButton, 1)
        # ifdef Q_OS_WIN
        displayButtonGroup.addButton(self._micaButton, 2)
        displayButtonGroup.addButton(self._micaAltButton, 3)
        displayButtonGroup.addButton(self._acrylicButton, 4)
        displayButtonGroup.addButton(self._dwmBlurnormalButton, 5)
        # endif
        displayModes = [
            ElaApplicationType.WindowDisplayMode.Normal,
            ElaApplicationType.WindowDisplayMode.ElaMica,
            ElaApplicationType.WindowDisplayMode.Mica,
            ElaApplicationType.WindowDisplayMode.MicaAlt,
            ElaApplicationType.WindowDisplayMode.Acrylic,
            ElaApplicationType.WindowDisplayMode.DWMBlur,
        ]
        displayButtonGroup.buttonToggled.connect(
            lambda button, isToggled: (
                eApp.setWindowDisplayMode(displayModes[displayButtonGroup.id(button)])
                if isToggled
                else None
            )
        )

        def __pWindowDisplayModeChanged():
            button = displayButtonGroup.button(eApp.getWindowDisplayMode())
            elaRadioButton = button
            if elaRadioButton:
                elaRadioButton.setChecked(True)

        eApp.pWindowDisplayModeChanged.connect(__pWindowDisplayModeChanged)

        micaSwitchArea = ElaScrollPageArea(self)
        micaSwitchLayout = QHBoxLayout(micaSwitchArea)
        micaSwitchLayout.addWidget(micaSwitchText)
        micaSwitchLayout.addStretch()
        micaSwitchLayout.addWidget(self._normalButton)
        micaSwitchLayout.addWidget(self._elaMicaButton)
        # ifdef Q_OS_WIN
        micaSwitchLayout.addWidget(self._micaButton)
        micaSwitchLayout.addWidget(self._micaAltButton)
        micaSwitchLayout.addWidget(self._acrylicButton)
        micaSwitchLayout.addWidget(self._dwmBlurnormalButton)
        # endif

        self._logSwitchButton = ElaToggleSwitch(self)
        logSwitchArea = ElaScrollPageArea(self)
        logSwitchLayout = QHBoxLayout(logSwitchArea)
        logSwitchText = ElaText("启用日志功能", self)
        logSwitchText.setWordWrap(False)
        logSwitchText.setTextPixelSize(15)
        logSwitchLayout.addWidget(logSwitchText)
        logSwitchLayout.addStretch()
        logSwitchLayout.addWidget(self._logSwitchButton)

        def __logSwitchToggled(checked: bool):
            ElaLog.getInstance().initMessageLog(checked)
            if checked:
                print("日志已启用!")
            else:
                print("日志已关闭!")

        self._logSwitchButton.toggled.connect(__logSwitchToggled)

        self._userCardSwitchButton = ElaToggleSwitch(self)
        userCardSwitchArea = ElaScrollPageArea(self)
        userCardSwitchLayout = QHBoxLayout(userCardSwitchArea)
        userCardSwitchText = ElaText("隐藏用户卡片", self)
        userCardSwitchText.setWordWrap(False)
        userCardSwitchText.setTextPixelSize(15)
        userCardSwitchLayout.addWidget(userCardSwitchText)
        userCardSwitchLayout.addStretch()
        userCardSwitchLayout.addWidget(self._userCardSwitchButton)
        self._userCardSwitchButton.toggled.connect(
            lambda checked: window.setUserInfoCardVisible(not checked)
        )

        self._minimumButton = ElaRadioButton("Minimum", self)
        self._compactButton = ElaRadioButton("Compact", self)
        self._maximumButton = ElaRadioButton("Maximum", self)
        self._autoButton = ElaRadioButton("Auto", self)
        self._autoButton.setChecked(True)
        displayModeArea = ElaScrollPageArea(self)
        displayModeLayout = QHBoxLayout(displayModeArea)
        displayModeText = ElaText("导航栏模式选择", self)
        displayModeText.setWordWrap(False)
        displayModeText.setTextPixelSize(15)
        displayModeLayout.addWidget(displayModeText)
        displayModeLayout.addStretch()
        displayModeLayout.addWidget(self._minimumButton)
        displayModeLayout.addWidget(self._compactButton)
        displayModeLayout.addWidget(self._maximumButton)
        displayModeLayout.addWidget(self._autoButton)

        navigationGroup = QButtonGroup(self)
        navigationGroup.addButton(self._autoButton, 0)
        navigationGroup.addButton(self._minimumButton, 1)
        navigationGroup.addButton(self._compactButton, 2)
        navigationGroup.addButton(self._maximumButton, 3)
        navigationModes = [
            ElaNavigationType.NavigationDisplayMode.Auto,
            ElaNavigationType.NavigationDisplayMode.Minimal,
            ElaNavigationType.NavigationDisplayMode.Compact,
            ElaNavigationType.NavigationDisplayMode.Maximal,
        ]
        navigationGroup.buttonToggled.connect(
            lambda button, isToggled: (
                window.setNavigationBarDisplayMode(
                    navigationModes[navigationGroup.id(button)]
                )
                if isToggled
                else None
            )
        )

        self._noneButton = ElaRadioButton("None", self)
        self._popupButton = ElaRadioButton("Popup", self)
        self._popupButton.setChecked(True)
        self._scaleButton = ElaRadioButton("Scale", self)
        self._flipButton = ElaRadioButton("Flip", self)
        self._blurButton = ElaRadioButton("Blur", self)
        stackSwitchModeArea = ElaScrollPageArea(self)
        stackSwitchModeLayout = QHBoxLayout(stackSwitchModeArea)
        stackSwitchModeText = ElaText("堆栈切换模式选择", self)
        stackSwitchModeText.setWordWrap(False)
        stackSwitchModeText.setTextPixelSize(15)
        stackSwitchModeLayout.addWidget(stackSwitchModeText)
        stackSwitchModeLayout.addStretch()
        stackSwitchModeLayout.addWidget(self._noneButton)
        stackSwitchModeLayout.addWidget(self._popupButton)
        stackSwitchModeLayout.addWidget(self._scaleButton)
        stackSwitchModeLayout.addWidget(self._flipButton)
        stackSwitchModeLayout.addWidget(self._blurButton)

        stackSwitchGroup = QButtonGroup(self)
        stackSwitchGroup.addButton(self._noneButton, 0)
        stackSwitchGroup.addButton(self._popupButton, 1)
        stackSwitchGroup.addButton(self._scaleButton, 2)
        stackSwitchGroup.addButton(self._flipButton, 3)
        stackSwitchGroup.addButton(self._blurButton, 4)
        stackSwitchModes = [
            ElaWindowType.StackSwitchMode.None_,
            ElaWindowType.StackSwitchMode.Popup,
            ElaWindowType.StackSwitchMode.Scale,
            ElaWindowType.StackSwitchMode.Flip,
            ElaWindowType.StackSwitchMode.Blur,
        ]
        stackSwitchGroup.buttonToggled.connect(
            lambda button, isToggled: (
                window.setStackSwitchMode(
                    stackSwitchModes[stackSwitchGroup.id(button)]
                )
                if isToggled
                else None
            )
        )

        def __pStackSwitchModeChanged():
            button = stackSwitchGroup.button(window.getStackSwitchMode())
            elaRadioButton = button
            if elaRadioButton:
                elaRadioButton.setChecked(True)

        window.pStackSwitchModeChanged.connect(__pStackSwitchModeChanged)

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("Setting")
        centerLayout = QVBoxLayout(centralWidget)
        centerLayout.addSpacing(30)
        centerLayout.addWidget(themeText)
        centerLayout.addSpacing(10)
        centerLayout.addWidget(themeSwitchArea)
        centerLayout.addSpacing(15)
        centerLayout.addWidget(helperText)
        centerLayout.addSpacing(10)
        centerLayout.addWidget(logSwitchArea)
        centerLayout.addWidget(userCardSwitchArea)
        centerLayout.addWidget(windowPaintModeArea)
        centerLayout.addWidget(micaSwitchArea)
        centerLayout.addWidget(displayModeArea)
        centerLayout.addWidget(stackSwitchModeArea)
        centerLayout.addStretch()
        centerLayout.setContentsMargins(0, 0, 0, 0)
        self.addCentralWidget(centralWidget, True, True, 0)
