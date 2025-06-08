%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaTheme : public QObject
{
%TypeHeaderCode
#include "Def.h"
#include "ElaTheme.h"
%End

public: static ElaTheme* getInstance();
private:
  explicit ElaTheme(QObject * parent = nullptr);
  ~ElaTheme();

public:
  void setThemeMode(ElaThemeType::ThemeMode themeMode) ;
  ElaThemeType::ThemeMode getThemeMode() const ;
  void drawEffectShadow(QPainter * painter, QRect widgetRect, int shadowBorderWidth, int borderRadius) ;
  void setThemeColor(ElaThemeType::ThemeMode themeMode, ElaThemeType::ThemeColor themeColor, QColor newColor) ;
  const QColor& getThemeColor(ElaThemeType::ThemeMode themeMode, ElaThemeType::ThemeColor themeColor) ;

Q_SIGNALS:
Q_SIGNAL  void themeModeChanged(ElaThemeType::ThemeMode themeMode);

};