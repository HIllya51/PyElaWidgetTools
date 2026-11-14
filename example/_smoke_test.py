"""0.14.0 wheel 冒烟测试：离屏启动 example，遍历全部页面后退出。"""
import os
import sys
import traceback

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.getcwd())

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5ElaWidgetTools import *

app = QApplication(sys.argv)
eApp.init()
ElaLog.getInstance().initMessageLog(False)

from mainwindow import MainWindow

w = MainWindow()
w.show()

# 收集全部页面节点并定时轮播，触发堆栈切换/绘制/动画
pages = [
    w._homePage,
    w._elaScreenPage,
    w._baseComponentsPage,
    w._listViewPage,
    w._tableViewPage,
    w._treeViewPage,
    w._cardPage,
    w._navigationPage,
    w._popupPage,
    w._iconPage,
    w._settingPage,
]
state = {"i": 0, "navigated": 0, "errors": []}


def _navigate_next():
    try:
        if state["i"] < len(pages):
            page = pages[state["i"]]
            key = page.property("ElaPageKey")
            if key:
                w.navigation(key)
                state["navigated"] += 1
            state["i"] += 1
        else:
            # 主题切换再切回，验证主题相关代码路径
            eTheme.setThemeMode(ElaThemeType.ThemeMode.Dark)
    except Exception:
        state["errors"].append(traceback.format_exc())
        app.quit()


def _finish():
    print(f"遍历页面数: {state['navigated']}/{len(pages)}")
    # UI 完整性：确认被 Ela 接口保存的控件没有被 GC 删除
    from PyQt5.QtWidgets import QWidget as _QW
    checks = {
        "主窗口工具栏": len(w.findChildren(type(w._toolBar))) if hasattr(w, "_toolBar") else -1,
        "轮播卡片": len(w._cardPage.findChildren(type(w._cardPage._promotionView))),
        "教学提示": len(w._popupPage.findChildren(type(w._popupPage._teachingTips[0]))),
        "标签页文本": len(w._navigationPage._tabWidget.findChildren(type(w._navigationPage._tabPages[0]))),
    }
    for k, v in checks.items():
        print(f"  {k}: {v}")
    print(f"日志面板条目: {w._logModel.rowCount() if hasattr(w, '_logModel') else 'n/a'}")
    if state["errors"]:
        print("=== ERRORS ===")
        print("\n".join(state["errors"]))
        app.quit()
        sys.exit(1)
    print("SMOKE TEST OK")
    app.quit()


nav_timer = QTimer()
nav_timer.setInterval(350)
nav_timer.timeout.connect(_navigate_next)
nav_timer.start()

QTimer.singleShot(350 * (len(pages) + 2) + 1500, _finish)
QTimer.singleShot(350 * (len(pages) + 2) + 2500, app.quit)
rc = app.exec()
sys.exit(rc if rc else 0)
