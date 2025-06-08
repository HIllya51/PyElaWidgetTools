%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaToolTip : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaToolTip.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pDisplayMsecChanged();
  void setDisplayMsec(int DisplayMsec);
  int getDisplayMsec() const;
public: Q_SIGNAL void pShowDelayMsecChanged();
  void setShowDelayMsec(int ShowDelayMsec);
  int getShowDelayMsec() const;
public: Q_SIGNAL void pHideDelayMsecChanged();
  void setHideDelayMsec(int HideDelayMsec);
  int getHideDelayMsec() const;
public: Q_SIGNAL void pToolTipChanged();
  void setToolTip(QString ToolTip);
  QString getToolTip() const;
public: Q_SIGNAL void pCustomWidgetChanged();
  void setCustomWidget(QWidget* CustomWidget);
  QWidget* getCustomWidget() const;
public:
  explicit ElaToolTip(QWidget * parent = nullptr);
  ~ElaToolTip();
  void updatePos() ;

protected:
  virtual void paintEvent(QPaintEvent * event) ;

};