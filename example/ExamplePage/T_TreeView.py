from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *
from ModelView.T_TreeViewModel import *


class T_TreeView(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaTreeView")

        self.createCustomWidget("树型视图被放置于此，可在此界面体验其效果并按需添加进项目中")

        treeModel = T_TreeViewModel(self)
        treeLayout = QHBoxLayout()
        treeLayout.setContentsMargins(0, 0, 10, 0)
        treeSettingWidget = QWidget(self)
        treeSettingWidgetLayout = QVBoxLayout(treeSettingWidget)
        treeSettingWidgetLayout.setContentsMargins(0, 0, 0, 0)
        treeSettingWidgetLayout.setSpacing(15)

        dataText = ElaText("树模型总数据条数：{}".format(treeModel.getItemCount()), self)
        dataText.setTextPixelSize(15)

        # ItemHeight
        itemHeightText = ElaText("ItemHeight", self)
        itemHeightText.setTextPixelSize(15)
        itemHeightSlider = ElaSlider(self)
        itemHeightSlider.setRange(200, 600)
        itemHeightSlider.setValue(350)
        itemHeightValueText = ElaText("35", self)
        itemHeightValueText.setTextPixelSize(15)
        itemHeightSlider.valueChanged.connect(
            lambda value: self._onItemHeightChanged(
                value, itemHeightValueText
            )
        )
        itemHeightLayout = QHBoxLayout()
        itemHeightLayout.setContentsMargins(0, 0, 0, 0)
        itemHeightLayout.addWidget(itemHeightText)
        itemHeightLayout.addWidget(itemHeightSlider)
        itemHeightLayout.addWidget(itemHeightValueText)

        # HeaderMargin
        headerMarginText = ElaText("HeaderMargin", self)
        headerMarginText.setTextPixelSize(15)
        headerMarginSlider = ElaSlider(self)
        headerMarginSlider.setRange(0, 200)
        headerMarginSlider.setValue(50)
        headerMarginValueText = ElaText("5", self)
        headerMarginValueText.setTextPixelSize(15)
        headerMarginSlider.valueChanged.connect(
            lambda value: self._onHeaderMarginChanged(
                value, headerMarginValueText
            )
        )
        headerMarginLayout = QHBoxLayout()
        headerMarginLayout.setContentsMargins(0, 0, 0, 0)
        headerMarginLayout.addWidget(headerMarginText)
        headerMarginLayout.addWidget(headerMarginSlider)
        headerMarginLayout.addWidget(headerMarginValueText)

        # Indentation
        indentationText = ElaText("Indentation", self)
        indentationText.setTextPixelSize(15)
        indentationSlider = ElaSlider(self)
        indentationSlider.setRange(200, 1000)
        indentationSlider.setValue(200)
        indentationValueText = ElaText("20", self)
        indentationValueText.setTextPixelSize(15)
        indentationSlider.valueChanged.connect(
            lambda value: self._onIndentationChanged(
                value, indentationValueText
            )
        )
        indentationLayout = QHBoxLayout()
        indentationLayout.setContentsMargins(0, 0, 0, 0)
        indentationLayout.addWidget(indentationText)
        indentationLayout.addWidget(indentationSlider)
        indentationLayout.addWidget(indentationValueText)

        # 展开/收起全部
        expandCollapseLayout = QHBoxLayout()
        expandCollapseLayout.setContentsMargins(0, 0, 0, 0)
        expandButton = ElaPushButton("展开全部", self)
        expandButton.setFixedWidth(80)
        expandButton.clicked.connect(lambda: self._treeView.expandAll())

        collapseButton = ElaPushButton("收起全部", self)
        collapseButton.setFixedWidth(80)
        collapseButton.clicked.connect(lambda: self._treeView.collapseAll())
        expandCollapseLayout.addWidget(expandButton)
        expandCollapseLayout.addWidget(collapseButton)
        expandCollapseLayout.addStretch()

        treeSettingWidgetLayout.addWidget(dataText)
        treeSettingWidgetLayout.addLayout(itemHeightLayout)
        treeSettingWidgetLayout.addLayout(headerMarginLayout)
        treeSettingWidgetLayout.addLayout(indentationLayout)
        treeSettingWidgetLayout.addLayout(expandCollapseLayout)
        treeSettingWidgetLayout.addStretch()

        # TreeView
        treeText = ElaText("ElaTreeView", self)
        treeText.setTextPixelSize(18)
        self._treeView = ElaTreeView(self)
        treeViewFloatScrollBar = ElaScrollBar(
            self._treeView.verticalScrollBar(), self._treeView
        )
        treeViewFloatScrollBar.setIsAnimation(True)
        headerFont = self._treeView.header().font()
        headerFont.setPixelSize(16)
        self._treeView.header().setFont(headerFont)
        self._treeView.setFixedHeight(450)
        self._treeView.setModel(treeModel)
        treeViewLayout = QVBoxLayout()
        treeViewLayout.setContentsMargins(0, 0, 0, 0)
        treeViewLayout.addWidget(self._treeView)
        treeViewLayout.addStretch()
        treeLayout.addWidget(treeSettingWidget)
        treeLayout.addLayout(treeViewLayout)

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaView")
        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setContentsMargins(0, 0, 0, 0)
        centerVLayout.addWidget(treeText)
        centerVLayout.addSpacing(10)
        centerVLayout.addLayout(treeLayout)
        self.addCentralWidget(centralWidget, True, False, 0)

    def _onItemHeightChanged(self, value, valueText):
        valueText.setText(str(value // 10))
        self._treeView.setItemHeight(value // 10)

    def _onHeaderMarginChanged(self, value, valueText):
        valueText.setText(str(value // 10))
        self._treeView.setHeaderMargin(value // 10)

    def _onIndentationChanged(self, value, valueText):
        valueText.setText(str(value // 10))
        self._treeView.setIndentation(value // 10)
