from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_Popup(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("弹出与选择")
        self.createCustomWidget("展开菜单、选择日期与颜色，体验对话框和可展开区域。", "弹出与选择")
        mainLayout = self.createPageLayout()

        # 菜单与对话框
        menuSection = self.addExampleSection(
            mainLayout, "菜单与对话框", "点击菜单项可查看选择结果，对话框用于需要确认的操作。"
        )
        popupLayout = ElaFlowLayout(0, 16, 16)
        menuResultText = ElaText("菜单选择：尚未选择", self)
        self._toolButton = ElaToolButton(self)
        self._toolButton.setIsTransparent(False)
        self._toolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self._toolButton.setText("文件操作")
        self._toolButton.setElaIcon(ElaIconType.IconName.FolderOpen)
        menu = ElaMenu(self)
        for text in ["新建项目", "保存项目", "导出副本"]:
            menu.addAction(text).triggered.connect(
                lambda _checked=False, t=text: menuResultText.setText("菜单选择：" + t)
            )
        self._toolButton.setMenu(menu)

        confirmButton = ElaPushButton("显示确认对话框", self)
        confirmDialog = ElaContentDialog(self)
        confirmWidget = QWidget(confirmDialog)
        confirmLayout = QVBoxLayout(confirmWidget)
        confirmLayout.setContentsMargins(24, 24, 24, 16)
        confirmLayout.setSpacing(8)
        confirmTitleText = ElaText("是否保存当前更改？", confirmWidget)
        confirmTitleText.setTextPixelSize(confirmTitleText.getTextPixelSize() + 6)
        confirmTitleText.setIsBold(True)
        confirmDescriptionText = ElaText("选择一个操作，结果会显示在示例区域。", confirmWidget)
        confirmLayout.addWidget(confirmTitleText)
        confirmLayout.addWidget(confirmDescriptionText)
        confirmDialog.setCentralWidget(confirmWidget)
        confirmDialog.setLeftButtonText("取消")
        confirmDialog.setMiddleButtonText("不保存")
        confirmDialog.setRightButtonText("保存")
        confirmButton.clicked.connect(confirmDialog.exec_)
        confirmDialog.rightButtonClicked.connect(
            lambda: menuResultText.setText("对话框结果：保存更改")
        )
        confirmDialog.middleButtonClicked.connect(
            lambda: menuResultText.setText("对话框结果：不保存")
        )
        popupLayout.addWidget(self._toolButton)
        popupLayout.addWidget(confirmButton)
        menuSection.addLayout(popupLayout)
        menuSection.addWidget(menuResultText)

        # 教学提示
        teachingSection = self.addExampleSection(
            mainLayout, "教学提示", "ElaTeachingTip 指向目标控件，支持自定义内容与点击外部关闭。"
        )
        teachingLayout = ElaFlowLayout(0, 16, 16)
        teachingButton = ElaPushButton("功能引导", self)
        customTipButton = ElaPushButton("自定义内容", self)
        transientTipButton = ElaPushButton("轻量提示", self)
        teachingResultText = ElaText("提示中的按钮和自定义控件可直接交互。", self)

        teachingTip = ElaTeachingTip(self)
        teachingTip.setTargetWidget(teachingButton)
        teachingTip.setTitle("试试新的工作方式")
        teachingTip.setSubTitle("提示会指向相关控件，\n帮助你了解功能和操作方式。")
        teachingTip.setElaIcon(ElaIconType.IconName.Lightbulb)
        teachingTip.setActionButtonText("了解更多")
        teachingTip.setCloseButtonText("知道了")
        teachingTip.actionButtonClicked.connect(
            lambda: (
                teachingResultText.setText("已选择：了解更多"),
                teachingTip.setIsOpen(False),
            )
        )

        customTip = ElaTeachingTip(self)
        customTip.setTargetWidget(customTipButton)
        customTip.setTitle("调整提示内容")
        customTip.setSubTitle("可以在提示中直接使用输入框和选项。")
        customTip.setTipWidth(336)
        # C++ 中 new QWidget 由 setCustomWidget 接管所有权；Python 侧给它一个父对象，
        # 避免无引用时被 GC 提前析构（sip 未标注 /Transfer/）
        customTipWidget = QWidget(self)
        customTipLayout = QVBoxLayout(customTipWidget)
        customTipLayout.setContentsMargins(0, 0, 0, 0)
        customTipLayout.setSpacing(8)
        displayNameEdit = ElaLineEdit(customTipWidget)
        displayNameEdit.setPlaceholderText("输入显示名称")
        displayNameEdit.setText("我的工作区")
        rememberCheckBox = ElaCheckBox("下次继续显示提示", customTipWidget)
        rememberCheckBox.setChecked(True)
        customTipLayout.addWidget(displayNameEdit)
        customTipLayout.addWidget(rememberCheckBox)
        customTip.setCustomWidget(customTipWidget)
        customTip.setActionButtonText("应用")
        customTip.setCloseButtonText("取消")
        customTip.actionButtonClicked.connect(
            lambda: (
                teachingResultText.setText("已应用：" + displayNameEdit.text()),
                customTip.setIsOpen(False),
            )
        )

        transientTip = ElaTeachingTip(self)
        transientTip.setTargetWidget(transientTipButton)
        transientTip.setTitle("点击其他位置即可关闭")
        transientTip.setSubTitle("点击或滚动提示外部区域，浮层会自动收起。")
        transientTip.setIsLightDismissEnabled(True)

        tips = [teachingTip, customTip, transientTip]

        def _showTip(current):
            isOpening = not current.getIsOpen()
            for tip in tips:
                tip.setIsOpen(tip is current and isOpening)

        teachingButton.clicked.connect(lambda: _showTip(teachingTip))
        customTipButton.clicked.connect(lambda: _showTip(customTip))
        transientTipButton.clicked.connect(lambda: _showTip(transientTip))
        teachingLayout.addWidget(teachingButton)
        teachingLayout.addWidget(customTipButton)
        teachingLayout.addWidget(transientTipButton)
        teachingSection.addLayout(teachingLayout)
        teachingSection.addWidget(teachingResultText)

        # 颜色选择
        colorSection = self.addExampleSection(
            mainLayout, "颜色选择", "ElaColorDialog 支持颜色预览、RGB / HSV 输入和自定义色位。"
        )
        self._colorDialog = ElaColorDialog(self)
        colorDialogButton = ElaPushButton("选择颜色", self)
        colorPreviewButton = ElaPushButton(self)
        colorPreviewButton.setFixedSize(40, 32)
        colorPreviewButton.setAccessibleName("当前颜色预览")
        colorText = ElaText(self)

        def _updateColor(color):
            colorPreviewButton.setLightDefaultColor(color)
            colorPreviewButton.setLightHoverColor(color)
            colorPreviewButton.setLightPressColor(color)
            colorPreviewButton.setDarkDefaultColor(color)
            colorPreviewButton.setDarkHoverColor(color)
            colorPreviewButton.setDarkPressColor(color)
            colorPreviewButton.update()
            colorText.setText(color.name().upper())

        _updateColor(self._colorDialog.getCurrentColor())
        self._colorDialog.colorSelected.connect(_updateColor)
        colorDialogButton.clicked.connect(self._colorDialog.exec_)
        colorPreviewButton.clicked.connect(self._colorDialog.exec_)
        colorLayout = QHBoxLayout()
        colorLayout.setSpacing(16)
        colorLayout.addWidget(colorDialogButton)
        colorLayout.addWidget(colorPreviewButton)
        colorLayout.addWidget(colorText)
        colorLayout.addStretch()
        colorSection.addLayout(colorLayout)

        # 日期选择
        calendarSection = self.addExampleSection(
            mainLayout, "日期选择", "ElaCalendarPicker 与 ElaCalendar 联动，支持月份切换和直接选择日期。"
        )
        self._calendar = ElaCalendar(self)
        self._calendarPicker = ElaCalendarPicker(self)
        dateText = ElaText(QDate.currentDate().toString("yyyy-MM-dd"), self)
        dateOptionsWidget = self.createLabeledControl("弹出式日期选择", self._calendarPicker)
        dateOptionsWidget.layout().addWidget(dateText)
        calendarLayout = ElaFlowLayout(0, 24, 16)
        calendarLayout.addWidget(self._calendar)
        calendarLayout.addWidget(dateOptionsWidget)

        def _onCalendarClicked(date):
            self._calendarPicker.setSelectedDate(date)
            dateText.setText(date.toString("yyyy-MM-dd"))

        def _onPickerDateChanged(date):
            self._calendar.setSelectedDate(date)
            dateText.setText(date.toString("yyyy-MM-dd"))

        self._calendar.clicked.connect(_onCalendarClicked)
        self._calendarPicker.selectedDateChanged.connect(_onPickerDateChanged)
        calendarSection.addLayout(calendarLayout)

        # 滚轮选择
        rollerSection = self.addExampleSection(
            mainLayout, "滚轮选择", "ElaRoller · ElaRollerPicker，使用滚轮或打开选择器设置值。"
        )
        self._roller = ElaRoller(self)
        months = []
        hours = []
        minutes = []
        for index in range(1, 13):
            months.append("{} 月".format(index))
        for index in range(24):
            hours.append("{:02d}".format(index))
        for index in range(60):
            minutes.append("{:02d}".format(index))
        self._roller.setItemList(months)
        self._timeRollerPicker = ElaRollerPicker(self)
        self._timeRollerPicker.addRoller(hours)
        self._timeRollerPicker.addRoller(minutes)
        currentTime = QTime.currentTime()
        self._timeRollerPicker.setCurrentData(
            [currentTime.toString("HH"), currentTime.toString("mm")]
        )
        self._clockRollerPicker = ElaRollerPicker(self)
        self._clockRollerPicker.addRoller(["工作日", "周末", "每天"], False)
        self._clockRollerPicker.setRollerWidth(0, 180)
        rollerLayout = ElaFlowLayout(0, 28, 16)
        rollerLayout.addWidget(self.createLabeledControl("月份", self._roller))
        rollerLayout.addWidget(self.createLabeledControl("24 小时时间", self._timeRollerPicker))
        rollerLayout.addWidget(self.createLabeledControl("提醒周期", self._clockRollerPicker))
        rollerSection.addLayout(rollerLayout)

        # 快捷键绑定
        keySection = self.addExampleSection(
            mainLayout, "快捷键绑定", "点击 ElaKeyBinder 后按下组合键，在对话框中确认或重置。"
        )
        self._keyBinder = ElaKeyBinder(self)
        self._keyBinder.setFixedWidth(260)
        keySection.addWidget(self._keyBinder, 0, Qt.AlignmentFlag.AlignLeft)

        # 可展开区域
        drawerSection = self.addExampleSection(
            mainLayout, "可展开区域", "ElaDrawerArea 将次要选项折叠收纳，点击标题展开。"
        )
        self._drawer = ElaDrawerArea(self)
        headerWidget = QWidget(self)
        headerLayout = QHBoxLayout(headerWidget)
        headerLayout.setContentsMargins(16, 8, 16, 8)
        headerLayout.addWidget(ElaText("更多偏好设置", self))
        headerLayout.addStretch()
        self._drawer.setDrawerHeader(headerWidget)
        for title in ["启动时恢复上次工作区", "完成操作后显示消息", "允许后台自动更新"]:
            optionWidget = QWidget(self)
            optionWidget.setFixedHeight(54)
            optionLayout = QHBoxLayout(optionWidget)
            optionLayout.setContentsMargins(20, 8, 20, 8)
            optionLayout.addWidget(ElaCheckBox(title, self))
            optionLayout.addStretch()
            self._drawer.addDrawer(optionWidget)
        drawerSection.addWidget(self._drawer)
