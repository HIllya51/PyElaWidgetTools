%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaPivot : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaPivot.h"
%End

public: Q_SIGNAL void pTextPixelSizeChanged();
  void setTextPixelSize(int TextPixelSize);
  int getTextPixelSize() const;
public: Q_SIGNAL void pCurrentIndexChanged();
  void setCurrentIndex(int CurrentIndex);
  int getCurrentIndex() const;
public: Q_SIGNAL void pPivotSpacingChanged();
  void setPivotSpacing(int PivotSpacing);
  int getPivotSpacing() const;
public: Q_SIGNAL void pMarkWidthChanged();
  void setMarkWidth(int MarkWidth);
  int getMarkWidth() const;
public:
  explicit ElaPivot(QWidget * parent = nullptr);
  ~ElaPivot();
  void appendPivot(QString pivotTitle) ;
  void removePivot(QString pivotTitle) ;

Q_SIGNALS:
Q_SIGNAL  void pivotClicked(int index);
Q_SIGNAL  void pivotDoubleClicked(int index);

};