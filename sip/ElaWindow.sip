%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaWindow : public QMainWindow
{
%TypeHeaderCode
#include "Def.h"
#include "ElaWindow.h"
%End

public: Q_SIGNAL void pIsStayTopChanged();
  void setIsStayTop(bool IsStayTop);
  bool getIsStayTop() const;
public: Q_SIGNAL void pIsFixedSizeChanged();
  void setIsFixedSize(bool IsFixedSize);
  bool getIsFixedSize() const;
public: Q_SIGNAL void pIsDefaultClosedChanged();
  void setIsDefaultClosed(bool IsDefaultClosed);
  bool getIsDefaultClosed() const;
public: Q_SIGNAL void pAppBarHeightChanged();
  void setAppBarHeight(int AppBarHeight);
  int getAppBarHeight() const;
public: Q_SIGNAL void pCustomWidgetMaximumWidthChanged();
  void setCustomWidgetMaximumWidth(int CustomWidgetMaximumWidth);
  int getCustomWidgetMaximumWidth() const;
public: Q_SIGNAL void pThemeChangeTimeChanged();
  void setThemeChangeTime(int ThemeChangeTime);
  int getThemeChangeTime() const;
public: Q_SIGNAL void pIsCentralStackedWidgetTransparentChanged();
  void setIsCentralStackedWidgetTransparent(bool IsCentralStackedWidgetTransparent);
  bool getIsCentralStackedWidgetTransparent() const;
public: Q_SIGNAL void pIsAllowPageOpenInNewWindowChanged();
  void setIsAllowPageOpenInNewWindow(bool IsAllowPageOpenInNewWindow);
  bool getIsAllowPageOpenInNewWindow() const;
public: Q_SIGNAL void pNavigationBarDisplayModeChanged();
  void setNavigationBarDisplayMode(ElaNavigationType::NavigationDisplayMode NavigationBarDisplayMode);
  ElaNavigationType::NavigationDisplayMode getNavigationBarDisplayMode() const;
public: Q_SIGNAL void pStackSwitchModeChanged();
  void setStackSwitchMode(ElaWindowType::StackSwitchMode StackSwitchMode);
  ElaWindowType::StackSwitchMode getStackSwitchMode() const;
public:
  explicit ElaWindow(QWidget * parent = nullptr);
  ~ElaWindow();
  void moveToCenter() ;
  void setCustomWidget(ElaAppBarType::CustomArea customArea, QWidget * customWidget) ;
  QWidget* getCustomWidget() const ;
  void setIsNavigationBarEnable(bool isEnable) ;
  bool getIsNavigationBarEnable() const ;
  void setUserInfoCardVisible(bool isVisible) ;
  void setUserInfoCardPixmap(QPixmap pix) ;
  void setUserInfoCardTitle(QString title) ;
  void setUserInfoCardSubTitle(QString subTitle) ;
  ElaNavigationType::NodeOperateReturnType addExpanderNode(QString expanderTitle, QString & expanderKey /Out/, ElaIconType::IconName awesome = ElaIconType::None) const ;
  ElaNavigationType::NodeOperateReturnType addExpanderNode(QString expanderTitle, QString & expanderKey /Out/, QString targetExpanderKey, ElaIconType::IconName awesome = ElaIconType::None) const ;
  ElaNavigationType::NodeOperateReturnType addPageNode(QString pageTitle, QWidget * page, ElaIconType::IconName awesome = ElaIconType::None) const ;
  ElaNavigationType::NodeOperateReturnType addPageNode(QString pageTitle, QWidget * page, QString targetExpanderKey, ElaIconType::IconName awesome = ElaIconType::None) const ;
  ElaNavigationType::NodeOperateReturnType addPageNode(QString pageTitle, QWidget * page, int keyPoints = 0, ElaIconType::IconName awesome = ElaIconType::None) const /PyName=addPageNodeKeyPoints/;
  ElaNavigationType::NodeOperateReturnType addPageNode(QString pageTitle, QWidget * page, QString targetExpanderKey, int keyPoints = 0, ElaIconType::IconName awesome = ElaIconType::None) const /PyName=addPageNodeKeyPoints/;
  ElaNavigationType::NodeOperateReturnType addFooterNode(QString footerTitle, QString & footerKey /Out/, int keyPoints = 0, ElaIconType::IconName awesome = ElaIconType::None) const ;
  ElaNavigationType::NodeOperateReturnType addFooterNode(QString footerTitle, QWidget * page, QString & footerKey /Out/, int keyPoints = 0, ElaIconType::IconName awesome = ElaIconType::None) const ;
  bool getNavigationNodeIsExpanded(QString expanderKey) const ;
  void expandNavigationNode(QString expanderKey) ;
  void collpaseNavigationNode(QString expanderKey) ;
  void removeNavigationNode(QString nodeKey) const ;
  int getPageOpenInNewWindowCount(QString nodeKey) const ;
  void setNodeKeyPoints(QString nodeKey, int keyPoints) ;
  int getNodeKeyPoints(QString nodeKey) const ;
  void navigation(QString pageKey) ;
  void setWindowButtonFlag(ElaAppBarType::ButtonType buttonFlag, bool isEnable = true) ;
  void setWindowButtonFlags(ElaAppBarType::ButtonFlags buttonFlags) ;
  ElaAppBarType::ButtonFlags getWindowButtonFlags() const ;
  void closeWindow() ;

Q_SIGNALS:
Q_SIGNAL  void userInfoCardClicked();
Q_SIGNAL  void closeButtonClicked();
Q_SIGNAL  void navigationNodeClicked(ElaNavigationType::NavigationNodeType nodeType, QString nodeKey);
Q_SIGNAL  void customWidgetChanged();
Q_SIGNAL  void pageOpenInNewWindow(QString nodeKey);

};