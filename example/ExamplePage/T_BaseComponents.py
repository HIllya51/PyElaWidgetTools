from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_BaseComponents(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("基础控件")
        self.createCustomWidget("直接试用按钮、选择、输入与进度控件，观察状态变化和操作结果。", "基础控件")
        mainLayout = self.createPageLayout()

        # 按钮与操作
        buttonsSection = self.addExampleSection(
            mainLayout, "按钮与操作", "ElaPushButton · ElaToolButton · ElaToggleButton"
        )
        buttonLayout = ElaFlowLayout(0, 16, 16)
        normalButton = ElaPushButton("普通按钮", self)
        accentButton = ElaPushButton("保存更改", self)
        accentButton.setIsAccent(True)
        disabledButton = ElaPushButton("不可用", self)
        disabledButton.setEnabled(False)
        iconButton = ElaToolButton(self)
        iconButton.setElaIcon(ElaIconType.IconName.FloppyDisk)
        iconButton.setText("保存")
        iconButton.setIsTransparent(False)
        iconButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self._toggleButton = ElaToggleButton("固定到顶部", self)
        self._toggleButton.setFixedSize(
            max(
                100,
                self._toggleButton.fontMetrics().horizontalAdvance(self._toggleButton.getText()) + 24,
            ),
            normalButton.height(),
        )
        iconButton.setFixedHeight(normalButton.height())
        for button in [normalButton, accentButton, disabledButton]:
            button.setMinimumWidth(100)
            buttonLayout.addWidget(button)
        buttonLayout.addWidget(iconButton)
        buttonLayout.addWidget(self._toggleButton)
        buttonResultText = ElaText("操作结果：等待点击", self)
        for button in [normalButton, accentButton]:
            button.clicked.connect(
                lambda _checked=False, b=button: buttonResultText.setText(
                    "操作结果：已点击 " + b.text()
                )
            )
        iconButton.clicked.connect(lambda: buttonResultText.setText("操作结果：已保存"))
        self._toggleButton.toggled.connect(
            lambda checked: buttonResultText.setText(
                "操作结果：已固定" if checked else "操作结果：已取消固定"
            )
        )
        buttonsSection.addLayout(buttonLayout)
        buttonsSection.addWidget(buttonResultText)

        # 开关与选择
        selectionSection = self.addExampleSection(
            mainLayout,
            "开关与选择",
            "开关控制即时设置，复选框支持多个选项，单选按钮用于互斥选择。",
        )
        selectionLayout = ElaFlowLayout(0, 28, 18)
        self._toggleSwitch = ElaToggleSwitch(self)
        self._checkBox = ElaCheckBox("接收通知", self)
        partialCheckBox = ElaCheckBox("部分选中", self)
        partialCheckBox.setTristate(True)
        partialCheckBox.setCheckState(Qt.CheckState.PartiallyChecked)
        selectionLayout.addWidget(self.createLabeledControl("ElaToggleSwitch", self._toggleSwitch))
        selectionLayout.addWidget(self.createLabeledControl("ElaCheckBox", self._checkBox))
        selectionLayout.addWidget(self.createLabeledControl("三态复选框", partialCheckBox))
        radioLayout = ElaFlowLayout(0, 20, 12)
        radioGroup = QButtonGroup(self)
        self._radioButton = ElaRadioButton("每天", self)
        radioButtons = [self._radioButton, ElaRadioButton("工作日", self), ElaRadioButton("周末", self)]
        for radioButton in radioButtons:
            radioGroup.addButton(radioButton)
            radioLayout.addWidget(radioButton)
        self._radioButton.setChecked(True)
        selectionSection.addLayout(selectionLayout)
        selectionSection.addWidget(ElaText("提醒频率 · ElaRadioButton", self))
        selectionSection.addLayout(radioLayout)

        # 下拉选择
        comboSection = self.addExampleSection(
            mainLayout, "下拉选择", "单选确定一个选项，多选以标签展示结果，可直接移除标签。"
        )
        comboLayout = ElaFlowLayout(0, 24, 16)
        self._comboBox = ElaComboBox(self)
        self._comboBox.setFixedWidth(240)
        self._comboBox.addItems(["设计模式", "开发模式", "阅读模式"])
        self._multiSelectComboBox = ElaMultiSelectComboBox(self)
        self._multiSelectComboBox.setFixedWidth(240)
        self._multiSelectComboBox.addItems(
            ["界面设计", "交互开发", "质量验证", "跨平台兼容", "文档", "性能优化"]
        )
        self._multiSelectComboBox.setCurrentSelection(["界面设计", "文档"])
        comboLayout.addWidget(self.createLabeledControl("ElaComboBox", self._comboBox))
        comboLayout.addWidget(
            self.createLabeledControl("ElaMultiSelectComboBox", self._multiSelectComboBox)
        )
        comboResultText = ElaText("当前模式：设计模式", self)
        multiResultText = ElaText("已选标签：界面设计、文档", self)
        multiResultText.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        self._comboBox.currentTextChanged.connect(
            lambda text: comboResultText.setText("当前模式：" + text)
        )
        self._multiSelectComboBox.currentTextListChanged.connect(
            lambda values: multiResultText.setText(
                "已选标签：无" if not values else "已选标签：" + "、".join(values)
            )
        )
        disableComboCheckBox = ElaCheckBox("禁用本组选择控件", self)
        disableComboCheckBox.toggled.connect(
            lambda checked: (
                self._comboBox.setDisabled(checked),
                self._multiSelectComboBox.setDisabled(checked),
            )
        )
        comboSection.addLayout(comboLayout)
        comboSection.addWidget(comboResultText)
        comboSection.addWidget(multiResultText)
        comboSection.addWidget(disableComboCheckBox)

        # 文本输入
        textSection = self.addExampleSection(
            mainLayout, "文本输入", "ElaLineEdit · ElaPlainTextEdit，点击输入框可观察焦点底线的展开。"
        )
        editLayout = ElaFlowLayout(0, 24, 16)
        projectEdit = ElaLineEdit(self)
        projectEdit.setFixedWidth(240)
        projectEdit.setPlaceholderText("输入项目名称")
        projectEdit.setClearButtonEnabled(True)
        passwordEdit = ElaLineEdit(self)
        passwordEdit.setFixedWidth(240)
        passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        passwordEdit.setPlaceholderText("输入密码")
        editLayout.addWidget(self.createLabeledControl("项目名称", projectEdit))
        editLayout.addWidget(self.createLabeledControl("密码输入", passwordEdit))
        descriptionEdit = ElaPlainTextEdit(self)
        descriptionEdit.setPlaceholderText("填写项目说明，支持多行输入和右键编辑菜单。")
        descriptionEdit.setFixedHeight(120)
        descriptionEdit.setPlainText("这是一个多行文本输入示例。\n可以自由编辑内容，或使用右键菜单进行常用编辑操作。")
        textSection.addLayout(editLayout)
        textSection.addWidget(ElaText("项目说明 · ElaPlainTextEdit", self))
        textSection.addWidget(descriptionEdit)

        # 数值输入
        numberSection = self.addExampleSection(
            mainLayout, "数值输入", "ElaSpinBox · ElaDoubleSpinBox，可切换整数输入框的按钮布局。"
        )
        numberLayout = ElaFlowLayout(0, 24, 16)
        self._spinBox = ElaSpinBox(self)
        self._spinBox.setRange(0, 100)
        self._spinBox.setValue(24)
        self._spinBox.setFixedWidth(180)
        decimalSpinBox = ElaDoubleSpinBox(self)
        decimalSpinBox.setRange(0, 100)
        decimalSpinBox.setDecimals(1)
        decimalSpinBox.setSingleStep(0.5)
        decimalSpinBox.setValue(3.5)
        decimalSpinBox.setFixedWidth(180)
        modeComboBox = ElaComboBox(self)
        modeComboBox.setFixedWidth(180)
        modeComboBox.addItem("内嵌按钮", int(ElaSpinBoxType.ButtonMode.Inline))
        modeComboBox.addItem("紧凑按钮", int(ElaSpinBoxType.ButtonMode.Compact))
        modeComboBox.addItem("两侧箭头", int(ElaSpinBoxType.ButtonMode.Side))
        modeComboBox.addItem("两侧加减", int(ElaSpinBoxType.ButtonMode.PMSide))

        def _onSpinButtonModeChanged(index):
            self._spinBox.setButtonMode(
                ElaSpinBoxType.ButtonMode(int(modeComboBox.itemData(index)))
            )

        modeComboBox.currentIndexChanged.connect(_onSpinButtonModeChanged)
        numberLayout.addWidget(self.createLabeledControl("整数", self._spinBox))
        numberLayout.addWidget(self.createLabeledControl("小数", decimalSpinBox))
        numberLayout.addWidget(self.createLabeledControl("按钮布局", modeComboBox))
        numberSection.addLayout(numberLayout)

        # 滑块与进度
        progressSection = self.addExampleSection(
            mainLayout, "滑块与进度", "拖动滑块，同时观察进度条和进度环；不确定进度用于等待中的操作。"
        )
        self._slider = ElaSlider(self)
        self._slider.setRange(0, 100)
        self._slider.setValue(45)
        self._slider.setAccessibleName("演示进度")
        self._progressBar = ElaProgressBar(self)
        self._progressBar.setRange(0, 100)
        self._progressBar.setValue(45)
        self._progressRing = ElaProgressRing(self)
        self._progressRing.setValue(45)
        self._progressPercentRing = ElaProgressRing(self)
        self._progressPercentRing.setValue(45)
        self._progressPercentRing.setValueDisplayMode(ElaProgressRingType.ValueDisplayMode.Percent)
        self._progressBusyRing = ElaProgressRing(self)
        self._progressBusyRing.setIsBusying(True)
        self._progressBusyTransparentRing = ElaProgressRing(self)
        self._progressBusyTransparentRing.setIsBusying(True)
        self._progressBusyTransparentRing.setIsTransparent(True)
        progressLayout = ElaFlowLayout(0, 28, 16)
        for ring in [
            self._progressRing,
            self._progressPercentRing,
            self._progressBusyRing,
            self._progressBusyTransparentRing,
        ]:
            ring.setFixedSize(54, 54)
        progressLayout.addWidget(self.createLabeledControl("数值", self._progressRing))
        progressLayout.addWidget(self.createLabeledControl("百分比", self._progressPercentRing))
        progressLayout.addWidget(self.createLabeledControl("等待中", self._progressBusyRing))
        progressLayout.addWidget(
            self.createLabeledControl("透明背景", self._progressBusyTransparentRing)
        )

        def _onSliderValueChanged(value):
            self._progressBar.setValue(value)
            self._progressRing.setValue(value)
            self._progressPercentRing.setValue(value)

        self._slider.valueChanged.connect(_onSliderValueChanged)
        progressSection.addWidget(self._slider)
        progressSection.addWidget(self._progressBar)
        progressSection.addLayout(progressLayout)

        # 状态反馈
        messageSection = self.addExampleSection(
            mainLayout, "状态反馈", "ElaMessageButton，点击不同按钮查看成功、提示、警告和错误消息。"
        )
        messageLayout = ElaFlowLayout(0, 12, 12)
        self._messageButton = ElaMessageButton("成功", self)
        self._infoMessageButton = ElaMessageButton("提示", self)
        self._warningMessageButton = ElaMessageButton("警告", self)
        self._errorMessageButton = ElaMessageButton("错误", self)
        self._infoMessageButton.setMessageMode(ElaMessageBarType.MessageMode.Information)
        self._warningMessageButton.setMessageMode(ElaMessageBarType.MessageMode.Warning)
        self._errorMessageButton.setMessageMode(ElaMessageBarType.MessageMode.Error)
        for button in [
            self._messageButton,
            self._infoMessageButton,
            self._warningMessageButton,
            self._errorMessageButton,
        ]:
            button.setBarTitle(button.text())
            button.setBarText("这是一条状态消息示例，可用于反馈操作结果。")
            button.setMessageTargetWidget(self)
            button.setDisplayMsec(2500)
            messageLayout.addWidget(button)
        messageSection.addLayout(messageLayout)
