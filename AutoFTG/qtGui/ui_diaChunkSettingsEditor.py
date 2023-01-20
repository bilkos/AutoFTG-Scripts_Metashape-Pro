# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diaChunkSettingsEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import qtresources_rc

class Ui_DialogChunkSettings(object):
    def setupUi(self, DialogChunkSettings):
        if not DialogChunkSettings.objectName():
            DialogChunkSettings.setObjectName(u"DialogChunkSettings")
        DialogChunkSettings.resize(720, 360)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogChunkSettings.sizePolicy().hasHeightForWidth())
        DialogChunkSettings.setSizePolicy(sizePolicy)
        DialogChunkSettings.setMinimumSize(QSize(720, 360))
        DialogChunkSettings.setMaximumSize(QSize(720, 360))
        DialogChunkSettings.setWindowTitle(u"Chunk Settings Editor")
        icon = QIcon()
        icon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogChunkSettings.setWindowIcon(icon)
        self.gridLayoutWidget = QWidget(DialogChunkSettings)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 701, 341))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_menuSet_2 = QLabel(self.gridLayoutWidget)
        self.label_menuSet_2.setObjectName(u"label_menuSet_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_menuSet_2.sizePolicy().hasHeightForWidth())
        self.label_menuSet_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_menuSet_2.setFont(font)
        self.label_menuSet_2.setFrameShape(QFrame.StyledPanel)
        self.label_menuSet_2.setText(u"Chunk Definitions")
        self.label_menuSet_2.setIndent(5)

        self.gridLayout.addWidget(self.label_menuSet_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_close = QPushButton(self.gridLayoutWidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip(u"Close Chunk Settings Editor")
#endif // QT_CONFIG(tooltip)
        self.pushButton_close.setText(u"Close")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon1)
        self.pushButton_close.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pushButton_close)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 2, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(5)
        self.label_menuSet = QLabel(self.gridLayoutWidget)
        self.label_menuSet.setObjectName(u"label_menuSet")
        sizePolicy1.setHeightForWidth(self.label_menuSet.sizePolicy().hasHeightForWidth())
        self.label_menuSet.setSizePolicy(sizePolicy1)
        self.label_menuSet.setFont(font)
        self.label_menuSet.setFrameShape(QFrame.StyledPanel)
        self.label_menuSet.setText(u"Menu")
        self.label_menuSet.setIndent(5)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_menuSet)

        self.label_nameicon = QLabel(self.gridLayoutWidget)
        self.label_nameicon.setObjectName(u"label_nameicon")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_nameicon.sizePolicy().hasHeightForWidth())
        self.label_nameicon.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_nameicon.setFont(font1)
        self.label_nameicon.setText(u"Name")
        self.label_nameicon.setIndent(10)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_nameicon)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_name = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_name.setSizePolicy(sizePolicy4)
        self.lineEdit_name.setPlaceholderText(u"Name shown in list...")

        self.horizontalLayout_4.addWidget(self.lineEdit_name)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_nameicon_2 = QLabel(self.gridLayoutWidget)
        self.label_nameicon_2.setObjectName(u"label_nameicon_2")
        sizePolicy3.setHeightForWidth(self.label_nameicon_2.sizePolicy().hasHeightForWidth())
        self.label_nameicon_2.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        self.label_nameicon_2.setFont(font2)
        self.label_nameicon_2.setText(u"Icon")
        self.label_nameicon_2.setIndent(10)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_nameicon_2)

        self.comboBox_icon = QComboBox(self.gridLayoutWidget)
        self.comboBox_icon.setObjectName(u"comboBox_icon")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox_icon.sizePolicy().hasHeightForWidth())
        self.comboBox_icon.setSizePolicy(sizePolicy5)
        self.comboBox_icon.setMaximumSize(QSize(100, 16777215))
#if QT_CONFIG(tooltip)
        self.comboBox_icon.setToolTip(u"Choose icon to be used in list...")
