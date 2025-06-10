from PyQt5.QtCore import *
from PyQt5.QtGui import *


class T_TableViewModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._header = ["预览", "歌名", "歌手", "专辑", "时长"]
        self._dataList = []
        data0 = [
            "夜航星(Night Voyager)",
            "不才/三体宇宙",
            "我的三体之章北海传",
            "05:03",
        ]
        data1 = ["玫瑰少年", "五月天", "玫瑰少年", "03:55"]
        data2 = [
            "Collapsing World(Original Mix)",
            "Lightscape",
            "Collapsing World",
            "03:10",
        ]
        data3 = ["RAIN MAN (雨人)", "AKIHIDE (佐藤彰秀)", "RAIN STORY", "05:37"]
        data4 = ["黑暗森林", "雲翼星辰", "黑暗森林", "05:47"]
        data5 = ["轻(我的三体第四季主题曲)", "刘雪茗", "我的三体第四季", "01:59"]
        data6 = ["STYX HELIX", "MYTH & ROID", "STYX HELIX", "04:51"]
        data7 = ["LAST STARDUST", "Aimer", "DAWN", "05:18"]
        data8 = [
            "Running In The Dark",
            "MONKEY MAJIK/塞壬唱片",
            "Running In The Dark",
            "03:40",
        ]
        self._dataList.append(data0)
        self._dataList.append(data1)
        self._dataList.append(data2)
        self._dataList.append(data3)
        self._dataList.append(data4)
        self._dataList.append(data5)
        self._dataList.append(data6)
        self._dataList.append(data7)
        self._dataList.append(data8)
        self._iconList = []
        self._iconList.append(
            QIcon(
                QPixmap(
                    r"C:\Users\11737\Pictures\luna\3d144c38-7128-4154-9440-c2a6d80c1ae1.jpg"
                ).scaled(
                    38,
                    38,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        )
        self._iconList.append(
            QIcon(
                QPixmap(
                    r"C:\Users\11737\Pictures\luna\3d144c38-7128-4154-9440-c2a6d80c1ae1.jpg"
                ).scaled(
                    38,
                    38,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        )
        self._iconList.append(
            QIcon(
                QPixmap(
                    r"C:\Users\11737\Pictures\luna\3d144c38-7128-4154-9440-c2a6d80c1ae1.jpg"
                ).scaled(
                    38,
                    38,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        )
        self._iconList.append(
            QIcon(
                QPixmap(
                    r"C:\Users\11737\Pictures\luna\3d144c38-7128-4154-9440-c2a6d80c1ae1.jpg"
                ).scaled(
                    38,
                    38,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        )
        self._iconList.append(
            QIcon(
                QPixmap(
                    r"C:\Users\11737\Pictures\luna\3d144c38-7128-4154-9440-c2a6d80c1ae1.jpg"
                ).scaled(
                    38,
                    38,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        )
        self._iconList.append(
            QIcon(
                QPixmap(
                    r"C:\Users\11737\Pictures\luna\3d144c38-7128-4154-9440-c2a6d80c1ae1.jpg"
                ).scaled(
                    38,
                    38,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        )
        self._iconList.append(
            QIcon(
                QPixmap(
                    r"C:\Users\11737\Pictures\luna\3d144c38-7128-4154-9440-c2a6d80c1ae1.jpg"
                ).scaled(
                    38,
                    38,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        )
        self._iconList.append(
            QIcon(
                QPixmap(
                    r"C:\Users\11737\Pictures\luna\3d144c38-7128-4154-9440-c2a6d80c1ae1.jpg"
                ).scaled(
                    38,
                    38,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        )
        self._iconList.append(
            QIcon(
                QPixmap(
                    r"C:\Users\11737\Pictures\luna\3d144c38-7128-4154-9440-c2a6d80c1ae1.jpg"
                ).scaled(
                    38,
                    38,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        )

    def rowCount(self, *_):
        return 100

    def columnCount(self, *_):
        return len(self._header)

    def data(self, index: QModelIndex, role: int):
        if role == Qt.ItemDataRole.DisplayRole and index.column() != 0:
            return self._dataList[index.row() % 9][index.column() - 1]
        elif role == Qt.ItemDataRole.DecorationRole and index.column() == 0:
            return self._iconList[index.row() % 9]
        elif role == 27:  # Qt.ItemDataRole.DecorationPropertyRole:
            return Qt.AlignmentFlag.AlignCenter
        elif role == Qt.ItemDataRole.TextAlignmentRole and index.column() == 4:
            return Qt.AlignmentFlag.AlignCenter

    def headerData(self, section, orientation, role):
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return self._header[section]
