from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_BaseComponents(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("ElaBaseComponents")

        self.createCustomWidget(
            "一些常用的基础组件被放置于此，可在此界面体验其效果并按需添加进项目中"
        )

        _toggleSwitch = ElaToggleSwitch(self)
        toggleSwitchArea = ElaScrollPageArea(self)
        toggleSwitchLayout = QHBoxLayout(toggleSwitchArea)
        toggleSwitchText = ElaText("ElaToggleSwitch", self)
        toggleSwitchText.setTextPixelSize(15)
        toggleSwitchLayout.addWidget(toggleSwitchText)
        toggleSwitchLayout.addWidget(_toggleSwitch)
        toggleSwitchLayout.addStretch()
        toggleSwitchDisableSwitch = ElaToggleSwitch(self)
        toggleSwitchDisableText = ElaText("禁用", self)
        toggleSwitchDisableText.setTextPixelSize(15)
        toggleSwitchDisableSwitch.toggled.connect(_toggleSwitch.setDisabled)
        toggleSwitchLayout.addWidget(toggleSwitchDisableSwitch)
        toggleSwitchLayout.addWidget(toggleSwitchDisableText)
        toggleSwitchLayout.addSpacing(10)

        _toggleButton = ElaToggleButton("ToggleButton", self)
        _toggleButton.setFixedWidth(120)
        toggleButtonArea = ElaScrollPageArea(self)
        toggleButtonLayout = QHBoxLayout(toggleButtonArea)
        toggleButtonText = ElaText("ElaToggleButton", self)
        toggleButtonText.setTextPixelSize(15)
        toggleButtonLayout.addWidget(toggleButtonText)
        toggleButtonLayout.addWidget(_toggleButton)
        toggleButtonLayout.addStretch()
        toggleButtonDisableSwitch = ElaToggleSwitch(self)
        toggleButtonDisableText = ElaText("禁用", self)
        toggleButtonDisableText.setTextPixelSize(15)
        toggleButtonDisableSwitch.toggled.connect(_toggleButton.setDisabled)
        toggleButtonLayout.addWidget(toggleButtonDisableSwitch)
        toggleButtonLayout.addWidget(toggleButtonDisableText)
        toggleButtonLayout.addSpacing(10)

        _comboBox = ElaComboBox(self)
        comboList = [
            "我愿投身前途未卜的群星",
            "潜行 步伐小心翼翼",
            "不留游走痕迹",
            "如同一簇幽灵",
            "所谓 道德加上伦理",
            "抱歉只能律己",
        ]
        _comboBox.addItems(comboList)
        comboBoxArea = ElaScrollPageArea(self)
        comboBoxLayout = QHBoxLayout(comboBoxArea)
        comboBoxText = ElaText("ElaComboBox", self)
        comboBoxText.setTextPixelSize(15)
        comboBoxLayout.addWidget(comboBoxText)
        comboBoxLayout.addWidget(_comboBox)
        comboBoxLayout.addStretch()
        comboBoxDisableSwitch = ElaToggleSwitch(self)
        comboBoxDisableText = ElaText("禁用", self)
        comboBoxDisableText.setTextPixelSize(15)
        comboBoxDisableSwitch.toggled.connect(_comboBox.setDisabled)
        comboBoxLayout.addWidget(comboBoxDisableSwitch)
        comboBoxLayout.addWidget(comboBoxDisableText)
        comboBoxLayout.addSpacing(10)

        _multiSelectComboBox = ElaMultiSelectComboBox(self)
        multiComboList = [
            "执念的鱼",
            "提着灯闯过远洋的甄选",
            "继续下潜",
            "无需誓言",
            "我的心像自沉的旧母舰",
            "没入深渊",
            "我曾凝望曾是航向的日出",
        ]
        multiSelectComboList = [
            "执念的鱼",
            "提着灯闯过远洋的甄选",
            "无需誓言",
            "我的心像自沉的旧母舰",
        ]
        _multiSelectComboBox.addItems(multiComboList)
        _multiSelectComboBox.setCurrentSelection(multiSelectComboList)
        multiSelectComboBoxArea = ElaScrollPageArea(self)
        multiSelectComboBoxLayout = QHBoxLayout(multiSelectComboBoxArea)
        multiSelectComboBoxText = ElaText("ElaMutilSelectComboBox", self)
        multiSelectComboBoxText.setTextPixelSize(15)
        multiSelectComboBoxLayout.addWidget(multiSelectComboBoxText)
        multiSelectComboBoxLayout.addWidget(_multiSelectComboBox)
        multiSelectComboBoxLayout.addStretch()
        multiSelectComboBoxDisableSwitch = ElaToggleSwitch(self)
        multiSelectComboBoxDisableText = ElaText("禁用", self)
        multiSelectComboBoxDisableText.setTextPixelSize(15)
        multiSelectComboBoxDisableSwitch.toggled.connect(
            _multiSelectComboBox.setDisabled
        )
        multiSelectComboBoxLayout.addWidget(multiSelectComboBoxDisableSwitch)
        multiSelectComboBoxLayout.addWidget(multiSelectComboBoxDisableText)
        multiSelectComboBoxLayout.addSpacing(10)

        _messageButton = ElaMessageButton("Success", self)
        _messageButton.setBarTitle("Success")
        _messageButton.setBarText(
            "点燃星 亲手点燃黑暗森林的火星 蒙昧初醒 而我却 轻声告别这新生的黎明"
        )

        _infoMessageButton = ElaMessageButton("Info", self)
        _infoMessageButton.setBarTitle("Information")
        _infoMessageButton.setBarText(
            "点燃星 亲手点燃黑暗森林的火星 蒙昧初醒 而我却 轻声告别这新生的黎明"
        )
        _infoMessageButton.setMessageMode(ElaMessageBarType.MessageMode.Information)
        _infoMessageButton.setPositionPolicy(ElaMessageBarType.PositionPolicy.TopLeft)

        _warningMessageButton = ElaMessageButton("Warning", self)
        _warningMessageButton.setBarTitle("Warning")
        _warningMessageButton.setBarText(
            "点燃星 亲手点燃黑暗森林的火星 蒙昧初醒 而我却 轻声告别这新生的黎明"
        )
        _warningMessageButton.setMessageMode(ElaMessageBarType.MessageMode.Warning)
        _warningMessageButton.setPositionPolicy(
            ElaMessageBarType.PositionPolicy.BottomLeft
        )

        _errorMessageButton = ElaMessageButton("Error", self)
        _errorMessageButton.setBarTitle("Error")
        _errorMessageButton.setBarText(
            "点燃星 亲手点燃黑暗森林的火星 蒙昧初醒 而我却 轻声告别这新生的黎明"
        )
        _errorMessageButton.setMessageMode(ElaMessageBarType.MessageMode.Error)
        _errorMessageButton.setPositionPolicy(
            ElaMessageBarType.PositionPolicy.BottomRight
        )

        messageButtonArea = ElaScrollPageArea(self)
        messageButtonLayout = QHBoxLayout(messageButtonArea)
        messageButtonText = ElaText("ElaMessageButton", self)
        messageButtonText.setTextPixelSize(15)
        messageButtonLayout.addWidget(messageButtonText)
        messageButtonLayout.addWidget(_messageButton)
        messageButtonLayout.addWidget(_infoMessageButton)
        messageButtonLayout.addWidget(_warningMessageButton)
        messageButtonLayout.addWidget(_errorMessageButton)
        messageButtonLayout.addStretch()
        messageButtonDisableSwitch = ElaToggleSwitch(self)
        messageButtonDisableText = ElaText("禁用", self)
        messageButtonDisableText.setTextPixelSize(15)
        messageButtonDisableSwitch.toggled.connect(
            lambda checked: (
                _messageButton.setDisabled(checked),
                _infoMessageButton.setDisabled(checked),
                _warningMessageButton.setDisabled(checked),
                _errorMessageButton.setDisabled(checked),
            )
        )
        messageButtonLayout.addWidget(messageButtonDisableSwitch)
        messageButtonLayout.addWidget(messageButtonDisableText)
        messageButtonLayout.addSpacing(10)

        _checkBox = ElaCheckBox("CheckBox", self)
        checkBoxArea = ElaScrollPageArea(self)
        checkBoxLayout = QHBoxLayout(checkBoxArea)
        checkBoxText = ElaText("ElacheckBox", self)
        checkBoxText.setTextPixelSize(15)
        checkBoxLayout.addWidget(checkBoxText)
        checkBoxLayout.addWidget(_checkBox)
        checkBoxLayout.addStretch()
        checkBoxDisableSwitch = ElaToggleSwitch(self)
        checkBoxDisableText = ElaText("禁用", self)
        checkBoxDisableText.setTextPixelSize(15)
        checkBoxDisableSwitch.toggled.connect(_checkBox.setDisabled)
        checkBoxLayout.addWidget(checkBoxDisableSwitch)
        checkBoxLayout.addWidget(checkBoxDisableText)
        checkBoxLayout.addSpacing(10)

        _spinBox = ElaSpinBox(self)
        spinBoxArea = ElaScrollPageArea(self)
        spinBoxLayout = QHBoxLayout(spinBoxArea)
        spinBoxText = ElaText("ElaSpinBox", self)
        spinBoxText.setTextPixelSize(15)
        spinBoxLayout.addWidget(spinBoxText)
        spinBoxLayout.addWidget(_spinBox)
        spinBoxLayout.addStretch()

        _slider = ElaSlider(self)
        sliderArea = ElaScrollPageArea(self)
        sliderLayout = QHBoxLayout(sliderArea)
        sliderText = ElaText("ElaSlider", self)
        sliderText.setTextPixelSize(15)
        sliderLayout.addWidget(sliderText)
        sliderLayout.addWidget(_slider)
        sliderLayout.addStretch()

        _radioButton = ElaRadioButton("RadioButton", self)
        radioButtonArea = ElaScrollPageArea(self)
        radioButtonLayout = QHBoxLayout(radioButtonArea)
        radioButtonText = ElaText("ElaRadioButton", self)
        radioButtonText.setTextPixelSize(15)
        radioButtonLayout.addWidget(radioButtonText)
        radioButtonLayout.addWidget(_radioButton)
        radioButtonLayout.addStretch()

        _progressBar = ElaProgressBar(self)
        _progressBar.setMinimum(0)
        _progressBar.setMaximum(0)
        progressBarArea = ElaScrollPageArea(self)
        progressBarLayout = QHBoxLayout(progressBarArea)
        progressBarText = ElaText("ElaProgressBar", self)
        progressBarText.setTextPixelSize(15)
        progressBarLayout.addWidget(progressBarText)
        progressBarLayout.addWidget(_progressBar)
        progressBarLayout.addStretch()

        _progressRing = ElaProgressRing(self)
        _progressRing.setValue(30)
        _progressPercentRing = ElaProgressRing(self)
        _progressPercentRing.setValue(50)
        _progressPercentRing.setValueDisplayMode(
            ElaProgressRingType.ValueDisplayMode.Percent
        )
        _progressBusyRing = ElaProgressRing(self)
        _progressBusyRing.setIsBusying(True)
        _progressBusyTransparentRing = ElaProgressRing(self)
        _progressBusyTransparentRing.setIsBusying(True)
        _progressBusyTransparentRing.setIsTransparent(True)
        progressRingArea = ElaScrollPageArea(self)
        progressRingArea.setFixedHeight(90)
        progressRingLayout = QHBoxLayout(progressRingArea)
        progressRingText = ElaText("ElaProgressRing", self)
        progressRingText.setTextPixelSize(15)
        progressRingLayout.addWidget(progressRingText)
        progressRingLayout.addWidget(_progressRing)
        progressRingLayout.addSpacing(10)
        progressRingLayout.addWidget(_progressPercentRing)
        progressRingLayout.addSpacing(10)
        progressRingLayout.addWidget(_progressBusyRing)
        progressRingLayout.addSpacing(10)
        progressRingLayout.addWidget(_progressBusyTransparentRing)
        progressRingLayout.addStretch()

        edit = ElaPlainTextEdit(self)
        edit.setPlainText("这是一个ElaPlainTextEdit  暂时放在这里")

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaBaseComponents")
        centerLayout = QVBoxLayout(centralWidget)
        centerLayout.addWidget(toggleSwitchArea)
        centerLayout.addWidget(toggleButtonArea)
        centerLayout.addWidget(comboBoxArea)
        centerLayout.addWidget(multiSelectComboBoxArea)
        centerLayout.addWidget(messageButtonArea)
        centerLayout.addWidget(checkBoxArea)
        centerLayout.addWidget(spinBoxArea)
        centerLayout.addWidget(sliderArea)
        centerLayout.addWidget(radioButtonArea)
        centerLayout.addWidget(progressBarArea)
        centerLayout.addWidget(progressRingArea)
        centerLayout.addWidget(edit)
        centerLayout.addStretch()
        centerLayout.setContentsMargins(0, 0, 0, 0)
        self.addCentralWidget(centralWidget, True, True, 0)

        homeStack1 = ElaText("HomeStack1", self)
        font = homeStack1.font()
        font.setPixelSize(32)
        homeStack1.setFont(font)
        homeStack1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        homeStack1.setWindowTitle("HomeStack1")
        self.addCentralWidget(homeStack1)
        homeStack2 = ElaText("HomeStack2", self)
        homeStack2.setFont(font)
        homeStack2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        homeStack2.setWindowTitle("HomeStack2")
        self.addCentralWidget(homeStack2)

    def mouseReleaseEvent(self, event: QMouseEvent):

        if event.button() == Qt.MouseButton.LeftButton:
            # //ElaMessageBar::success(ElaMessageBarType::TopRight, "Success", "Never Close Your Eyes", 2500);
            # //ElaMessageBar::success(ElaMessageBarType::TopRight, "Success", "Never Close Your Eyes", 1500);
            pass
        elif event.button() == Qt.MouseButton.BackButton:
            self.navigation(0)
        elif event.button() == Qt.MouseButton.ForwardButton:
            self.navigation(1)
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.navigation(2)
        return super().mouseReleaseEvent(event)
