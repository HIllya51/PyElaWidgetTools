%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaApplication : public QObject
{
%TypeHeaderCode
#include "Def.h"
#include "ElaApplication.h"
%End

public: Q_SIGNAL void pWindowDisplayModeChanged();
  void setWindowDisplayMode(ElaApplicationType::WindowDisplayMode WindowDisplayMode);
  ElaApplicationType::WindowDisplayMode getWindowDisplayMode() const;
public: Q_SIGNAL void pElaMicaImagePathChanged();
  void setElaMicaImagePath(QString ElaMicaImagePath);
  QString getElaMicaImagePath() const;
public: static ElaApplication* getInstance();
private:
  explicit ElaApplication(QObject * parent = nullptr);
  ~ElaApplication();

public:
  void init() ;
  void syncWindowDisplayMode(QWidget * widget, bool isSync = true) ;
  static bool containsCursorToItem(QWidget * item) ;

};