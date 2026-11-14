from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5ElaWidgetTools import *
from _res import *


class T_About(ElaDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(460, 440)
        self.setWindowTitle("关于 ElaWidgetTools")
        self.setWindowIcon(QIcon(placeholderPixmap(60, 60)))
        self.setIsFixedSize(True)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowButtonFlags(ElaAppBarType.ButtonType.CloseButtonHint)

        imageCard = ElaImageCard(self)
        imageCard.setFixedSize(64, 64)
        imageCard.setIsPreserveAspectCrop(False)
        imageCard.setCardImage(placeholderImage(64, 64))
        titleText = ElaText("ElaWidgetTools", self)
        titleText.setTextPixelSize(24)
        titleText.setIsBold(True)
        subtitleText = ElaText("Fluent 风格的 Qt Widgets 通用组件库", self)
        titleLayout = QVBoxLayout()
        titleLayout.setSpacing(6)
        titleLayout.addWidget(titleText)
        titleLayout.addWidget(subtitleText)
        identityLayout = QHBoxLayout()
        identityLayout.setSpacing(20)
        identityLayout.addWidget(imageCard)
        identityLayout.addLayout(titleLayout, 1)
        runtimeText = ElaText(
            "当前运行环境\nQt {} · {}".format(qVersion(), QSysInfo.buildCpuArchitecture()), self
        )
        licenseText = ElaText(
            "开源许可 · MIT\n可在项目中使用、修改和分发，具体条款请参阅项目许可证。", self
        )
        contactText = ElaText("联系作者 · 80985@qq.com\n交流社区 · 850243692（QQ）", self)
        contactText.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        repositoryButton = ElaPushButton("打开项目主页", self)
        repositoryButton.setIsAccent(True)
        repositoryButton.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://github.com/Liniyous/ElaWidgetTools"))
        )
        copyrightText = ElaText("© 2026 Liniyous", self)
        copyrightText.setTextPixelSize(12)
        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(28, 52, 28, 24)
        mainLayout.setSpacing(20)
        mainLayout.addLayout(identityLayout)
        mainLayout.addWidget(runtimeText)
        mainLayout.addWidget(licenseText)
        mainLayout.addWidget(contactText)
        mainLayout.addStretch()
        actionLayout = QHBoxLayout()
        actionLayout.addWidget(copyrightText)
        actionLayout.addStretch()
        actionLayout.addWidget(repositoryButton)
        mainLayout.addLayout(actionLayout)
