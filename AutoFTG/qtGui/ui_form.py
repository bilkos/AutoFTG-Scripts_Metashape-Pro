# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateTimeEdit,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QToolBar, QTreeWidget, QTreeWidgetItem, QWidget)
import qtresources_rc
import qtresources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 846)
        self.actionNova = QAction(MainWindow)
        self.actionNova.setObjectName(u"actionNova")
        icon = QIcon()
        icon.addFile(u":/icons/icons8-add-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNova.setIcon(icon)
        self.actionNastavitve = QAction(MainWindow)
        self.actionNastavitve.setObjectName(u"actionNastavitve")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-tools-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNastavitve.setIcon(icon1)
        self.actionNastavitve.setAutoRepeat(False)
        self.actionKopiraj_Podatke = QAction(MainWindow)
        self.actionKopiraj_Podatke.setObjectName(u"actionKopiraj_Podatke")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-downloading-updates-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionKopiraj_Podatke.setIcon(icon2)
        self.actionIzhod = QAction(MainWindow)
        self.actionIzhod.setObjectName(u"actionIzhod")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionIzhod.setIcon(icon3)
        self.actionKamere = QAction(MainWindow)
        self.actionKamere.setObjectName(u"actionKamere")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-cameras-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionKamere.setIcon(icon4)
        self.actionKategorije_Pod_kategorije = QAction(MainWindow)
        self.actionKategorije_Pod_kategorije.setObjectName(u"actionKategorije_Pod_kategorije")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons8-product-documents-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionKategorije_Pod_kategorije.setIcon(icon5)
        self.actionSeznam_Oseb = QAction(MainWindow)
        self.actionSeznam_Oseb.setObjectName(u"actionSeznam_Oseb")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons8-user-menu-male-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSeznam_Oseb.setIcon(icon6)
        self.actionInstrumenti = QAction(MainWindow)
        self.actionInstrumenti.setObjectName(u"actionInstrumenti")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons8-land-surveying-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionInstrumenti.setIcon(icon7)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 751, 521))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QSize(20, 20))
        self.tab_meta = QWidget()
        self.tab_meta.setObjectName(u"tab_meta")
        self.formLayoutWidget = QWidget(self.tab_meta)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(5, 5, 546, 476))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setSpacing(5)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QSize(30, 30))
        self.label_4.setPixmap(QPixmap(u":/icons/icons8-clipboard-50.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        self.label_3.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_3)

        self.line = QFrame(self.formLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.line)

        self.datumInUraLabel = QLabel(self.formLayoutWidget)
        self.datumInUraLabel.setObjectName(u"datumInUraLabel")
        self.datumInUraLabel.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.datumInUraLabel)

        self.datumInUraDateTimeEdit = QDateTimeEdit(self.formLayoutWidget)
        self.datumInUraDateTimeEdit.setObjectName(u"datumInUraDateTimeEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.datumInUraDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.datumInUraDateTimeEdit.setSizePolicy(sizePolicy1)
        self.datumInUraDateTimeEdit.setFont(font)
        self.datumInUraDateTimeEdit.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.datumInUraDateTimeEdit.setCalendarPopup(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.datumInUraDateTimeEdit)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(self.formLayoutWidget)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons8-underground-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon9, "")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons8-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon10, "")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.comboBox.setFont(font2)
        self.comboBox.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.formLayoutWidget)
        icon11 = QIcon()
        icon11.addFile(u":/icons/template_kalota-zelena.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon11, "")
        icon12 = QIcon()
        icon12.addFile(u":/icons/template_stopnica-zelena.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon12, "")
        self.comboBox_2.addItem(icon12, "")
        icon13 = QIcon()
        icon13.addFile(u":/icons/template_kalota-modra.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon13, "")
        icon14 = QIcon()
        icon14.addFile(u":/icons/template_stopnica-modra.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon14, "")
        self.comboBox_2.addItem(icon14, "")
        icon15 = QIcon()
        icon15.addFile(u":/icons/template_kalota-oranzna.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon15, "")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy1.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy1)
        self.comboBox_2.setFont(font2)
        self.comboBox_2.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy2)
        self.lineEdit_3.setMaximumSize(QSize(200, 16777215))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox_3 = QComboBox(self.formLayoutWidget)
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons8-rename-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_3.addItem(icon16, "")
        self.comboBox_3.addItem(icon6, "")
        self.comboBox_3.addItem(icon6, "")
        self.comboBox_3.addItem(icon6, "")
        self.comboBox_3.addItem(icon6, "")
        self.comboBox_3.addItem(icon6, "")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy1.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy1)
        self.comboBox_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.comboBox_3)

        self.lineEdit_4 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy2.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy2)
        self.lineEdit_4.setMinimumSize(QSize(250, 0))
        self.lineEdit_4.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_10 = QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_10)

        self.comboBox_5 = QComboBox(self.formLayoutWidget)
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons8-camera-on-tripod-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_5.addItem(icon17, "")
        self.comboBox_5.addItem(icon9, "")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons8-slr-small-lens-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_5.addItem(icon18, "")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons8-slr-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_5.addItem(icon19, "")
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons8-touchscreen-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_5.addItem(icon20, "")
        self.comboBox_5.setObjectName(u"comboBox_5")
        sizePolicy1.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy1)
        self.comboBox_5.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.comboBox_5)

        self.label_11 = QLabel(self.formLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_11)

        self.comboBox_4 = QComboBox(self.formLayoutWidget)
        self.comboBox_4.addItem(icon7, "")
        self.comboBox_4.addItem(icon7, "")
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons8-satellite-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_4.addItem(icon21, "")
        self.comboBox_4.addItem(icon7, "")
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons8-satellite-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_4.addItem(icon22, "")
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy1.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy1)
        self.comboBox_4.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.comboBox_4)

        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_5 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(9, QFormLayout.FieldRole, self.verticalSpacer)

        icon23 = QIcon()
        icon23.addFile(u":/icons/icons8-clipboard-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_meta, icon23, "")
        self.tab_posnetki = QWidget()
        self.tab_posnetki.setObjectName(u"tab_posnetki")
        self.gridLayoutWidget = QWidget(self.tab_posnetki)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(5, 5, 736, 481))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.treeWidget = QTreeWidget(self.gridLayoutWidget)
        font3 = QFont()
        font3.setPointSize(8)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setFont(2, font3);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setFont(1, font3);
        __qtreewidgetitem.setText(0, u"Naziv");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        icon24 = QIcon()
        icon24.addFile(u":/icons/icons8-afternoon-50.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1.setIcon(0, icon24);
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem2.setIcon(0, icon24);
        self.treeWidget.setObjectName(u"treeWidget")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(11)
        self.treeWidget.setFont(font4)
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.treeWidget.setIconSize(QSize(20, 20))
        self.treeWidget.setIndentation(0)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.header().setMinimumSectionSize(150)
        self.treeWidget.header().setStretchLastSection(False)

        self.gridLayout.addWidget(self.treeWidget, 3, 0, 1, 2)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 0, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QSize(30, 30))
        self.label_7.setPixmap(QPixmap(u":/icons/icons8-camera-50.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setMinimumSize(QSize(350, 0))
        self.lineEdit_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(100, 0))
        icon25 = QIcon()
        icon25.addFile(u":/icons/icons8-images-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon25)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_posnetki, icon10, "")
        self.tab_markerji = QWidget()
        self.tab_markerji.setObjectName(u"tab_markerji")
        self.gridLayoutWidget_2 = QWidget(self.tab_markerji)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(5, 4, 736, 491))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.gridLayoutWidget_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font5 = QFont()
        font5.setFamilies([u"Consolas"])
        font5.setPointSize(11)
        font5.setBold(False)
        self.plainTextEdit.setFont(font5)
        self.plainTextEdit.setFrameShape(QFrame.Box)
        self.plainTextEdit.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.gridLayout_2.addWidget(self.plainTextEdit, 3, 0, 1, 2)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QSize(30, 30))
        self.label_12.setPixmap(QPixmap(u":/icons/icons8-my-location-50.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 0))
        icon26 = QIcon()
        icon26.addFile(u":/icons/icons8-move-to-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon26)
        self.pushButton.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)

        self.line_3 = QFrame(self.gridLayoutWidget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 1, 0, 1, 2)

        icon27 = QIcon()
        icon27.addFile(u":/icons/icons8-my-location-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_markerji, icon27, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 750, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuNastavitve = QMenu(self.menubar)
        self.menuNastavitve.setObjectName(u"menuNastavitve")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(Qt.TopToolBarArea)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuNastavitve.menuAction())
        self.menuFile.addAction(self.actionNova)
        self.menuFile.addAction(self.actionKopiraj_Podatke)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionIzhod)
        self.menuNastavitve.addAction(self.actionKategorije_Pod_kategorije)
        self.menuNastavitve.addAction(self.actionSeznam_Oseb)
        self.menuNastavitve.addAction(self.actionKamere)
        self.menuNastavitve.addAction(self.actionInstrumenti)
        self.menuNastavitve.addSeparator()
        self.menuNastavitve.addAction(self.actionNastavitve)
        self.toolBar.addAction(self.actionNova)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionKopiraj_Podatke)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.comboBox_3.currentTextChanged.connect(self.lineEdit_4.setText)
        self.comboBox.currentTextChanged.connect(self.lineEdit_5.setText)
        self.tabWidget.currentChanged.connect(self.statusbar.clearMessage)

        self.tabWidget.setCurrentIndex(1)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNova.setText(QCoreApplication.translate("MainWindow", u"Nova", None))
