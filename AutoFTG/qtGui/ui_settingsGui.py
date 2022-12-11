# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsGuiXTiUdO.ui'
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
        settingsDialog.resize(510, 233)
        settingsDialog.setWindowTitle(u"AutoFTG Settings")
        self.gridLayoutWidget = QWidget(settingsDialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 489, 217))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.lineDataFolder = QLineEdit(self.gridLayoutWidget)
        self.lineDataFolder.setObjectName(u"lineDataFolder")
        self.lineDataFolder.setInputMask(u"")
        self.lineDataFolder.setText(u"settings.folderData")
        self.lineDataFolder.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineDataFolder, 4, 0, 1, 3)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.lineProjFolder = QLineEdit(self.gridLayoutWidget)
        self.lineProjFolder.setObjectName(u"lineProjFolder")
        self.lineProjFolder.setInputMask(u"")
        self.lineProjFolder.setText(u"settings.folderProject")
        self.lineProjFolder.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineProjFolder, 1, 0, 1, 3)

        self.comboBoxCamera = QComboBox(self.gridLayoutWidget)
        self.comboBoxCamera.setObjectName(u"comboBoxCamera")
        self.comboBoxCamera.setCurrentText(u"")

        self.gridLayout.addWidget(self.comboBoxCamera, 7, 0, 1, 2)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.btnDataFolder = QPushButton(self.gridLayoutWidget)
        self.btnDataFolder.setObjectName(u"btnDataFolder")
        self.btnDataFolder.setText(u"Browse")
        icon = QIcon()
        icon.addFile(u":/AutoFTG/openfolder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDataFolder.setIcon(icon)
        self.btnDataFolder.setIconSize(QSize(21, 21))
        self.btnDataFolder.setFlat(False)

        self.gridLayout.addWidget(self.btnDataFolder, 4, 3, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 8, 0, 1, 4)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.btnProjFolder = QPushButton(self.gridLayoutWidget)
        self.btnProjFolder.setObjectName(u"btnProjFolder")
        self.btnProjFolder.setText(u"Browse")
        self.btnProjFolder.setIcon(icon)
        self.btnProjFolder.setIconSize(QSize(21, 21))
        self.btnProjFolder.setFlat(False)

        self.gridLayout.addWidget(self.btnProjFolder, 1, 3, 1, 1)

        self.btnClose = QPushButton(self.gridLayoutWidget)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setText(u"Close")
        icon1 = QIcon()
        icon1.addFile(u":/AutoFTG/icons8-close-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClose.setIcon(icon1)

        self.gridLayout.addWidget(self.btnClose, 9, 2, 1, 1)

        self.btnSave = QPushButton(self.gridLayoutWidget)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setText(u"Save")
        icon2 = QIcon()
        icon2.addFile(u":/AutoFTG/DeviceManager.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSave.setIcon(icon2)

        self.gridLayout.addWidget(self.btnSave, 9, 3, 1, 1)

        self.line_7 = QFrame(self.gridLayoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_7, 2, 0, 1, 4)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 4)


        self.retranslateUi(settingsDialog)

        self.comboBoxCamera.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(settingsDialog)
    # setupUi

    def retranslateUi(self, settingsDialog):
        self.label_3.setText(QCoreApplication.translate("settingsDialog", u"Default Camera:", None))
        self.label.setText(QCoreApplication.translate("settingsDialog", u"Project Folder:", None))
        self.label_2.setText(QCoreApplication.translate("settingsDialog", u"Data Folder:", None))
        pass
    # retranslateUi

