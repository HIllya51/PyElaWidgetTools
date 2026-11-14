from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5ElaWidgetTools import *
from ExamplePage.T_BasePage import *
from ModelView.T_TreeViewModel import *


class T_TreeView(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("树形视图")
        self.createCustomWidget("浏览多层项目资源，调节行高、缩进和表头间距，观察层级结构的变化。", "树形视图")
        mainLayout = self.createPageLayout()
        section = self.addExampleSection(
            mainLayout, "项目资源 · ElaTreeView", "点击箭头展开节点，支持多级资源与滚动浏览。"
        )
        resourceModel = T_TreeViewModel(self)
        self._treeView = ElaTreeView(self)
        self._treeView.setModel(resourceModel)
        self._treeView.setFixedHeight(380)
        self._treeView.setUniformRowHeights(True)
        self._treeView.header().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self._treeView.expandToDepth(0)

        expandButton = ElaPushButton("展开全部", self)
        collapseButton = ElaPushButton("收起全部", self)
        expandButton.clicked.connect(self._treeView.expandAll)
        collapseButton.clicked.connect(self._treeView.collapseAll)
        actionLayout = ElaFlowLayout(0, 12, 12)
        actionLayout.addWidget(expandButton)
        actionLayout.addWidget(collapseButton)

        optionsLayout = ElaFlowLayout(0, 24, 16)
        heightSpinBox = ElaSpinBox(self)
        heightSpinBox.setRange(24, 60)
        heightSpinBox.setValue(35)
        heightSpinBox.setFixedWidth(120)
        marginSpinBox = ElaSpinBox(self)
        marginSpinBox.setRange(0, 20)
        marginSpinBox.setValue(5)
        marginSpinBox.setFixedWidth(120)
        indentSpinBox = ElaSpinBox(self)
        indentSpinBox.setRange(12, 64)
        indentSpinBox.setValue(20)
        indentSpinBox.setFixedWidth(120)
        heightSpinBox.valueChanged.connect(self._treeView.setItemHeight)
        marginSpinBox.valueChanged.connect(self._treeView.setHeaderMargin)
        indentSpinBox.valueChanged.connect(self._treeView.setIndentation)
        optionsLayout.addWidget(self.createLabeledControl("行高（像素）", heightSpinBox))
        optionsLayout.addWidget(self.createLabeledControl("表头间距（像素）", marginSpinBox))
        optionsLayout.addWidget(self.createLabeledControl("层级缩进（像素）", indentSpinBox))

        section.addLayout(actionLayout)
        section.addWidget(self._treeView)
        section.addLayout(optionsLayout)
        section.addWidget(
            ElaText("四级资源结构 · 共 {} 个节点".format(resourceModel.getItemCount()), self)
        )
