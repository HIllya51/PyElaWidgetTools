%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaScrollPage : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaScrollPage.h"
%End

public: Q_SIGNAL void pCustomWidgetChanged();
  void setCustomWidget(QWidget* CustomWidget);
  QWidget* getCustomWidget() const;
public:
  explicit ElaScrollPage(QWidget * parent = nullptr);
  ~ElaScrollPage();
  void addCentralWidget(QWidget * centralWidget, bool isWidgetResizeable = true, bool isVerticalGrabGesture = true, qreal mousePressEventDelay = 0.5) ;
  void navigation(int widgetIndex, bool isLogRoute = true) ;
  void setPageTitleSpacing(int spacing) ;
  int getPageTitleSpacing() const ;
  void setTitleVisible(bool isVisible) ;

};