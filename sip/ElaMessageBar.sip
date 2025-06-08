%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaMessageBar : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaMessageBar.h"
%End

public:
  static void success(ElaMessageBarType::PositionPolicy policy, QString title, QString text, int displayMsec, QWidget * parent = nullptr) ;
  static void warning(ElaMessageBarType::PositionPolicy policy, QString title, QString text, int displayMsec, QWidget * parent = nullptr) ;
  static void information(ElaMessageBarType::PositionPolicy policy, QString title, QString text, int displayMsec, QWidget * parent = nullptr) ;
  static void error(ElaMessageBarType::PositionPolicy policy, QString title, QString text, int displayMsec, QWidget * parent = nullptr) ;

protected:
  virtual void paintEvent(QPaintEvent * event) ;
  virtual bool eventFilter(QObject * watched, QEvent * event) ;

private:
  explicit ElaMessageBar(ElaMessageBarType::PositionPolicy policy, ElaMessageBarType::MessageMode messageMode, QString & title /Out/, QString & text /Out/, int displayMsec, QWidget * parent = nullptr);
  ~ElaMessageBar();

};