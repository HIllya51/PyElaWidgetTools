%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaPlainTextEdit : public QPlainTextEdit
{
%TypeHeaderCode
#include "Def.h"
#include "ElaPlainTextEdit.h"
%End

public:
  explicit ElaPlainTextEdit(QWidget * parent = nullptr);
  explicit ElaPlainTextEdit(const QString & text, QWidget * parent = nullptr);
  virtual ~ElaPlainTextEdit();

protected:
  virtual void focusInEvent(QFocusEvent * event) ;
  virtual void focusOutEvent(QFocusEvent * event) ;
  virtual void contextMenuEvent(QContextMenuEvent * event) ;

};