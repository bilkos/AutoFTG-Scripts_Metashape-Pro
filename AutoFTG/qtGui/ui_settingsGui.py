# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsGuiDcNeRr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import qtresources_rc

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        if not settingsDialog.objectName():
            settingsDialog.setObjectName(u"settingsDialog")
        settingsDialog.resize(400, 245)
        settingsDialog.setWindowTitle(u"AutoFTG Settings")
        self.buttonBox = QDialogButtonBox(settingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(230, 210, 161, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox = QGroupBox(settingsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 30, 381, 51))
        self.lineProjFolder = QLineEdit(self.groupBox)
        self.lineProjFolder.setObjectName(u"lineProjFolder")
        self.lineProjFolder.setGeometry(QRect(10, 20, 331, 20))
        self.lineProjFolder.setText(u"settings.folderProject")
        self.btnProjFolder = QPushButton(self.groupBox)
        self.btnProjFolder.setObjectName(u"btnProjFolder")
        self.btnProjFolder.setGeometry(QRect(340, 20, 41, 23))
        icon = QIcon()
        icon.addFile(u":/AutoFTG/openfolder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnProjFolder.setIcon(icon)
        self.btnProjFolder.setIconSize(QSize(24, 24))
        self.btnProjFolder.setFlat(True)
        self.groupBox_2 = QGroupBox(settingsDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 90, 381, 51))
        self.lineDataFolder = QLineEdit(self.groupBox_2)
        self.lineDataFolder.setObjectName(u"lineDataFolder")
        self.lineDataFolder.setGeometry(QRect(10, 20, 331, 20))
        self.lineDataFolder.setText(u"settings.folderData")
        self.btnDataFolder = QPushButton(self.groupBox_2)
        self.btnDataFolder.setObjectName(u"btnDataFolder")
        self.btnDataFolder.setGeometry(QRect(340, 20, 41, 23))
        icon1 = QIcon()
        icon1.addFile(u":/AutoFTG/picture-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDataFolder.setIcon(icon1)
        self.btnDataFolder.setIconSize(QSize(21, 21))
        self.btnDataFolder.setFlat(True)
        self.groupBox_3 = QGroupBox(settingsDialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 150, 381, 51))
        self.comboBoxCamera = QComboBox(self.groupBox_3)
        self.comboBoxCamera.addItem(u"settings.defaultCamera")
        self.comboBoxCamera.addItem(u"seee")
        self.comboBoxCamera.setObjectName(u"comboBoxCamera")
        self.comboBoxCamera.setGeometry(QRect(10, 20, 331, 22))
        self.comboBoxCamera.setCurrentText(u"settings.defaultCamera")
        self.comboBoxCamera.setPlaceholderText(u"")

        self.retranslateUi(settingsDialog)
        self.buttonBox.accepted.connect(settingsDialog.accept)
        self.buttonBox.rejected.connect(settingsDialog.reject)

        QMetaObject.connectSlotsByName(settingsDialog)
    # setupUi

    def retranslateUi(self, settingsDialog):
        self.groupBox.setTitle(QCoreApplication.translate("settingsDialog", u"Project Folder", None))
        self.btnProjFolder.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("settingsDialog", u"Data Folder", None))
        self.btnDataFolder.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("settingsDialog", u"Default Camera", None))

        pass
    # retranslateUi

