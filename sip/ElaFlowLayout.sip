%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaFlowLayout : public QLayout
{
%TypeHeaderCode
#include "Def.h"
#include "ElaFlowLayout.h"
%End

public:
  explicit ElaFlowLayout(QWidget * parent, int margin = -1, int hSpacing = -1, int vSpacing = -1);
  explicit ElaFlowLayout(int margin = -1, int hSpacing = -1, int vSpacing = -1);
  ~ElaFlowLayout();
  void addItem(QLayoutItem * item) ;
  int horizontalSpacing() const ;
  int verticalSpacing() const ;
  Qt::Orientations expandingDirections() const ;
  bool hasHeightForWidth() const ;
  int heightForWidth(int arg1) const ;
  int count() const ;
  QLayoutItem* itemAt(int index) const ;
  QSize minimumSize() const ;
  void setGeometry(const QRect & rect) ;
  QSize sizeHint() const ;
  QLayoutItem* takeAt(int index) ;
  void setIsAnimation(bool isAnimation) ;

};