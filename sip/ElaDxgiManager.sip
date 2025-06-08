%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaDxgiManager : public QObject
{
%TypeHeaderCode
#include "Def.h"
#include "ElaDxgiManager.h"
%End

public: static ElaDxgiManager* getInstance();
private:
  explicit ElaDxgiManager(QObject * parent = nullptr);
  ~ElaDxgiManager();

public:
  QStringList getDxDeviceList() const ;
  QStringList getOutputDeviceList() const ;
  QImage grabScreenToImage() const ;
  void startGrabScreen() ;
  void stopGrabScreen() ;
  bool getIsGrabScreen() const ;
  bool setDxDeviceID(int dxID) ;
  int getDxDeviceID() const ;
  bool setOutputDeviceID(int deviceID) ;
  int getOutputDeviceID() const ;
  void setGrabArea(int width, int height) ;
  void setGrabArea(int x, int y, int width, int height) ;
  QRect getGrabArea() const ;
  void setGrabFrameRate(int frameRateValue) ;
  int getGrabFrameRate() const ;
  void setTimeoutMsValue(int timeoutValue) ;
  int getTimeoutMsValue() const ;

Q_SIGNALS:
Q_SIGNAL  void grabImageUpdate(QImage img);

};
class ElaDxgiScreen : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaDxgiManager.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public:
  explicit ElaDxgiScreen(QWidget * parent = nullptr);
  ~ElaDxgiScreen();
  void setIsSyncGrabSize(bool isSyncGrabSize) ;
  bool getIsSyncGrabSize() const ;

protected:
  void paintEvent(QPaintEvent * event) ;

};