from PyQt5.QtCore import *


class T_LogModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._logList = []

    def rowCount(self, parent=QModelIndex()):
        return len(self._logList)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._logList[index.row()]
        return None

    def setLogList(self, list):
        self.beginResetModel()
        self._logList = list
        self.endResetModel()

    def appendLogList(self, log):
        self.beginResetModel()
        self._logList.append(log)
        self.endResetModel()

    def getLogList(self):
        return self._logList
