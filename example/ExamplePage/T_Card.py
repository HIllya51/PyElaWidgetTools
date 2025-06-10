from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_Card(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("ElaCard")

        self.createCustomWidget(
            "一些常用的卡片组件被放置于此，可在此界面体验其效果并按需添加进项目中"
        )

        _lcdNumber = ElaLCDNumber(self)
        _lcdNumber.setIsUseAutoClock(True)
        _lcdNumber.setIsTransparent(False)
        _lcdNumber.setFixedHeight(100)

        _promotionCard = ElaPromotionCard(self)
        _promotionCard.setFixedSize(600, 300)
        _promotionCard.setCardPixmap(
            QPixmap(
                r"C:\Users\11737\Pictures\luna\3d144c38-7128-4154-9440-c2a6d80c1ae1.jpg"
            )
        )
        _promotionCard.setCardTitle("MiKu")
        _promotionCard.setPromotionTitle("SONG~")
        _promotionCard.setTitle("STYX HELIX")
        _promotionCard.setSubTitle("Never close your eyes, Searching for a True fate")

        _promotionView = ElaPromotionView(self)

        exampleCard1 = ElaPromotionCard(self)
        exampleCard1.setCardPixmap(
            QPixmap(
                r"C:\Users\11737\Pictures\luna\0ab5ebd5-8d21-42ea-ba56-526025d5ee7c.jpg"
            )
        )
        exampleCard1.setCardTitle("MiKu")
        exampleCard1.setPromotionTitle("SONG~")
        exampleCard1.setTitle("STYX HELIX")
        exampleCard1.setSubTitle("Never close your eyes, Searching for a True fate")

        exampleCard2 = ElaPromotionCard(self)
        exampleCard2.setCardPixmap(
            QPixmap(
                r"C:\Users\11737\Pictures\luna\0d80ac41-5265-403d-970c-7f6f286d4fa9.jpg"
            )
        )
        exampleCard2.setCardTitle("Beach")
        exampleCard2.setPromotionTitle("SONG~")
        exampleCard2.setTitle("STYX HELIX")
        exampleCard2.setSubTitle("Never close your eyes, Searching for a True fate")

        exampleCard3 = ElaPromotionCard(self)
        exampleCard3.setCardPixmap(
            QPixmap(
                r"C:\Users\11737\Pictures\luna\1bf95892-6e03-4b8b-b20b-1294350d5655.jpg"
            )
        )
        exampleCard3.setCardTitle("Dream")
        exampleCard3.setPromotionTitle("SONG~")
        exampleCard3.setTitle("STYX HELIX")
        exampleCard3.setSubTitle("Never close your eyes, Searching for a True fate")

        exampleCard4 = ElaPromotionCard(self)
        exampleCard4.setCardPixmap(
            QPixmap(
                r"C:\Users\11737\Pictures\luna\2cf04aa7d933c895a56eab53971373f0830200dd.jpg"
            )
        )
        exampleCard4.setCardTitle("Classroom")
        exampleCard4.setPromotionTitle("SONG~")
        exampleCard4.setTitle("STYX HELIX")
        exampleCard4.setSubTitle("Never close your eyes, Searching for a True fate")

        self.__ref = []
        _promotionView.appendPromotionCard(exampleCard1)
        _promotionView.appendPromotionCard(exampleCard2)
        _promotionView.appendPromotionCard(exampleCard3)
        _promotionView.appendPromotionCard(exampleCard4)
        self.__ref.append(exampleCard1)
        self.__ref.append(exampleCard2)
        self.__ref.append(exampleCard3)
        self.__ref.append(exampleCard4)
        _promotionView.setIsAutoScroll(True)

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaCard")
        centerLayout = QVBoxLayout(centralWidget)
        centerLayout.setContentsMargins(0, 0, 0, 0)
        centerLayout.addWidget(_lcdNumber)
        centerLayout.addSpacing(20)
        centerLayout.addWidget(_promotionCard)
        centerLayout.addSpacing(20)
        centerLayout.addWidget(_promotionView)
        centerLayout.addSpacing(100)
        centerLayout.addStretch()
        self.addCentralWidget(centralWidget, True, True, 0)
