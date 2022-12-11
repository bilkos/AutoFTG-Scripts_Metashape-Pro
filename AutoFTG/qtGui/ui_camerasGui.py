# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camerasGuiTPYcId.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import qtresources_rc

class Ui_DialogCameras(object):
    def setupUi(self, DialogCameras):
        if not DialogCameras.objectName():
            DialogCameras.setObjectName(u"DialogCameras")
        DialogCameras.resize(400, 170)
        DialogCameras.setWindowTitle(u"Edit Cameras")
        self.formLayoutWidget = QWidget(DialogCameras)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 381, 151))
        self.gridLayout = QGridLayout(self.formLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btnBrowseXML = QPushButton(self.formLayoutWidget)
        self.btnBrowseXML.setObjectName(u"btnBrowseXML")
        self.btnBrowseXML.setText(u"Browse")
        icon = QIcon()
        icon.addFile(u":/AutoFTG/openfolder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBrowseXML.setIcon(icon)

        self.gridLayout.addWidget(self.btnBrowseXML, 4, 3, 1, 1)

        self.comboBoxType = QComboBox(self.formLayoutWidget)
        self.comboBoxType.addItem(u"Frame")
        self.comboBoxType.addItem(u"Fisheye")
        self.comboBoxType.addItem(u"Spherical")
        self.comboBoxType.addItem(u"Cylindrical")
        self.comboBoxType.setObjectName(u"comboBoxType")
        self.comboBoxType.setCurrentText(u"Frame")

        self.gridLayout.addWidget(self.comboBoxType, 2, 1, 1, 1)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"Name:")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.btnAddCam = QPushButton(self.formLayoutWidget)
        self.btnAddCam.setObjectName(u"btnAddCam")
        self.btnAddCam.setText(u"Add Camera")
        icon1 = QIcon()
        icon1.addFile(u":/AutoFTG/CamImages.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAddCam.setIcon(icon1)

        self.gridLayout.addWidget(self.btnAddCam, 6, 3, 1, 1)

        self.line_2 = QFrame(self.formLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 4)

        self.line = QFrame(self.formLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 4)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setText(u"Type:")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setText(u"File:")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.btnCloseCamDialog = QPushButton(self.formLayoutWidget)
        self.btnCloseCamDialog.setObjectName(u"btnCloseCamDialog")
        self.btnCloseCamDialog.setText(u"Close")
        icon2 = QIcon()
        icon2.addFile(u":/AutoFTG/icons8-close-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCloseCamDialog.setIcon(icon2)

        self.gridLayout.addWidget(self.btnCloseCamDialog, 6, 2, 1, 1)

        self.lineEditFile = QLineEdit(self.formLayoutWidget)
        self.lineEditFile.setObjectName(u"lineEditFile")
        self.lineEditFile.setInputMask(u"")
        self.lineEditFile.setText(u"")
        self.lineEditFile.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEditFile, 4, 1, 1, 2)

        self.lineEditName = QLineEdit(self.formLayoutWidget)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setInputMask(u"")
        self.lineEditName.setText(u"")
        self.lineEditName.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEditName, 3, 1, 1, 2)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setText(u"Add Camera Calibration")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 4)


        self.retranslateUi(DialogCameras)

        QMetaObject.connectSlotsByName(DialogCameras)
    # setupUi

    def retranslateUi(self, DialogCameras):

        pass
    # retranslateUi

