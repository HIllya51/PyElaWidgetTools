from PyQt5.QtCore import *


class T_TreeItem(object):
    def __init__(self, itemTitle, parent=None):
        self._itemKey = (
            QUuid.createUuid().toString().replace("{", "").replace("}", "").replace("-", "")
        )
        self._itemTitle = itemTitle
        self._pParentItem = parent
        self._pIsChecked = False
        self._pChildrenItems = []

    def getItemKey(self):
        return self._itemKey

    def getItemTitle(self):
        return self._itemTitle

    def setChildChecked(self, isChecked):
        if isChecked:
            for node in self._pChildrenItems:
                node.setIsChecked(isChecked)
                node.setChildChecked(isChecked)
        else:
            for node in self._pChildrenItems:
                node.setChildChecked(isChecked)
                node.setIsChecked(isChecked)

    def getChildCheckState(self):
        isAllChecked = True
        isAnyChecked = False
        for node in self._pChildrenItems:
            if node.getIsChecked():
                isAnyChecked = True
            else:
                isAllChecked = False
            childState = node.getChildCheckState()
            if childState == Qt.CheckState.PartiallyChecked:
                isAllChecked = False
                isAnyChecked = True
                break
            elif childState == Qt.CheckState.Unchecked:
                isAllChecked = False
        if len(self._pChildrenItems) > 0:
            if isAllChecked:
                return Qt.CheckState.Checked
            if isAnyChecked:
                return Qt.CheckState.PartiallyChecked
            return Qt.CheckState.Unchecked
        return Qt.CheckState.Checked

    def appendChildItem(self, childItem):
        self._pChildrenItems.append(childItem)

    def getIsHasChild(self):
        return len(self._pChildrenItems) > 0

    def getRow(self):
        if self._pParentItem is not None:
            return self._pParentItem.getChildrenItems().index(self)
        return 0

    def getChildrenItems(self):
        return self._pChildrenItems

    def setChildrenItems(self, childrenItems):
        self._pChildrenItems = childrenItems

    def getIsChecked(self):
        return self._pIsChecked

    def setIsChecked(self, isChecked):
        self._pIsChecked = isChecked

    def getParentItem(self):
        return self._pParentItem

    def setParentItem(self, parentItem):
        self._pParentItem = parentItem
