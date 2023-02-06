# Class for settings editing UI
import os
import pydoc
import shutil
import sys
import time
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


class Ui_DialogAddChunkQuick(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"DialogAddChunkQuick")
		self.resize(310, 155)
		appIcon = QIcon()
		appIcon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(appIcon)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)
		self.setMinimumSize(QSize(310, 155))
		self.setMaximumSize(QSize(310, 155))
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(9)
		self.setFont(font)
		self.setWindowTitle(u"Create New Chunk")
		self.verticalLayoutWidget = QWidget(self)
		self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
		self.verticalLayoutWidget.setGeometry(QRect(9, 9, 295, 141))
		self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setSpacing(5)
		self.verticalLayout.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.labelQuickAdd = QLabel(self.verticalLayoutWidget)
		self.labelQuickAdd.setObjectName(u"labelQuickAdd")
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.labelQuickAdd.sizePolicy().hasHeightForWidth())
		self.labelQuickAdd.setSizePolicy(sizePolicy)
		font1 = QFont()
		font1.setFamily(u"Segoe UI")
		font1.setPointSize(11)
		font1.setBold(True)
		font1.setWeight(75)
		self.labelQuickAdd.setFont(font1)
		self.labelQuickAdd.setText(u"Create New Chunk")

		self.verticalLayout.addWidget(self.labelQuickAdd)

		self.line_2 = QFrame(self.verticalLayoutWidget)
		self.line_2.setObjectName(u"line_2")
		self.line_2.setFrameShape(QFrame.HLine)
		self.line_2.setFrameShadow(QFrame.Sunken)

		self.verticalLayout.addWidget(self.line_2)

		self.label = QLabel(self.verticalLayoutWidget)
		self.label.setObjectName(u"label")
		sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy)
		self.label.setText(u"Select chunk creation settings:")
		self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

		self.verticalLayout.addWidget(self.label)

		self.cbChunkSettings = QComboBox(self.verticalLayoutWidget)
		for section in autoftg_main.chunk_sections:
			menu_icon = autoftg_main.menuCfg.get(section, "menu_icon")
			menu_icon_path = u":/icons/" + autoftg_main.icoCfg.get("ICONS", menu_icon)
			seticon = QIcon()
			seticon.addFile(menu_icon_path, QSize(), QIcon.Normal, QIcon.Off)
			self.cbChunkSettings.addItem(seticon, section)
		
		
		self.cbChunkSettings.setObjectName(u"cbChunkSettings")
		sizePolicy.setHeightForWidth(self.cbChunkSettings.sizePolicy().hasHeightForWidth())
		self.cbChunkSettings.setSizePolicy(sizePolicy)
		font2 = QFont()
		font2.setFamily(u"Segoe UI")
		font2.setPointSize(11)
		self.cbChunkSettings.setFont(font2)
		self.cbChunkSettings.setCursor(QCursor(Qt.PointingHandCursor))

		self.cbChunkSettings.setCurrentText(u"GENERAL")
		self.cbChunkSettings.setIconSize(QSize(20, 20))

		self.verticalLayout.addWidget(self.cbChunkSettings)

		self.line = QFrame(self.verticalLayoutWidget)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.verticalLayout.addWidget(self.line)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setSpacing(5)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.btnCreate = QPushButton(self.verticalLayoutWidget)
		self.btnCreate.setObjectName(u"btnCreate")
		sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
		sizePolicy3.setHorizontalStretch(0)
		sizePolicy3.setVerticalStretch(0)
		sizePolicy3.setHeightForWidth(self.btnCreate.sizePolicy().hasHeightForWidth())
		self.btnCreate.setSizePolicy(sizePolicy3)
		self.btnCreate.setText(u"Create")
		icon4 = QIcon()
		icon4.addFile(u":/icons/icons8-add-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.btnCreate.setIcon(icon4)
		self.btnCreate.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.btnCreate)

		self.checkBoxAutoProc = QCheckBox(self.verticalLayoutWidget)
		self.checkBoxAutoProc.setObjectName(u"checkBoxAutoProc")
		self.checkBoxAutoProc.setText(u"Auto Processing")
		icon5 = QIcon()
		icon5.addFile(u":/icons/icons8-in-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBoxAutoProc.setIcon(icon5)
		self.checkBoxAutoProc.setChecked(True)

		self.horizontalLayout.addWidget(self.checkBoxAutoProc)

		self.btnCancel = QPushButton(self.verticalLayoutWidget)
		self.btnCancel.setObjectName(u"btnCancel")
		sizePolicy3.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
		self.btnCancel.setSizePolicy(sizePolicy3)
		self.btnCancel.setText(u"Close")
		icon6 = QIcon()
		icon6.addFile(u":/icons/icons8-enter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.btnCancel.setIcon(icon6)
		self.btnCancel.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.btnCancel)

		self.verticalLayout.addLayout(self.horizontalLayout)


		QtCore.QObject.connect(self.btnCreate, QtCore.SIGNAL("clicked()"), self.startProcess)
		QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))			
		
		self.exec()


	def startProcess(self):
		global selected_pre
		global selected_suf
		selected_menu = self.cbChunkSettings.currentText()
		selected_pre = autoftg_main.menuCfg.get(selected_menu, "chunk_name_prefix")
		selected_suf = autoftg_main.menuCfg.get(selected_menu, "chunk_name_suffix")
		selected_workfolder = autoftg_main.menuCfg.get(selected_menu, "work_folder")

		if self.checkBoxAutoProc.isChecked == False:
			self.accept()
			autoftg_main.newchunk_manual(selected_pre, selected_suf, selected_workfolder)
		else:
			self.accept()
			autoftg_main.newchunk_auto(selected_pre, selected_suf, selected_workfolder)		


