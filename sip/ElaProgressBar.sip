%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaProgressBar : public QProgressBar
{
%TypeHeaderCode
#include "Def.h"
#include "ElaProgressBar.h"
%End

public:
  explicit ElaProgressBar(QWidget * parent = nullptr);
  ~ElaProgressBar();
  void setMinimum(int minimum) ;
  void setMaximum(int maximum) ;

protected:
  virtual void paintEvent(QPaintEvent * event) ;
  virtual void resizeEvent(QResizeEvent * event) ;

};