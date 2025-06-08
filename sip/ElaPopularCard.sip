%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class ElaPopularCard : public QWidget
{
%TypeHeaderCode
#include "Def.h"
#include "ElaPopularCard.h"
%End

public: Q_SIGNAL void pBorderRadiusChanged();
  void setBorderRadius(int BorderRadius);
  int getBorderRadius() const;
public: Q_SIGNAL void pCardPixmapChanged();
  void setCardPixmap(QPixmap CardPixmap);
  QPixmap getCardPixmap() const;
public: Q_SIGNAL void pTitleChanged();
  void setTitle(QString Title);
  QString getTitle() const;
public: Q_SIGNAL void pSubTitleChanged();
  void setSubTitle(QString SubTitle);
  QString getSubTitle() const;
public: Q_SIGNAL void pInteractiveTipsChanged();
  void setInteractiveTips(QString InteractiveTips);
  QString getInteractiveTips() const;
public: Q_SIGNAL void pDetailedTextChanged();
  void setDetailedText(QString DetailedText);
  QString getDetailedText() const;
public: Q_SIGNAL void pCardButtontextChanged();
  void setCardButtontext(QString CardButtontext);
  QString getCardButtontext() const;
public: Q_SIGNAL void pCardFloatAreaChanged();
  void setCardFloatArea(QWidget* CardFloatArea);
  QWidget* getCardFloatArea() const;
public: Q_SIGNAL void pCardFloatPixmapChanged();
  void setCardFloatPixmap(QPixmap CardFloatPixmap);
  QPixmap getCardFloatPixmap() const;
public:
  explicit ElaPopularCard(QWidget * parent = nullptr);
  ~ElaPopularCard();

Q_SIGNALS:
Q_SIGNAL  void popularCardClicked();
Q_SIGNAL  void popularCardButtonClicked();

};