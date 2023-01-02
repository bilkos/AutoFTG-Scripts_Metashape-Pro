# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiDefaulCamera.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import qtresources

class Ui_dialogDefCam(QtWidgets.QDialog):
	def __init__(self, dialogDefCam):
		QtWidgets.QDialog.__init__(self, dialogDefCam)
		self.setObjectName(u"settingsDialog")
		self.resize(400, 170)
		self.setWindowTitle(u"AutoFTG Settings")
		
		icon = QIcon()
		icon.addFile(u":/AutoFTG/resources/openfolder.png", QSize(), QIcon.Normal, QIcon.Off)

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
#if QT_CONFIG(tooltip)
		self.label.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
		self.label.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
		self.label.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
		self.label.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
		self.label.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
		self.label.setText(u"Choose default camera")

		self.verticalLayout.addWidget(self.label)

		self.listWidget = QListWidget(self.verticalLayoutWidget)
		icon = QIcon()
		icon.addFile(u":/AutoFTG/resources/CamImages.png", QSize(), QIcon.Normal, QIcon.Off)
		__qlistwidgetitem = QListWidgetItem(self.listWidget)
		__qlistwidgetitem.setText(u"Item 1");
		__qlistwidgetitem.setIcon(icon);
		__qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
		__qlistwidgetitem1 = QListWidgetItem(self.listWidget)
		__qlistwidgetitem1.setText(u"Item 2");
		__qlistwidgetitem1.setIcon(icon);
		__qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
		icon1 = QIcon()
		icon1.addFile(u":/AutoFTG/resources/Pictures.png", QSize(), QIcon.Normal, QIcon.Off)
		brush = QBrush(QColor(253, 255, 211, 255))
		brush.setStyle(Qt.SolidPattern)
		font1 = QFont()
		font1.setBold(True)
		font1.setWeight(75)
		__qlistwidgetitem2 = QListWidgetItem(self.listWidget)
		__qlistwidgetitem2.setText(u"Item 3");
		__qlistwidgetitem2.setFont(font1);
		__qlistwidgetitem2.setBackground(brush);
		__qlistwidgetitem2.setIcon(icon1);
		__qlistwidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
		__qlistwidgetitem3 = QListWidgetItem(self.listWidget)
		__qlistwidgetitem3.setText(u"Item 4");
		__qlistwidgetitem3.setIcon(icon);
		__qlistwidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
		self.listWidget.setObjectName(u"listWidget")
		font2 = QFont()
		font2.setPointSize(10)
		self.listWidget.setFont(font2)
#if QT_CONFIG(tooltip)
		self.listWidget.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
		self.listWidget.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
		self.listWidget.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
		self.listWidget.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
		self.listWidget.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
		self.listWidget.setFrameShape(QFrame.StyledPanel)
		self.listWidget.setFrameShadow(QFrame.Plain)
		self.listWidget.setDefaultDropAction(Qt.IgnoreAction)
		self.listWidget.setAlternatingRowColors(True)
		self.listWidget.setIconSize(QSize(20, 20))

		self.verticalLayout.addWidget(self.listWidget)

		self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget)
		self.buttonBox.setObjectName(u"buttonBox")
		self.buttonBox.setOrientation(Qt.Horizontal)
		self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

		self.verticalLayout.addWidget(self.buttonBox)


		self.retranslateUi(dialogDefCam)
		self.buttonBox.accepted.connect(dialogDefCam.accept)
		self.buttonBox.rejected.connect(dialogDefCam.reject)

		self.listWidget.setCurrentRow(-1)

	# setupUi

	def retranslateUi(self, dialogDefCam):

		__sortingEnabled = self.listWidget.isSortingEnabled()
		self.listWidget.setSortingEnabled(False)
		self.listWidget.setSortingEnabled(__sortingEnabled)

		pass
	# retranslateUi

