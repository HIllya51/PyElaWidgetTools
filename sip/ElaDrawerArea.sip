%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaDrawerArea : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaDrawerArea.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pHeaderHeightChanged();
  void setHeaderHeight(int HeaderHeight);
  int getHeaderHeight() const;
public:
  explicit ElaDrawerArea(QWidget * parent = nullptr);
  ~ElaDrawerArea();
  void setDrawerHeader(QWidget * widget) ;
  void addDrawer(QWidget * widget) ;
  void removeDrawer(QWidget * widget) ;
  void expand() ;
  void collpase() ;
  bool getIsExpand() const ;

Q_SIGNALS:
Q_SIGNAL  void expandStateChanged(bool isExpand);

};