%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaScrollBar : public QScrollBar
{
%TypeHeaderCode
#include "Def.h"
#include "ElaScrollBar.h"
%End

public: Q_SIGNAL void pIsAnimationChanged();
  void setIsAnimation(bool IsAnimation);
  bool getIsAnimation() const;
public: Q_SIGNAL void pSpeedLimitChanged();
  void setSpeedLimit(qreal SpeedLimit);
  qreal getSpeedLimit() const;
public:
  explicit ElaScrollBar(QWidget * parent = nullptr);
  explicit ElaScrollBar(Qt::Orientation orientation, QWidget * parent = nullptr);
  explicit ElaScrollBar(QScrollBar * originScrollBar, QAbstractScrollArea * parent = nullptr);
  ~ElaScrollBar();

Q_SIGNALS:
Q_SIGNAL  void rangeAnimationFinished();

};