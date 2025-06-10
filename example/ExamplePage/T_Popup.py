from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_Popup(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("ElaPopup")

        self.createCustomWidget(
            "一些常用的弹出组件被放置于此，可在此界面体验其效果并按需添加进项目中"
        )

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaPopup")

        _toolButton = ElaToolButton(self)
        _toolButton.setIsTransparent(False)
        _toolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        _toolButton.setText("ElaToolButton")

        menu = ElaMenu(self)
        menu.addElaIconAction(ElaIconType.IconName.JackOLantern, "JackOLantern")
        menu.addElaIconAction(ElaIconType.IconName.LacrosseStick, "LacrosseStick")
        _toolButton.setMenu(menu)
        _toolButton.setElaIcon(ElaIconType.IconName.Broom)

        toolButtonArea = ElaScrollPageArea(self)
        toolButtonLayout = QHBoxLayout(toolButtonArea)
        toolButtonText = ElaText("ElaToolButton", self)
        toolButtonText.setTextPixelSize(15)
        toolButtonLayout.addWidget(toolButtonText)
        toolButtonLayout.addWidget(_toolButton)
        toolButtonLayout.addStretch()

        _colorDialog = ElaColorDialog(self)
        colorText = ElaText(_colorDialog.getCurrentColorRGB(), self)
        colorText.setTextPixelSize(15)
        colorDialogButton = ElaPushButton(self)
        colorDialogButton.setFixedSize(35, 35)
        colorDialogButton.setLightDefaultColor(_colorDialog.getCurrentColor())
        colorDialogButton.setLightHoverColor(_colorDialog.getCurrentColor())
        colorDialogButton.setLightPressColor(_colorDialog.getCurrentColor())
        colorDialogButton.setDarkDefaultColor(_colorDialog.getCurrentColor())
        colorDialogButton.setDarkHoverColor(_colorDialog.getCurrentColor())
        colorDialogButton.setDarkPressColor(_colorDialog.getCurrentColor())
        colorDialogButton.clicked.connect(lambda: _colorDialog.exec())

        def __(color: QColor):
            colorDialogButton.setLightDefaultColor(color)
            colorDialogButton.setLightHoverColor(color)
            colorDialogButton.setLightPressColor(color)
            colorDialogButton.setDarkDefaultColor(color)
            colorDialogButton.setDarkHoverColor(color)
            colorDialogButton.setDarkPressColor(color)
            colorText.setText(_colorDialog.getCurrentColorRGB())

        _colorDialog.colorSelected.connect(__)
        colorDialogArea = ElaScrollPageArea(self)
        colorDialogLayout = QHBoxLayout(colorDialogArea)
        colorDialogText = ElaText("ElaColorDialog", self)
        colorDialogText.setTextPixelSize(15)
        colorDialogLayout.addWidget(colorDialogText)
        colorDialogLayout.addWidget(colorDialogButton)
        colorDialogLayout.addWidget(colorText)
        colorDialogLayout.addStretch()

        _calendar = ElaCalendar(self)

        _calendarPicker = ElaCalendarPicker(self)
        calendarPickerArea = ElaScrollPageArea(self)
        calendarPickerLayout = QHBoxLayout(calendarPickerArea)
        calendarPickerText = ElaText("ElaCalendarPicker", self)
        calendarPickerText.setTextPixelSize(15)
        calendarPickerLayout.addWidget(calendarPickerText)
        calendarPickerLayout.addWidget(_calendarPicker)
        calendarPickerLayout.addStretch()

        _keyBinder = ElaKeyBinder(self)
        keyBinderArea = ElaScrollPageArea(self)
        keyBinderLayout = QHBoxLayout(keyBinderArea)
        keyBinderText = ElaText("ElaKeyBinder", self)
        keyBinderText.setTextPixelSize(15)
        keyBinderLayout.addWidget(keyBinderText)
        keyBinderLayout.addWidget(_keyBinder)
        keyBinderLayout.addStretch()

        _roller = ElaRoller(self)
        rollerItemList = []
        for i in range(100):
            rollerItemList.append(str(i + 1))
        _roller.setItemList(rollerItemList)
        rollerArea = ElaScrollPageArea(self)
        rollerArea.setFixedHeight(220)
        rollerLayout = QHBoxLayout(rollerArea)
        rollerText = ElaText("ElaRoller", self)
        rollerText.setTextPixelSize(15)
        rollerLayout.addWidget(rollerText)
        rollerLayout.addWidget(_roller)
        rollerLayout.addStretch()

        _drawer = ElaDrawerArea(self)
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

        def __(toggled: bool):
            if toggled:
                drawerSwitchText.setText("开")
                _drawer.expand()
            else:
                drawerSwitchText.setText("关")
                _drawer.collpase()

        drawerSwitch.toggled.connect(__)
        _drawer.expandStateChanged.connect(drawerSwitch.setIsToggled)

        drawerHeaderLayout.addWidget(drawerIcon)
        drawerHeaderLayout.addWidget(drawerText)
        drawerHeaderLayout.addStretch()
        drawerHeaderLayout.addWidget(drawerSwitchText)
        drawerHeaderLayout.addWidget(drawerSwitch)

        _drawer.setDrawerHeader(drawerHeader)
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

        _drawer.addDrawer(drawerWidget1)
        _drawer.addDrawer(drawerWidget2)
        _drawer.addDrawer(drawerWidget3)

        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setContentsMargins(0, 0, 0, 0)
        centerVLayout.addWidget(toolButtonArea)
        centerVLayout.addWidget(colorDialogArea)
        centerVLayout.addWidget(calendarPickerArea)
        centerVLayout.addWidget(_calendar)
        centerVLayout.addWidget(keyBinderArea)
        centerVLayout.addWidget(_drawer)
        centerVLayout.addWidget(rollerArea)
        centerVLayout.addStretch()
        self.addCentralWidget(centralWidget, True, False, 0)
