%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaPromotionView : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaPromotionView.h"
%End

public: Q_SIGNAL void pCardExpandWidthChanged();
  void setCardExpandWidth(int CardExpandWidth);
  int getCardExpandWidth() const;
public: Q_SIGNAL void pCardCollapseWidthChanged();
  void setCardCollapseWidth(int CardCollapseWidth);
  int getCardCollapseWidth() const;
public: Q_SIGNAL void pCurrentIndexChanged();
  void setCurrentIndex(int CurrentIndex);
  int getCurrentIndex() const;
public: Q_SIGNAL void pIsAutoScrollChanged();
  void setIsAutoScroll(bool IsAutoScroll);
  bool getIsAutoScroll() const;
public: Q_SIGNAL void pAutoScrollIntervalChanged();
  void setAutoScrollInterval(int AutoScrollInterval);
  int getAutoScrollInterval() const;
public:
  explicit ElaPromotionView(QWidget * parent = nullptr);
  ~ElaPromotionView();
  void appendPromotionCard(ElaPromotionCard * card) ;

protected:
  virtual void wheelEvent(QWheelEvent * event) ;
  virtual void paintEvent(QPaintEvent * event) ;

};