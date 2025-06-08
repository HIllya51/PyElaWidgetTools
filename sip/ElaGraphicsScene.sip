%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaGraphicsScene : public QGraphicsScene
{
%TypeHeaderCode
#include "Def.h"
#include "ElaGraphicsScene.h"
%End

public: Q_SIGNAL void pIsCheckLinkPortChanged();
  void setIsCheckLinkPort(bool IsCheckLinkPort);
  bool getIsCheckLinkPort() const;
public: Q_SIGNAL void pSerializePathChanged();
  void setSerializePath(QString SerializePath);
  QString getSerializePath() const;
public:
  explicit ElaGraphicsScene(QObject * parent = nullptr);
  ~ElaGraphicsScene();
  void addItem(ElaGraphicsItem * item) ;
  void removeItem(ElaGraphicsItem * item) ;
  void removeSelectedItems() ;
  void clear() ;
  QList<ElaGraphicsItem*> createAndAddItem(int width, int height, int count = 1) ;
  QList<ElaGraphicsItem*> getSelectedElaItems() const ;
  QList<ElaGraphicsItem*> getElaItems() ;
  QList<ElaGraphicsItem*> getElaItems(QPoint pos) ;
  QList<ElaGraphicsItem*> getElaItems(QPointF pos) ;
  QList<ElaGraphicsItem*> getElaItems(QRect rect) ;
  QList<ElaGraphicsItem*> getElaItems(QRectF rect) ;
  void setSceneMode(ElaGraphicsSceneType::SceneMode mode) ;
  ElaGraphicsSceneType::SceneMode getSceneMode() const ;
  void selectAllItems() ;
  bool addItemLink(ElaGraphicsItem * item1, ElaGraphicsItem * item2, int port1 = 0, int port2 = 0) ;
  bool removeItemLink(ElaGraphicsItem * item1) ;
  bool removeItemLink(ElaGraphicsItem * item1, ElaGraphicsItem * item2, int port1 = 0, int port2 = 0) ;
  void serialize() ;
  void deserialize() ;

Q_SIGNALS:

};