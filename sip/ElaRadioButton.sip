%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaRadioButton : public QRadioButton
{
%TypeHeaderCode
#include "Def.h"
#include "ElaRadioButton.h"
%End

public:
  explicit ElaRadioButton(QWidget * parent = nullptr);
  explicit ElaRadioButton(const QString & text, QWidget * parent = nullptr);
  ~ElaRadioButton();

};