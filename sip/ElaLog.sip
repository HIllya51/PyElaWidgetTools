%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaLog : public QObject
{
%TypeHeaderCode
#include "Def.h"
#include "ElaLog.h"
%End

public: Q_SIGNAL void pLogSavePathChanged();
  void setLogSavePath(QString LogSavePath);
  QString getLogSavePath() const;
public: Q_SIGNAL void pLogFileNameChanged();
  void setLogFileName(QString LogFileName);
  QString getLogFileName() const;
public: Q_SIGNAL void pIsLogFileNameWithTimeChanged();
  void setIsLogFileNameWithTime(bool IsLogFileNameWithTime);
  bool getIsLogFileNameWithTime() const;
public: static ElaLog* getInstance();
private:
  explicit ElaLog(QObject * parent = nullptr);
  ~ElaLog();

public:
  void initMessageLog(bool isEnable) ;

Q_SIGNALS:

};