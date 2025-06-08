%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaAcrylicUrlCard : public QPushButton
{
%TypeHeaderCode
#include "Def.h"
#include "ElaAcrylicUrlCard.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pMainOpacityChanged();
  void setMainOpacity(qreal MainOpacity);
  qreal getMainOpacity() const;
public: Q_SIGNAL void pNoiseOpacityChanged();
  void setNoiseOpacity(qreal NoiseOpacity);
  qreal getNoiseOpacity() const;
public: Q_SIGNAL void pBrushAlphaChanged();
  void setBrushAlpha(int BrushAlpha);
  int getBrushAlpha() const;
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
public: Q_SIGNAL void pSubTitleSpacingChanged();
  void setSubTitleSpacing(int SubTitleSpacing);
  int getSubTitleSpacing() const;
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
public: Q_SIGNAL void pUrlChanged();
  void setUrl(QString Url);
  QString getUrl() const;
public:
  explicit ElaAcrylicUrlCard(QWidget * parent = nullptr);
  ~ElaAcrylicUrlCard();
  void setCardPixmapSize(int width, int height) ;

protected:
  virtual void paintEvent(QPaintEvent * event) ;

};