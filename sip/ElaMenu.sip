%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaMenu : public QMenu
{
%TypeHeaderCode
#include "Def.h"
#include "ElaMenu.h"
%End

public:
  explicit ElaMenu(QWidget * parent = nullptr);
  explicit ElaMenu(const QString & title, QWidget * parent = nullptr);
  ~ElaMenu();
  void setMenuItemHeight(int menuItemHeight) ;
  int getMenuItemHeight() const ;
  QAction* addMenu(QMenu * menu) ;
  ElaMenu* addMenu(const QString & title) ;
  ElaMenu* addMenu(const QIcon & icon, const QString & title) ;
  ElaMenu* addMenu(ElaIconType::IconName icon, const QString & title) ;
  QAction* addElaIconAction(ElaIconType::IconName icon, const QString & text) ;
  QAction* addElaIconAction(ElaIconType::IconName icon, const QString & text, const QKeySequence & shortcut) ;
  bool isHasChildMenu() const ;
  bool isHasIcon() const ;

Q_SIGNALS:
Q_SIGNAL  void menuShow();

};