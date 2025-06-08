%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaSuggestBox : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaSuggestBox.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pCaseSensitivityChanged();
  void setCaseSensitivity(Qt::CaseSensitivity CaseSensitivity);
  Qt::CaseSensitivity getCaseSensitivity() const;
public:
  explicit ElaSuggestBox(QWidget * parent = nullptr);
  ~ElaSuggestBox();
  void setPlaceholderText(const QString & placeholderText) ;
  QString addSuggestion(const QString & suggestText, const QVariantMap & suggestData = {}) ;
  QString addSuggestion(ElaIconType::IconName icon, const QString & suggestText, const QVariantMap & suggestData = {}) ;
  void removeSuggestion(const QString & suggestKey) ;
  void removeSuggestion(int index) ;

Q_SIGNALS:
Q_SIGNAL  void suggestionClicked(QString suggestText, QVariantMap suggestData);

};