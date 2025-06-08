%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaMessageButton : public QPushButton
{
%TypeHeaderCode
#include "Def.h"
#include "ElaMessageButton.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pBarTitleChanged();
  void setBarTitle(QString BarTitle);
  QString getBarTitle() const;
public: Q_SIGNAL void pBarTextChanged();
  void setBarText(QString BarText);
  QString getBarText() const;
public: Q_SIGNAL void pDisplayMsecChanged();
  void setDisplayMsec(int DisplayMsec);
  int getDisplayMsec() const;
public: Q_SIGNAL void pMessageTargetWidgetChanged();
  void setMessageTargetWidget(QWidget* MessageTargetWidget);
  QWidget* getMessageTargetWidget() const;
public: Q_SIGNAL void pMessageModeChanged();
  void setMessageMode(ElaMessageBarType::MessageMode MessageMode);
  ElaMessageBarType::MessageMode getMessageMode() const;
public: Q_SIGNAL void pPositionPolicyChanged();
  void setPositionPolicy(ElaMessageBarType::PositionPolicy PositionPolicy);
  ElaMessageBarType::PositionPolicy getPositionPolicy() const;
public:
  explicit ElaMessageButton(QWidget * parent = nullptr);
  explicit ElaMessageButton(QString text, QWidget * parent = nullptr);
  ~ElaMessageButton();

protected:
  virtual void mousePressEvent(QMouseEvent * event) ;
  virtual void mouseReleaseEvent(QMouseEvent * event) ;
  virtual void paintEvent(QPaintEvent * event) ;

};