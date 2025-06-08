%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaLCDNumber : public QLCDNumber
{
%TypeHeaderCode
#include "Def.h"
#include "ElaLCDNumber.h"
%End

public: Q_SIGNAL void pIsUseAutoClockChanged();
  void setIsUseAutoClock(bool IsUseAutoClock);
  bool getIsUseAutoClock() const;
public: Q_SIGNAL void pAutoClockFormatChanged();
  void setAutoClockFormat(QString AutoClockFormat);
  QString getAutoClockFormat() const;
public: Q_SIGNAL void pIsTransparentChanged();
  void setIsTransparent(bool IsTransparent);
  bool getIsTransparent() const;
public:
  explicit ElaLCDNumber(QWidget * parent = nullptr);
  explicit ElaLCDNumber(uint numDigits, QWidget * parent = nullptr);
  ~ElaLCDNumber();

};