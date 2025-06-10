from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_Graphics(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("ElaGraphics")

        self.createCustomWidget(
            "图形视图框架被放置于此，可在此界面体验其效果，按住Ctrl进行缩放，按住Shitf进行连接"
        )

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaGraphics")

        scene = ElaGraphicsScene(self)
        scene.setSceneRect(0, 0, 1500, 1500)
        item1 = ElaGraphicsItem()
        item1.setWidth(100)
        item1.setHeight(100)
        item1.setMaxLinkPortCount(100)
        item1.setMaxLinkPortCount(1)
        item2 = ElaGraphicsItem()
        item2.setWidth(100)
        item2.setHeight(100)
        scene.addItem(item1)
        scene.addItem(item2)
        view = ElaGraphicsView(scene)
        view.setScene(scene)
        view.setFixedHeight(600)
        viewLayout = QHBoxLayout()
        viewLayout.setContentsMargins(0, 0, 12, 0)
        viewLayout.addWidget(view)

        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setContentsMargins(0, 0, 0, 0)
        centerVLayout.addLayout(viewLayout)
        centerVLayout.addStretch()
        self.addCentralWidget(centralWidget, True, False, 0)
