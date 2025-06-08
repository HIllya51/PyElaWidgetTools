%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaImageCard : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaImageCard.h"
%End

public: Q_SIGNAL void pCardImageChanged();
  void setCardImage(QImage CardImage);
  QImage getCardImage() const;
public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pIsPreserveAspectCropChanged();
  void setIsPreserveAspectCrop(bool IsPreserveAspectCrop);
  bool getIsPreserveAspectCrop() const;
public: Q_SIGNAL void pMaximumAspectRatioChanged();
  void setMaximumAspectRatio(qreal MaximumAspectRatio);
  qreal getMaximumAspectRatio() const;
public:
  explicit ElaImageCard(QWidget * parent = nullptr);
  ~ElaImageCard();

protected:
  virtual void paintEvent(QPaintEvent * event) ;

};