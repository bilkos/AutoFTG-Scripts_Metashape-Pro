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


class Ui_DialogAlignPhotos(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"DialogAlignPhotos")
		self.resize(290, 460)
		self.setWindowTitle(u"Align Photos Settings")
		self.formLayoutWidget = QWidget(self)
		self.formLayoutWidget.setObjectName(u"formLayoutWidget")
		self.formLayoutWidget.setGeometry(QRect(0, 0, 291, 461))
		self.formLayout = QFormLayout(self.formLayoutWidget)
		self.formLayout.setObjectName(u"formLayout")
		self.formLayout.setContentsMargins(10, 10, 10, 10)
		self.label_4 = QLabel(self.formLayoutWidget)
		self.label_4.setObjectName(u"label_4")
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
		self.label_4.setSizePolicy(sizePolicy)
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.label_4.setFont(font)
		self.label_4.setText(u"Align Photos Settings")

		self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_4)

		self.line = QFrame(self.formLayoutWidget)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.line)

		self.label = QLabel(self.formLayoutWidget)
		self.label.setObjectName(u"label")
		font1 = QFont()
		font1.setFamily(u"Segoe UI")
		font1.setPointSize(11)
		self.label.setFont(font1)
		self.label.setText(u"Quality")

		self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

		self.comboBox_quality = QComboBox(self.formLayoutWidget)
		self.comboBox_quality.addItem(u"Highest")
		self.comboBox_quality.addItem(u"High")
		self.comboBox_quality.addItem(u"Medium")
		self.comboBox_quality.addItem(u"Low")
		self.comboBox_quality.addItem(u"Lowest")
		self.comboBox_quality.setObjectName(u"comboBox_quality")
		self.comboBox_quality.setCurrentText(u"Highest")

		self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_quality)

		self.line_2 = QFrame(self.formLayoutWidget)
		self.line_2.setObjectName(u"line_2")
		self.line_2.setFrameShape(QFrame.HLine)
		self.line_2.setFrameShadow(QFrame.Sunken)

		self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.line_2)

		self.label_2 = QLabel(self.formLayoutWidget)
		self.label_2.setObjectName(u"label_2")
		self.label_2.setFont(font1)
		self.label_2.setText(u"Pre-selection")

		self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

		self.checkBox_gen = QCheckBox(self.formLayoutWidget)
		self.checkBox_gen.setObjectName(u"checkBox_gen")
		self.checkBox_gen.setText(u"Generic")

		self.formLayout.setWidget(4, QFormLayout.FieldRole, self.checkBox_gen)

		self.checkBox_ref = QCheckBox(self.formLayoutWidget)
		self.checkBox_ref.setObjectName(u"checkBox_ref")
		self.checkBox_ref.setText(u"Reference")

		self.formLayout.setWidget(5, QFormLayout.FieldRole, self.checkBox_ref)

		self.comboBox_ref = QComboBox(self.formLayoutWidget)
		self.comboBox_ref.addItem(u"Source")
		self.comboBox_ref.addItem(u"Estimated")
		self.comboBox_ref.addItem(u"Sequential")
		self.comboBox_ref.setObjectName(u"comboBox_ref")
		self.comboBox_ref.setEnabled(False)
		self.comboBox_ref.setCurrentText(u"Source")

		self.formLayout.setWidget(6, QFormLayout.FieldRole, self.comboBox_ref)

		self.line_5 = QFrame(self.formLayoutWidget)
		self.line_5.setObjectName(u"line_5")
		self.line_5.setFrameShape(QFrame.HLine)
		self.line_5.setFrameShadow(QFrame.Sunken)

		self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.line_5)

		self.label_3 = QLabel(self.formLayoutWidget)
		self.label_3.setObjectName(u"label_3")
		self.label_3.setFont(font1)
		self.label_3.setText(u"Point Limit")

		self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_3)

		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.label_6 = QLabel(self.formLayoutWidget)
		self.label_6.setObjectName(u"label_6")
		sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
		self.label_6.setSizePolicy(sizePolicy)
		self.label_6.setText(u"Key")

		self.horizontalLayout_2.addWidget(self.label_6)

		self.label_5 = QLabel(self.formLayoutWidget)
		self.label_5.setObjectName(u"label_5")
		sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
		self.label_5.setSizePolicy(sizePolicy)
		self.label_5.setText(u"Tie")

		self.horizontalLayout_2.addWidget(self.label_5)


		self.formLayout.setLayout(8, QFormLayout.FieldRole, self.horizontalLayout_2)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.lineEdit_keypoints = QLineEdit(self.formLayoutWidget)
		self.lineEdit_keypoints.setObjectName(u"lineEdit_keypoints")
		self.lineEdit_keypoints.setPlaceholderText(u"40000")

		self.horizontalLayout.addWidget(self.lineEdit_keypoints)

		self.lineEdit_tiepoints = QLineEdit(self.formLayoutWidget)
		self.lineEdit_tiepoints.setObjectName(u"lineEdit_tiepoints")
		self.lineEdit_tiepoints.setPlaceholderText(u"10000")

		self.horizontalLayout.addWidget(self.lineEdit_tiepoints)


		self.formLayout.setLayout(9, QFormLayout.FieldRole, self.horizontalLayout)

		self.line_4 = QFrame(self.formLayoutWidget)
		self.line_4.setObjectName(u"line_4")
		self.line_4.setFrameShape(QFrame.HLine)
		self.line_4.setFrameShadow(QFrame.Sunken)

		self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.line_4)

		self.label_7 = QLabel(self.formLayoutWidget)
		self.label_7.setObjectName(u"label_7")
		self.label_7.setFont(font1)
		self.label_7.setText(u"Other")

		self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_7)

		self.checkBox_filtmask = QCheckBox(self.formLayoutWidget)
		self.checkBox_filtmask.setObjectName(u"checkBox_filtmask")
		self.checkBox_filtmask.setText(u"Filter Masked")

		self.formLayout.setWidget(11, QFormLayout.FieldRole, self.checkBox_filtmask)

		self.checkBox_masktie = QCheckBox(self.formLayoutWidget)
		self.checkBox_masktie.setObjectName(u"checkBox_masktie")
		self.checkBox_masktie.setText(u"Mask Tie Points")

		self.formLayout.setWidget(13, QFormLayout.FieldRole, self.checkBox_masktie)

		self.checkBox_keepkey = QCheckBox(self.formLayoutWidget)
		self.checkBox_keepkey.setObjectName(u"checkBox_keepkey")
		self.checkBox_keepkey.setText(u"Keep Key Points")

		self.formLayout.setWidget(14, QFormLayout.FieldRole, self.checkBox_keepkey)

		self.checkBox_guided = QCheckBox(self.formLayoutWidget)
		self.checkBox_guided.setObjectName(u"checkBox_guided")
		self.checkBox_guided.setText(u"Guided Matching")

		self.formLayout.setWidget(15, QFormLayout.FieldRole, self.checkBox_guided)

		self.checkBox_reset = QCheckBox(self.formLayoutWidget)
		self.checkBox_reset.setObjectName(u"checkBox_reset")
		self.checkBox_reset.setText(u"Reset Alignement")

		self.formLayout.setWidget(16, QFormLayout.FieldRole, self.checkBox_reset)

		self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.formLayout.setItem(17, QFormLayout.FieldRole, self.verticalSpacer)

		self.horizontalLayout_3 = QHBoxLayout()
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.pushButton_save = QPushButton(self.formLayoutWidget)
		self.pushButton_save.setObjectName(u"pushButton_save")
		self.pushButton_save.setText(u"Save")
		icon = QIcon()
		icon.addFile(u":/icons/icons8-save-as-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_save.setIcon(icon)
		self.pushButton_save.setIconSize(QSize(20, 20))

		self.horizontalLayout_3.addWidget(self.pushButton_save)

		self.pushButton_cancel = QPushButton(self.formLayoutWidget)
		self.pushButton_cancel.setObjectName(u"pushButton_cancel")
		self.pushButton_cancel.setText(u"Cancel")
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons8-close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_cancel.setIcon(icon1)
		self.pushButton_cancel.setIconSize(QSize(20, 20))

		self.horizontalLayout_3.addWidget(self.pushButton_cancel)


		self.formLayout.setLayout(18, QFormLayout.FieldRole, self.horizontalLayout_3)

		self.checkBox_filtsta = QCheckBox(self.formLayoutWidget)
		self.checkBox_filtsta.setObjectName(u"checkBox_filtsta")
		self.checkBox_filtsta.setText(u"Filter Stationary Points")

		self.formLayout.setWidget(12, QFormLayout.FieldRole, self.checkBox_filtsta)

		self.pushButton_cancel.clicked.connect(self.reject)
		self.pushButton_save.clicked.connect(self.saveSettingsAlign)

		self.currentChkDef = autoftg_batch.chunkSet

		self.loadSettingsAlign()


		self.exec_()

		
	def loadSettingsAlign(self):
		autoftg_main.menuCfg.get(self.currentChkDef, "mesh_depthmaps")
		align_quality = autoftg_main.menuCfg.get(self.currentChkDef, "align_quality")
		align_gen_presel = autoftg_main.menuCfg.getboolean(self.currentChkDef, "align_gen_presel")
		align_ref_presel = autoftg_main.menuCfg.getboolean(self.currentChkDef, "align_ref_presel")
		align_ref_presel_mode = autoftg_main.menuCfg.get(self.currentChkDef, "align_ref_presel_mode")
		align_key_limit = autoftg_main.menuCfg.getint(self.currentChkDef, "align_key_limit")
		align_tie_limit = autoftg_main.menuCfg.getint(self.currentChkDef, "align_tie_limit")
		align_filter_mask = autoftg_main.menuCfg.getboolean(self.currentChkDef, "align_filter_mask")
		align_mask_tiepoint = autoftg_main.menuCfg.getboolean(self.currentChkDef, "align_mask_tiepoint")
		align_filter_stationary = autoftg_main.menuCfg.getboolean(self.currentChkDef, "align_filter_stationary")
		align_keep_keypoints = autoftg_main.menuCfg.getboolean(self.currentChkDef, "align_keep_keypoints")
		align_guided_matching = autoftg_main.menuCfg.getboolean(self.currentChkDef, "align_guided_matching")
		align_reset_current = autoftg_main.menuCfg.getboolean(self.currentChkDef, "align_reset_current")

		self.comboBox_quality.setCurrentText(align_quality)
		self.checkBox_gen.setChecked(align_gen_presel)
		self.checkBox_ref.setChecked(align_ref_presel)
		self.comboBox_ref.setCurrentText(align_ref_presel_mode)
		self.lineEdit_keypoints.setText(str(align_key_limit))
		self.lineEdit_tiepoints.setText(str(align_tie_limit))
		self.checkBox_filtmask.setChecked(align_filter_mask)
		self.checkBox_masktie.setChecked(align_mask_tiepoint)
		self.checkBox_filtsta.setChecked(align_filter_stationary)
		self.checkBox_keepkey.setChecked(align_keep_keypoints)
		self.checkBox_guided.setChecked(align_guided_matching)
		self.checkBox_reset.setChecked(align_reset_current)

		print("Align Photos settings loaded...")


	def saveSettingsAlign(self):
		align_quality = self.comboBox_quality.currentText()
		align_gen_presel = self.checkBox_gen.isChecked()
		align_ref_presel = self.checkBox_ref.isChecked()
		align_ref_presel_mode = self.comboBox_ref.currentText()
		align_key_limit = self.lineEdit_keypoints.text()
		align_tie_limit = self.lineEdit_tiepoints.text()
		align_filter_mask = self.checkBox_filtmask.isChecked()
		align_mask_tiepoint = self.checkBox_masktie.isChecked()
		align_filter_stationary = self.checkBox_filtsta.isChecked()
		align_keep_keypoints = self.checkBox_keepkey.isChecked()
		align_guided_matching = self.checkBox_guided.isChecked()
		align_reset_current = self.checkBox_reset.isChecked()
		
		autoftg_main.menuCfg.set(self.currentChkDef, "align_quality", str(align_quality))
		autoftg_main.menuCfg.set(self.currentChkDef, "align_gen_presel", str(align_gen_presel))
		autoftg_main.menuCfg.set(self.currentChkDef, "align_ref_presel", str(align_ref_presel))
		autoftg_main.menuCfg.set(self.currentChkDef, "align_ref_presel_mode", str(align_ref_presel_mode))
		autoftg_main.menuCfg.set(self.currentChkDef, "align_key_limit", str(align_key_limit))
		autoftg_main.menuCfg.set(self.currentChkDef, "align_tie_limit", str(align_tie_limit))
		autoftg_main.menuCfg.set(self.currentChkDef, "align_filter_mask", str(align_filter_mask))
		autoftg_main.menuCfg.set(self.currentChkDef, "align_mask_tiepoint", str(align_mask_tiepoint))
		autoftg_main.menuCfg.set(self.currentChkDef, "align_filter_stationary", str(align_filter_stationary))
		autoftg_main.menuCfg.set(self.currentChkDef, "align_keep_keypoints", str(align_keep_keypoints))
		autoftg_main.menuCfg.set(self.currentChkDef, "align_guided_matching", str(align_guided_matching))
		autoftg_main.menuCfg.set(self.currentChkDef, "align_reset_current", str(align_reset_current))
		
		with open(autoftg_main.menuCfgFilePath, 'w') as configfile:
			autoftg_main.menuCfg.write(configfile)

		print("Align Photos settings saved...")
		
		self.accept()

