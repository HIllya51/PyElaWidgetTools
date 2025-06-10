from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_Setting(T_BasePage):
    def __init__(self, window: ElaWindow = None):
        super().__init__(window)

        self.setWindowTitle("Setting")

        themeText = ElaText("主题设置", self)
        themeText.setWordWrap(False)
        themeText.setTextPixelSize(18)

        _themeComboBox = ElaComboBox(self)
        _themeComboBox.addItem("日间模式")
        _themeComboBox.addItem("夜间模式")
        themeSwitchArea = ElaScrollPageArea(self)
        themeSwitchLayout = QHBoxLayout(themeSwitchArea)
        themeSwitchText = ElaText("主题切换", self)
        themeSwitchText.setWordWrap(False)
        themeSwitchText.setTextPixelSize(15)
        themeSwitchLayout.addWidget(themeSwitchText)
        themeSwitchLayout.addStretch()
        themeSwitchLayout.addWidget(_themeComboBox)
        _themeComboBox.currentIndexChanged.connect(
            lambda index: (
                eTheme.setThemeMode(ElaThemeType.ThemeMode.Light)
                if index == 0
                else eTheme.setThemeMode(ElaThemeType.ThemeMode.Dark)
            )
        )

        def __themeModeChanged(themeMode: ElaThemeType.ThemeMode):
            _themeComboBox.blockSignals(True)
            if themeMode == ElaThemeType.ThemeMode.Light:
                _themeComboBox.setCurrentIndex(0)
            else:
                _themeComboBox.setCurrentIndex(1)
            _themeComboBox.blockSignals(False)

        eTheme.themeModeChanged.connect(__themeModeChanged)

        helperText = ElaText("应用程序设置", self)
        helperText.setWordWrap(False)
        helperText.setTextPixelSize(18)

        _normalButton = ElaRadioButton("Normal", self)
        _elaMicaButton = ElaRadioButton("ElaMica", self)
        # ifdef Q_OS_WIN
        _micaButton = ElaRadioButton("Mica", self)
        _micaAltButton = ElaRadioButton("Mica-Alt", self)
        _acrylicButton = ElaRadioButton("Acrylic", self)
        _dwmBlurnormalButton = ElaRadioButton("Dwm-Blur", self)
        # endif
        _normalButton.setChecked(True)
        displayButtonGroup = QButtonGroup(self)
        displayButtonGroup.addButton(_normalButton, 0)
        displayButtonGroup.addButton(_elaMicaButton, 1)
        # ifdef Q_OS_WIN
        displayButtonGroup.addButton(_micaButton, 2)
        displayButtonGroup.addButton(_micaAltButton, 3)
        displayButtonGroup.addButton(_acrylicButton, 4)
        displayButtonGroup.addButton(_dwmBlurnormalButton, 5)
        # endif
        displayButtonGroup.buttonToggled.connect(
            lambda button, isToggled: (
                eApp.setWindowDisplayMode(displayButtonGroup.id(button))
                if isToggled
                else None
            )
        )

        def __pWindowDisplayModeChanged():
            elaRadioButton: ElaRadioButton = displayButtonGroup.button(
                eApp.getWindowDisplayMode()
            )
            if elaRadioButton:
                elaRadioButton.setChecked(True)

        eApp.pWindowDisplayModeChanged.connect(__pWindowDisplayModeChanged)
        micaSwitchArea = ElaScrollPageArea(self)
        micaSwitchLayout = QHBoxLayout(micaSwitchArea)
        micaSwitchText = ElaText("窗口效果", self)
        micaSwitchText.setWordWrap(False)
        micaSwitchText.setTextPixelSize(15)
        micaSwitchLayout.addWidget(micaSwitchText)
        micaSwitchLayout.addStretch()
        micaSwitchLayout.addWidget(_normalButton)
        micaSwitchLayout.addWidget(_elaMicaButton)
        # ifdef Q_OS_WIN
        micaSwitchLayout.addWidget(_micaButton)
        micaSwitchLayout.addWidget(_micaAltButton)
        micaSwitchLayout.addWidget(_acrylicButton)
        micaSwitchLayout.addWidget(_dwmBlurnormalButton)
        # endif

        _logSwitchButton = ElaToggleSwitch(self)
        logSwitchArea = ElaScrollPageArea(self)
        logSwitchLayout = QHBoxLayout(logSwitchArea)
        logSwitchText = ElaText("启用日志功能", self)
        logSwitchText.setWordWrap(False)
        logSwitchText.setTextPixelSize(15)
        logSwitchLayout.addWidget(logSwitchText)
        logSwitchLayout.addStretch()
        logSwitchLayout.addWidget(_logSwitchButton)

        def __(checked: bool):
            ElaLog.getInstance().initMessageLog(checked)
            if checked:
                print("日志已启用!")
            else:
                print("日志已关闭!")

        _logSwitchButton.toggled.connect(__)

        _minimumButton = ElaRadioButton("Minimum", self)
        _compactButton = ElaRadioButton("Compact", self)
        _maximumButton = ElaRadioButton("Maximum", self)
        _autoButton = ElaRadioButton("Auto", self)
        _autoButton.setChecked(True)
        displayModeArea = ElaScrollPageArea(self)
        displayModeLayout = QHBoxLayout(displayModeArea)
        displayModeText = ElaText("导航栏模式选择", self)
        displayModeText.setWordWrap(False)
        displayModeText.setTextPixelSize(15)
        displayModeLayout.addWidget(displayModeText)
        displayModeLayout.addStretch()
        displayModeLayout.addWidget(_minimumButton)
        displayModeLayout.addWidget(_compactButton)
        displayModeLayout.addWidget(_maximumButton)
        displayModeLayout.addWidget(_autoButton)

        navigationGroup = QButtonGroup(self)
        navigationGroup.addButton(_autoButton, 0)
        navigationGroup.addButton(_minimumButton, 1)
        navigationGroup.addButton(_compactButton, 2)
        navigationGroup.addButton(_maximumButton, 3)
        navigationGroup.buttonToggled.connect(
            lambda button, isToggled: (
                window.setNavigationBarDisplayMode(navigationGroup.id(button))
                if isToggled
                else None
            )
        )

        _noneButton = ElaRadioButton("None", self)
        _popupButton = ElaRadioButton("Popup", self)
        _popupButton.setChecked(True)
        _scaleButton = ElaRadioButton("Scale", self)
        _flipButton = ElaRadioButton("Flip", self)
        stackSwitchModeArea = ElaScrollPageArea(self)
        stackSwitchModeLayout = QHBoxLayout(stackSwitchModeArea)
        stackSwitchModeText = ElaText("堆栈切换模式选择", self)
        stackSwitchModeText.setWordWrap(False)
        stackSwitchModeText.setTextPixelSize(15)
        stackSwitchModeLayout.addWidget(stackSwitchModeText)
        stackSwitchModeLayout.addStretch()
        stackSwitchModeLayout.addWidget(_noneButton)
        stackSwitchModeLayout.addWidget(_popupButton)
        stackSwitchModeLayout.addWidget(_scaleButton)
        stackSwitchModeLayout.addWidget(_flipButton)

        stackSwitchGroup = QButtonGroup(self)
        stackSwitchGroup.addButton(_noneButton, 0)
        stackSwitchGroup.addButton(_popupButton, 1)
        stackSwitchGroup.addButton(_scaleButton, 2)
        stackSwitchGroup.addButton(_flipButton, 3)
        stackSwitchGroup.buttonToggled.connect(
            lambda button, isToggled: (
                window.setStackSwitchMode(stackSwitchGroup.id(button))
                if isToggled
                else None
            )
        )

        def __pStackSwitchModeChanged():
            elaRadioButton: ElaRadioButton = stackSwitchGroup.button(
                window.getStackSwitchMode()
            )
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
        centerLayout.addWidget(micaSwitchArea)
        centerLayout.addWidget(displayModeArea)
        centerLayout.addWidget(stackSwitchModeArea)
        centerLayout.addStretch()
        centerLayout.setContentsMargins(0, 0, 0, 0)
        self.addCentralWidget(centralWidget, True, True, 0)
