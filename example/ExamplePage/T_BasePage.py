from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *


class T_BasePage(ElaScrollPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        eTheme.themeModeChanged.connect(lambda _: self.update() if parent else None)

    def createCustomWidget(self, desText: str):
        customWidget = QWidget(self)
        subTitleText = ElaText(self)
        subTitleText.setText("https://github.com/Liniyous/ElaWidgetTools")
        subTitleText.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        subTitleText.setTextPixelSize(11)

        documentationButton = ElaToolButton(self)
        documentationButton.setFixedHeight(35)
        documentationButton.setIsTransparent(False)
        documentationButton.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        )

        documentationButton.setText("Documentation")
        documentationButton.setElaIcon(ElaIconType.IconName.FileDoc)
        documentationMenu = ElaMenu(self)
        documentationMenu.addElaIconAction(
            ElaIconType.IconName.CardsBlank, "CardsBlank"
        )
        documentationMenu.addElaIconAction(
            ElaIconType.IconName.EarthAmericas, "EarthAmericas"
        )
        self._documentationMenu = documentationMenu
        documentationButton.setMenu(documentationMenu)

        sourceButton = ElaToolButton(self)
        sourceButton.setFixedHeight(35)
        sourceButton.setIsTransparent(False)
        sourceButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        sourceButton.setText("Source")
        sourceButton.setElaIcon(ElaIconType.IconName.NfcSymbol)
        sourceMenu = ElaMenu(self)
        sourceMenu.addElaIconAction(ElaIconType.IconName.FireBurner, "FireBurner")
        sourceMenu.addElaIconAction(ElaIconType.IconName.Galaxy, "Galaxy~~~~")
        self._sourceMenu = sourceMenu
        sourceButton.setMenu(sourceMenu)

        themeButton = ElaToolButton(self)
        themeButton.setFixedSize(35, 35)
        themeButton.setIsTransparent(False)
        themeButton.setElaIcon(ElaIconType.IconName.MoonStars)
        themeButton.clicked.connect(
            lambda: eTheme.setThemeMode(
                ElaThemeType.ThemeMode.Dark
                if eTheme.getThemeMode() == ElaThemeType.ThemeMode.Light
                else ElaThemeType.ThemeMode.Light
            )
        )

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(documentationButton)
        buttonLayout.addSpacing(5)
        buttonLayout.addWidget(sourceButton)
        buttonLayout.addStretch()
        buttonLayout.addWidget(themeButton)
        buttonLayout.addSpacing(15)

        descText = ElaText(self)
        descText.setText(desText)
        descText.setTextPixelSize(13)

        topLayout = QVBoxLayout(customWidget)
        topLayout.setContentsMargins(0, 0, 0, 0)
        topLayout.addWidget(subTitleText)
        topLayout.addSpacing(5)
        topLayout.addLayout(buttonLayout)
        topLayout.addSpacing(5)
        topLayout.addWidget(descText)
        self.setCustomWidget(customWidget)
