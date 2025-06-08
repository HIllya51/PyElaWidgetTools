%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaPushButton : public QPushButton
{
%TypeHeaderCode
#include "Def.h"
#include "ElaPushButton.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pLightDefaultColorChanged();
  void setLightDefaultColor(QColor LightDefaultColor);
  QColor getLightDefaultColor() const;
public: Q_SIGNAL void pDarkDefaultColorChanged();
  void setDarkDefaultColor(QColor DarkDefaultColor);
  QColor getDarkDefaultColor() const;
public: Q_SIGNAL void pLightHoverColorChanged();
  void setLightHoverColor(QColor LightHoverColor);
  QColor getLightHoverColor() const;
public: Q_SIGNAL void pDarkHoverColorChanged();
  void setDarkHoverColor(QColor DarkHoverColor);
  QColor getDarkHoverColor() const;
public: Q_SIGNAL void pLightPressColorChanged();
  void setLightPressColor(QColor LightPressColor);
  QColor getLightPressColor() const;
public: Q_SIGNAL void pDarkPressColorChanged();
  void setDarkPressColor(QColor DarkPressColor);
  QColor getDarkPressColor() const;
public:
  explicit ElaPushButton(QWidget * parent = nullptr);
  explicit ElaPushButton(QString text, QWidget * parent = nullptr);
  ~ElaPushButton();
  void setLightTextColor(QColor color) ;
  QColor getLightTextColor() const ;
  void setDarkTextColor(QColor color) ;
  QColor getDarkTextColor() const ;

protected:
  virtual void mousePressEvent(QMouseEvent * event) ;
  virtual void mouseReleaseEvent(QMouseEvent * event) ;
  virtual void paintEvent(QPaintEvent * event) ;

};