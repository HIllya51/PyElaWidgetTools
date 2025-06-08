%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaContentDialog : public QDialog
{
%TypeHeaderCode
#include "Def.h"
#include "ElaContentDialog.h"
%End

public:
  explicit ElaContentDialog(QWidget * parent);
  ~ElaContentDialog();
  Q_SLOT virtual void onLeftButtonClicked() ;
  Q_SLOT virtual void onMiddleButtonClicked() ;
  Q_SLOT virtual void onRightButtonClicked() ;
  void setCentralWidget(QWidget * centralWidget) ;
  void setLeftButtonText(QString text) ;
  void setMiddleButtonText(QString text) ;
  void setRightButtonText(QString text) ;
  void close() ;

Q_SIGNALS:
Q_SIGNAL  void leftButtonClicked();
Q_SIGNAL  void middleButtonClicked();
Q_SIGNAL  void rightButtonClicked();

};