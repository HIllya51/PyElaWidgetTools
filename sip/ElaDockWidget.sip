%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaDockWidget : public QDockWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaDockWidget.h"
%End

public:
  explicit ElaDockWidget(QWidget * parent = nullptr, Qt::WindowFlags flags = Qt::WindowFlags());
  explicit ElaDockWidget(const QString & title, QWidget * parent = nullptr, Qt::WindowFlags flags = Qt::WindowFlags());
  ~ElaDockWidget();

protected:
  virtual void paintEvent(QPaintEvent * event) ;
  virtual bool event(QEvent * event) ;
  virtual bool nativeEvent(const QByteArray & eventType, void * message, qintptr * result) ;

};