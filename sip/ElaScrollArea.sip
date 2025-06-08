%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaScrollArea : public QScrollArea
{
%TypeHeaderCode
#include "Def.h"
#include "ElaScrollArea.h"
%End

public:
  explicit ElaScrollArea(QWidget * parent = nullptr);
  ~ElaScrollArea();
  void setIsGrabGesture(bool isEnable, qreal mousePressEventDelay = 0.5) ;
  void setIsOverShoot(Qt::Orientation orientation, bool isEnable) ;
  bool getIsOverShoot(Qt::Orientation orientation) const ;
  void setIsAnimation(Qt::Orientation orientation, bool isAnimation) ;
  bool getIsAnimation(Qt::Orientation orientation) const ;

};