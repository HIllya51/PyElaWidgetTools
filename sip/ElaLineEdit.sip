%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaLineEdit : public QLineEdit
{
%TypeHeaderCode
#include "Def.h"
#include "ElaLineEdit.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pIsClearButtonEnableChanged();
  void setIsClearButtonEnable(bool IsClearButtonEnable);
  bool getIsClearButtonEnable() const;
public:
  explicit ElaLineEdit(QWidget * parent = nullptr);
  ~ElaLineEdit();

Q_SIGNALS:
Q_SIGNAL  void focusIn(QString text);
Q_SIGNAL  void focusOut(QString text);
Q_SIGNAL  void wmFocusOut(QString text);

};