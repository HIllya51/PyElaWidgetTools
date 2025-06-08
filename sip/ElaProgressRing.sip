%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaProgressRing : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaProgressRing.h"
%End

public: Q_SIGNAL void pIsBusyingChanged();
  void setIsBusying(bool IsBusying);
  bool getIsBusying() const;
public: Q_SIGNAL void pIsTransparentChanged();
  void setIsTransparent(bool IsTransparent);
  bool getIsTransparent() const;
public: Q_SIGNAL void pIsDisplayValueChanged();
  void setIsDisplayValue(bool IsDisplayValue);
  bool getIsDisplayValue() const;
public: Q_SIGNAL void pValueDisplayModeChanged();
  void setValueDisplayMode(ElaProgressRingType::ValueDisplayMode ValueDisplayMode);
  ElaProgressRingType::ValueDisplayMode getValueDisplayMode() const;
public: Q_SIGNAL void pBusyingWidthChanged();
  void setBusyingWidth(int BusyingWidth);
  int getBusyingWidth() const;
public: Q_SIGNAL void pBusyingDurationTimeChanged();
  void setBusyingDurationTime(int BusyingDurationTime);
  int getBusyingDurationTime() const;
public: Q_SIGNAL void pMinimumChanged();
  void setMinimum(int Minimum);
  int getMinimum() const;
public: Q_SIGNAL void pMaximumChanged();
  void setMaximum(int Maximum);
  int getMaximum() const;
public: Q_SIGNAL void pValueChanged();
  void setValue(int Value);
  int getValue() const;
public: Q_SIGNAL void pValuePixelSizeChanged();
  void setValuePixelSize(int ValuePixelSize);
  int getValuePixelSize() const;
public:
  explicit ElaProgressRing(QWidget * parent = nullptr);
  ~ElaProgressRing();
  void setRange(int min, int max) ;

Q_SIGNALS:
Q_SIGNAL  void rangeChanged(int min, int max);

};