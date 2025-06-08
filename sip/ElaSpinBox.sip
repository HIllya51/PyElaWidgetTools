%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaSpinBox : public QSpinBox
{
%TypeHeaderCode
#include "Def.h"
#include "ElaSpinBox.h"
%End

public:
  explicit ElaSpinBox(QWidget * parent = nullptr);
  ~ElaSpinBox();

protected:
  void contextMenuEvent(QContextMenuEvent * event) ;

};