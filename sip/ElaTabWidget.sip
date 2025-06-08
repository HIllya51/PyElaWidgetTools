%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaTabWidget : public QTabWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaTabWidget.h"
%End

public:
  explicit ElaTabWidget(QWidget * parent = nullptr);
  ~ElaTabWidget();
  void setTabPosition(TabPosition position) ;

protected:
  virtual void paintEvent(QPaintEvent * event) ;
  virtual void dragEnterEvent(QDragEnterEvent * event) ;
  virtual void dropEvent(QDropEvent * event) ;

};