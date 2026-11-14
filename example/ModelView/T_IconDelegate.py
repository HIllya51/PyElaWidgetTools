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
        painter.setRenderHints(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.TextAntialiasing)
        iconFont = QFont("ElaAwesome")
        iconFont.setPixelSize(28)
        painter.setFont(iconFont)
        painter.setPen(ElaThemeColor(self._themeMode, ElaThemeType.ThemeColor.BasicText))
        painter.drawText(
            QRect(option.rect.x(), option.rect.y() + 12, option.rect.width(), 36),
            Qt.AlignmentFlag.AlignCenter,
            iconValue,
        )
        labelFont = option.font
        labelFont.setPixelSize(12)
        painter.setFont(labelFont)
        labelRect = QRect(
            option.rect.x() + 6, option.rect.y() + 58, option.rect.width() - 12, 20
        )
        painter.drawText(
            labelRect,
            Qt.AlignmentFlag.AlignCenter,
            painter.fontMetrics().elidedText(
                iconName, Qt.TextElideMode.ElideRight, labelRect.width()
            ),
        )
        painter.restore()

    def sizeHint(self, option, index):
        return QSize(104, 88)
