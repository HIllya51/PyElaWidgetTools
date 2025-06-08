%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaSlider : public QSlider
{
%TypeHeaderCode
#include "Def.h"
#include "ElaSlider.h"
%End

public:
  explicit ElaSlider(QWidget * parent = nullptr);
  explicit ElaSlider(Qt::Orientation orientation, QWidget * parent = nullptr);
  ~ElaSlider();

};