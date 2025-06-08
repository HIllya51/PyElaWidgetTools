%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaWidget : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaWidget.h"
%End

public: Q_SIGNAL void pIsStayTopChanged();
  void setIsStayTop(bool IsStayTop);
  bool getIsStayTop() const;
public: Q_SIGNAL void pIsFixedSizeChanged();
  void setIsFixedSize(bool IsFixedSize);
  bool getIsFixedSize() const;
public: Q_SIGNAL void pIsDefaultClosedChanged();
  void setIsDefaultClosed(bool IsDefaultClosed);
  bool getIsDefaultClosed() const;
public: Q_SIGNAL void pAppBarHeightChanged();
  void setAppBarHeight(int AppBarHeight);
  int getAppBarHeight() const;
public:
  explicit ElaWidget(QWidget * parent = nullptr);
  ~ElaWidget();
  void moveToCenter() ;
  void setWindowButtonFlag(ElaAppBarType::ButtonType buttonFlag, bool isEnable = true) ;
  void setWindowButtonFlags(ElaAppBarType::ButtonFlags buttonFlags) ;
  ElaAppBarType::ButtonFlags getWindowButtonFlags() const ;

Q_SIGNALS:
Q_SIGNAL  void routeBackButtonClicked();
Q_SIGNAL  void navigationButtonClicked();
Q_SIGNAL  void themeChangeButtonClicked();
Q_SIGNAL  void closeButtonClicked();

};