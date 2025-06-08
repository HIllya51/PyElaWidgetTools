%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaCheckBox : public QCheckBox
{
%TypeHeaderCode
#include "Def.h"
#include "ElaCheckBox.h"
%End

public:
  explicit ElaCheckBox(QWidget * parent = nullptr);
  explicit ElaCheckBox(const QString & text, QWidget * parent = nullptr);
  ~ElaCheckBox();

};