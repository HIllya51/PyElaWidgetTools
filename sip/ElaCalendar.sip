%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaCalendar : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaCalendar.h"
%End

public: Q_SIGNAL void pBorderRaiudsChanged();
  void setBorderRaiuds(int BorderRaiuds);
  int getBorderRaiuds() const;
public: Q_SIGNAL void pSelectedDateChanged();
  void setSelectedDate(QDate SelectedDate);
  QDate getSelectedDate() const;
public: Q_SIGNAL void pMinimumDateChanged();
  void setMinimumDate(QDate MinimumDate);
  QDate getMinimumDate() const;
public: Q_SIGNAL void pMaximumDateChanged();
  void setMaximumDate(QDate MaximumDate);
  QDate getMaximumDate() const;
public:
  explicit ElaCalendar(QWidget * parent = nullptr);
  ~ElaCalendar();

Q_SIGNALS:
Q_SIGNAL  void clicked(QDate date);

};