#if QT_CONFIG(tooltip)
        self.actionNova.setToolTip(QCoreApplication.translate("MainWindow", u"Nova", None))
#endif // QT_CONFIG(tooltip)
        self.actionNastavitve.setText(QCoreApplication.translate("MainWindow", u"Splo\u0161ne Nastavitve", None))
#if QT_CONFIG(shortcut)
        self.actionNastavitve.setShortcut(QCoreApplication.translate("MainWindow", u"N", None))
#endif // QT_CONFIG(shortcut)
        self.actionKopiraj_Podatke.setText(QCoreApplication.translate("MainWindow", u"Kopiraj Podatke", None))
        self.actionIzhod.setText(QCoreApplication.translate("MainWindow", u"Izhod", None))
        self.actionKamere.setText(QCoreApplication.translate("MainWindow", u"Kamere", None))
#if QT_CONFIG(shortcut)
        self.actionKamere.setShortcut(QCoreApplication.translate("MainWindow", u"C", None))
#endif // QT_CONFIG(shortcut)
        self.actionKategorije_Pod_kategorije.setText(QCoreApplication.translate("MainWindow", u"Kategorije Podatkov", None))
#if QT_CONFIG(shortcut)
        self.actionKategorije_Pod_kategorije.setShortcut(QCoreApplication.translate("MainWindow", u"K", None))
