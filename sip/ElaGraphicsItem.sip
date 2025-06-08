%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaGraphicsItem : public QGraphicsObject
{
%TypeHeaderCode
#include "Def.h"
#include "ElaGraphicsItem.h"
%End

public: Q_SIGNAL void pWidthChanged();
  void setWidth(int Width);
  int getWidth() const;
public: Q_SIGNAL void pHeightChanged();
  void setHeight(int Height);
  int getHeight() const;
public: Q_SIGNAL void pItemImageChanged();
  void setItemImage(QImage ItemImage);
  QImage getItemImage() const;
public: Q_SIGNAL void pItemSelectedImageChanged();
  void setItemSelectedImage(QImage ItemSelectedImage);
  QImage getItemSelectedImage() const;
public: Q_SIGNAL void pItemNameChanged();
  void setItemName(QString ItemName);
  QString getItemName() const;
public: Q_SIGNAL void pDataRoutesChanged();
  void setDataRoutes(QVariantMap DataRoutes);
  QVariantMap getDataRoutes() const;
public: Q_SIGNAL void pMaxLinkPortCountChanged();
  void setMaxLinkPortCount(int MaxLinkPortCount);
  int getMaxLinkPortCount() const;
public:
  explicit ElaGraphicsItem(QGraphicsItem * parent = nullptr);
  explicit ElaGraphicsItem(int width, int height, QGraphicsItem * parent = nullptr);
  ~ElaGraphicsItem();
  QString getItemUID() const ;
  void setLinkPortState(bool isFullLink) ;
  void setLinkPortState(bool isLink, int portIndex) ;
  bool getLinkPortState(int portIndex) const ;
  int getUsedLinkPortCount() const ;
  int getUnusedLinkPortCount() const ;

protected:
  virtual QRectF boundingRect() const ;
  virtual void paint(QPainter * painter, const QStyleOptionGraphicsItem * option, QWidget * widget = nullptr) ;

};