#endif // QT_CONFIG(tooltip)
        self.comboBox_icon.setIconSize(QSize(24, 24))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_icon)

        self.label_chunkSet = QLabel(self.gridLayoutWidget)
        self.label_chunkSet.setObjectName(u"label_chunkSet")
        sizePolicy1.setHeightForWidth(self.label_chunkSet.sizePolicy().hasHeightForWidth())
        self.label_chunkSet.setSizePolicy(sizePolicy1)
        self.label_chunkSet.setFont(font)
        self.label_chunkSet.setFrameShape(QFrame.StyledPanel)
        self.label_chunkSet.setText(u"Chunk")
        self.label_chunkSet.setIndent(5)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.label_chunkSet)

        self.label_wfolder = QLabel(self.gridLayoutWidget)
        self.label_wfolder.setObjectName(u"label_wfolder")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_wfolder.setFont(font3)
        self.label_wfolder.setText(u"Data Folder")
        self.label_wfolder.setIndent(10)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_wfolder)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_browsewf = QPushButton(self.gridLayoutWidget)
        self.pushButton_browsewf.setObjectName(u"pushButton_browsewf")
        sizePolicy2.setHeightForWidth(self.pushButton_browsewf.sizePolicy().hasHeightForWidth())
        self.pushButton_browsewf.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.pushButton_browsewf.setToolTip(u"<html><head/><body><p>Select location with working data for this definition.</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.pushButton_browsewf.setText(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-opened-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_browsewf.setIcon(icon2)
        self.pushButton_browsewf.setIconSize(QSize(20, 20))
        self.pushButton_browsewf.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.pushButton_browsewf)

        self.lineEdit_wfolder = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_wfolder.setObjectName(u"lineEdit_wfolder")
        sizePolicy4.setHeightForWidth(self.lineEdit_wfolder.sizePolicy().hasHeightForWidth())
        self.lineEdit_wfolder.setSizePolicy(sizePolicy4)
        self.lineEdit_wfolder.setPlaceholderText(u"Folder path...")

        self.horizontalLayout.addWidget(self.lineEdit_wfolder)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_camera = QLabel(self.gridLayoutWidget)
        self.label_camera.setObjectName(u"label_camera")
        self.label_camera.setFont(font3)
        self.label_camera.setText(u"Camera")
        self.label_camera.setIndent(10)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_camera)

        self.comboBox_camera = QComboBox(self.gridLayoutWidget)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_camera.addItem(icon3, u"None")
        self.comboBox_camera.setObjectName(u"comboBox_camera")
        sizePolicy2.setHeightForWidth(self.comboBox_camera.sizePolicy().hasHeightForWidth())
        self.comboBox_camera.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.comboBox_camera.setToolTip(u"<html><head/><body><p>Choose default camera to be used for this definition.</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.comboBox_camera.setCurrentText(u"None")
        self.comboBox_camera.setIconSize(QSize(20, 20))
        self.comboBox_camera.setFrame(False)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.comboBox_camera)

        self.label_prefix = QLabel(self.gridLayoutWidget)
        self.label_prefix.setObjectName(u"label_prefix")
        self.label_prefix.setText(u"Prefix/Suffix")
        self.label_prefix.setIndent(10)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_prefix)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_pre = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_pre.setObjectName(u"lineEdit_pre")
        sizePolicy4.setHeightForWidth(self.lineEdit_pre.sizePolicy().hasHeightForWidth())
        self.lineEdit_pre.setSizePolicy(sizePolicy4)
        self.lineEdit_pre.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_pre.setPlaceholderText(u"PREFIX_")

        self.horizontalLayout_5.addWidget(self.lineEdit_pre)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(157, 158, 149);")
        self.label.setText(u"<folder name>")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.lineEdit_suf = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_suf.setObjectName(u"lineEdit_suf")
        sizePolicy4.setHeightForWidth(self.lineEdit_suf.sizePolicy().hasHeightForWidth())
        self.lineEdit_suf.setSizePolicy(sizePolicy4)
        self.lineEdit_suf.setPlaceholderText(u"_SUFFIX")

        self.horizontalLayout_5.addWidget(self.lineEdit_suf)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_save = QPushButton(self.gridLayoutWidget)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.pushButton_save.setToolTip(u"<html><head/><body><p>Save currently selected chunk definition</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.pushButton_save.setText(u"Save")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-save-as-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save.setIcon(icon4)
        self.pushButton_save.setIconSize(QSize(20, 20))
        self.pushButton_save.setAutoDefault(False)
        self.pushButton_save.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_save)

        self.pushButton_add = QPushButton(self.gridLayoutWidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy2.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.pushButton_add.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Add new</span><br/>Add new chunk settings definition</p><p>*Crates new chunk definition with current options.<br/>**Definition Name must be unique.</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.pushButton_add.setText(u"Add")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons8-add-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add.setIcon(icon5)
        self.pushButton_add.setIconSize(QSize(20, 20))
        self.pushButton_add.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.pushButton_add)


        self.formLayout.setLayout(7, QFormLayout.SpanningRole, self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(8, QFormLayout.FieldRole, self.verticalSpacer)


        self.gridLayout.addLayout(self.formLayout, 0, 2, 3, 1)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Raised)
        self.line_2.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_2, 0, 1, 3, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_sremove = QPushButton(self.gridLayoutWidget)
        self.pushButton_sremove.setObjectName(u"pushButton_sremove")
        self.pushButton_sremove.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.pushButton_sremove.sizePolicy().hasHeightForWidth())
        self.pushButton_sremove.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.pushButton_sremove.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Remove<br/></span>Remove selected definition</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.pushButton_sremove.setText(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons8-full-recycle-bin-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_sremove.setIcon(icon6)
        self.pushButton_sremove.setIconSize(QSize(20, 20))
        self.pushButton_sremove.setAutoDefault(False)
        self.pushButton_sremove.setFlat(True)

        self.horizontalLayout_6.addWidget(self.pushButton_sremove)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.pushButton_sedit = QPushButton(self.gridLayoutWidget)
        self.pushButton_sedit.setObjectName(u"pushButton_sedit")
        self.pushButton_sedit.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.pushButton_sedit.sizePolicy().hasHeightForWidth())
        self.pushButton_sedit.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.pushButton_sedit.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Edit</span><br/>Edit selected chunk definition</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.pushButton_sedit.setText(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons8-design-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_sedit.setIcon(icon7)
        self.pushButton_sedit.setIconSize(QSize(20, 20))
        self.pushButton_sedit.setAutoDefault(False)
        self.pushButton_sedit.setFlat(True)

        self.horizontalLayout_6.addWidget(self.pushButton_sedit)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.listWidgetChunkDefs = QListWidget(self.gridLayoutWidget)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons8-add-tab-50.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.listWidgetChunkDefs)
        __qlistwidgetitem.setText(u"Default");
        __qlistwidgetitem.setIcon(icon8);
        icon9 = QIcon()
        icon9.addFile(u":/icons/template_kalota-zelena.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidgetChunkDefs)
        __qlistwidgetitem1.setText(u"T8 GC - KALOTA");
        __qlistwidgetitem1.setIcon(icon9);
        icon10 = QIcon()
        icon10.addFile(u":/icons/template_stopnica-zelena.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.listWidgetChunkDefs)
        __qlistwidgetitem2.setText(u"T8 GC - STOPNICA - IZKOP");
        __qlistwidgetitem2.setIcon(icon10);
        icon11 = QIcon()
        icon11.addFile(u":/icons/template_kalota-oranzna.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidgetChunkDefs)
        __qlistwidgetitem3.setText(u"T8 PRECNIK-4");
        __qlistwidgetitem3.setIcon(icon11);
        icon12 = QIcon()
        icon12.addFile(u":/icons/template_kalota-modra.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem4 = QListWidgetItem(self.listWidgetChunkDefs)
        __qlistwidgetitem4.setText(u"T8 SC - KALOTA");
        __qlistwidgetitem4.setIcon(icon12);
        icon13 = QIcon()
        icon13.addFile(u":/icons/template_stopnica-modra.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem5 = QListWidgetItem(self.listWidgetChunkDefs)
        __qlistwidgetitem5.setText(u"T8 SC - STOPNICA - IZKOP");
        __qlistwidgetitem5.setIcon(icon13);
        self.listWidgetChunkDefs.setObjectName(u"listWidgetChunkDefs")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.listWidgetChunkDefs.sizePolicy().hasHeightForWidth())
        self.listWidgetChunkDefs.setSizePolicy(sizePolicy6)
        self.listWidgetChunkDefs.setFont(font3)
        self.listWidgetChunkDefs.setAutoScrollMargin(20)
        self.listWidgetChunkDefs.setAlternatingRowColors(False)
        self.listWidgetChunkDefs.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidgetChunkDefs.setIconSize(QSize(20, 20))
        self.listWidgetChunkDefs.setViewMode(QListView.ListMode)
        self.listWidgetChunkDefs.setUniformItemSizes(True)
        self.listWidgetChunkDefs.setSortingEnabled(True)

        self.gridLayout.addWidget(self.listWidgetChunkDefs, 1, 0, 1, 1)


        self.retranslateUi(DialogChunkSettings)
        self.pushButton_sremove.clicked.connect(self.lineEdit_name.clear)
        self.pushButton_sremove.clicked.connect(self.comboBox_camera.clearEditText)
        self.pushButton_sremove.clicked.connect(self.lineEdit_wfolder.clear)
        self.pushButton_sremove.clicked.connect(self.lineEdit_pre.clear)
        self.pushButton_sremove.clicked.connect(self.lineEdit_suf.clear)
        self.pushButton_sremove.clicked.connect(self.pushButton_save.toggle)
        self.pushButton_close.clicked.connect(DialogChunkSettings.reject)
        self.listWidgetChunkDefs.currentItemChanged.connect(self.pushButton_add.toggle)
        self.listWidgetChunkDefs.currentItemChanged.connect(self.pushButton_sedit.toggle)
        self.listWidgetChunkDefs.currentItemChanged.connect(self.pushButton_sremove.toggle)
        self.listWidgetChunkDefs.itemDoubleClicked.connect(self.pushButton_sedit.click)

        self.comboBox_camera.setCurrentIndex(0)

    # setupUi

    def retranslateUi(self, DialogChunkSettings):


        __sortingEnabled = self.listWidgetChunkDefs.isSortingEnabled()
        self.listWidgetChunkDefs.setSortingEnabled(False)
        self.listWidgetChunkDefs.setSortingEnabled(__sortingEnabled)

        pass
    # retranslateUi

