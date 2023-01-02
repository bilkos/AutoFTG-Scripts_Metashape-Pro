/********************************************************************************
** Form generated from reading UI file 'uiCustomMenuSettings.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_UICUSTOMMENUSETTINGS_H
#define UI_UICUSTOMMENUSETTINGS_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QWidget *formLayoutWidget;
    QFormLayout *formLayout;
    QLabel *label_7;
    QLabel *label_5;
    QLineEdit *lineEdit_1;
    QLabel *label;
    QHBoxLayout *horizontalLayout_2;
    QLineEdit *lineEdit_0;
    QLineEdit *lineEdit_6;
    QFrame *line_3;
    QLabel *label_8;
    QLabel *label_2;
    QLineEdit *lineEdit_2;
    QLabel *label_6;
    QHBoxLayout *horizontalLayout_4;
    QLineEdit *lineEdit_3;
    QLineEdit *lineEdit_9;
    QFrame *line;
    QLabel *label_9;
    QLabel *label_3;
    QLineEdit *lineEdit_4;
    QLabel *label_4;
    QHBoxLayout *horizontalLayout_5;
    QLineEdit *lineEdit_5;
    QLineEdit *lineEdit_10;
    QFrame *line_2;
    QHBoxLayout *horizontalLayout;
    QPushButton *pushButtonCancel;
    QPushButton *pushButtonSave;
    QToolButton *toolButton;
    QToolButton *toolButton_2;
    QToolButton *toolButton_3;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName("Dialog");
        Dialog->resize(300, 340);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(Dialog->sizePolicy().hasHeightForWidth());
        Dialog->setSizePolicy(sizePolicy);
        Dialog->setMinimumSize(QSize(300, 340));
        Dialog->setMaximumSize(QSize(300, 340));
        QFont font;
        font.setFamilies({QString::fromUtf8("Segoe UI")});
        font.setPointSize(9);
        Dialog->setFont(font);
        Dialog->setWindowTitle(QString::fromUtf8("New Chunk : Custom Menu Settings"));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/AutoFTG/resources/AutoFTG-appicon.png"), QSize(), QIcon::Normal, QIcon::Off);
        Dialog->setWindowIcon(icon);
        formLayoutWidget = new QWidget(Dialog);
        formLayoutWidget->setObjectName("formLayoutWidget");
        formLayoutWidget->setGeometry(QRect(10, 10, 281, 311));
        formLayout = new QFormLayout(formLayoutWidget);
        formLayout->setSpacing(5);
        formLayout->setContentsMargins(10, 10, 10, 10);
        formLayout->setObjectName("formLayout");
        formLayout->setHorizontalSpacing(5);
        formLayout->setVerticalSpacing(5);
        formLayout->setContentsMargins(0, 0, 0, 0);
        label_7 = new QLabel(formLayoutWidget);
        label_7->setObjectName("label_7");
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(label_7->sizePolicy().hasHeightForWidth());
        label_7->setSizePolicy(sizePolicy1);
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Segoe UI")});
        font1.setPointSize(10);
        font1.setBold(true);
        label_7->setFont(font1);
        label_7->setText(QString::fromUtf8("Menu 1"));

        formLayout->setWidget(0, QFormLayout::LabelRole, label_7);

        label_5 = new QLabel(formLayoutWidget);
        label_5->setObjectName("label_5");
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(label_5->sizePolicy().hasHeightForWidth());
        label_5->setSizePolicy(sizePolicy2);
        label_5->setText(QString::fromUtf8("Menu Label"));

        formLayout->setWidget(1, QFormLayout::LabelRole, label_5);

        lineEdit_1 = new QLineEdit(formLayoutWidget);
        lineEdit_1->setObjectName("lineEdit_1");
        sizePolicy.setHeightForWidth(lineEdit_1->sizePolicy().hasHeightForWidth());
        lineEdit_1->setSizePolicy(sizePolicy);
        lineEdit_1->setMinimumSize(QSize(80, 25));
        lineEdit_1->setMaximumSize(QSize(180, 25));
        lineEdit_1->setFocusPolicy(Qt::TabFocus);
        lineEdit_1->setContextMenuPolicy(Qt::DefaultContextMenu);
        lineEdit_1->setText(QString::fromUtf8("KALOTA"));
        lineEdit_1->setCursorPosition(0);
        lineEdit_1->setPlaceholderText(QString::fromUtf8(""));
        lineEdit_1->setClearButtonEnabled(true);

        formLayout->setWidget(1, QFormLayout::FieldRole, lineEdit_1);

        label = new QLabel(formLayoutWidget);
        label->setObjectName("label");
        sizePolicy2.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy2);
        label->setText(QString::fromUtf8("Name Prefix/Suffix"));

        formLayout->setWidget(2, QFormLayout::LabelRole, label);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(5);
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        lineEdit_0 = new QLineEdit(formLayoutWidget);
        lineEdit_0->setObjectName("lineEdit_0");
        sizePolicy.setHeightForWidth(lineEdit_0->sizePolicy().hasHeightForWidth());
        lineEdit_0->setSizePolicy(sizePolicy);
        lineEdit_0->setMinimumSize(QSize(80, 25));
        lineEdit_0->setMaximumSize(QSize(150, 25));
        lineEdit_0->setFocusPolicy(Qt::TabFocus);
        lineEdit_0->setStyleSheet(QString::fromUtf8("background-color: rgb(220, 245, 255)"));
        lineEdit_0->setInputMask(QString::fromUtf8(""));
        lineEdit_0->setText(QString::fromUtf8(""));
        lineEdit_0->setCursorPosition(0);
        lineEdit_0->setPlaceholderText(QString::fromUtf8(""));
        lineEdit_0->setClearButtonEnabled(true);

        horizontalLayout_2->addWidget(lineEdit_0);

        lineEdit_6 = new QLineEdit(formLayoutWidget);
        lineEdit_6->setObjectName("lineEdit_6");
        sizePolicy.setHeightForWidth(lineEdit_6->sizePolicy().hasHeightForWidth());
        lineEdit_6->setSizePolicy(sizePolicy);
        lineEdit_6->setMinimumSize(QSize(80, 25));
        lineEdit_6->setMaximumSize(QSize(150, 25));
        lineEdit_6->setFocusPolicy(Qt::TabFocus);
        lineEdit_6->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 254, 238)"));
        lineEdit_6->setInputMask(QString::fromUtf8(""));
        lineEdit_6->setText(QString::fromUtf8(""));
        lineEdit_6->setCursorPosition(0);
        lineEdit_6->setPlaceholderText(QString::fromUtf8(""));
        lineEdit_6->setClearButtonEnabled(true);

        horizontalLayout_2->addWidget(lineEdit_6);


        formLayout->setLayout(2, QFormLayout::FieldRole, horizontalLayout_2);

        line_3 = new QFrame(formLayoutWidget);
        line_3->setObjectName("line_3");
        line_3->setFrameShape(QFrame::HLine);
        line_3->setFrameShadow(QFrame::Sunken);

        formLayout->setWidget(3, QFormLayout::SpanningRole, line_3);

        label_8 = new QLabel(formLayoutWidget);
        label_8->setObjectName("label_8");
        sizePolicy1.setHeightForWidth(label_8->sizePolicy().hasHeightForWidth());
        label_8->setSizePolicy(sizePolicy1);
        label_8->setFont(font1);
        label_8->setText(QString::fromUtf8("Menu 2"));

        formLayout->setWidget(4, QFormLayout::LabelRole, label_8);

        label_2 = new QLabel(formLayoutWidget);
        label_2->setObjectName("label_2");
        sizePolicy2.setHeightForWidth(label_2->sizePolicy().hasHeightForWidth());
        label_2->setSizePolicy(sizePolicy2);
        label_2->setText(QString::fromUtf8("Menu Label"));

        formLayout->setWidget(5, QFormLayout::LabelRole, label_2);

        lineEdit_2 = new QLineEdit(formLayoutWidget);
        lineEdit_2->setObjectName("lineEdit_2");
        sizePolicy.setHeightForWidth(lineEdit_2->sizePolicy().hasHeightForWidth());
        lineEdit_2->setSizePolicy(sizePolicy);
        lineEdit_2->setMinimumSize(QSize(80, 25));
        lineEdit_2->setMaximumSize(QSize(1780, 25));
        lineEdit_2->setFocusPolicy(Qt::TabFocus);
        lineEdit_2->setText(QString::fromUtf8("STOPNICA - IZKOP"));
        lineEdit_2->setCursorPosition(0);
        lineEdit_2->setPlaceholderText(QString::fromUtf8(""));
        lineEdit_2->setClearButtonEnabled(true);

        formLayout->setWidget(5, QFormLayout::FieldRole, lineEdit_2);

        label_6 = new QLabel(formLayoutWidget);
        label_6->setObjectName("label_6");
        sizePolicy2.setHeightForWidth(label_6->sizePolicy().hasHeightForWidth());
        label_6->setSizePolicy(sizePolicy2);
        label_6->setText(QString::fromUtf8("Name Prefix/Suffix"));

        formLayout->setWidget(6, QFormLayout::LabelRole, label_6);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(5);
        horizontalLayout_4->setObjectName("horizontalLayout_4");
        lineEdit_3 = new QLineEdit(formLayoutWidget);
        lineEdit_3->setObjectName("lineEdit_3");
        sizePolicy.setHeightForWidth(lineEdit_3->sizePolicy().hasHeightForWidth());
        lineEdit_3->setSizePolicy(sizePolicy);
        lineEdit_3->setMinimumSize(QSize(80, 25));
        lineEdit_3->setMaximumSize(QSize(150, 25));
        lineEdit_3->setFocusPolicy(Qt::TabFocus);
        lineEdit_3->setStyleSheet(QString::fromUtf8("background-color: rgb(220, 245, 255)"));
        lineEdit_3->setInputMask(QString::fromUtf8(""));
        lineEdit_3->setText(QString::fromUtf8(""));
        lineEdit_3->setCursorPosition(0);
        lineEdit_3->setPlaceholderText(QString::fromUtf8(""));
        lineEdit_3->setClearButtonEnabled(true);

        horizontalLayout_4->addWidget(lineEdit_3);

        lineEdit_9 = new QLineEdit(formLayoutWidget);
        lineEdit_9->setObjectName("lineEdit_9");
        sizePolicy.setHeightForWidth(lineEdit_9->sizePolicy().hasHeightForWidth());
        lineEdit_9->setSizePolicy(sizePolicy);
        lineEdit_9->setMinimumSize(QSize(80, 25));
        lineEdit_9->setMaximumSize(QSize(150, 25));
        lineEdit_9->setFocusPolicy(Qt::TabFocus);
        lineEdit_9->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 254, 238)"));
        lineEdit_9->setInputMask(QString::fromUtf8(""));
        lineEdit_9->setText(QString::fromUtf8("_IZ"));
        lineEdit_9->setCursorPosition(0);
        lineEdit_9->setPlaceholderText(QString::fromUtf8(""));
        lineEdit_9->setClearButtonEnabled(true);

        horizontalLayout_4->addWidget(lineEdit_9);


        formLayout->setLayout(6, QFormLayout::FieldRole, horizontalLayout_4);

        line = new QFrame(formLayoutWidget);
        line->setObjectName("line");
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        formLayout->setWidget(7, QFormLayout::SpanningRole, line);

        label_9 = new QLabel(formLayoutWidget);
        label_9->setObjectName("label_9");
        sizePolicy1.setHeightForWidth(label_9->sizePolicy().hasHeightForWidth());
        label_9->setSizePolicy(sizePolicy1);
        label_9->setFont(font1);
        label_9->setText(QString::fromUtf8("Menu 3"));

        formLayout->setWidget(8, QFormLayout::LabelRole, label_9);

        label_3 = new QLabel(formLayoutWidget);
        label_3->setObjectName("label_3");
        sizePolicy2.setHeightForWidth(label_3->sizePolicy().hasHeightForWidth());
        label_3->setSizePolicy(sizePolicy2);
        label_3->setText(QString::fromUtf8("Menu Label"));

        formLayout->setWidget(9, QFormLayout::LabelRole, label_3);

        lineEdit_4 = new QLineEdit(formLayoutWidget);
        lineEdit_4->setObjectName("lineEdit_4");
        sizePolicy.setHeightForWidth(lineEdit_4->sizePolicy().hasHeightForWidth());
        lineEdit_4->setSizePolicy(sizePolicy);
        lineEdit_4->setMinimumSize(QSize(80, 25));
        lineEdit_4->setMaximumSize(QSize(1780, 25));
        lineEdit_4->setFocusPolicy(Qt::TabFocus);
        lineEdit_4->setText(QString::fromUtf8("STOPNICA - B.BET."));
        lineEdit_4->setCursorPosition(0);
        lineEdit_4->setPlaceholderText(QString::fromUtf8(""));
        lineEdit_4->setClearButtonEnabled(true);

        formLayout->setWidget(9, QFormLayout::FieldRole, lineEdit_4);

        label_4 = new QLabel(formLayoutWidget);
        label_4->setObjectName("label_4");
        sizePolicy2.setHeightForWidth(label_4->sizePolicy().hasHeightForWidth());
        label_4->setSizePolicy(sizePolicy2);
        label_4->setText(QString::fromUtf8("Name Prefix/Suffix"));

        formLayout->setWidget(10, QFormLayout::LabelRole, label_4);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setSpacing(5);
        horizontalLayout_5->setObjectName("horizontalLayout_5");
        lineEdit_5 = new QLineEdit(formLayoutWidget);
        lineEdit_5->setObjectName("lineEdit_5");
        sizePolicy.setHeightForWidth(lineEdit_5->sizePolicy().hasHeightForWidth());
        lineEdit_5->setSizePolicy(sizePolicy);
        lineEdit_5->setMinimumSize(QSize(80, 25));
        lineEdit_5->setMaximumSize(QSize(150, 25));
        lineEdit_5->setFocusPolicy(Qt::TabFocus);
        lineEdit_5->setStyleSheet(QString::fromUtf8("background-color: rgb(220, 245, 255)"));
        lineEdit_5->setInputMask(QString::fromUtf8(""));
        lineEdit_5->setText(QString::fromUtf8(""));
        lineEdit_5->setCursorPosition(0);
        lineEdit_5->setPlaceholderText(QString::fromUtf8(""));
        lineEdit_5->setClearButtonEnabled(true);

        horizontalLayout_5->addWidget(lineEdit_5);

        lineEdit_10 = new QLineEdit(formLayoutWidget);
        lineEdit_10->setObjectName("lineEdit_10");
        sizePolicy.setHeightForWidth(lineEdit_10->sizePolicy().hasHeightForWidth());
        lineEdit_10->setSizePolicy(sizePolicy);
        lineEdit_10->setMinimumSize(QSize(80, 25));
        lineEdit_10->setMaximumSize(QSize(150, 25));
        lineEdit_10->setFocusPolicy(Qt::TabFocus);
        lineEdit_10->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 254, 238)"));
        lineEdit_10->setInputMask(QString::fromUtf8(""));
        lineEdit_10->setText(QString::fromUtf8("_ST_BB"));
        lineEdit_10->setCursorPosition(0);
        lineEdit_10->setPlaceholderText(QString::fromUtf8(""));
        lineEdit_10->setClearButtonEnabled(true);

        horizontalLayout_5->addWidget(lineEdit_10);


        formLayout->setLayout(10, QFormLayout::FieldRole, horizontalLayout_5);

        line_2 = new QFrame(formLayoutWidget);
        line_2->setObjectName("line_2");
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);

        formLayout->setWidget(11, QFormLayout::SpanningRole, line_2);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(5);
        horizontalLayout->setObjectName("horizontalLayout");
        pushButtonCancel = new QPushButton(formLayoutWidget);
        pushButtonCancel->setObjectName("pushButtonCancel");
        sizePolicy2.setHeightForWidth(pushButtonCancel->sizePolicy().hasHeightForWidth());
        pushButtonCancel->setSizePolicy(sizePolicy2);
        pushButtonCancel->setMinimumSize(QSize(0, 0));
        pushButtonCancel->setText(QString::fromUtf8("Cancel"));

        horizontalLayout->addWidget(pushButtonCancel);

        pushButtonSave = new QPushButton(formLayoutWidget);
        pushButtonSave->setObjectName("pushButtonSave");
        sizePolicy2.setHeightForWidth(pushButtonSave->sizePolicy().hasHeightForWidth());
        pushButtonSave->setSizePolicy(sizePolicy2);
        pushButtonSave->setMinimumSize(QSize(0, 0));
        pushButtonSave->setText(QString::fromUtf8("Save"));

        horizontalLayout->addWidget(pushButtonSave);


        formLayout->setLayout(12, QFormLayout::FieldRole, horizontalLayout);

        toolButton = new QToolButton(formLayoutWidget);
        toolButton->setObjectName("toolButton");
        toolButton->setEnabled(false);
        toolButton->setText(QString::fromUtf8("M1"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/AutoFTG/resources/kalota_m.png"), QSize(), QIcon::Normal, QIcon::Off);
        icon1.addFile(QString::fromUtf8(":/AutoFTG/resources/kalota_m.png"), QSize(), QIcon::Disabled, QIcon::Off);
        icon1.addFile(QString::fromUtf8(":/AutoFTG/resources/kalota_m.png"), QSize(), QIcon::Disabled, QIcon::On);
        toolButton->setIcon(icon1);
        toolButton->setIconSize(QSize(24, 24));
        toolButton->setToolButtonStyle(Qt::ToolButtonIconOnly);
        toolButton->setAutoRaise(true);
        toolButton->setArrowType(Qt::NoArrow);

        formLayout->setWidget(0, QFormLayout::FieldRole, toolButton);

        toolButton_2 = new QToolButton(formLayoutWidget);
        toolButton_2->setObjectName("toolButton_2");
        toolButton_2->setEnabled(false);
        toolButton_2->setText(QString::fromUtf8("M1"));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/AutoFTG/resources/stopnca_o.png"), QSize(), QIcon::Normal, QIcon::Off);
        icon2.addFile(QString::fromUtf8(":/AutoFTG/resources/stopnca_o.png"), QSize(), QIcon::Disabled, QIcon::Off);
        toolButton_2->setIcon(icon2);
        toolButton_2->setIconSize(QSize(24, 24));
        toolButton_2->setToolButtonStyle(Qt::ToolButtonIconOnly);
        toolButton_2->setAutoRaise(true);
        toolButton_2->setArrowType(Qt::NoArrow);

        formLayout->setWidget(4, QFormLayout::FieldRole, toolButton_2);

        toolButton_3 = new QToolButton(formLayoutWidget);
        toolButton_3->setObjectName("toolButton_3");
        toolButton_3->setEnabled(false);
        toolButton_3->setText(QString::fromUtf8("M1"));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/AutoFTG/resources/stopnca_s.png"), QSize(), QIcon::Normal, QIcon::Off);
        icon3.addFile(QString::fromUtf8(":/AutoFTG/resources/stopnca_s.png"), QSize(), QIcon::Disabled, QIcon::Off);
        toolButton_3->setIcon(icon3);
        toolButton_3->setIconSize(QSize(24, 24));
        toolButton_3->setToolButtonStyle(Qt::ToolButtonIconOnly);
        toolButton_3->setAutoRaise(true);
        toolButton_3->setArrowType(Qt::NoArrow);

        formLayout->setWidget(8, QFormLayout::FieldRole, toolButton_3);


        retranslateUi(Dialog);

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        (void)Dialog;
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_UICUSTOMMENUSETTINGS_H
