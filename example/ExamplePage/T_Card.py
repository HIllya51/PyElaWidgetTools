from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *
from _res import *


class T_Card(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("卡片展示")
        self.createCustomWidget("组合图片、标题和操作入口，体验卡片悬停、轮播与数字显示。", "卡片与内容展示")
        mainLayout = self.createPageLayout()

        # 推广卡片
        promotionSection = self.addExampleSection(
            mainLayout, "推广卡片 · ElaPromotionCard", "移动指针或点击卡片，观察图片上的光效。"
        )
        self._promotionCard = ElaPromotionCard(self)
        self._promotionCard.setMinimumWidth(0)
        self._promotionCard.setFixedHeight(260)
        self._promotionCard.setCardPixmap(placeholderPixmap(600, 260))
        self._promotionCard.setCardTitle("Ela 组件展示")
        self._promotionCard.setPromotionTitle("精选内容")
        self._promotionCard.setTitle("发现更好的界面")
        self._promotionCard.setSubTitle("图片与文字组成内容入口")
        promotionSection.addWidget(self._promotionCard)

        # 链接与交互卡片
        linkSection = self.addExampleSection(
            mainLayout,
            "链接与交互卡片",
            "ElaAcrylicUrlCard 用于链接入口，ElaInteractiveCard 用于可点击的内容项。",
        )
        linkLayout = ElaFlowLayout(0, 24, 16)
        repositoryCard = ElaAcrylicUrlCard(self)
        repositoryCard.setFixedSize(210, 210)
        repositoryCard.setCardPixmap(placeholderPixmap(210, 210))
        repositoryCard.setTitle("项目源码")
        repositoryCard.setSubTitle("浏览 ElaWidgetTools 的组件与示例")
        repositoryCard.setUrl("https://github.com/Liniyous/ElaWidgetTools")
        projectCard = ElaInteractiveCard(self)
        projectCard.setFixedSize(300, 100)
        projectCard.setCardPixmap(placeholderPixmap(300, 100))
        projectCard.setTitle("示例项目")
        projectCard.setSubTitle("点击选择此项目")
        cardResultText = ElaText("尚未选择项目", self)
        projectCard.clicked.connect(lambda: cardResultText.setText("已选择：示例项目"))
        linkLayout.addWidget(repositoryCard)
        linkLayout.addWidget(self.createLabeledControl("内容入口", projectCard))
        linkSection.addLayout(linkLayout)
        linkSection.addWidget(cardResultText)

        # 卡片轮播
        carouselSection = self.addExampleSection(
            mainLayout, "卡片轮播 · ElaPromotionView", "点击两侧卡片或滚动鼠标滚轮切换，也可以启用自动轮播。"
        )
        self._promotionView = ElaPromotionView(self)
        self._promotionView.setFixedHeight(260)
        titles = ["灵感画廊", "海边时光", "梦境色彩", "学习空间"]
        for index, title in enumerate(titles):
            card = ElaPromotionCard(self)
            card.setCardPixmap(placeholderPixmap(600, 260))
            card.setCardTitle("精选 {}".format(index + 1))
            card.setTitle(title)
            card.setSubTitle("点击切换当前卡片")
            card.setTitlePixelSize(22)
            self._promotionView.appendPromotionCard(card)
        self._promotionView.setCardExpandWidth(360)
        self._promotionView.setCardCollapseWidth(170)
        autoScrollCheckBox = ElaCheckBox("自动轮播", self)
        autoScrollCheckBox.toggled.connect(self._promotionView.setIsAutoScroll)
        carouselSection.addWidget(autoScrollCheckBox)
        carouselSection.addWidget(self._promotionView)

        # 数字显示
        clockSection = self.addExampleSection(
            mainLayout, "数字显示 · ElaLCDNumber", "使用自动时钟显示当前时间，可切换为透明背景。"
        )
        self._lcdNumber = ElaLCDNumber(self)
        self._lcdNumber.setFixedSize(300, 86)
        self._lcdNumber.setIsUseAutoClock(True)
        self._lcdNumber.setAutoClockFormat("hh:mm:ss")
        transparentCheckBox = ElaCheckBox("透明背景", self)
        transparentCheckBox.toggled.connect(self._lcdNumber.setIsTransparent)
        clockSection.addWidget(self._lcdNumber, 0, Qt.AlignmentFlag.AlignLeft)
        clockSection.addWidget(transparentCheckBox)
