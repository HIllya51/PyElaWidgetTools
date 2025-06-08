%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaMultiSelectComboBox : public QComboBox
{
%TypeHeaderCode
#include "Def.h"
#include "ElaMultiSelectComboBox.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public:
  explicit ElaMultiSelectComboBox(QWidget * parent = nullptr);
  ~ElaMultiSelectComboBox();
  void setCurrentSelection(QString selection) ;
  void setCurrentSelection(QStringList selection) ;
  void setCurrentSelection(int index) ;
  void setCurrentSelection(QList<int> selectionIndex) ;
  QStringList getCurrentSelection() const ;
  QList<int> getCurrentSelectionIndex() const ;

Q_SIGNALS:
Q_SIGNAL  void currentTextListChanged(QStringList selectedTextList);

};