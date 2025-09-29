# PyElaWidgetTools

[ElaWidgetTools](https://github.com/Liniyous/ElaWidgetTools)的Python绑定。目前支持PyQt5、PyQt6、PySide6。

PyQt5: `pip install PyQt5-ElaWidgetTools`，PyQt5>=5.15.5

PyQt6: `pip install PyQt6-ElaWidgetTools`，PyQt6>=6.4.2

PySide6: `pip install PySide6-ElaWidgetTools`，PySide6==6.6.2 

请使用推荐的PyQt/PySide版本，否则可能不兼容。尤其是PySide，其绑定无法跨大版本兼容，而6.6.2是Ela推荐使用的版本，故使用此版本编译发布。若需要其他PyQt/PySide版本，请fork，然后修改.github/workflows/build_internal.yml中的`version`，github会自动帮你编译。

