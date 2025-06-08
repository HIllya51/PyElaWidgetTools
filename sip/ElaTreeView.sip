%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaTreeView : public QTreeView
{
%TypeHeaderCode
#include "Def.h"
#include "ElaTreeView.h"
%End

public: Q_SIGNAL void pItemHeightChanged();
  void setItemHeight(int ItemHeight);
  int getItemHeight() const;
public: Q_SIGNAL void pHeaderMarginChanged();
  void setHeaderMargin(int HeaderMargin);
  int getHeaderMargin() const;
public:
  explicit ElaTreeView(QWidget * parent = nullptr);
  ~ElaTreeView();

};