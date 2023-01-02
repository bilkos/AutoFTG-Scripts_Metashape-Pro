/********************************************************************************
** Form generated from reading UI file 'uiCamEditor.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_UICAMEDITOR_H
#define UI_UICAMEDITOR_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_dialogCamGui
{
public:
    QAction *actionAction1;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout;
    QPushButton *btnRemoveCam;
    QPushButton *btnEditCam;
    QPushButton *btnAddNewCam;
    QPushButton *pushButton;
    QHBoxLayout *hLayout_MainBtn;
    QPushButton *btnMainCancel;
    QPushButton *btnMainSave;
    QTableWidget *tableWidgetCam;

    void setupUi(QDialog *dialogCamGui)
    {
        if (dialogCamGui->objectName().isEmpty())
            dialogCamGui->setObjectName("dialogCamGui");
        dialogCamGui->resize(460, 290);
        QFont font;
        font.setFamilies({QString::fromUtf8("Segoe UI")});
        font.setPointSize(9);
        dialogCamGui->setFont(font);
        dialogCamGui->setWindowTitle(QString::fromUtf8("Cameras Editor"));
        actionAction1 = new QAction(dialogCamGui);
        actionAction1->setObjectName("actionAction1");
        gridLayoutWidget = new QWidget(dialogCamGui);
        gridLayoutWidget->setObjectName("gridLayoutWidget");
        gridLayoutWidget->setGeometry(QRect(10, 10, 441, 271));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setObjectName("gridLayout");
        gridLayout->setContentsMargins(0, 0, 0, 0);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName("horizontalLayout");
        btnRemoveCam = new QPushButton(gridLayoutWidget);
        btnRemoveCam->setObjectName("btnRemoveCam");
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(btnRemoveCam->sizePolicy().hasHeightForWidth());
        btnRemoveCam->setSizePolicy(sizePolicy);
        btnRemoveCam->setText(QString::fromUtf8(" Remove"));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/AutoFTG/resources/icons8-clear-symbol-48.png"), QSize(), QIcon::Normal, QIcon::Off);
        btnRemoveCam->setIcon(icon);
        btnRemoveCam->setIconSize(QSize(20, 20));

        horizontalLayout->addWidget(btnRemoveCam);

        btnEditCam = new QPushButton(gridLayoutWidget);
        btnEditCam->setObjectName("btnEditCam");
        sizePolicy.setHeightForWidth(btnEditCam->sizePolicy().hasHeightForWidth());
        btnEditCam->setSizePolicy(sizePolicy);
        btnEditCam->setText(QString::fromUtf8(" Edit"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/AutoFTG/resources/pencil-writing_107734.png"), QSize(), QIcon::Normal, QIcon::Off);
        btnEditCam->setIcon(icon1);

        horizontalLayout->addWidget(btnEditCam);

        btnAddNewCam = new QPushButton(gridLayoutWidget);
        btnAddNewCam->setObjectName("btnAddNewCam");
        sizePolicy.setHeightForWidth(btnAddNewCam->sizePolicy().hasHeightForWidth());
        btnAddNewCam->setSizePolicy(sizePolicy);
        btnAddNewCam->setText(QString::fromUtf8(" Add"));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/AutoFTG/resources/CamImages.png"), QSize(), QIcon::Normal, QIcon::Off);
        btnAddNewCam->setIcon(icon2);
        btnAddNewCam->setIconSize(QSize(20, 20));

        horizontalLayout->addWidget(btnAddNewCam);

        pushButton = new QPushButton(gridLayoutWidget);
        pushButton->setObjectName("pushButton");
        pushButton->setText(QString::fromUtf8(" Default"));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/AutoFTG/resources/Pictures Library.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton->setIcon(icon3);
        pushButton->setIconSize(QSize(20, 20));

        horizontalLayout->addWidget(pushButton);


        gridLayout->addLayout(horizontalLayout, 1, 2, 1, 1);

        hLayout_MainBtn = new QHBoxLayout();
        hLayout_MainBtn->setObjectName("hLayout_MainBtn");
        btnMainCancel = new QPushButton(gridLayoutWidget);
        btnMainCancel->setObjectName("btnMainCancel");
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Minimum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(btnMainCancel->sizePolicy().hasHeightForWidth());
        btnMainCancel->setSizePolicy(sizePolicy1);
        btnMainCancel->setText(QString::fromUtf8("Cancel"));
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/AutoFTG/resources/icons8-close-30.png"), QSize(), QIcon::Normal, QIcon::Off);
        btnMainCancel->setIcon(icon4);

        hLayout_MainBtn->addWidget(btnMainCancel);

        btnMainSave = new QPushButton(gridLayoutWidget);
        btnMainSave->setObjectName("btnMainSave");
        sizePolicy1.setHeightForWidth(btnMainSave->sizePolicy().hasHeightForWidth());
        btnMainSave->setSizePolicy(sizePolicy1);
        btnMainSave->setText(QString::fromUtf8(" Save"));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/AutoFTG/resources/gui_save_icon_157040.png"), QSize(), QIcon::Normal, QIcon::Off);
        btnMainSave->setIcon(icon5);
        btnMainSave->setIconSize(QSize(16, 16));

        hLayout_MainBtn->addWidget(btnMainSave);


        gridLayout->addLayout(hLayout_MainBtn, 2, 2, 1, 1);

        tableWidgetCam = new QTableWidget(gridLayoutWidget);
        if (tableWidgetCam->columnCount() < 3)
            tableWidgetCam->setColumnCount(3);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        __qtablewidgetitem->setText(QString::fromUtf8("Camera Name"));
        tableWidgetCam->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        __qtablewidgetitem1->setText(QString::fromUtf8("Type"));
        tableWidgetCam->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        __qtablewidgetitem2->setText(QString::fromUtf8("Resolution"));
        tableWidgetCam->setHorizontalHeaderItem(2, __qtablewidgetitem2);
        if (tableWidgetCam->rowCount() < 3)
            tableWidgetCam->setRowCount(3);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        __qtablewidgetitem3->setText(QString::fromUtf8("1"));
        tableWidgetCam->setVerticalHeaderItem(0, __qtablewidgetitem3);
        QTableWidgetItem *__qtablewidgetitem4 = new QTableWidgetItem();
        __qtablewidgetitem4->setText(QString::fromUtf8("2"));
        tableWidgetCam->setVerticalHeaderItem(1, __qtablewidgetitem4);
        QTableWidgetItem *__qtablewidgetitem5 = new QTableWidgetItem();
        __qtablewidgetitem5->setText(QString::fromUtf8("3"));
        tableWidgetCam->setVerticalHeaderItem(2, __qtablewidgetitem5);
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/AutoFTG/resources/CAMScreenCap.png"), QSize(), QIcon::Normal, QIcon::Off);
        QFont font1;
        font1.setBold(false);
        font1.setItalic(true);
        QTableWidgetItem *__qtablewidgetitem6 = new QTableWidgetItem();
        __qtablewidgetitem6->setText(QString::fromUtf8("Default"));
        __qtablewidgetitem6->setFont(font1);
        __qtablewidgetitem6->setIcon(icon6);
        __qtablewidgetitem6->setFlags(Qt::ItemIsSelectable|Qt::ItemIsEnabled);
        tableWidgetCam->setItem(0, 0, __qtablewidgetitem6);
        QFont font2;
        font2.setItalic(true);
        QTableWidgetItem *__qtablewidgetitem7 = new QTableWidgetItem();
        __qtablewidgetitem7->setText(QString::fromUtf8("Frame"));
        __qtablewidgetitem7->setTextAlignment(Qt::AlignCenter);
        __qtablewidgetitem7->setFont(font2);
        __qtablewidgetitem7->setFlags(Qt::ItemIsSelectable|Qt::ItemIsEnabled);
        tableWidgetCam->setItem(0, 1, __qtablewidgetitem7);
        QTableWidgetItem *__qtablewidgetitem8 = new QTableWidgetItem();
        __qtablewidgetitem8->setText(QString::fromUtf8("0MP"));
        __qtablewidgetitem8->setTextAlignment(Qt::AlignCenter);
        __qtablewidgetitem8->setFont(font2);
        __qtablewidgetitem8->setFlags(Qt::ItemIsSelectable|Qt::ItemIsEnabled);
        tableWidgetCam->setItem(0, 2, __qtablewidgetitem8);
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/AutoFTG/resources/Mac FaceTime.png"), QSize(), QIcon::Normal, QIcon::Off);
        QBrush brush(QColor(255, 253, 219, 255));
        brush.setStyle(Qt::SolidPattern);
        QFont font3;
        font3.setBold(true);
        QTableWidgetItem *__qtablewidgetitem9 = new QTableWidgetItem();
        __qtablewidgetitem9->setText(QString::fromUtf8("NULL: Fisheye"));
        __qtablewidgetitem9->setFont(font3);
        __qtablewidgetitem9->setBackground(brush);
        __qtablewidgetitem9->setIcon(icon7);
        __qtablewidgetitem9->setFlags(Qt::ItemIsSelectable|Qt::ItemIsEditable|Qt::ItemIsEnabled);
        tableWidgetCam->setItem(1, 0, __qtablewidgetitem9);
        QTableWidgetItem *__qtablewidgetitem10 = new QTableWidgetItem();
        __qtablewidgetitem10->setText(QString::fromUtf8("Fisheye"));
        __qtablewidgetitem10->setTextAlignment(Qt::AlignCenter);
        __qtablewidgetitem10->setFont(font3);
        __qtablewidgetitem10->setBackground(brush);
        __qtablewidgetitem10->setFlags(Qt::ItemIsSelectable|Qt::ItemIsEnabled);
        tableWidgetCam->setItem(1, 1, __qtablewidgetitem10);
        QTableWidgetItem *__qtablewidgetitem11 = new QTableWidgetItem();
        __qtablewidgetitem11->setText(QString::fromUtf8("0MP"));
        __qtablewidgetitem11->setTextAlignment(Qt::AlignCenter);
        __qtablewidgetitem11->setFont(font3);
        __qtablewidgetitem11->setBackground(brush);
        __qtablewidgetitem11->setFlags(Qt::ItemIsSelectable|Qt::ItemIsEnabled);
        tableWidgetCam->setItem(1, 2, __qtablewidgetitem11);
        QTableWidgetItem *__qtablewidgetitem12 = new QTableWidgetItem();
        __qtablewidgetitem12->setFlags(Qt::ItemIsSelectable|Qt::ItemIsEditable|Qt::ItemIsEnabled);
        tableWidgetCam->setItem(2, 0, __qtablewidgetitem12);
        QTableWidgetItem *__qtablewidgetitem13 = new QTableWidgetItem();
        __qtablewidgetitem13->setTextAlignment(Qt::AlignCenter);
        __qtablewidgetitem13->setFlags(Qt::ItemIsSelectable|Qt::ItemIsEditable|Qt::ItemIsEnabled);
        tableWidgetCam->setItem(2, 1, __qtablewidgetitem13);
        QTableWidgetItem *__qtablewidgetitem14 = new QTableWidgetItem();
        __qtablewidgetitem14->setTextAlignment(Qt::AlignCenter);
        __qtablewidgetitem14->setFlags(Qt::ItemIsSelectable|Qt::ItemIsEditable|Qt::ItemIsEnabled);
        tableWidgetCam->setItem(2, 2, __qtablewidgetitem14);
        tableWidgetCam->setObjectName("tableWidgetCam");
        tableWidgetCam->setFrameShape(QFrame::Box);
        tableWidgetCam->setFrameShadow(QFrame::Plain);
        tableWidgetCam->setMidLineWidth(1);
        tableWidgetCam->setAlternatingRowColors(true);
        tableWidgetCam->setSelectionMode(QAbstractItemView::SingleSelection);
        tableWidgetCam->setSelectionBehavior(QAbstractItemView::SelectRows);
        tableWidgetCam->horizontalHeader()->setCascadingSectionResizes(true);
        tableWidgetCam->horizontalHeader()->setDefaultSectionSize(145);
        tableWidgetCam->verticalHeader()->setVisible(false);
        tableWidgetCam->verticalHeader()->setProperty("showSortIndicator", QVariant(true));

        gridLayout->addWidget(tableWidgetCam, 0, 2, 1, 1);


        retranslateUi(dialogCamGui);

        QMetaObject::connectSlotsByName(dialogCamGui);
    } // setupUi

    void retranslateUi(QDialog *dialogCamGui)
    {
        actionAction1->setText(QCoreApplication::translate("dialogCamGui", "Action1", nullptr));

        const bool __sortingEnabled = tableWidgetCam->isSortingEnabled();
        tableWidgetCam->setSortingEnabled(false);
        tableWidgetCam->setSortingEnabled(__sortingEnabled);

        (void)dialogCamGui;
    } // retranslateUi

};

namespace Ui {
    class dialogCamGui: public Ui_dialogCamGui {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_UICAMEDITOR_H
