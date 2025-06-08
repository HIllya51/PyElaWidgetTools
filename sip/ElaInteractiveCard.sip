%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaInteractiveCard : public QPushButton
{
%TypeHeaderCode
#include "Def.h"
#include "ElaInteractiveCard.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pTitleChanged();
  void setTitle(QString Title);
  QString getTitle() const;
public: Q_SIGNAL void pSubTitleChanged();
  void setSubTitle(QString SubTitle);
  QString getSubTitle() const;
public: Q_SIGNAL void pTitlePixelSizeChanged();
  void setTitlePixelSize(int TitlePixelSize);
  int getTitlePixelSize() const;
public: Q_SIGNAL void pSubTitlePixelSizeChanged();
  void setSubTitlePixelSize(int SubTitlePixelSize);
  int getSubTitlePixelSize() const;
public: Q_SIGNAL void pTitleSpacingChanged();
  void setTitleSpacing(int TitleSpacing);
  int getTitleSpacing() const;
public: Q_SIGNAL void pCardPixmapChanged();
  void setCardPixmap(QPixmap CardPixmap);
  QPixmap getCardPixmap() const;
public: Q_SIGNAL void pCardPixmapSizeChanged();
  void setCardPixmapSize(QSize CardPixmapSize);
  QSize getCardPixmapSize() const;
public: Q_SIGNAL void pCardPixmapBorderRadiusChanged();
  void setCardPixmapBorderRadius(int CardPixmapBorderRadius);
  int getCardPixmapBorderRadius() const;
public: Q_SIGNAL void pCardPixModeChanged();
  void setCardPixMode(ElaCardPixType::PixMode CardPixMode);
  ElaCardPixType::PixMode getCardPixMode() const;
public:
  explicit ElaInteractiveCard(QWidget * parent = nullptr);
  ~ElaInteractiveCard();
  void setCardPixmapSize(int width, int height) ;

protected:
  void paintEvent(QPaintEvent * event) ;

};