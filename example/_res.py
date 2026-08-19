from PyQt5.QtGui import *
from PyQt5.QtCore import *


def placeholderImage(w: int = 1, h: int = 1, color: QColor = QColor(120, 120, 130)) -> QImage:
    """纯色占位图，替代 C++ 示例里 :/Resource/... 的图片资源。"""
    img = QImage(w, h, QImage.Format.Format_RGB32)
    img.fill(color)
    return img


def placeholderPixmap(w: int = 1, h: int = 1, color: QColor = QColor(120, 120, 130)) -> QPixmap:
    """纯色占位 pixmap。"""
    pm = QPixmap(w, h)
    if not pm.isNull():
        pm.fill(color)
    return pm
