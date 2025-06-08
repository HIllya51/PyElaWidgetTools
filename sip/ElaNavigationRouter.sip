%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaNavigationRouter : public QObject
{
%TypeHeaderCode
#include "Def.h"
#include "ElaNavigationRouter.h"
%End

public: Q_SIGNAL void pMaxRouteCountChanged();
  void setMaxRouteCount(int MaxRouteCount);
  int getMaxRouteCount() const;
public: static ElaNavigationRouter* getInstance();
private:
  explicit ElaNavigationRouter(QObject * parent = nullptr);
  ~ElaNavigationRouter();

Q_SIGNALS:
Q_SIGNAL  void navigationRouterStateChanged(bool state);

};