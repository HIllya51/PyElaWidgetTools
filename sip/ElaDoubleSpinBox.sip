%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaDoubleSpinBox : public QDoubleSpinBox
{
%TypeHeaderCode
#include "Def.h"
#include "ElaDoubleSpinBox.h"
%End

public:
  explicit ElaDoubleSpinBox(QWidget * parent = nullptr);
  ~ElaDoubleSpinBox();

protected:
  void contextMenuEvent(QContextMenuEvent * event) ;

};