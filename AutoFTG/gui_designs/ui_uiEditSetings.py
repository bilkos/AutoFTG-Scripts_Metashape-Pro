# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiEditSetings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import qtresources_rc

class Ui_DialogEditSettings(object):
    def setupUi(self, DialogEditSettings):
        if not DialogEditSettings.objectName():
            DialogEditSettings.setObjectName(u"DialogEditSettings")
        DialogEditSettings.resize(420, 170)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogEditSettings.sizePolicy().hasHeightForWidth())
        DialogEditSettings.setSizePolicy(sizePolicy)
        DialogEditSettings.setMinimumSize(QSize(420, 170))
        DialogEditSettings.setMaximumSize(QSize(420, 170))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(9)
        DialogEditSettings.setFont(font)
        DialogEditSettings.setWindowTitle(u"Data Folder")
        self.gridLayoutWidget = QWidget(DialogEditSettings)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 401, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(0, 28))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(7)
        self.lineEdit.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        self.label_3.setFont(font2)
        self.label_3.setText(u"Default Camera")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget)
        icon = QIcon()
        icon.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon, u"Frame")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-video-wall-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon1, u"Fisheye")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-live-photos-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon2, u"Spherical")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon3, u"Cylindical")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-ios-application-placeholder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon4, u"RPC")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy3)
        self.comboBox_2.setCurrentText(u"Frame")
        self.comboBox_2.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy3.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy3)
        self.pushButton_3.setText(u"Cancel")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon5)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)
        self.pushButton_2.setText(u"Ok")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons8-done-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon6)

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 3)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setFont(font2)
        self.label_2.setText(u"Data Folder")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)
        self.label.setText(u"Edit Settings")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        self.pushButton.setText(u"Browse")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons8-opened-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)


        self.retranslateUi(DialogEditSettings)
    # setupUi

    def retranslateUi(self, DialogEditSettings):

        pass
    # retranslateUi

