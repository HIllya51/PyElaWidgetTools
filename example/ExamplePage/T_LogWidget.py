import threading

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *
from ModelView.T_LogModel import *


class T_LogWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(0, 5, 5, 0)
        logView = ElaListView(self)
        logView.setIsTransparent(True)
        logView.setUniformItemSizes(True)
        self._logModel = T_LogModel(self)
        logView.setModel(self._logModel)
        mainLayout.addWidget(logView)

        # 日志可能在其它线程产生：先缓存，由界面线程的定时器批量取出。
        # 缓冲不挂在 self 上，窗口销毁后回调仍可安全结束（对应 C++ 的 QSharedPointer）
        pendingLogs = {"lock": threading.Lock(), "logs": []}

        def _onLogMessage(log):
            with pendingLogs["lock"]:
                if len(pendingLogs["logs"]) == T_LogModel.MaximumLogCount:
                    pendingLogs["logs"].pop(0)
                pendingLogs["logs"].append(log)

        ElaLog.getInstance().logMessage.connect(_onLogMessage, Qt.ConnectionType.DirectConnection)

        refreshTimer = QTimer(self)
        refreshTimer.setInterval(33)

        def _onRefreshTimeout():
            with pendingLogs["lock"]:
                logs = pendingLogs["logs"]
                pendingLogs["logs"] = []
            self._logModel.appendLogs(logs)

        refreshTimer.timeout.connect(_onRefreshTimeout)
        refreshTimer.start()
        # 界面仅保留最近一万条，完整日志由 ElaLog 写入文件
        self._logModel.appendLogs(
            ["[信息] 日志服务已就绪", "[信息] 加载界面组件", "[信息] 初始化导航页面", "[信息] 等待用户操作"]
        )