#endif // QT_CONFIG(shortcut)
        self.actionSeznam_Oseb.setText(QCoreApplication.translate("MainWindow", u"Seznam Oseb", None))
#if QT_CONFIG(shortcut)
        self.actionSeznam_Oseb.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.actionInstrumenti.setText(QCoreApplication.translate("MainWindow", u"Instrumenti", None))
#if QT_CONFIG(shortcut)
        self.actionInstrumenti.setShortcut(QCoreApplication.translate("MainWindow", u"I", None))
#endif // QT_CONFIG(shortcut)
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Meta Podatki", None))
        self.datumInUraLabel.setText(QCoreApplication.translate("MainWindow", u"Datum / Ura", None))
        self.datumInUraDateTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy HH:mm", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Snemanje", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Predor T8", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Aerosnemanje", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Drugo", None))

#if QT_CONFIG(statustip)
        self.comboBox.setStatusTip(QCoreApplication.translate("MainWindow", u"Kategorija podatkov (izbere za\u010detno mapo)...", None))
#endif // QT_CONFIG(statustip)
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"GC - KALOTA", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"GC - STOPNICA - IZKOP", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"GC - STOPNICA- BBET", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"SC - KALOTA", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"SC - STOPNICA - IZKOP", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"SC - STOPNICA- BBET", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"PRECNIK - 4", None))

#if QT_CONFIG(statustip)
        self.comboBox_2.setStatusTip(QCoreApplication.translate("MainWindow", u"Pod-kategorija za podatke...", None))
#endif // QT_CONFIG(statustip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Naziv Mape", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Naziv mape za podatke...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Meril", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Ni podatka", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Boris B.", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Gregor \u017d.", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Darko M.", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Dragan B.", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Slavi\u0161a M.", None))

        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ime osebe, ki je izvedla snemanje/meritve...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Kamera</p></body></html>", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"dibit kamera", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Dron", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"DSLR", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"Standard", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"Smartphone", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Instrument", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Leica TS16 1\" (Total Station)", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Leica MS50 1\" (Multi Station)", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Leica GS15 (GPS)", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"TPS", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"GPS", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Mapa za podatke", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Osnovna mapa za nove podatke...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_meta), QCoreApplication.translate("MainWindow", u"Meta podatki", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Velikost", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Ustvarjen", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"11,2 MB", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"16.01.\u200e2023 \u200f\u200e23:44:55", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"SAM_9088.jpg", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"10,5 MB", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"16.01.\u200e2023 \u200f\u200e23:44:46", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"SAM_9087.jpg", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.label_7.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Posnetki", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lokacija kjer so novi posnetki...", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Brskaj", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_posnetki), QCoreApplication.translate("MainWindow", u"Posnetki", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Markerji", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Delovi\u0161\u010de: T8 Koper\n"
"Podatki o izkopu: GC - Brizgani beton stopnice na staciona\u017ei: 24+081,6\n"
"Datum in \u010das slikanja: 16.01.2023. 20:00\n"
"Serijska \u0161t. tanjhimetra: ------\n"
"Ime in priimek: Slavi\u0161a M.\n"
"    \n"
"target 1,406920.499,47561.936,52.565\n"
"target 2,406920.265,47563.500,52.684\n"
"target 3,406919.880,47564.966,52.793\n"
"target 4,406919.537,47566.364,52.871\n"
"target 5,406922.064,47568.283,51.895\n"
"target 6,406924.877,47568.800,51.841\n"
"target 7,406927.629,47567.396,52.717\n"
"target 8,406927.718,47565.965,52.726\n"
"target 9,406927.795,47564.618,52.663\n"
"target 10,406927.990,47563.095,52.727    \n"
"", None))
        self.label_12.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Datoteka z koordinatami markerjev...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Brskaj", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_markerji), QCoreApplication.translate("MainWindow", u"Markerji", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Meni", None))
        self.menuNastavitve.setTitle(QCoreApplication.translate("MainWindow", u"Nastavitve", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

