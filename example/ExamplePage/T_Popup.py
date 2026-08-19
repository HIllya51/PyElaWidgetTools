from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_Popup(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaPopup")

        self.createCustomWidget("一些常用的弹出组件被放置于此，可在此界面体验其效果并按需添加进项目中")

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaPopup")

        self._toolButton = ElaToolButton(self)
        self._toolButton.setIsTransparent(False)
        self._toolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        # self._toolButton.setPopupMode(QToolButton::MenuButtonPopup)
        self._toolButton.setText("ElaToolButton")

        menu = ElaMenu(self)
        menu.addElaIconAction(ElaIconType.IconName.JackOLantern, "JackOLantern")
        menu.addElaIconAction(ElaIconType.IconName.LacrosseStick, "LacrosseStick")
        self._toolButton.setMenu(menu)
        self._toolButton.setElaIcon(ElaIconType.IconName.Broom)

        toolButtonArea = ElaScrollPageArea(self)
        toolButtonLayout = QHBoxLayout(toolButtonArea)
        toolButtonText = ElaText("ElaToolButton", self)
        toolButtonText.setTextPixelSize(15)
        toolButtonLayout.addWidget(toolButtonText)
        toolButtonLayout.addWidget(self._toolButton)
        toolButtonLayout.addStretch()

        self._colorDialog = ElaColorDialog(self)
        colorText = ElaText(self._colorDialog.getCurrentColorRGB(), self)
        colorText.setTextPixelSize(15)
        colorDialogButton = ElaPushButton(self)
        colorDialogButton.setFixedSize(35, 35)
        colorDialogButton.setLightDefaultColor(self._colorDialog.getCurrentColor())
        colorDialogButton.setLightHoverColor(self._colorDialog.getCurrentColor())
        colorDialogButton.setLightPressColor(self._colorDialog.getCurrentColor())
        colorDialogButton.setDarkDefaultColor(self._colorDialog.getCurrentColor())
        colorDialogButton.setDarkHoverColor(self._colorDialog.getCurrentColor())
        colorDialogButton.setDarkPressColor(self._colorDialog.getCurrentColor())

        def _colorDialogButtonClicked():
            self._colorDialog.exec_()

        colorDialogButton.clicked.connect(_colorDialogButtonClicked)

        def _onColorSelected(color):
            colorDialogButton.setLightDefaultColor(color)
            colorDialogButton.setLightHoverColor(color)
            colorDialogButton.setLightPressColor(color)
            colorDialogButton.setDarkDefaultColor(color)
            colorDialogButton.setDarkHoverColor(color)
            colorDialogButton.setDarkPressColor(color)
            colorText.setText(self._colorDialog.getCurrentColorRGB())

        self._colorDialog.colorSelected.connect(_onColorSelected)

        colorDialogArea = ElaScrollPageArea(self)
        colorDialogLayout = QHBoxLayout(colorDialogArea)
        colorDialogText = ElaText("ElaColorDialog", self)
        colorDialogText.setTextPixelSize(15)
        colorDialogLayout.addWidget(colorDialogText)
        colorDialogLayout.addWidget(colorDialogButton)
        colorDialogLayout.addWidget(colorText)
        colorDialogLayout.addStretch()

        self._calendar = ElaCalendar(self)

        self._calendarPicker = ElaCalendarPicker(self)
        calendarPickerArea = ElaScrollPageArea(self)
        calendarPickerLayout = QHBoxLayout(calendarPickerArea)
        calendarPickerText = ElaText("ElaCalendarPicker", self)
        calendarPickerText.setTextPixelSize(15)
        calendarPickerLayout.addWidget(calendarPickerText)
        calendarPickerLayout.addWidget(self._calendarPicker)
        calendarPickerLayout.addStretch()

        self._keyBinder = ElaKeyBinder(self)
        keyBinderArea = ElaScrollPageArea(self)
        keyBinderLayout = QHBoxLayout(keyBinderArea)
        keyBinderText = ElaText("ElaKeyBinder", self)
        keyBinderText.setTextPixelSize(15)
        keyBinderLayout.addWidget(keyBinderText)
        keyBinderLayout.addWidget(self._keyBinder)
        keyBinderLayout.addStretch()

        self._roller = ElaRoller(self)
        rollerItemList = []
        for i in range(100):
            rollerItemList.append(str(i + 1))
        self._roller.setItemList(rollerItemList)
        rollerArea = ElaScrollPageArea(self)
        rollerArea.setFixedHeight(220)
        rollerLayout = QHBoxLayout(rollerArea)
        rollerText = ElaText("ElaRoller", self)
        rollerText.setTextPixelSize(15)
        rollerLayout.addWidget(rollerText)
        rollerLayout.addWidget(self._roller)
        rollerLayout.addSpacing(30)

        rollerPickerText = ElaText("ElaRollerPicker", self)
        rollerPickerText.setTextPixelSize(15)
        rollerLayout.addWidget(rollerPickerText)

        currentTime = QTime.currentTime()
        currentHour = "{:02d}".format(currentTime.hour())
        currentMinute = "{:02d}".format(currentTime.minute())
        self._timeRollerPicker = ElaRollerPicker(self)
        hourItemList = []
        for i in range(24):
            hourItemList.append("{:02d}".format(i))
        minuteList = []
        for i in range(61):
            minuteList.append("{:02d}".format(i))
        self._timeRollerPicker.addRoller(hourItemList)
        self._timeRollerPicker.addRoller(minuteList)
        self._timeRollerPicker.addRoller(["AM", "PM"], False)
        self._timeRollerPicker.setCurrentData(
            [currentHour, currentMinute, "PM" if currentTime.hour() >= 12 else "AM"]
        )

        self._clockRollerPicker = ElaRollerPicker(self)
        self._clockRollerPicker.addRoller(hourItemList)
        self._clockRollerPicker.addRoller(minuteList)
        self._clockRollerPicker.setRollerWidth(0, 135)
        self._clockRollerPicker.setRollerWidth(1, 135)
        self._clockRollerPicker.setCurrentData([currentHour, currentMinute])

        rollerPickerLayout = QVBoxLayout()
        rollerPickerLayout.addWidget(self._timeRollerPicker)
        rollerPickerLayout.addWidget(self._clockRollerPicker)
        rollerLayout.addLayout(rollerPickerLayout)
        rollerLayout.addStretch()

        self._drawer = ElaDrawerArea(self)
        drawerHeader = QWidget(self)
        drawerHeaderLayout = QHBoxLayout(drawerHeader)
        drawerIcon = ElaText(self)
        drawerIcon.setTextPixelSize(15)
        drawerIcon.setElaIcon(ElaIconType.IconName.MessageArrowDown)
        drawerIcon.setFixedSize(25, 25)
        drawerText = ElaText("ElaDrawer", self)
        drawerText.setTextPixelSize(15)

        drawerSwitch = ElaToggleSwitch(self)
        drawerSwitchText = ElaText("关", self)
        drawerSwitchText.setTextPixelSize(15)

        def _onDrawerSwitchToggled(toggled):
            if toggled:
                drawerSwitchText.setText("开")
                self._drawer.expand()
            else:
                drawerSwitchText.setText("关")
                self._drawer.collapse()

        drawerSwitch.toggled.connect(_onDrawerSwitchToggled)

        def _onDrawerExpandStateChanged(isExpand):
            drawerSwitch.setIsToggled(isExpand)

        self._drawer.expandStateChanged.connect(_onDrawerExpandStateChanged)

        drawerHeaderLayout.addWidget(drawerIcon)
        drawerHeaderLayout.addWidget(drawerText)
        drawerHeaderLayout.addStretch()
        drawerHeaderLayout.addWidget(drawerSwitchText)
        drawerHeaderLayout.addWidget(drawerSwitch)

        self._drawer.setDrawerHeader(drawerHeader)
        drawerWidget1 = QWidget(self)
        drawerWidget1.setFixedHeight(75)
        drawerWidget1Layout = QHBoxLayout(drawerWidget1)
        drawerCheckBox1 = ElaCheckBox("测试窗口1", self)
        drawerWidget1Layout.addSpacing(60)
        drawerWidget1Layout.addWidget(drawerCheckBox1)

        drawerWidget2 = QWidget(self)
        drawerWidget2.setFixedHeight(75)
        drawerWidget2Layout = QHBoxLayout(drawerWidget2)
        drawerCheckBox2 = ElaCheckBox("测试窗口2", self)
        drawerWidget2Layout.addSpacing(60)
        drawerWidget2Layout.addWidget(drawerCheckBox2)

        drawerWidget3 = QWidget(self)
        drawerWidget3.setFixedHeight(75)
        drawerWidget3Layout = QHBoxLayout(drawerWidget3)
        drawerCheckBox3 = ElaCheckBox("测试窗口3", self)
        drawerWidget3Layout.addSpacing(60)
        drawerWidget3Layout.addWidget(drawerCheckBox3)

        self._drawer.addDrawer(drawerWidget1)
        self._drawer.addDrawer(drawerWidget2)
        self._drawer.addDrawer(drawerWidget3)

        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setContentsMargins(0, 0, 0, 0)
        centerVLayout.addWidget(toolButtonArea)
        centerVLayout.addWidget(colorDialogArea)
        centerVLayout.addWidget(calendarPickerArea)
        centerVLayout.addWidget(self._calendar)
        centerVLayout.addWidget(keyBinderArea)
        centerVLayout.addWidget(self._drawer)
        centerVLayout.addWidget(rollerArea)
        centerVLayout.addStretch()
        self.addCentralWidget(centralWidget, True, False, 0)
