# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiAddEditCam.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import qtresources_rc

class Ui_DialogAddEditCam(object):
    def setupUi(self, DialogAddEditCam):
        if not DialogAddEditCam.objectName():
            DialogAddEditCam.setObjectName(u"DialogAddEditCam")
        DialogAddEditCam.resize(480, 270)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogAddEditCam.sizePolicy().hasHeightForWidth())
        DialogAddEditCam.setSizePolicy(sizePolicy)
        DialogAddEditCam.setMinimumSize(QSize(480, 270))
        DialogAddEditCam.setMaximumSize(QSize(480, 270))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        DialogAddEditCam.setFont(font)
        DialogAddEditCam.setWindowTitle(u"Add/Edit Camera")
        icon = QIcon()
        icon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogAddEditCam.setWindowIcon(icon)
        self.gridLayoutWidget = QWidget(DialogAddEditCam)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 461, 251))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.gridLayoutWidget)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon1, u"Standard")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-slr-small-lens-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon2, u"DSLR")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-camera-on-tripod-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon3, u"Special")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon4, u"Drone")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons8-touchscreen-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon5, u"SmartPhone")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons8-gopro-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon6, u"SportCam")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setPlaceholderText(u"Camera name")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setMinimumSize(QSize(0, 28))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 28))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(8)
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setPlaceholderText(u"Choose calibration XML file...")

        self.horizontalLayout_2.addWidget(self.lineEdit_3)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setFont(font1)
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(u"Choose XML calibration file...")
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText(u"Browse")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons8-images-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setText(u"Camera Name")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(90, 30))
        self.pushButton.setText(u"Cancel")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setMaximumSize(QSize(90, 30))
        self.pushButton_2.setText(u"Save")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons8-save-all-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon9)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 2)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setFont(font)
        self.label.setText(u"Type")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(9)
        self.label_4.setFont(font3)
        self.label_4.setText(u"Resolution")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setText(u"Description")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 6, 0, 1, 2)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon10, u"Frame")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons8-video-wall-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon11, u"Fisheye")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons8-live-photos-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon12, u"Spherical")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon13, u"Cylindical")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons8-ios-application-placeholder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon14, u"RPC")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setText(u"Callibration")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setFont(font3)
        self.label_2.setText(u"Sub-Type")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(50, 16777215))
        self.lineEdit.setFont(font)
        self.lineEdit.setText(u"0")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setText(u"MP")

        self.horizontalLayout_3.addWidget(self.label_6)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setPlaceholderText(u"Description of camera (optional)")

        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton)

        self.retranslateUi(DialogAddEditCam)
        self.pushButton.clicked.connect(DialogAddEditCam.close)
    # setupUi

    def retranslateUi(self, DialogAddEditCam):


        pass
    # retranslateUi

