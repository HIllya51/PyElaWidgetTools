%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaComboBox : public QComboBox
{
%TypeHeaderCode
#include "Def.h"
#include "ElaComboBox.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public:
  explicit ElaComboBox(QWidget * parent = nullptr);
  ~ElaComboBox();
  void setEditable(bool editable) ;

protected:
  virtual void showPopup() ;
  virtual void hidePopup() ;

};