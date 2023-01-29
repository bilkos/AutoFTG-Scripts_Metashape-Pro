import os
import shutil
import sys
import time
import subprocess
from configparser import ConfigParser
from datetime import datetime
from os import path

import Metashape
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import AutoFTG.autoftg_main as autoftg_main
from AutoFTG.qtresources import *
import AutoFTG.autoftg_batch as autoftg_batch
from AutoFTG.autoftg_batch import *


class Ui_DialogSettingsMesh(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.currentChkDef = autoftg_batch.chunkSet
		self.setObjectName(u"DialogSettingsMesh")
		self.resize(350, 420)
		self.setWindowTitle(u"Settings: Mesh & Textures")
		icon = QIcon()
		icon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(icon)
		self.formLayoutWidget = QWidget(self)
		self.formLayoutWidget.setObjectName(u"formLayoutWidget")
		self.formLayoutWidget.setGeometry(QRect(0, 0, 351, 421))
		self.formLayout = QFormLayout(self.formLayoutWidget)
		self.formLayout.setObjectName(u"formLayout")
		self.formLayout.setContentsMargins(10, 5, 10, 10)
		self.label = QLabel(self.formLayoutWidget)
		self.label.setObjectName(u"label")
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setText(u"Mesh Options")

		self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label)

		self.label_2 = QLabel(self.formLayoutWidget)
		self.label_2.setObjectName(u"label_2")
		self.label_2.setText(u"Surface Type")

		self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

		self.cbMeshType = QComboBox(self.formLayoutWidget)
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons8-3d-48.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbMeshType.addItem(icon1, u"Arbitrary")
		icon2 = QIcon()
		icon2.addFile(u":/icons/icons8-national-park-48.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbMeshType.addItem(icon2, u"Height Field")
		self.cbMeshType.setObjectName(u"cbMeshType")
#if QT_CONFIG(tooltip)
		self.cbMeshType.setToolTip(u"Choose type of model reconstruction")
#endif // QT_CONFIG(tooltip)
		self.cbMeshType.setIconSize(QSize(20, 20))

		self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cbMeshType)

		self.label_3 = QLabel(self.formLayoutWidget)
		self.label_3.setObjectName(u"label_3")
		self.label_3.setText(u"Face Count")

		self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

		self.cbFaceCount = QComboBox(self.formLayoutWidget)
		icon3 = QIcon()
		icon3.addFile(u":/icons/icons8-signal-full-48.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbFaceCount.addItem(icon3, u"High")
		icon4 = QIcon()
		icon4.addFile(u":/icons/icons8-signal-48.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbFaceCount.addItem(icon4, u"Medium")
		icon5 = QIcon()
		icon5.addFile(u":/icons/icons8-low-connection-48.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbFaceCount.addItem(icon5, u"Low")
		icon6 = QIcon()
		icon6.addFile(u":/icons/icons8-rename-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbFaceCount.addItem(icon6, u"Custom")
		self.cbFaceCount.setObjectName(u"cbFaceCount")
#if QT_CONFIG(tooltip)
		self.cbFaceCount.setToolTip(u"Choose face count density")
#endif // QT_CONFIG(tooltip)
		self.cbFaceCount.setIconSize(QSize(20, 20))

		self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cbFaceCount)

		self.lineEditFaceCount = QLineEdit(self.formLayoutWidget)
		self.lineEditFaceCount.setObjectName(u"lineEditFaceCount")
		self.lineEditFaceCount.setEnabled(False)
		self.lineEditFaceCount.setPlaceholderText(u"Custom face count")

		self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEditFaceCount)

		self.checkBox_inter = QCheckBox(self.formLayoutWidget)
		self.checkBox_inter.setObjectName(u"checkBox_inter")
#if QT_CONFIG(tooltip)
		self.checkBox_inter.setToolTip(u"Enable interpolation")
#endif // QT_CONFIG(tooltip)
		self.checkBox_inter.setText(u"Interpolation")

		self.formLayout.setWidget(4, QFormLayout.FieldRole, self.checkBox_inter)

		self.checkBox_vcol = QCheckBox(self.formLayoutWidget)
		self.checkBox_vcol.setObjectName(u"checkBox_vcol")
#if QT_CONFIG(tooltip)
		self.checkBox_vcol.setToolTip(u"Calculate vertex colors")
#endif // QT_CONFIG(tooltip)
		self.checkBox_vcol.setText(u"Vertex Colors")
		self.checkBox_vcol.setChecked(True)

		self.formLayout.setWidget(5, QFormLayout.FieldRole, self.checkBox_vcol)

		self.checkBox_vcon = QCheckBox(self.formLayoutWidget)
		self.checkBox_vcon.setObjectName(u"checkBox_vcon")
#if QT_CONFIG(tooltip)
		self.checkBox_vcon.setToolTip(u"Calculate vertex confidence")
#endif // QT_CONFIG(tooltip)
		self.checkBox_vcon.setText(u"Vertex Confidence")

		self.formLayout.setWidget(6, QFormLayout.FieldRole, self.checkBox_vcon)

		self.line = QFrame(self.formLayoutWidget)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.line)

		self.groupBox_buildTex = QGroupBox(self.formLayoutWidget)
		self.groupBox_buildTex.setObjectName(u"groupBox_buildTex")
		self.groupBox_buildTex.setMinimumSize(QSize(0, 90))
		self.groupBox_buildTex.setTitle(u"Build Textures")
		self.groupBox_buildTex.setCheckable(True)
		self.gridLayoutWidget = QWidget(self.groupBox_buildTex)
		self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
		self.gridLayoutWidget.setGeometry(QRect(10, 30, 311, 52))
		self.gridLayout = QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setObjectName(u"gridLayout")
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.label_4 = QLabel(self.gridLayoutWidget)
		self.label_4.setObjectName(u"label_4")
		self.label_4.setText(u"Size")

		self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

		self.checkBox_texFillHoles = QCheckBox(self.gridLayoutWidget)
		self.checkBox_texFillHoles.setObjectName(u"checkBox_texFillHoles")
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.checkBox_texFillHoles.sizePolicy().hasHeightForWidth())
		self.checkBox_texFillHoles.setSizePolicy(sizePolicy)
		self.checkBox_texFillHoles.setText(u"Fill Holes")
		self.checkBox_texFillHoles.setChecked(True)

		self.gridLayout.addWidget(self.checkBox_texFillHoles, 0, 0, 1, 1)

		self.lineEdit_texSize = QLineEdit(self.gridLayoutWidget)
		self.lineEdit_texSize.setObjectName(u"lineEdit_texSize")
		sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
		sizePolicy1.setHorizontalStretch(0)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.lineEdit_texSize.sizePolicy().hasHeightForWidth())
		self.lineEdit_texSize.setSizePolicy(sizePolicy1)
		self.lineEdit_texSize.setMaximumSize(QSize(60, 16777215))
		self.lineEdit_texSize.setText(u"4096")

		self.gridLayout.addWidget(self.lineEdit_texSize, 1, 2, 1, 1)

		self.label_6 = QLabel(self.gridLayoutWidget)
		self.label_6.setObjectName(u"label_6")
		self.label_6.setText(u"Levels")

		self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)

		self.checkBox_texGhostFilt = QCheckBox(self.gridLayoutWidget)
		self.checkBox_texGhostFilt.setObjectName(u"checkBox_texGhostFilt")
		sizePolicy.setHeightForWidth(self.checkBox_texGhostFilt.sizePolicy().hasHeightForWidth())
		self.checkBox_texGhostFilt.setSizePolicy(sizePolicy)
		self.checkBox_texGhostFilt.setText(u"Ghosting Filter")
		self.checkBox_texGhostFilt.setChecked(True)

		self.gridLayout.addWidget(self.checkBox_texGhostFilt, 1, 0, 1, 1)

		self.lineEdit_texLevels = QLineEdit(self.gridLayoutWidget)
		self.lineEdit_texLevels.setObjectName(u"lineEdit_texLevels")
		sizePolicy1.setHeightForWidth(self.lineEdit_texLevels.sizePolicy().hasHeightForWidth())
		self.lineEdit_texLevels.setSizePolicy(sizePolicy1)
		self.lineEdit_texLevels.setMaximumSize(QSize(50, 16777215))
		self.lineEdit_texLevels.setText(u"1")
		self.lineEdit_texLevels.setMaxLength(2)

		self.gridLayout.addWidget(self.lineEdit_texLevels, 1, 4, 1, 1)

		self.label_7 = QLabel(self.gridLayoutWidget)
		self.label_7.setObjectName(u"label_7")
		sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
		sizePolicy2.setHorizontalStretch(0)
		sizePolicy2.setVerticalStretch(0)
		sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
		self.label_7.setSizePolicy(sizePolicy2)
		self.label_7.setText(u"x")

		self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)

		self.horizontalSpacer = QSpacerItem(20, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)


		self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.groupBox_buildTex)

		self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.formLayout.setItem(10, QFormLayout.FieldRole, self.verticalSpacer)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.pushButton_Save = QPushButton(self.formLayoutWidget)
		self.pushButton_Save.setObjectName(u"pushButton_Save")
		self.pushButton_Save.setText(u"Save")
		icon7 = QIcon()
		icon7.addFile(u":/icons/icons8-save-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_Save.setIcon(icon7)
		self.pushButton_Save.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton_Save)

		self.pushButton_Cancel = QPushButton(self.formLayoutWidget)
		self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")
		self.pushButton_Cancel.setText(u"Cancel")
		icon8 = QIcon()
		icon8.addFile(u":/icons/icons8-close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_Cancel.setIcon(icon8)
		self.pushButton_Cancel.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton_Cancel)


		self.formLayout.setLayout(12, QFormLayout.FieldRole, self.horizontalLayout)

		self.line_2 = QFrame(self.formLayoutWidget)
		self.line_2.setObjectName(u"line_2")
		self.line_2.setFrameShape(QFrame.HLine)
		self.line_2.setFrameShadow(QFrame.Sunken)

		self.formLayout.setWidget(11, QFormLayout.SpanningRole, self.line_2)

		self.label_5 = QLabel(self.formLayoutWidget)
		self.label_5.setObjectName(u"label_5")
		self.label_5.setFont(font)
		self.label_5.setText(u"Textures Options")

		self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.label_5)

		QWidget.setTabOrder(self.cbMeshType, self.cbFaceCount)
		QWidget.setTabOrder(self.cbFaceCount, self.lineEditFaceCount)
		QWidget.setTabOrder(self.lineEditFaceCount, self.checkBox_inter)
		QWidget.setTabOrder(self.checkBox_inter, self.checkBox_vcol)
		QWidget.setTabOrder(self.checkBox_vcol, self.checkBox_vcon)
		QWidget.setTabOrder(self.checkBox_vcon, self.groupBox_buildTex)
		QWidget.setTabOrder(self.groupBox_buildTex, self.checkBox_texFillHoles)
		QWidget.setTabOrder(self.checkBox_texFillHoles, self.checkBox_texGhostFilt)
		QWidget.setTabOrder(self.checkBox_texGhostFilt, self.lineEdit_texSize)
		QWidget.setTabOrder(self.lineEdit_texSize, self.lineEdit_texLevels)
		QWidget.setTabOrder(self.lineEdit_texLevels, self.pushButton_Save)
		QWidget.setTabOrder(self.pushButton_Save, self.pushButton_Cancel)

		self.pushButton_Cancel.clicked.connect(self.reject)
		self.pushButton_Save.clicked.connect(self.saveSettingsMesh)
		self.cbFaceCount.currentTextChanged.connect(self.customFaceCount)
		

		self.cbFaceCount.setCurrentIndex(1)
		self.pushButton_Save.setDefault(True)


		QMetaObject.connectSlotsByName(self)

		self.loadSettingsMesh()

		self.exec_()


	def customFaceCount(self):
		if self.cbFaceCount.currentText() == "Custom":
			self.lineEditFaceCount.setEnabled(True)
		else:
			self.lineEditFaceCount.setEnabled(False)
		

	def loadSettingsMesh(self):
		mesh_type = autoftg_main.menuCfg.get(self.currentChkDef, "mesh_type")
		mesh_face_count = autoftg_main.menuCfg.get(self.currentChkDef, "mesh_face_count")
		mesh_face_count_custom = autoftg_main.menuCfg.get(self.currentChkDef, "mesh_face_count_custom")
		mesh_interpolation = autoftg_main.menuCfg.getboolean(self.currentChkDef, "mesh_interpolation")
		mesh_vertex_color = autoftg_main.menuCfg.getboolean(self.currentChkDef, "mesh_vertex_color")
		mesh_vertex_confidence = autoftg_main.menuCfg.getboolean(self.currentChkDef, "mesh_vertex_confidence")
		texture_build = autoftg_main.menuCfg.getboolean(self.currentChkDef, "texture_build")
		texture_size = autoftg_main.menuCfg.get(self.currentChkDef, "texture_size")
		texture_levels = autoftg_main.menuCfg.get(self.currentChkDef, "texture_levels")
		texture_fill = autoftg_main.menuCfg.getboolean(self.currentChkDef, "texture_fill")
		texture_ghosting = autoftg_main.menuCfg.getboolean(self.currentChkDef, "texture_ghosting")
		
		self.cbMeshType.setCurrentText(mesh_type)
		self.cbFaceCount.setCurrentText(mesh_face_count)
		self.lineEditFaceCount.setText(mesh_face_count_custom)
		self.checkBox_inter.setChecked(mesh_interpolation)
		self.checkBox_vcol.setChecked(mesh_vertex_color)
		self.checkBox_vcon.setChecked(mesh_vertex_confidence)
		self.groupBox_buildTex.setChecked(texture_build)
		self.checkBox_texFillHoles.setChecked(texture_fill)
		self.checkBox_texGhostFilt.setChecked(texture_ghosting)
		self.lineEdit_texSize.setText(texture_size)
		self.lineEdit_texLevels.setText(texture_levels)		
		
		print("Mesh and textures settings loaded...")


	def saveSettingsMesh(self):
		mesh_type = self.cbMeshType.currentText()
		mesh_face_count = str(self.cbFaceCount.currentIndex())
		mesh_face_count_custom = self.lineEditFaceCount.text()
		mesh_interpolation = self.checkBox_inter.isChecked()
		mesh_vertex_color = self.checkBox_vcol.isChecked()
		mesh_vertex_confidence = self.checkBox_vcon.isChecked()
		texture_build = self.groupBox_buildTex.isChecked()
		texture_size = self.lineEdit_texSize.text()
		texture_levels = self.lineEdit_texLevels.text()
		texture_fill = self.checkBox_texFillHoles.isChecked()
		texture_ghosting = self.checkBox_texGhostFilt.isChecked()

		autoftg_main.menuCfg.set(self.currentChkDef, "mesh_type", mesh_type)
		autoftg_main.menuCfg.set(self.currentChkDef, "mesh_face_count", mesh_face_count)
		autoftg_main.menuCfg.set(self.currentChkDef, "mesh_face_count_custom", mesh_face_count_custom)
		autoftg_main.menuCfg.set(self.currentChkDef, "mesh_interpolation", str(mesh_interpolation))
		autoftg_main.menuCfg.set(self.currentChkDef, "mesh_vertex_color", str(mesh_vertex_color))
		autoftg_main.menuCfg.set(self.currentChkDef, "mesh_vertex_confidence", str(mesh_vertex_confidence))
		autoftg_main.menuCfg.set(self.currentChkDef, "texture_build", str(texture_build))
		autoftg_main.menuCfg.set(self.currentChkDef, "texture_size", texture_size)
		autoftg_main.menuCfg.set(self.currentChkDef, "texture_levels", texture_levels)
		autoftg_main.menuCfg.set(self.currentChkDef, "texture_fill", str(texture_fill))
		autoftg_main.menuCfg.set(self.currentChkDef, "texture_ghosting", str(texture_ghosting))
		
		with open(autoftg_main.menuCfgFilePath, 'w') as configfile:
			autoftg_main.menuCfg.write(configfile)

		print("Mesh and textures settings saved...")
		
		self.accept()

