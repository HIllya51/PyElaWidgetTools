%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaScrollPageArea : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaScrollPageArea.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public:
  explicit ElaScrollPageArea(QWidget * parent = nullptr);
  ~ElaScrollPageArea();

protected:
  virtual void paintEvent(QPaintEvent * event) ;

};