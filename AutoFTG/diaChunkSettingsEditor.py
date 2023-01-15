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
        DialogChunkSettings.resize(640, 290)
        DialogChunkSettings.setWindowTitle(u"Chunk Settings Editor")
        icon = QIcon()
        icon.addFile(u":/icons/icons8-stationery-50.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogChunkSettings.setWindowIcon(icon)
        self.gridLayoutWidget = QWidget(DialogChunkSettings)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 621, 271))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(5)
        self.label_def = QLabel(self.gridLayoutWidget)
        self.label_def.setObjectName(u"label_def")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_def.sizePolicy().hasHeightForWidth())
        self.label_def.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_def.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_def)

        self.label_nameicon = QLabel(self.gridLayoutWidget)
        self.label_nameicon.setObjectName(u"label_nameicon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_nameicon.sizePolicy().hasHeightForWidth())
        self.label_nameicon.setSizePolicy(sizePolicy1)
        self.label_nameicon.setText(u"Name/Icon")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_nameicon)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_name = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.horizontalLayout_4.addWidget(self.lineEdit_name)

        self.comboBox_icon = QComboBox(self.gridLayoutWidget)
        self.comboBox_icon.setObjectName(u"comboBox_icon")
        self.comboBox_icon.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.comboBox_icon)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_camera = QLabel(self.gridLayoutWidget)
        self.label_camera.setObjectName(u"label_camera")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_camera)

        self.comboBox_camera = QComboBox(self.gridLayoutWidget)
        self.comboBox_camera.setObjectName(u"comboBox_camera")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_camera.sizePolicy().hasHeightForWidth())
        self.comboBox_camera.setSizePolicy(sizePolicy2)
        self.comboBox_camera.setIconSize(QSize(20, 20))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_camera)

        self.label_wfolder = QLabel(self.gridLayoutWidget)
        self.label_wfolder.setObjectName(u"label_wfolder")
        self.label_wfolder.setText(u"Data Folder")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_wfolder)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_wfolder = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_wfolder.setObjectName(u"lineEdit_wfolder")

        self.horizontalLayout.addWidget(self.lineEdit_wfolder)

        self.pushButton_browsewf = QPushButton(self.gridLayoutWidget)
        self.pushButton_browsewf.setObjectName(u"pushButton_browsewf")
        sizePolicy2.setHeightForWidth(self.pushButton_browsewf.sizePolicy().hasHeightForWidth())
        self.pushButton_browsewf.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.pushButton_browsewf.setToolTip(u"<html><head/><body><p>Select location with working data for this definition.</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.pushButton_browsewf.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-opened-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_browsewf.setIcon(icon1)
        self.pushButton_browsewf.setIconSize(QSize(21, 21))

        self.horizontalLayout.addWidget(self.pushButton_browsewf)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_def_2 = QLabel(self.gridLayoutWidget)
        self.label_def_2.setObjectName(u"label_def_2")
        sizePolicy.setHeightForWidth(self.label_def_2.sizePolicy().hasHeightForWidth())
        self.label_def_2.setSizePolicy(sizePolicy)
        self.label_def_2.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.label_def_2)

        self.label_prefix = QLabel(self.gridLayoutWidget)
        self.label_prefix.setObjectName(u"label_prefix")
        self.label_prefix.setText(u"Prefix/Suffix")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_prefix)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_pre = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_pre.setObjectName(u"lineEdit_pre")
        self.lineEdit_pre.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit_pre)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(157, 158, 149);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.lineEdit_suf = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_suf.setObjectName(u"lineEdit_suf")

        self.horizontalLayout_5.addWidget(self.lineEdit_suf)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_sremove = QPushButton(self.gridLayoutWidget)
        self.pushButton_sremove.setObjectName(u"pushButton_sremove")
        self.pushButton_sremove.setEnabled(False)
