%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaNavigationBar : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaNavigationBar.h"
%End

public: Q_SIGNAL void pIsTransparentChanged();
  void setIsTransparent(bool IsTransparent);
  bool getIsTransparent() const;
public: Q_SIGNAL void pIsAllowPageOpenInNewWindowChanged();
  void setIsAllowPageOpenInNewWindow(bool IsAllowPageOpenInNewWindow);
  bool getIsAllowPageOpenInNewWindow() const;
public:
  explicit ElaNavigationBar(QWidget * parent = nullptr);
  ~ElaNavigationBar();
  void setUserInfoCardVisible(bool isVisible) ;
  void setUserInfoCardPixmap(QPixmap pix) ;
  void setUserInfoCardTitle(QString title) ;
  void setUserInfoCardSubTitle(QString subTitle) ;
  ElaNavigationType::NodeOperateReturnType addExpanderNode(QString expanderTitle, QString & expanderKey /Out/, ElaIconType::IconName awesome = ElaIconType::None) ;
  ElaNavigationType::NodeOperateReturnType addExpanderNode(QString expanderTitle, QString & expanderKey /Out/, QString targetExpanderKey, ElaIconType::IconName awesome = ElaIconType::None) ;
  ElaNavigationType::NodeOperateReturnType addPageNode(QString pageTitle, QWidget * page, ElaIconType::IconName awesome = ElaIconType::None) ;
  ElaNavigationType::NodeOperateReturnType addPageNode(QString pageTitle, QWidget * page, QString targetExpanderKey, ElaIconType::IconName awesome = ElaIconType::None) ;
  ElaNavigationType::NodeOperateReturnType addPageNode(QString pageTitle, QWidget * page, int keyPoints = 0, ElaIconType::IconName awesome = ElaIconType::None) /PyName=addPageNodeKeyPoints/;
  ElaNavigationType::NodeOperateReturnType addPageNode(QString pageTitle, QWidget * page, QString targetExpanderKey, int keyPoints = 0, ElaIconType::IconName awesome = ElaIconType::None) /PyName=addPageNodeKeyPoints/;
  ElaNavigationType::NodeOperateReturnType addFooterNode(QString footerTitle, QString & footerKey /Out/, int keyPoints = 0, ElaIconType::IconName awesome = ElaIconType::None) ;
  ElaNavigationType::NodeOperateReturnType addFooterNode(QString footerTitle, QWidget * page, QString & footerKey /Out/, int keyPoints = 0, ElaIconType::IconName awesome = ElaIconType::None) ;
  bool getNavigationNodeIsExpanded(QString expanderKey) const ;
  void expandNavigationNode(QString expanderKey) ;
  void collpaseNavigationNode(QString expanderKey) ;
  void removeNavigationNode(QString nodeKey) ;
  void setNodeKeyPoints(QString nodeKey, int keyPoints) ;
  int getNodeKeyPoints(QString nodeKey) const ;
  void navigation(QString pageKey, bool isLogClicked = true, bool isRouteBack = false) ;
  void setDisplayMode(ElaNavigationType::NavigationDisplayMode displayMode, bool isAnimation = true) ;
  int getPageOpenInNewWindowCount(QString nodeKey) const ;

Q_SIGNALS:
Q_SIGNAL  void pageOpenInNewWindow(QString nodeKey);
Q_SIGNAL  void userInfoCardClicked();
Q_SIGNAL  void navigationNodeClicked(ElaNavigationType::NavigationNodeType nodeType, QString nodeKey, bool isRouteBack);
Q_SIGNAL  void navigationNodeAdded(ElaNavigationType::NavigationNodeType nodeType, QString nodeKey, QWidget* page);
Q_SIGNAL  void navigationNodeRemoved(ElaNavigationType::NavigationNodeType nodeType, QString nodeKey);

};