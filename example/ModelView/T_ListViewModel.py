from PyQt5.QtCore import *


class T_ListViewModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._dataList = []
        self._dataList.append("最轻一个灵魂 送出玫瑰星光")
        self._dataList.append("最轻一句提问 答案是生命的存亡")
        self._dataList.append("最轻一颗麦种 由云帆托起")
        self._dataList.append("流浪至黑暗的心脏")
        self._dataList.append("轻轻的一支航船")
        self._dataList.append("归来却被囚困旧港湾")
        self._dataList.append("轻轻的一些落叶")
        self._dataList.append("飘零在梦萦故乡彼岸")
        self._dataList.append("轻轻的虫 森林鸣唱")
        self._dataList.append("轻轻的鱼 渡向汪洋")
        self._dataList.append("我们是 轻轻轻轻摇曳的篝火")
        self._dataList.append("轻轻对天空哼一支歌")
        self._dataList.append("轻轻被谁听见了")
        self._dataList.append("轻轻的被随意熄灭了")
        self._dataList.append("可我要 重重将夜灼伤")
        self._dataList.append("可我要 重重将夜点燃")
        self._dataList.append("更明亮的 也曾尘埃一样")
        self._dataList.append("最轻一段目光 注视年岁漫长")
        self._dataList.append("最轻一根琴弦 沉默着致命的声浪")
        self._dataList.append("最轻一线悬丝 紧握住锋芒")
        self._dataList.append("牵系着存亡的衡量")
        self._dataList.append("轻轻的一枚棋子 阻挡在骑士前进路上")
        self._dataList.append("轻轻的一双手掌 爱抚的婴孩不再成长")
        self._dataList.append("轻轻的虫 童话里唱")
        self._dataList.append("轻轻的鱼 向宇宙望")
        self._dataList.append("我们是 轻轻轻轻摇曳的篝火")
        self._dataList.append("轻轻对天空哼一支歌")
        self._dataList.append("轻轻被谁听见了")
        self._dataList.append("轻轻的被随意熄灭了")
        self._dataList.append("可我要 重重将夜灼伤")
        self._dataList.append("可我要 重重将夜点燃")
        self._dataList.append("更明亮的 也曾尘埃一样")
        self._dataList.append("轻轻时间 重重浩荡纪年")
        self._dataList.append("轻轻的文明 重重书写")
        self._dataList.append("轻轻身躯 重重对峙黑夜")
        self._dataList.append("轻轻的人类 重重思想")
        self._dataList.append("向宇宙望 向宇宙望")
        self._dataList.append("向远航")
        self._dataList.append("最重一粒微光")

    def rowCount(self, *_):
        return len(self._dataList)

    def data(self, index: QModelIndex, role: int):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._dataList[index.row()]
