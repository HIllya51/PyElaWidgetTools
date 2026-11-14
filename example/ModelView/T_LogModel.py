from PyQt5.QtCore import *


class T_LogModel(QAbstractListModel):
    # 界面仅保留最近一万条，完整日志由 ElaLog 写入文件
    MaximumLogCount = 10000

    def __init__(self, parent=None):
        super().__init__(parent)
        self._logList = []

    def rowCount(self, parent=QModelIndex()):
        return 0 if parent.isValid() else len(self._logList)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if (
            index.isValid()
            and 0 <= index.row() < len(self._logList)
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return self._logList[index.row()]
        return None

    def setLogList(self, list):
        self.beginResetModel()
        self._logList = list[max(0, len(list) - T_LogModel.MaximumLogCount):]
        self.endResetModel()

    def appendLogList(self, log):
        self.appendLogs([log])

    def appendLogs(self, logs):
        if not logs:
            return
        incoming = logs[max(0, len(logs) - T_LogModel.MaximumLogCount):]
        removeCount = max(0, len(self._logList) + len(incoming) - T_LogModel.MaximumLogCount)
        if removeCount > 0:
            self.beginRemoveRows(QModelIndex(), 0, removeCount - 1)
            self._logList = self._logList[removeCount:]
            self.endRemoveRows()
        firstRow = len(self._logList)
        self.beginInsertRows(QModelIndex(), firstRow, firstRow + len(incoming) - 1)
        self._logList.extend(incoming)
        self.endInsertRows()

    def getLogList(self):
        return self._logList
