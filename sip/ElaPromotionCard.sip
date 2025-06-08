%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaPromotionCard : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaPromotionCard.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pCardPixmapChanged();
  void setCardPixmap(QPixmap CardPixmap);
  QPixmap getCardPixmap() const;
public: Q_SIGNAL void pCardTitleChanged();
  void setCardTitle(QString CardTitle);
  QString getCardTitle() const;
public: Q_SIGNAL void pPromotionTitleChanged();
  void setPromotionTitle(QString PromotionTitle);
  QString getPromotionTitle() const;
public: Q_SIGNAL void pTitleChanged();
  void setTitle(QString Title);
  QString getTitle() const;
public: Q_SIGNAL void pSubTitleChanged();
  void setSubTitle(QString SubTitle);
  QString getSubTitle() const;
public: Q_SIGNAL void pCardTitleColorChanged();
  void setCardTitleColor(QColor CardTitleColor);
  QColor getCardTitleColor() const;
public: Q_SIGNAL void pPromotionTitleColorChanged();
  void setPromotionTitleColor(QColor PromotionTitleColor);
  QColor getPromotionTitleColor() const;
public: Q_SIGNAL void pPromotionTitleBaseColorChanged();
  void setPromotionTitleBaseColor(QColor PromotionTitleBaseColor);
  QColor getPromotionTitleBaseColor() const;
public: Q_SIGNAL void pTitleColorChanged();
  void setTitleColor(QColor TitleColor);
  QColor getTitleColor() const;
public: Q_SIGNAL void pSubTitleColorChanged();
  void setSubTitleColor(QColor SubTitleColor);
  QColor getSubTitleColor() const;
public: Q_SIGNAL void pCardTitlePixelSizeChanged();
  void setCardTitlePixelSize(int CardTitlePixelSize);
  int getCardTitlePixelSize() const;
public: Q_SIGNAL void pPromotionTitlePixelSizeChanged();
  void setPromotionTitlePixelSize(int PromotionTitlePixelSize);
  int getPromotionTitlePixelSize() const;
public: Q_SIGNAL void pTitlePixelSizeChanged();
  void setTitlePixelSize(int TitlePixelSize);
  int getTitlePixelSize() const;
public: Q_SIGNAL void pSubTitlePixelSizeChanged();
  void setSubTitlePixelSize(int SubTitlePixelSize);
  int getSubTitlePixelSize() const;
public: Q_SIGNAL void pHorizontalCardPixmapRatioChanged();
  void setHorizontalCardPixmapRatio(qreal HorizontalCardPixmapRatio);
  qreal getHorizontalCardPixmapRatio() const;
public: Q_SIGNAL void pVerticalCardPixmapRatioChanged();
  void setVerticalCardPixmapRatio(qreal VerticalCardPixmapRatio);
  qreal getVerticalCardPixmapRatio() const;
public:
  explicit ElaPromotionCard(QWidget * parent = nullptr);
  ~ElaPromotionCard();

Q_SIGNALS:
Q_SIGNAL  void promotionCardClicked();

};