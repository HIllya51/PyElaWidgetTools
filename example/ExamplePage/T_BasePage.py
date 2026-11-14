import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5ElaWidgetTools import *


class T_BasePage(ElaScrollPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        eTheme.themeModeChanged.connect(lambda _mode: self.update() if not parent else None)
        self.setContentsMargins(20, 5, 0, 0)

    def createCustomWidget(self, description: str, title: str = ""):
        # 展示页显式启用统一页头 Home 沿用自己的布局
        self.setTitleVisible(False)
        self.setContentsMargins(28, 12, 20, 0)
        headerWidget = QWidget(self)
        titleText = ElaText(title if title else self.windowTitle(), self)
        titleText.setTextPixelSize(eApp.getFontPixelSize() + 14)
        titleText.setIsBold(True)
        titleText.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)

        themeButton = ElaToolButton(self)
        themeButton.setFixedSize(32, 32)
        themeButton.setIsTransparent(False)
        themeButton.setElaIcon(ElaIconType.IconName.MoonStars)
        themeButton.setToolTip("切换浅色与深色主题")
        themeButton.setAccessibleName("切换主题")
        themeButton.clicked.connect(
            lambda: eTheme.setThemeMode(
                ElaThemeType.ThemeMode.Dark
                if eTheme.getThemeMode() == ElaThemeType.ThemeMode.Light
                else ElaThemeType.ThemeMode.Light
            )
        )

        # 对应 C++ 的 QFileInfo(__FILE__)：本文件与各页面同目录，取调用者类的源文件
        sourcePath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), type(self).__name__ + ".py"
        )
        sourceButton = ElaToolButton(self)
        sourceButton.setText("示例源码")
        sourceButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        sourceButton.setElaIcon(ElaIconType.IconName.Code)
        sourceButton.setIsTransparent(False)
        sourceButton.setVisible(os.path.exists(sourcePath))
        sourceButton.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl.fromLocalFile(sourcePath))
        )

        titleLayout = QHBoxLayout()
        titleLayout.setSpacing(12)
        titleLayout.addWidget(titleText, 1)
        titleLayout.addWidget(sourceButton)
        titleLayout.addWidget(themeButton)
        descriptionText = ElaText(description, self)
        descriptionText.setTextPixelSize(eApp.getFontPixelSize())
        descriptionText.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        mainLayout = QVBoxLayout(headerWidget)
        mainLayout.setContentsMargins(0, 0, 0, 20)
        mainLayout.setSpacing(10)
        mainLayout.addLayout(titleLayout)
        mainLayout.addWidget(descriptionText)
        self.setTopCustomWidget(headerWidget)

    def createPageLayout(self):
        contentWidget = QWidget(self)
        contentWidget.setObjectName("ElaExampleContent")
        contentWidget.setStyleSheet("#ElaExampleContent{background-color:transparent;}")
        contentWidget.setWindowTitle(self.windowTitle())
        mainLayout = QVBoxLayout(contentWidget)
        mainLayout.setContentsMargins(0, 0, 2, 28)
        mainLayout.setSpacing(24)
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        mainLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.addCentralWidget(contentWidget, True, False, 0)
        return mainLayout

    def addExampleSection(self, pageLayout, title: str, description: str = ""):
        sectionWidget = QWidget(self)
        sectionWidget.setObjectName("ElaExampleSection")
        sectionWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sectionWidget.setStyleSheet("#ElaExampleSection{background-color:transparent;}")
        titleText = ElaText(title, self)
        titleText.setTextPixelSize(eApp.getFontPixelSize() + 5)
        titleText.setIsBold(True)
        mainLayout = QVBoxLayout(sectionWidget)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(10)
        mainLayout.addWidget(titleText)
        if description:
            descriptionText = ElaText(description, self)
            descriptionText.setTextPixelSize(eApp.getFontPixelSize())
            descriptionText.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
            mainLayout.addWidget(descriptionText)
        previewArea = ElaScrollPageArea(self)
        previewArea.setMinimumHeight(0)
        # QWIDGETSIZE_MAX 的值（各 Python 绑定未必导出该宏，直接写字面量）
        previewArea.setMaximumHeight(16777215)
        previewArea.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        previewArea.setBorderRadius(8)
        previewArea.setProperty("ElaExampleCard", True)
        previewLayout = QVBoxLayout(previewArea)
        previewLayout.setContentsMargins(20, 20, 20, 20)
        previewLayout.setSpacing(16)
        mainLayout.addWidget(previewArea)
        pageLayout.addWidget(sectionWidget)
        return previewLayout

    def createLabeledControl(self, title: str, control):
        fieldWidget = QWidget(self)
        fieldWidget.setObjectName("ElaExampleField")
        fieldWidget.setStyleSheet("#ElaExampleField{background-color:transparent;}")
        labelText = ElaText(title, self)
        labelText.setTextPixelSize(eApp.getFontPixelSize())
        labelText.setBuddy(control)
        control.setAccessibleName(title)
        mainLayout = QVBoxLayout(fieldWidget)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(10)
        mainLayout.addWidget(labelText)
        mainLayout.addWidget(control, 0, Qt.AlignmentFlag.AlignLeft)
        return fieldWidget

    def createSettingRow(self, title: str, description: str, control):
        rowWidget = QWidget(self)
        rowWidget.setObjectName("ElaExampleSettingRow")
        rowWidget.setStyleSheet("#ElaExampleSettingRow{background-color:transparent;}")
        titleText = ElaText(title, self)
        titleText.setTextPixelSize(eApp.getFontPixelSize() + 1)
        descriptionText = ElaText(description, self)
        descriptionText.setTextPixelSize(eApp.getFontPixelSize() - 1)
        descriptionText.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        textLayout = QVBoxLayout()
        textLayout.setSpacing(4)
        textLayout.addWidget(titleText)
        textLayout.addWidget(descriptionText)
        mainLayout = QHBoxLayout(rowWidget)
        mainLayout.setContentsMargins(0, 4, 0, 4)
        mainLayout.setSpacing(20)
        mainLayout.addLayout(textLayout, 1)
        mainLayout.addWidget(control, 0, Qt.AlignmentFlag.AlignVCenter)
        control.setAccessibleName(title)
        return rowWidget

    def setPreviewPlaceholder(self, previewCard, description: str):
        previewCard.setMinimumWidth(0)
        previewCard.setFixedHeight(678)
        previewCard.setIsPreserveAspectCrop(True)
        placeholderText = ElaText(description, previewCard)
        placeholderText.setTextPixelSize(eApp.getFontPixelSize() + 2)
        placeholderText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLayout = QVBoxLayout(previewCard)
        mainLayout.addWidget(placeholderText)

        def _onCardImageChanged():
            placeholderText.setVisible(previewCard.getCardImage().isNull())

        previewCard.pCardImageChanged.connect(_onCardImageChanged)
