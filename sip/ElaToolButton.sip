%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaToolButton : public QToolButton
{
%TypeHeaderCode
#include "Def.h"
#include "ElaToolButton.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pIsSelectedChanged();
  void setIsSelected(bool IsSelected);
  bool getIsSelected() const;
public:
  explicit ElaToolButton(QWidget * parent = nullptr);
  ~ElaToolButton();
  void setIsTransparent(bool isTransparent) ;
  bool getIsTransparent() const ;
  void setMenu(ElaMenu * menu) ;
  void setElaIcon(ElaIconType::IconName icon) ;

protected:
  virtual bool eventFilter(QObject * watched, QEvent * event) ;

};