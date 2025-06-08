%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaEvent : public QObject
{
%TypeHeaderCode
#include "Def.h"
#include "ElaEventBus.h"
%End

public: Q_SIGNAL void pEventNameChanged();
  void setEventName(QString EventName);
  QString getEventName() const;
public: Q_SIGNAL void pFunctionNameChanged();
  void setFunctionName(QString FunctionName);
  QString getFunctionName() const;
public: Q_SIGNAL void pConnectionTypeChanged();
  void setConnectionType(Qt::ConnectionType ConnectionType);
  Qt::ConnectionType getConnectionType() const;
public:
  explicit ElaEvent(QObject * parent = nullptr);
  explicit ElaEvent(QString eventName, QString functionName, QObject * parent = nullptr);
  ~ElaEvent();
  ElaEventBusType::EventBusReturnType registerAndInit() ;

};
class ElaEventBus : public QObject
{
%TypeHeaderCode
#include "Def.h"
#include "ElaEventBus.h"
%End

public: static ElaEventBus* getInstance();
private:
  explicit ElaEventBus(QObject * parent = nullptr);
  ~ElaEventBus();

public:
  ElaEventBusType::EventBusReturnType post(const QString & eventName, const QVariantMap & data = {}) ;
  QStringList getRegisteredEventsName() const ;

private:

};