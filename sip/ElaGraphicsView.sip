%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaGraphicsView : public QGraphicsView
{
%TypeHeaderCode
#include "Def.h"
#include "ElaGraphicsView.h"
%End

public: Q_SIGNAL void pMaxTransformChanged();
  void setMaxTransform(qreal MaxTransform);
  qreal getMaxTransform() const;
public: Q_SIGNAL void pMinTransformChanged();
  void setMinTransform(qreal MinTransform);
  qreal getMinTransform() const;
public:
  explicit ElaGraphicsView(QWidget * parent = nullptr);
  explicit ElaGraphicsView(QGraphicsScene * scene, QWidget * parent = nullptr);
  ~ElaGraphicsView();

protected:
  void wheelEvent(QWheelEvent * event) ;
  void keyPressEvent(QKeyEvent * event) ;
  void keyReleaseEvent(QKeyEvent * event) ;

};