from PyQt5.QtCore import *
from PyQt5.QtGui import *
from _res import *
from ModelView.T_TreeItem import *


class T_TreeViewModel(QAbstractItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._itemsMap = {}
        self._rootItem = T_TreeItem("root")
        for i in range(20):
            level1Item = T_TreeItem("Lv1--TreeItem{}".format(i + 1), self._rootItem)
            for j in range(6):
                level2Item = T_TreeItem(
                    "Lv2--TreeItem{}".format(j + 1), level1Item
                )
                for k in range(6):
                    level3Item = T_TreeItem(
                        "Lv3--TreeItem{}".format(k + 1), level2Item
                    )
                    for l in range(6):
                        level4Item = T_TreeItem(
                            "Lv4--TreeItem{}".format(l + 1), level3Item
                        )
                        level3Item.appendChildItem(level4Item)
                        self._itemsMap[level4Item.getItemKey()] = level4Item
                    level2Item.appendChildItem(level3Item)
                    self._itemsMap[level3Item.getItemKey()] = level3Item
                level1Item.appendChildItem(level2Item)
                self._itemsMap[level2Item.getItemKey()] = level2Item
            self._rootItem.appendChildItem(level1Item)
            self._itemsMap[level1Item.getItemKey()] = level1Item

    def parent(self, child):
        if not child.isValid():
            return QModelIndex()
        childItem = child.internalPointer()
        parentItem = childItem.getParentItem()
        if parentItem == self._rootItem:
            return QModelIndex()
        elif parentItem is None:
            return QModelIndex()
        return self.createIndex(parentItem.getRow(), 0, parentItem)

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        if not parent.isValid():
            parentItem = self._rootItem
        else:
            parentItem = parent.internalPointer()
        childItem = None
        if len(parentItem.getChildrenItems()) > row:
            childItem = parentItem.getChildrenItems()[row]
        if childItem is not None:
            return self.createIndex(row, column, childItem)
        return QModelIndex()

    def rowCount(self, parent=QModelIndex()):
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parentItem = self._rootItem
        else:
            parentItem = parent.internalPointer()
        return len(parentItem.getChildrenItems())

    def columnCount(self, parent=QModelIndex()):
        return 1

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return index.internalPointer().getItemTitle()
        elif role == Qt.ItemDataRole.DecorationRole:
            return QIcon(placeholderPixmap(38, 38))
        elif role == Qt.ItemDataRole.CheckStateRole:
            item = index.internalPointer()
            if item.getIsHasChild():
                return item.getChildCheckState()
            else:
                return (
                    Qt.CheckState.Checked if item.getIsChecked() else Qt.CheckState.Unchecked
                )
        return None

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.CheckStateRole:
            item = index.internalPointer()
            item.setIsChecked(not item.getIsChecked())
            item.setChildChecked(item.getIsChecked())
            self.dataChanged.emit(QModelIndex(), QModelIndex(), [role])
            return True
        return super().setData(index, value, role)

    def flags(self, index):
        flags = super().flags(index)
        flags |= Qt.ItemFlag.ItemIsUserCheckable
        return flags

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return "ElaTreeView-Example-4Level"
        return super().headerData(section, orientation, role)

    def getItemCount(self):
        return len(self._itemsMap)
