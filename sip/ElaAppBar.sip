%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaAppBar : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaAppBar.h"
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
public: Q_SIGNAL void pIsOnlyAllowMinAndCloseChanged();
  void setIsOnlyAllowMinAndClose(bool IsOnlyAllowMinAndClose);
  bool getIsOnlyAllowMinAndClose() const;
public: Q_SIGNAL void pAppBarHeightChanged();
  void setAppBarHeight(int AppBarHeight);
  int getAppBarHeight() const;
public: Q_SIGNAL void pCustomWidgetMaximumWidthChanged();
  void setCustomWidgetMaximumWidth(int CustomWidgetMaximumWidth);
  int getCustomWidgetMaximumWidth() const;
public:
  explicit ElaAppBar(QWidget * parent = nullptr);
  ~ElaAppBar();
  void setCustomWidget(ElaAppBarType::CustomArea customArea, QWidget * customWidget) ;
  QWidget* getCustomWidget() const ;
  void setWindowButtonFlag(ElaAppBarType::ButtonType buttonFlag, bool isEnable = true) ;
  void setWindowButtonFlags(ElaAppBarType::ButtonFlags buttonFlags) ;
  ElaAppBarType::ButtonFlags getWindowButtonFlags() const ;
  void setRouteBackButtonEnable(bool isEnable) ;
  void closeWindow() ;
  int takeOverNativeEvent(const QByteArray & eventType, void * message, qintptr * result) ;

Q_SIGNALS:
Q_SIGNAL  void routeBackButtonClicked();
Q_SIGNAL  void navigationButtonClicked();
Q_SIGNAL  void themeChangeButtonClicked();
Q_SIGNAL  void closeButtonClicked();
Q_SIGNAL  void customWidgetChanged();

};