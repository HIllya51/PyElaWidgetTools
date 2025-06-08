%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaText : public QLabel
{
%TypeHeaderCode
#include "Def.h"
#include "ElaText.h"
%End

public: Q_SIGNAL void pIsWrapAnywhereChanged();
  void setIsWrapAnywhere(bool IsWrapAnywhere);
  bool getIsWrapAnywhere() const;
public: Q_SIGNAL void pTextPixelSizeChanged();
  void setTextPixelSize(int TextPixelSize);
  int getTextPixelSize() const;
public: Q_SIGNAL void pTextPointSizeChanged();
  void setTextPointSize(int TextPointSize);
  int getTextPointSize() const;
public: Q_SIGNAL void pTextStyleChanged();
  void setTextStyle(ElaTextType::TextStyle TextStyle);
  ElaTextType::TextStyle getTextStyle() const;
public: Q_SIGNAL void pElaIconChanged();
  void setElaIcon(ElaIconType::IconName ElaIcon);
  ElaIconType::IconName getElaIcon() const;
public:
  explicit ElaText(QWidget * parent = nullptr);
  explicit ElaText(QString text, QWidget * parent = nullptr);
  explicit ElaText(QString text, int pixelSize, QWidget * parent = nullptr);
  ~ElaText();

protected:
  virtual void paintEvent(QPaintEvent * event) ;

};