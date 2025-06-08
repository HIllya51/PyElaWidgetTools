%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaTabBar : public QTabBar
{
%TypeHeaderCode
#include "Def.h"
#include "ElaTabBar.h"
%End

public:
  explicit ElaTabBar(QWidget * parent = nullptr);
  ~ElaTabBar();

Q_SIGNALS:
Q_SIGNAL  void tabBarPress(int index);
Q_SIGNAL  void tabDragCreate(QDrag* drag);
Q_SIGNAL  void tabDragDrop(const QMimeData* mimeData);

};