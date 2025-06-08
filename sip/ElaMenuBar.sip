%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaMenuBar : public QMenuBar
{
%TypeHeaderCode
#include "Def.h"
#include "ElaMenuBar.h"
%End

public:
  explicit ElaMenuBar(QWidget * parent = nullptr);
  ~ElaMenuBar();
  QAction* addMenu(QMenu * menu) ;
  ElaMenu* addMenu(const QString & title) ;
  ElaMenu* addMenu(const QIcon & icon, const QString & title) ;
  ElaMenu* addMenu(ElaIconType::IconName arg1, const QString & title) ;
  QAction* addElaIconAction(ElaIconType::IconName icon, const QString & text) ;

};