%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaTableView : public QTableView
{
%TypeHeaderCode
#include "Def.h"
#include "ElaTableView.h"
%End

public: Q_SIGNAL void pHeaderMarginChanged();
  void setHeaderMargin(int HeaderMargin);
  int getHeaderMargin() const;
public:
  explicit ElaTableView(QWidget * parent = nullptr);
  ~ElaTableView();

Q_SIGNALS:
Q_SIGNAL  void tableViewShow();
Q_SIGNAL  void tableViewHide();

};