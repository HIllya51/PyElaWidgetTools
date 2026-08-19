from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5ElaWidgetTools import *


class T_IconDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._themeMode = eTheme.getThemeMode()
        eTheme.themeModeChanged.connect(self.__themeModeChanged)

    def __themeModeChanged(self, themeMode):
        self._themeMode = themeMode

    def paint(self, painter, option, index):
        viewOption = QStyleOptionViewItem(option)
        self.initStyleOption(viewOption, index)

        if option.state & QStyle.StateFlag.State_HasFocus:
            viewOption.state &= ~QStyle.StateFlag.State_HasFocus
        super().paint(painter, viewOption, index)

        iconList = index.data(Qt.ItemDataRole.UserRole)
        if iconList is None or len(iconList) != 2:
            return
        iconName = iconList[0]
        iconValue = iconList[1]

        painter.save()
        painter.setRenderHints(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.SmoothPixmapTransform)

        painter.save()
        iconFont = QFont("ElaAwesome")
        iconFont.setPixelSize(22)
        painter.setFont(iconFont)
        painter.setPen(ElaThemeColor(self._themeMode, ElaThemeType.ThemeColor.BasicText))
        painter.drawText(
            option.rect.x() + option.rect.width() // 2 - 11,
            option.rect.y() + option.rect.height() // 2 - 11,
            iconValue,
        )
        painter.restore()

        # 文字绘制
        painter.setPen(ElaThemeColor(self._themeMode, ElaThemeType.ThemeColor.BasicText))
        titlefont = painter.font()
        titlefont.setPixelSize(13)
        painter.setFont(titlefont)
        rowTextWidth = option.rect.width() * 0.8
        subTitleRow = int(painter.fontMetrics().horizontalAdvance(iconName) / rowTextWidth)
        if subTitleRow > 0:
            subTitleText = iconName
            for i in range(subTitleRow + 1):
                text = painter.fontMetrics().elidedText(
                    subTitleText, Qt.TextElideMode.ElideRight, int(rowTextWidth)
                )
                if "…" in text[-3:]:
                    text = text.replace("…", subTitleText[len(text) - 1:len(text)])
                subTitleText = subTitleText[len(text):]
                painter.drawText(
                    option.rect.x() + option.rect.width() // 2 - painter.fontMetrics().horizontalAdvance(text) // 2,
                    option.rect.y() + option.rect.height() - 10 * (subTitleRow + 1 - i),
                    text,
                )
        else:
            painter.drawText(
                option.rect.x() + option.rect.width() // 2 - painter.fontMetrics().horizontalAdvance(iconName) // 2,
                option.rect.y() + option.rect.height() - 20,
                iconName,
            )
        painter.restore()

    def sizeHint(self, option, index):
        return QSize(100, 100)
