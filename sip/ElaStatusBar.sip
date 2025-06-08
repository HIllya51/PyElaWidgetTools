%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaStatusBar : public QStatusBar
{
%TypeHeaderCode
#include "Def.h"
#include "ElaStatusBar.h"
%End

public:
  explicit ElaStatusBar(QWidget * parent = nullptr);
  ~ElaStatusBar();

};