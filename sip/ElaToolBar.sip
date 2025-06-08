%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaToolBar : public QToolBar
{
%TypeHeaderCode
#include "Def.h"
#include "ElaToolBar.h"
%End

public:
  explicit ElaToolBar(QWidget * parent = nullptr);
  explicit ElaToolBar(const QString & title, QWidget * parent = nullptr);
  ~ElaToolBar();
  void setToolBarSpacing(int spacing) ;
  int getToolBarSpacing() const ;
  QAction* addElaIconAction(ElaIconType::IconName icon, const QString & text) ;
  QAction* addElaIconAction(ElaIconType::IconName icon, const QString & text, const QKeySequence & shortcut) ;

protected:
  virtual void paintEvent(QPaintEvent * event) ;

};