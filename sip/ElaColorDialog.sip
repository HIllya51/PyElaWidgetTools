%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaColorDialog : public QDialog
{
%TypeHeaderCode
#include "Def.h"
#include "ElaColorDialog.h"
%End

public: Q_SIGNAL void pCurrentColorChanged();
  void setCurrentColor(QColor CurrentColor);
  QColor getCurrentColor() const;
public:
  explicit ElaColorDialog(QWidget * parent = nullptr);
  ~ElaColorDialog();
  QList<QColor> getCustomColorList() const ;
  QColor getCustomColor(int index) const ;
  QString getCurrentColorRGB() const ;

Q_SIGNALS:
Q_SIGNAL  void colorSelected(const QColor& color);

};