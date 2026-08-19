from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5ElaWidgetTools import *


def _enumerateIconName():
    """枚举 ElaIconType.IconName，返回 [(name, member), ...]，跳过 None(value 0)。
    兼容经典 sip.enumtype（无 __members__/.value，PyQt5）与 IntEnum（PyQt6/PySide6）。"""
    enum = ElaIconType.IconName
    members = getattr(enum, "__members__", None)
    if members is not None:
        return [(k, v) for k, v in members.items() if not (k in ("None", "None_") or int(v) == 0)]
    # 经典 sip.enumtype：dir() + isinstance 过滤出枚举成员
    result = []
    for name in dir(enum):
        if name.startswith("_"):
            continue
        try:
            val = getattr(enum, name)
        except Exception:
            continue
        if isinstance(val, enum):
            result.append((name, val))
    return [(n, v) for n, v in result if not (n in ("None", "None_") or int(v) == 0)]


def _iconValue(member):
    """取枚举成员的整数值（int 值），兼容经典 sip.enumtype 与 IntEnum。"""
    try:
        return int(member.value)
    except Exception:
        return int(member)


class T_IconModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 等价于 C++ 的 QMetaEnum::fromType<ElaIconType::IconName>()
        self._icons = _enumerateIconName()  # [(name, member), ...]
        self._iconMap = {name: member for name, member in self._icons}
        self._searchKeyList = []
        self._rowCount = len(self._icons)
        self._pIsSearchMode = False

    def rowCount(self, parent=QModelIndex()):
        return self._rowCount

    def setSearchKeyList(self, list):
        self.beginResetModel()
        self._searchKeyList = list
        if self._pIsSearchMode:
            self._rowCount = len(self.getSearchKeyList())
        else:
            self._rowCount = len(self._icons)
        self.endResetModel()

    def getSearchKeyList(self):
        return self._searchKeyList

    def setIsSearchMode(self, isSearchMode):
        self._pIsSearchMode = isSearchMode

    def getIsSearchMode(self):
        return self._pIsSearchMode

    def getAllIconNames(self):
        return [name for name, _ in self._icons]

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.UserRole:
            if not self._pIsSearchMode:
                if index.row() >= len(self._icons):
                    return None
                name, member = self._icons[index.row()]
                return [name, chr(_iconValue(member))]
            else:
                if index.row() >= len(self._searchKeyList):
                    return None
                key = self._searchKeyList[index.row()]
                member = self._iconMap.get(key)
                if member is None:
                    return None
                return [key, chr(_iconValue(member))]
        return None

    def getIconNameFromModelIndex(self, index):
        iconName = ""
        if self._pIsSearchMode:
            if index.row() < len(self._searchKeyList):
                iconName = "ElaIconType::" + self._searchKeyList[index.row()]
        else:
            if index.row() < len(self._icons):
                iconName = "ElaIconType::" + self._icons[index.row()][0]
        return iconName
