%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaExponentialBlur : public QObject
{
%TypeHeaderCode
#include "Def.h"
#include "ElaExponentialBlur.h"
%End

public: static ElaExponentialBlur* getInstance();
private:
  explicit ElaExponentialBlur(QObject * parent = nullptr);
  ~ElaExponentialBlur();

public:
  static QPixmap doExponentialBlur(QImage img, const quint16 & blurRadius) ;

};