from .ElaWidgetTools import *


def __wrapsingleton(T):

    class __:
        def __getattr__(self, name):
            return getattr(T.getInstance(), name)

    return __()


eTheme: ElaTheme = __wrapsingleton(ElaTheme)
eApp: ElaApplication = __wrapsingleton(ElaApplication)


def ElaThemeColor(
    themeMode: ElaThemeType.ThemeMode, themeColor: ElaThemeType.ThemeColor
):
    return eTheme.getThemeColor(themeMode, themeColor)
