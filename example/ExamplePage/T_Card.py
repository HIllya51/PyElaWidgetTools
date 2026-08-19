from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *
from _res import *


class T_Card(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaCard")

        self.createCustomWidget("一些常用的卡片组件被放置于此，可在此界面体验其效果并按需添加进项目中")

        self._lcdNumber = ElaLCDNumber(self)
        self._lcdNumber.setIsUseAutoClock(True)
        self._lcdNumber.setIsTransparent(False)
        # self._lcdNumber.setAutoClockFormat("hh:mm:ss")
        self._lcdNumber.setFixedHeight(100)

        self._promotionCard = ElaPromotionCard(self)
        self._promotionCard.setFixedSize(600, 300)
        self._promotionCard.setCardPixmap(placeholderPixmap(600, 300))
        self._promotionCard.setCardTitle("MiKu")
        self._promotionCard.setPromotionTitle("SONG~")
        self._promotionCard.setTitle("STYX HELIX")
        self._promotionCard.setSubTitle("Never close your eyes, Searching for a true fate")

        self._promotionView = ElaPromotionView(self)

        exampleCard1 = ElaPromotionCard(self)
        exampleCard1.setCardPixmap(placeholderPixmap(600, 300))
        exampleCard1.setCardTitle("MiKu")
        exampleCard1.setPromotionTitle("SONG~")
        exampleCard1.setTitle("STYX HELIX")
        exampleCard1.setSubTitle("Never close your eyes, Searching for a true fate")

        exampleCard2 = ElaPromotionCard(self)
        exampleCard2.setCardPixmap(placeholderPixmap(600, 300))
        exampleCard2.setCardTitle("Beach")
        exampleCard2.setPromotionTitle("SONG~")
        exampleCard2.setTitle("STYX HELIX")
        exampleCard2.setSubTitle("Never close your eyes, Searching for a true fate")

        exampleCard3 = ElaPromotionCard(self)
        exampleCard3.setCardPixmap(placeholderPixmap(600, 300))
        exampleCard3.setCardTitle("Dream")
        exampleCard3.setPromotionTitle("SONG~")
        exampleCard3.setTitle("STYX HELIX")
        exampleCard3.setSubTitle("Never close your eyes, Searching for a true fate")

        exampleCard4 = ElaPromotionCard(self)
        exampleCard4.setCardPixmap(placeholderPixmap(600, 300))
        exampleCard4.setCardTitle("Classroom")
        exampleCard4.setPromotionTitle("SONG~")
        exampleCard4.setTitle("STYX HELIX")
        exampleCard4.setSubTitle("Never close your eyes, Searching for a true fate")

        self._promotionView.appendPromotionCard(exampleCard1)
        self._promotionView.appendPromotionCard(exampleCard2)
        self._promotionView.appendPromotionCard(exampleCard3)
        self._promotionView.appendPromotionCard(exampleCard4)
        self._promotionView.setIsAutoScroll(True)
        # keep appended cards referenced to avoid GC
        self._ref = [exampleCard1, exampleCard2, exampleCard3, exampleCard4]

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaCard")
        centerLayout = QVBoxLayout(centralWidget)
        centerLayout.setContentsMargins(0, 0, 0, 0)
        centerLayout.addWidget(self._lcdNumber)
        centerLayout.addSpacing(20)
        centerLayout.addWidget(self._promotionCard)
        centerLayout.addSpacing(20)
        centerLayout.addWidget(self._promotionView)
        centerLayout.addSpacing(100)
        centerLayout.addStretch()
        self.addCentralWidget(centralWidget, True, True, 0)
