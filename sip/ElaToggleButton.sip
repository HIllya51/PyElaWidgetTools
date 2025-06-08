%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaToggleButton : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaToggleButton.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pTextChanged();
  void setText(QString Text);
  QString getText() const;
public:
  explicit ElaToggleButton(QWidget * parent = nullptr);
  explicit ElaToggleButton(QString text, QWidget * parent = nullptr);
  ~ElaToggleButton();
  void setIsToggled(bool isToggled) ;
  bool getIsToggled() const ;

Q_SIGNALS:
Q_SIGNAL  void toggled(bool checked);

};