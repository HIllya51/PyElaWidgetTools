%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaKeyBinder : public QLabel
{
%TypeHeaderCode
#include "Def.h"
#include "ElaKeyBinder.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pBinderKeyTextChanged();
  void setBinderKeyText(QString BinderKeyText);
  QString getBinderKeyText() const;
public: Q_SIGNAL void pNativeVirtualBinderKeyChanged();
  void setNativeVirtualBinderKey(quint32 NativeVirtualBinderKey);
  quint32 getNativeVirtualBinderKey() const;
public:
  explicit ElaKeyBinder(QWidget * parent = nullptr);
  ~ElaKeyBinder();

Q_SIGNALS:
Q_SIGNAL  void binderKeyTextChanged(QString binderKeyText);
Q_SIGNAL  void nativeVirtualBinderKeyChanged(quint32 binderKey);

};