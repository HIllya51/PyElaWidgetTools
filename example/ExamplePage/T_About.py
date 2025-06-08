from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *


class T_About(ElaWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("关于..")
        self.setWindowIcon(QIcon(":/include/Image/Moon.jpg"))
        self.setIsFixedSize(True)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowButtonFlags(ElaAppBarType.ButtonType.CloseButtonHint)
        pixCard = ElaImageCard(self)
        pixCard.setFixedSize(60, 60)
        pixCard.setIsPreserveAspectCrop(False)
        pixCard.setCardImage(QImage(":/include/Image/Moon.jpg"))

        pixCardLayout = QVBoxLayout()
        pixCardLayout.addWidget(pixCard)
        pixCardLayout.addStretch()

        versionText = ElaText("ElaWidgetTools-LK-2024", self)
        versionTextFont = versionText.font()
        versionTextFont.setWeight(QFont.Weight.Bold)
        versionText.setFont(versionTextFont)
        versionText.setWordWrap(False)
        versionText.setTextPixelSize(18)

        licenseText = ElaText("MIT授权协议", self)
        licenseText.setWordWrap(False)
        licenseText.setTextPixelSize(14)
        supportText = ElaText(
            "Windows支持版本: QT5.12以上\nLinux支持版本: Qt5.14以上", self
        )
        supportText.setWordWrap(False)
        supportText.setTextPixelSize(14)
        contactText = ElaText("作者: 3056769574@qq.com\n交流群: 850243692(QQ)", self)
        contactText.setWordWrap(False)
        contactText.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        contactText.setTextPixelSize(14)
        helperText = ElaText("用户手册及API文档付费提供\n提供额外的专业技术支持", self)
        helperText.setWordWrap(False)
        helperText.setTextPixelSize(14)
        copyrightText = ElaText("版权所有 © 2024 Liniyous", self)
        copyrightText.setWordWrap(False)
        copyrightText.setTextPixelSize(14)

        textLayout = QVBoxLayout()
        textLayout.setSpacing(15)
        textLayout.addWidget(versionText)
        textLayout.addWidget(licenseText)
        textLayout.addWidget(supportText)
        textLayout.addWidget(contactText)
        textLayout.addWidget(helperText)
        textLayout.addWidget(copyrightText)
        textLayout.addStretch()

        contentLayout = QHBoxLayout()
        contentLayout.addSpacing(30)
        contentLayout.addLayout(pixCardLayout)
        contentLayout.addSpacing(30)
        contentLayout.addLayout(textLayout)

        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(0, 25, 0, 0)
        mainLayout.addLayout(contentLayout)
