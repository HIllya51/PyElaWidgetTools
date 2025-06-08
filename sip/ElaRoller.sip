%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaRoller : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaRoller.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pItemListChanged();
  void setItemList(QStringList ItemList);
  QStringList getItemList() const;
public: Q_SIGNAL void pItemHeightChanged();
  void setItemHeight(int ItemHeight);
  int getItemHeight() const;
public: Q_SIGNAL void pMaxVisibleItemsChanged();
  void setMaxVisibleItems(int MaxVisibleItems);
  int getMaxVisibleItems() const;
public: Q_SIGNAL void pCurrentIndexChanged();
  void setCurrentIndex(int CurrentIndex);
  int getCurrentIndex() const;
public:
  explicit ElaRoller(QWidget * parent = nullptr);
  ~ElaRoller();
  QString getCurrentData() const ;

protected:
  virtual void wheelEvent(QWheelEvent * event) ;
  virtual void mouseReleaseEvent(QMouseEvent * event) ;
  virtual void mouseMoveEvent(QMouseEvent * event) ;
  virtual void leaveEvent(QEvent * event) ;
  virtual void paintEvent(QPaintEvent * event) ;

};