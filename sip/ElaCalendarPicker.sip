%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaCalendarPicker : public QPushButton
{
%TypeHeaderCode
#include "Def.h"
#include "ElaCalendarPicker.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public:
  explicit ElaCalendarPicker(QWidget * parent = nullptr);
  ~ElaCalendarPicker();

Q_SIGNALS:
Q_SIGNAL  void selectedDateChanged(QDate date);

};