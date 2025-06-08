%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaListView : public QListView
{
%TypeHeaderCode
#include "Def.h"
#include "ElaListView.h"
%End

public: Q_SIGNAL void pItemHeightChanged();
  void setItemHeight(int ItemHeight);
  int getItemHeight() const;
public: Q_SIGNAL void pIsTransparentChanged();
  void setIsTransparent(bool IsTransparent);
  bool getIsTransparent() const;
public:
  explicit ElaListView(QWidget * parent = nullptr);
  ~ElaListView();

};