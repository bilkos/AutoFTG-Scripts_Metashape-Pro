# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diaAddNewChunkBatchSetPoint.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import qtresources_rc

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		if not Dialog.objectName():
			Dialog.setObjectName(u"Dialog")
		Dialog.resize(320, 240)
		self.actionSetPointSampling = QAction(Dialog)
		self.actionSetPointSampling.setObjectName(u"actionSetPointSampling")
		icon = QIcon()
		icon.addFile(u":/icons/icons8-live-photos-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.actionSetPointSampling.setIcon(icon)
		self.gridLayoutWidget = QWidget(Dialog)
		self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
		self.gridLayoutWidget.setGeometry(QRect(0, 0, 321, 243))
		self.gridLayout = QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setSpacing(5)
		self.gridLayout.setContentsMargins(10, 10, 10, 10)
		self.gridLayout.setObjectName(u"gridLayout")
		self.gridLayout.setHorizontalSpacing(10)
		self.gridLayout.setContentsMargins(10, 10, 10, 10)
		self.checkBox_2 = QCheckBox(self.gridLayoutWidget)
		self.checkBox_2.setObjectName(u"checkBox_2")
		self.checkBox_2.setLayoutDirection(Qt.RightToLeft)
		self.checkBox_2.setText(u"Calculate Confidence")

		self.gridLayout.addWidget(self.checkBox_2, 3, 0, 1, 1)

		self.line = QFrame(self.gridLayoutWidget)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

		self.label_3 = QLabel(self.gridLayoutWidget)
		self.label_3.setObjectName(u"label_3")
		self.label_3.setText(u"Regular")

		self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)

		self.lineEdit = QLineEdit(self.gridLayoutWidget)
		self.lineEdit.setObjectName(u"lineEdit")
		self.lineEdit.setPlaceholderText(u"0.05")
		self.lineEdit.setClearButtonEnabled(True)

		self.gridLayout.addWidget(self.lineEdit, 5, 1, 1, 1)

		self.checkBox_3 = QCheckBox(self.gridLayoutWidget)
		self.checkBox_3.setObjectName(u"checkBox_3")
		self.checkBox_3.setLayoutDirection(Qt.RightToLeft)
		self.checkBox_3.setText(u"Point Sampling")

		self.gridLayout.addWidget(self.checkBox_3, 4, 0, 1, 1)

		self.label = QLabel(self.gridLayoutWidget)
		self.label.setObjectName(u"label")
		self.label.setText(u"Enabled")

		self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

		self.label_4 = QLabel(self.gridLayoutWidget)
		self.label_4.setObjectName(u"label_4")
		self.label_4.setText(u"Point spacing (m)")
		self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

		self.label_2 = QLabel(self.gridLayoutWidget)
		self.label_2.setObjectName(u"label_2")
		self.label_2.setText(u"Disabled")

		self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

		self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.gridLayout.addItem(self.verticalSpacer, 6, 1, 1, 1)

		self.checkBox = QCheckBox(self.gridLayoutWidget)
		self.checkBox.setObjectName(u"checkBox")
		self.checkBox.setLayoutDirection(Qt.RightToLeft)
		self.checkBox.setText(u"Calculate Colors")
		self.checkBox.setChecked(True)

		self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)

		self.label_5 = QLabel(self.gridLayoutWidget)
		self.label_5.setObjectName(u"label_5")
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(14)
		self.label_5.setFont(font)
		self.label_5.setText(u"Point Cloud Settings")

		self.gridLayout.addWidget(self.label_5, 0, 0, 1, 2)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setSpacing(5)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.pushButton = QPushButton(self.gridLayoutWidget)
		self.pushButton.setObjectName(u"pushButton")
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
		self.pushButton.setSizePolicy(sizePolicy)
		self.pushButton.setText(u"Cancel")
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons8-close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton.setIcon(icon1)
		self.pushButton.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton)

		self.pushButton_2 = QPushButton(self.gridLayoutWidget)
		self.pushButton_2.setObjectName(u"pushButton_2")
		sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
		self.pushButton_2.setSizePolicy(sizePolicy)
		self.pushButton_2.setText(u"Save")
		icon2 = QIcon()
		icon2.addFile(u":/icons/icons8-save-as-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_2.setIcon(icon2)
		self.pushButton_2.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton_2)


		self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 2)

#if QT_CONFIG(shortcut)
		self.label_4.setBuddy(self.lineEdit)
#endif // QT_CONFIG(shortcut)
		QWidget.setTabOrder(self.checkBox, self.checkBox_2)
		QWidget.setTabOrder(self.checkBox_2, self.checkBox_3)
		QWidget.setTabOrder(self.checkBox_3, self.lineEdit)
		QWidget.setTabOrder(self.lineEdit, self.pushButton_2)
		QWidget.setTabOrder(self.pushButton_2, self.pushButton)

		self.retranslateUi(Dialog)
		self.pushButton_2.clicked.connect(Dialog.accept)
		self.pushButton.clicked.connect(Dialog.reject)
		self.checkBox_3.toggled.connect(self.actionSetPointSampling.setVisible)
	# setupUi

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
		self.actionSetPointSampling.setText(QCoreApplication.translate("Dialog", u"Enabled", None))
	# retranslateUi

