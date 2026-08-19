import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


if sys.platform == "win32":
    class T_ElaScreen(T_BasePage):
        def __init__(self, parent=None):
            super().__init__(parent)
            # 预览窗口标题
            self.setWindowTitle("ElaScreen")

            # 顶部元素
            self.createCustomWidget("DXGI录制组件被放置于此，可在此界面预览录制效果")

            dxgiManager = ElaDxgiManager.getInstance()
            dxgiManager.setGrabArea(1920, 1080)

            dxgiScreenArea = ElaScrollPageArea(self)
            dxgiScreenArea.setFixedHeight(700)
            dxgiScreenLayout = QHBoxLayout(dxgiScreenArea)
            self._dxgiScreen = ElaImageCard(self)
            self._dxgiScreen.setFixedHeight(678)
            dxgiScreenLayout.addWidget(self._dxgiScreen)

            def _grabImageUpdate(img):
                self._dxgiScreen.setCardImage(img)

            dxgiManager.grabImageUpdate.connect(_grabImageUpdate)

            dxText = ElaText("显卡选择", self)
            dxText.setTextPixelSize(15)
            self._dxComboBox = ElaComboBox(self)
            self._dxComboBox.addItems(dxgiManager.getDxDeviceList())
            self._dxComboBox.setCurrentIndex(dxgiManager.getDxDeviceID())

            outputText = ElaText("屏幕选择", self)
            outputText.setTextPixelSize(15)
            self._outputComboBox = ElaComboBox(self)
            self._outputComboBox.addItems(dxgiManager.getOutputDeviceList())
            self._outputComboBox.setCurrentIndex(dxgiManager.getOutputDeviceID())

            def _dxCurrentIndexChanged(index):
                dxgiManager.setDxDeviceID(index)
                self._outputComboBox.blockSignals(True)
                self._outputComboBox.clear()
                self._outputComboBox.addItems(dxgiManager.getOutputDeviceList())
                self._outputComboBox.setCurrentIndex(dxgiManager.getOutputDeviceID())
                self._outputComboBox.blockSignals(False)
                self._dxgiScreen.update()

            self._dxComboBox.currentIndexChanged[int].connect(_dxCurrentIndexChanged)

            def _outputCurrentIndexChanged(index):
                dxgiManager.setOutputDeviceID(index)
                self._dxgiScreen.update()

            self._outputComboBox.currentIndexChanged[int].connect(_outputCurrentIndexChanged)

            startButton = ElaToggleButton("捕获", self)

            def _startToggled(isToggled):
                if isToggled:
                    dxgiManager.startGrabScreen()
                else:
                    dxgiManager.stopGrabScreen()
                    self._dxgiScreen.setCardImage(QImage())
                    self._dxgiScreen.update()

            startButton.toggled.connect(_startToggled)

            comboBoxLayout = QHBoxLayout()
            comboBoxLayout.addWidget(dxText)
            comboBoxLayout.addWidget(self._dxComboBox)
            comboBoxLayout.addSpacing(10)
            comboBoxLayout.addWidget(outputText)
            comboBoxLayout.addWidget(self._outputComboBox)
            comboBoxLayout.addWidget(startButton)
            comboBoxLayout.addStretch()

            centralWidget = QWidget(self)
            centralWidget.setWindowTitle("ElaScreen")
            centerLayout = QVBoxLayout(centralWidget)
            centerLayout.setContentsMargins(0, 0, 0, 0)
            centerLayout.addLayout(comboBoxLayout)
            centerLayout.addWidget(dxgiScreenArea)
            self.addCentralWidget(centralWidget, False, True)
else:
    T_ElaScreen = None
