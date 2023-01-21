# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDefaulCamera.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import qtresources_rc

class Ui_dialogDefCam(object):
    def setupUi(self, dialogDefCam):
        if not dialogDefCam.objectName():
            dialogDefCam.setObjectName(u"dialogDefCam")
        dialogDefCam.resize(280, 280)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogDefCam.sizePolicy().hasHeightForWidth())
        dialogDefCam.setSizePolicy(sizePolicy)
        dialogDefCam.setMinimumSize(QSize(280, 280))
        dialogDefCam.setMaximumSize(QSize(280, 280))
        dialogDefCam.setWindowTitle(u"Choose Camera")
#if QT_CONFIG(tooltip)
        dialogDefCam.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        dialogDefCam.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        dialogDefCam.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        dialogDefCam.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        dialogDefCam.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.verticalLayoutWidget = QWidget(dialogDefCam)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 261, 261))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setText(u"Choose default camera")

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget(self.verticalLayoutWidget)
        icon = QIcon()
        icon.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setText(u"Frame");
        __qlistwidgetitem.setIcon(icon);
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-panorama-50.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setText(u"Fisheye");
        __qlistwidgetitem1.setIcon(icon1);
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setText(u"Conical");
        __qlistwidgetitem2.setIcon(icon2);
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-video-stabilization-50.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setText(u"Spherical");
        __qlistwidgetitem3.setIcon(icon3);
        icon4 = QIcon()
        icon4.addFile(u"../../icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem4.setText(u"Drone");
        __qlistwidgetitem4.setIcon(icon4);
        self.listWidget.setObjectName(u"listWidget")
        font1 = QFont()
        font1.setPointSize(10)
        self.listWidget.setFont(font1)
        self.listWidget.setFrameShape(QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QFrame.Plain)
        self.listWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.listWidget.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons8-done-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(dialogDefCam)

        self.listWidget.setCurrentRow(-1)

    # setupUi

    def retranslateUi(self, dialogDefCam):

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_2.setText(QCoreApplication.translate("dialogDefCam", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("dialogDefCam", u"Ok", None))
        pass
    # retranslateUi

