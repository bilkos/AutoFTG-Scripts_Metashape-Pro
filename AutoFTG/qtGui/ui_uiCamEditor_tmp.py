# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiCamEditormizoWX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import qtresources_rc

class Ui_dialogCamGui(object):
    def setupUi(self, dialogCamGui):
        if not dialogCamGui.objectName():
            dialogCamGui.setObjectName(u"dialogCamGui")
        dialogCamGui.resize(340, 170)
        self.verticalLayoutWidget_2 = QWidget(dialogCamGui)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 321, 151))
        self.vLayout_Main = QVBoxLayout(self.verticalLayoutWidget_2)
        self.vLayout_Main.setObjectName(u"vLayout_Main")
        self.vLayout_Main.setContentsMargins(0, 0, 0, 0)
        self.hLayoutCamEdit = QHBoxLayout()
        self.hLayoutCamEdit.setObjectName(u"hLayoutCamEdit")
        self.listWidgetCam = QListWidget(self.verticalLayoutWidget_2)
        __qlistwidgetitem = QListWidgetItem(self.listWidgetCam)
        __qlistwidgetitem.setText(u"cam1");
        __qlistwidgetitem1 = QListWidgetItem(self.listWidgetCam)
        __qlistwidgetitem1.setText(u"cam2");
        self.listWidgetCam.setObjectName(u"listWidgetCam")

        self.hLayoutCamEdit.addWidget(self.listWidgetCam)

        self.vLayout_CamBtn = QVBoxLayout()
        self.vLayout_CamBtn.setObjectName(u"vLayout_CamBtn")
        self.btnAddNewCam = QPushButton(self.verticalLayoutWidget_2)
        self.btnAddNewCam.setObjectName(u"btnAddNewCam")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAddNewCam.sizePolicy().hasHeightForWidth())
        self.btnAddNewCam.setSizePolicy(sizePolicy)
        self.btnAddNewCam.setText(u"Add")
        icon = QIcon()
        icon.addFile(u":/AutoFTG/resources/CamImages.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAddNewCam.setIcon(icon)

        self.vLayout_CamBtn.addWidget(self.btnAddNewCam)

        self.btnEditCam = QPushButton(self.verticalLayoutWidget_2)
        self.btnEditCam.setObjectName(u"btnEditCam")
        sizePolicy.setHeightForWidth(self.btnEditCam.sizePolicy().hasHeightForWidth())
        self.btnEditCam.setSizePolicy(sizePolicy)
        self.btnEditCam.setText(u"Edit")
        icon1 = QIcon()
        icon1.addFile(u":/AutoFTG/resources/pencil-writing_107734.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEditCam.setIcon(icon1)

        self.vLayout_CamBtn.addWidget(self.btnEditCam)

        self.btnRemoveCam = QPushButton(self.verticalLayoutWidget_2)
        self.btnRemoveCam.setObjectName(u"btnRemoveCam")
        sizePolicy.setHeightForWidth(self.btnRemoveCam.sizePolicy().hasHeightForWidth())
        self.btnRemoveCam.setSizePolicy(sizePolicy)
        self.btnRemoveCam.setText(u"Remove")
        icon2 = QIcon()
        icon2.addFile(u":/AutoFTG/resources/icons8-close-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRemoveCam.setIcon(icon2)

        self.vLayout_CamBtn.addWidget(self.btnRemoveCam)


        self.hLayoutCamEdit.addLayout(self.vLayout_CamBtn)


        self.vLayout_Main.addLayout(self.hLayoutCamEdit)

        self.hLayout_MainBtn = QHBoxLayout()
        self.hLayout_MainBtn.setObjectName(u"hLayout_MainBtn")
        self.btnMainCancel = QPushButton(self.verticalLayoutWidget_2)
        self.btnMainCancel.setObjectName(u"btnMainCancel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnMainCancel.sizePolicy().hasHeightForWidth())
        self.btnMainCancel.setSizePolicy(sizePolicy1)
        self.btnMainCancel.setText(u"Cancel")

        self.hLayout_MainBtn.addWidget(self.btnMainCancel)

        self.btnMainSave = QPushButton(self.verticalLayoutWidget_2)
        self.btnMainSave.setObjectName(u"btnMainSave")
        sizePolicy1.setHeightForWidth(self.btnMainSave.sizePolicy().hasHeightForWidth())
        self.btnMainSave.setSizePolicy(sizePolicy1)
        self.btnMainSave.setText(u" Save")
        icon3 = QIcon()
        icon3.addFile(u":/AutoFTG/resources/Save-as_37111.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMainSave.setIcon(icon3)
        self.btnMainSave.setIconSize(QSize(12, 16))

        self.hLayout_MainBtn.addWidget(self.btnMainSave)


        self.vLayout_Main.addLayout(self.hLayout_MainBtn)


        self.retranslateUi(dialogCamGui)

        QMetaObject.connectSlotsByName(dialogCamGui)
    # setupUi

    def retranslateUi(self, dialogCamGui):
        dialogCamGui.setWindowTitle(QCoreApplication.translate("dialogCamGui", u"Cameras Editor", None))

        __sortingEnabled = self.listWidgetCam.isSortingEnabled()
        self.listWidgetCam.setSortingEnabled(False)
        self.listWidgetCam.setSortingEnabled(__sortingEnabled)

    # retranslateUi