#if QT_CONFIG(tooltip)
        self.pushButton_sremove.setToolTip(u"<html><head/><body><p>Remove currently selected chunk definition</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.pushButton_sremove.setText(u"Remove")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-remove-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_sremove.setIcon(icon2)
        self.pushButton_sremove.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButton_sremove)

        self.pushButton_save = QPushButton(self.gridLayoutWidget)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.pushButton_save.setToolTip(u"<html><head/><body><p>Save currently selected chunk definition</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.pushButton_save.setText(u"Update")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-save-as-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save.setIcon(icon3)
        self.pushButton_save.setIconSize(QSize(24, 24))
        self.pushButton_save.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.pushButton_save)

        self.pushButton_add = QPushButton(self.gridLayoutWidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy2.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.pushButton_add.setToolTip(u"<html><head/><body><p>Add new chunk settings definition</p><p>*Crates new chunk definition with current options.</p><p>**Definition Name must be unique.</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.pushButton_add.setText(u"Add New")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-add-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add.setIcon(icon4)
        self.pushButton_add.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButton_add)


        self.formLayout.setLayout(7, QFormLayout.SpanningRole, self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_close = QPushButton(self.gridLayoutWidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy2.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip(u"Close Chunk Settings Editor")
#endif // QT_CONFIG(tooltip)
        self.pushButton_close.setText(u"Close")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons8-enter-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon5)
        self.pushButton_close.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pushButton_close)


        self.formLayout.setLayout(9, QFormLayout.SpanningRole, self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(8, QFormLayout.SpanningRole, self.verticalSpacer)


        self.gridLayout.addLayout(self.formLayout, 0, 4, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons8-collapse-arrow-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons8-expand-arrow-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_2, 0, 3, 1, 1)

        self.listWidgetChunk = QListWidget(self.gridLayoutWidget)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons8-add-properties-50.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.listWidgetChunk)
        __qlistwidgetitem.setText(u"Default");
        __qlistwidgetitem.setIcon(icon8);
        icon9 = QIcon()
        icon9.addFile(u":/icons/template_kalota-modra.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidgetChunk)
        __qlistwidgetitem1.setText(u"T8 GC - KALOTA");
        __qlistwidgetitem1.setIcon(icon9);
        icon10 = QIcon()
        icon10.addFile(u":/icons/template_stopnica-modra.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.listWidgetChunk)
        __qlistwidgetitem2.setText(u"T8 GC - STOPNICA - IZKOP");
        __qlistwidgetitem2.setIcon(icon10);
        self.listWidgetChunk.setObjectName(u"listWidgetChunk")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.listWidgetChunk.sizePolicy().hasHeightForWidth())
        self.listWidgetChunk.setSizePolicy(sizePolicy3)
        self.listWidgetChunk.setTabKeyNavigation(True)
        self.listWidgetChunk.setAlternatingRowColors(True)
        self.listWidgetChunk.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidgetChunk.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.listWidgetChunk, 0, 0, 1, 1)


        self.retranslateUi(DialogChunkSettings)
        self.listWidgetChunk.currentTextChanged.connect(self.lineEdit_name.setText)
        self.listWidgetChunk.activated.connect(self.pushButton_save.toggle)
        self.listWidgetChunk.activated.connect(self.pushButton_sremove.toggle)
        self.pushButton_sremove.clicked.connect(self.listWidgetChunk.clearSelection)
        self.pushButton_sremove.clicked.connect(self.lineEdit_name.clear)
        self.pushButton_sremove.clicked.connect(self.comboBox_camera.clearEditText)
        self.pushButton_sremove.clicked.connect(self.lineEdit_wfolder.clear)
        self.pushButton_sremove.clicked.connect(self.lineEdit_pre.clear)
        self.pushButton_sremove.clicked.connect(self.lineEdit_suf.clear)
        self.pushButton_sremove.clicked.connect(self.pushButton_save.toggle)
    # setupUi

    def retranslateUi(self, DialogChunkSettings):
        self.label_def.setText(QCoreApplication.translate("DialogChunkSettings", u"Definition Settings", None))
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("DialogChunkSettings", u"Definition name shown in list...", None))
        self.label_camera.setText(QCoreApplication.translate("DialogChunkSettings", u"Camera", None))
        self.lineEdit_wfolder.setPlaceholderText(QCoreApplication.translate("DialogChunkSettings", u"Select folder...", None))
        self.label_def_2.setText(QCoreApplication.translate("DialogChunkSettings", u"Chunk Name Settings", None))
        self.lineEdit_pre.setPlaceholderText(QCoreApplication.translate("DialogChunkSettings", u"PREFIX_", None))
        self.label.setText(QCoreApplication.translate("DialogChunkSettings", u"<chunk name>", None))
        self.lineEdit_suf.setPlaceholderText(QCoreApplication.translate("DialogChunkSettings", u"_SUFFIX", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")

        __sortingEnabled = self.listWidgetChunk.isSortingEnabled()
        self.listWidgetChunk.setSortingEnabled(False)
        self.listWidgetChunk.setSortingEnabled(__sortingEnabled)

        pass
    # retranslateUi

