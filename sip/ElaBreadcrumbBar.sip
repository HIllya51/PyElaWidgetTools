%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaBreadcrumbBar : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaBreadcrumbBar.h"
%End

public: Q_SIGNAL void pTextPixelSizeChanged();
  void setTextPixelSize(int TextPixelSize);
  int getTextPixelSize() const;
public: Q_SIGNAL void pIsAutoRemoveChanged();
  void setIsAutoRemove(bool IsAutoRemove);
  bool getIsAutoRemove() const;
public:
  explicit ElaBreadcrumbBar(QWidget * parent = nullptr);
  ~ElaBreadcrumbBar();
  void setBreadcrumbList(QStringList breadcrumbList) ;
  QStringList appendBreadcrumb(QString breadcrumb) ;
  QStringList removeBreadcrumb(QString breadcrumb) ;
  int getBreadcrumbListCount() const ;
  QStringList getBreadcrumbList() const ;

Q_SIGNALS:
Q_SIGNAL  void breadcrumbClicked(QString breadcrumb, QStringList lastBreadcrumbList);

};