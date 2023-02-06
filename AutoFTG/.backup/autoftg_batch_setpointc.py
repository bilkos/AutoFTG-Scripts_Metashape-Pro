# AutoFTG - Scripts for Agisoft Metashape Pro
#
# Dialog: Batch Chunk Creator - Point Cloud Settings
# ----------------------------------------------------------------
from configparser import ConfigParser
from datetime import datetime
from os import path

import Metashape
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import AutoFTG.autoftg_batch as autoftg_batch
import AutoFTG.autoftg_main as autoftg_main
from AutoFTG.autoftg_batch import *
from AutoFTG.qtresources import *


class Ui_DialogPCloudSet(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"DialogPointCloud")
		self.resize(320, 240)
		self.setWindowTitle(u"Point Cloud Settings")
		icon = QIcon()
		icon.addFile(u":/icons/icons8-live-photos-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.gridLayoutWidget = QWidget(self)
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

		self.label_4.setBuddy(self.lineEdit)
		QWidget.setTabOrder(self.checkBox, self.checkBox_2)
		QWidget.setTabOrder(self.checkBox_2, self.checkBox_3)
		QWidget.setTabOrder(self.checkBox_3, self.lineEdit)
		QWidget.setTabOrder(self.lineEdit, self.pushButton_2)
		QWidget.setTabOrder(self.pushButton_2, self.pushButton)

		self.pushButton_2.clicked.connect(self.saveSetPCloud)
		self.pushButton.clicked.connect(self.reject)
		self.checkBox_3.toggled.connect(self.actionSetPointSampling.setVisible)

		self.setWindowTitle(u"Dialog")

		self.currentChkDef = autoftg_batch.chunkSet

		self.loadSetPCloud()

		self.exec_()



	def loadSetPCloud(self):
		self.pointcloud_source_data = autoftg_main.menuCfg.get(self.currentChkDef, "pointcloud_source_data")
		if self.pointcloud_source_data == "DepthMaps":
			self.source_data = Metashape.DataSource.DepthMapsData
		elif self.pointcloud_source_data == "Mesh":
			self.source_data = Metashape.DataSource.ModelData
		else:
			self.source_data = Metashape.DataSource.DepthMapsData

		pointcloud_point_colors = autoftg_main.menuCfg.getboolean(self.currentChkDef, "pointcloud_point_colors")
		self.checkBox.setChecked(pointcloud_point_colors)
		
		pointcloud_point_confidence = autoftg_main.menuCfg.getboolean(self.currentChkDef, "pointcloud_point_confidence")
		self.checkBox_2.setChecked(pointcloud_point_confidence)

		pointcloud_uniform_sam = autoftg_main.menuCfg.getboolean(self.currentChkDef, "pointcloud_uniform_sampling")
		self.checkBox_3.setChecked(pointcloud_uniform_sam)

		pointcloud_points_spacing = autoftg_main.menuCfg.get(self.currentChkDef, "pointcloud_points_spacing")
		self.lineEdit.setText(str(pointcloud_points_spacing))
		
		print("Point Cloud settings loaded...")


	def saveSetPCloud(self):
		autoftg_main.menuCfg.set(self.currentChkDef, "pointcloud_source_data", str(self.pointcloud_source_data))
		autoftg_main.menuCfg.set(self.currentChkDef, "pointcloud_point_colors", str(self.checkBox.isChecked))
		autoftg_main.menuCfg.set(self.currentChkDef, "pointcloud_point_confidence", str(self.checkBox_2.isChecked))
		autoftg_main.menuCfg.set(self.currentChkDef, "pointcloud_uniform_sampling", str(self.checkBox_3.isChecked))
		autoftg_main.menuCfg.set(self.currentChkDef, "pointcloud_points_spacing", str(self.lineEdit.text))
		with open(autoftg_main.menuCfgFilePath, 'w') as configfile:
			autoftg_main.menuCfg.write(configfile)

		print("Point Cloud settings saved...")

		self.accept()