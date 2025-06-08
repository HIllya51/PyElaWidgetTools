%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaIcon
{
%TypeHeaderCode
#include "ElaIcon.h"
%End

private:
    explicit ElaIcon(); // Private constructor, not for Python use
    ~ ElaIcon(); // Private constructor, not for Python use
public:
    static ElaIcon* getInstance();
private:
  // Public constructor for singleton? Unusual. getInstance() is preferred.
  // Public destructor for singleton? Unusual.
public:
  QIcon getElaIcon(ElaIconType::IconName awesome);
  QIcon getElaIcon(ElaIconType::IconName awesome, QColor iconColor);
  QIcon getElaIcon(ElaIconType::IconName awesome, int pixelSize);
  QIcon getElaIcon(ElaIconType::IconName awesome, int pixelSize, QColor iconColor);
  QIcon getElaIcon(ElaIconType::IconName awesome, int pixelSize, int fixedWidth, int fixedHeight);
  QIcon getElaIcon(ElaIconType::IconName awesome, int pixelSize, int fixedWidth, int fixedHeight, QColor iconColor);
};