from PyQt5.QtCore import *


class T_ListViewModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._dataList = [
            "项目概览",
            "界面设计规范",
            "颜色与主题",
            "图标资源",
            "按钮与操作",
            "文本输入",
            "下拉与多选",
            "菜单与弹出层",
            "导航与标签",
            "列表与表格",
            "项目资源树",
            "卡片与布局",
            "键盘与焦点",
            "屏幕采集",
            "窗口与布局",
            "发布检查清单",
        ]

    def rowCount(self, parent=QModelIndex()):
        return len(self._dataList)

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._dataList[index.row()]
        return None
