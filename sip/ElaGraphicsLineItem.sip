%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaGraphicsLineItem : public QGraphicsPathItem
{
%TypeHeaderCode
#include "Def.h"
#include "ElaGraphicsLineItem.h"
%End

public:
  explicit ElaGraphicsLineItem(ElaGraphicsItem * startItem, ElaGraphicsItem * endItem, int startItemPort, int endItemPort, QGraphicsItem * parent = nullptr);
  explicit ElaGraphicsLineItem(QPointF startPoint, QPointF endPoint, QGraphicsItem * parent = nullptr);
  ~ElaGraphicsLineItem();
  bool isTargetLink(ElaGraphicsItem * item) const ;
  bool isTargetLink(ElaGraphicsItem * item1, ElaGraphicsItem * item2) const ;
  bool isTargetLink(ElaGraphicsItem * item1, ElaGraphicsItem * item2, int port1, int port2) const ;

protected:
  void paint(QPainter * painter, const QStyleOptionGraphicsItem * option, QWidget * widget = nullptr) ;
  QRectF boundingRect() const ;

};