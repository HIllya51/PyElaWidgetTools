import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *


class T_ElaScreen(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("屏幕采集")
        self.createCustomWidget("选择显卡和显示器，使用 DXGI 预览本机屏幕画面。")
        mainLayout = self.createPageLayout()
        if sys.platform != "win32":
            descriptionText = ElaText(
                "DXGI 屏幕采集仅支持 Windows，其他控件示例可正常使用。", 15, self
            )
            descriptionText.setWordWrap(True)
            mainLayout.addWidget(descriptionText)
            return

        captureLayout = self.addExampleSection(
            mainLayout, "屏幕捕获", "选择捕获源后开启采集，画面仅在本地预览。"
        )
        dxgiManager = ElaDxgiManager.getInstance()
        self._graphicsComboBox = ElaComboBox(self)
        self._graphicsComboBox.setFixedWidth(240)
        self._graphicsComboBox.addItems(dxgiManager.getDxDeviceList())
        self._graphicsComboBox.setCurrentIndex(dxgiManager.getDxDeviceID())
        self._outputComboBox = ElaComboBox(self)
        self._outputComboBox.setFixedWidth(200)
        self._outputComboBox.addItems(dxgiManager.getOutputDeviceList())
        self._outputComboBox.setCurrentIndex(dxgiManager.getOutputDeviceID())
        self._captureToggleButton = ElaToggleButton("捕获", self)
        self._captureToggleButton.setEnabled(self._outputComboBox.count() > 0)
        self._captureImageCard = ElaImageCard(self)
        self.setPreviewPlaceholder(self._captureImageCard, "尚未开始捕获\n选择屏幕后点击捕获")

        def _onGraphicsChanged(index):
            dxgiManager.setDxDeviceID(index)
            self._outputComboBox.blockSignals(True)
            self._outputComboBox.clear()
            self._outputComboBox.addItems(dxgiManager.getOutputDeviceList())
            self._outputComboBox.setCurrentIndex(dxgiManager.getOutputDeviceID())
            self._outputComboBox.blockSignals(False)
            self._captureToggleButton.setEnabled(self._outputComboBox.count() > 0)
            self._captureImageCard.setCardImage(QImage())

        def _onOutputChanged(index):
            dxgiManager.setOutputDeviceID(index)
            self._captureImageCard.setCardImage(QImage())

        def _onCaptureToggled(isToggled):
            if isToggled:
                dxgiManager.startGrabScreen()
            else:
                dxgiManager.stopGrabScreen()
                self._captureImageCard.setCardImage(QImage())

        def _onGrabImageUpdate(image):
            if dxgiManager.getIsGrabScreen():
                self._captureImageCard.setCardImage(image)

        self._graphicsComboBox.currentIndexChanged.connect(_onGraphicsChanged)
        self._outputComboBox.currentIndexChanged.connect(_onOutputChanged)
        self._captureToggleButton.toggled.connect(_onCaptureToggled)
        dxgiManager.grabImageUpdate.connect(_onGrabImageUpdate)

        sourceLayout = ElaFlowLayout(0, 16, 16)
        sourceLayout.addWidget(self.createLabeledControl("显卡", self._graphicsComboBox))
        sourceLayout.addWidget(self.createLabeledControl("屏幕", self._outputComboBox))
        sourceLayout.addWidget(self.createLabeledControl("操作", self._captureToggleButton))
        captureLayout.addLayout(sourceLayout)
        captureLayout.addWidget(self._captureImageCard)

        # 对应 C++ 析构中的停止采集：窗口退出时确保采集停止
        def _stopGrabOnQuit():
            if ElaDxgiManager.getInstance().getIsGrabScreen():
                ElaDxgiManager.getInstance().stopGrabScreen()

        QApplication.instance().aboutToQuit.connect(_stopGrabOnQuit)
