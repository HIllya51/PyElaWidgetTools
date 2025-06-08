%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaIconButton : public QPushButton
{
%TypeHeaderCode
#include "Def.h"
#include "ElaIconButton.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pOpacityChanged();
  void setOpacity(qreal Opacity);
  qreal getOpacity() const;
public: Q_SIGNAL void pLightHoverColorChanged();
  void setLightHoverColor(QColor LightHoverColor);
  QColor getLightHoverColor() const;
public: Q_SIGNAL void pDarkHoverColorChanged();
  void setDarkHoverColor(QColor DarkHoverColor);
  QColor getDarkHoverColor() const;
public: Q_SIGNAL void pLightIconColorChanged();
  void setLightIconColor(QColor LightIconColor);
  QColor getLightIconColor() const;
public: Q_SIGNAL void pDarkIconColorChanged();
  void setDarkIconColor(QColor DarkIconColor);
  QColor getDarkIconColor() const;
public: Q_SIGNAL void pLightHoverIconColorChanged();
  void setLightHoverIconColor(QColor LightHoverIconColor);
  QColor getLightHoverIconColor() const;
public: Q_SIGNAL void pDarkHoverIconColorChanged();
  void setDarkHoverIconColor(QColor DarkHoverIconColor);
  QColor getDarkHoverIconColor() const;
public: Q_SIGNAL void pIsSelectedChanged();
  void setIsSelected(bool IsSelected);
  bool getIsSelected() const;
public:
  ElaIconButton(QPixmap pix, QWidget * parent = nullptr);
  ElaIconButton(ElaIconType::IconName awesome, QWidget * parent = nullptr);
  ElaIconButton(ElaIconType::IconName awesome, int pixelSize, QWidget * parent = nullptr);
  ElaIconButton(ElaIconType::IconName awesome, int pixelSize, int fixedWidth, int fixedHeight, QWidget * parent = nullptr);
  ~ElaIconButton();
  void setAwesome(ElaIconType::IconName awesome) ;
  ElaIconType::IconName getAwesome() const ;
  void setPixmap(QPixmap pix) ;

protected:
  virtual bool event(QEvent * event) ;
  virtual void paintEvent(QPaintEvent * event) ;

};