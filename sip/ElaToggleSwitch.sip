%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaToggleSwitch : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaToggleSwitch.h"
%End

public:
  explicit ElaToggleSwitch(QWidget * parent = nullptr);
  ~ElaToggleSwitch();
  void setIsToggled(bool isToggled) ;
  bool getIsToggled() const ;

Q_SIGNALS:
Q_SIGNAL  void toggled(bool checked);

};