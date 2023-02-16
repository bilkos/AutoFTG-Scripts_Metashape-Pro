# Class for settings editing UI
import os
import shutil
import subprocess
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
from AutoFTG.qtresources_rc2 import *


class Ui_settingsDialog(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"settingsDialog")
		self.resize(300, 100)
		self.setWindowTitle(u"AutoFTG Settings")
		appIcon = QIcon()
		appIcon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(appIcon)
		
		icon = QIcon()
		icon.addFile(u":/icons/icons8-opened-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon0 = QIcon()
		icon0.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons8-panorama-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon2 = QIcon()
		icon2.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon3 = QIcon()
		icon3.addFile(u":/icons/icons8-video-stabilization-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon4 = QIcon()
		icon4.addFile(u":/icons/icons8-touchscreen-48.png", QSize(), QIcon.Normal, QIcon.Off)
		icon5 = QIcon()
		icon5.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon5a = QIcon()
		icon5a.addFile(u":/icons/icons8-ios-application-placeholder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icoTripod = QIcon()
		icoTripod.addFile(u":/icons/icons8-camera-on-tripod-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.label_2 = QtWidgets.QLabel()
		self.label_2.setObjectName(u"label_2")
		self.label_2.setGeometry(QRect(10, 40, 80, 16))
		self.label_2.setText("Data Folder:")
		self.lineDataFolder = QtWidgets.QLineEdit()
		self.lineDataFolder.setObjectName(u"lineDataFolder")
		self.lineDataFolder.setGeometry(QRect(10, 40, 280, 24))
		self.lineDataFolder.setText(str(autoftg_main.selected_data_folder))
		self.lineDataFolder.setClearButtonEnabled(True)
		self.btnDataFolder = QtWidgets.QPushButton()
		self.btnDataFolder.setObjectName(u"btnDataFolder")
		self.btnDataFolder.setGeometry(QRect(300, 40, 80, 24))
		self.btnDataFolder.setText(u" Browse")
		self.btnDataFolder.setIcon(icon)
		self.btnDataFolder.setIconSize(QSize(21, 21))
		
		self.label_3 = QtWidgets.QLabel()
		self.label_3.setObjectName(u"label_3")
		self.label_3.setGeometry(QRect(10, 70, 90, 16))
		self.label_3.setText("Default Camera:")
		self.comboBoxCamera = QtWidgets.QComboBox()
		self.comboBoxCamera.setObjectName(u"comboBoxCamera")
		self.comboBoxCamera.setGeometry(QRect(10, 70, 280, 24))
		for cam in autoftg_main.cam_list:
			icon_type = autoftg_main.camCfg.get(cam, "Type")
			icon_subtype = autoftg_main.camCfg.get(cam, "SubType")
			if icon_subtype == "SmartPhone":
				self.comboBoxCamera.addItem(icon4, cam)
			elif icon_subtype == "Drone":
				self.comboBoxCamera.addItem(icon5, cam)
			elif icon_subtype == "Special":
				self.comboBoxCamera.addItem(icoTripod, cam)
			else:
				if icon_type == "Fisheye":
					self.comboBoxCamera.addItem(icon1, cam)
				elif icon_type == "Spherical":
					self.comboBoxCamera.addItem(icon3, cam)
				elif icon_type == "Cylindrical":
					self.comboBoxCamera.addItem(icon2, cam)
				elif icon_type == "RPC":
					self.comboBoxCamera.addItem(icon5a, cam)
				else:
					self.comboBoxCamera.addItem(icon0, cam)

		self.comboBoxCamera.setCurrentText(str(autoftg_main.selected_camera))
		
		self.btnClose = QtWidgets.QPushButton()
		self.btnClose.setObjectName(u"btnClose")
		self.btnClose.setGeometry(QRect(220, 90, 75, 24))
		self.btnClose.setText(u"Close")
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.btnClose.setIcon(icon1)

		self.btnSave = QtWidgets.QPushButton()
		self.btnSave.setObjectName(u"btnSave")
		self.btnSave.setGeometry(QRect(300, 90, 75, 24))
		self.btnSave.setText(u" Save")
		icon2 = QIcon()
		icon2.addFile(u":/icons/icons8-save-as-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.btnSave.setIcon(icon2)
		self.btnSave.setIconSize(QSize(12, 12))
		
		layout = QtWidgets.QGridLayout()  # creating layout
		layout.setRowMinimumHeight(0, 24)
		layout.setRowMinimumHeight(1, 24)
		layout.setRowMinimumHeight(2, 24)
		layout.setVerticalSpacing(1)

		layout.setColumnMinimumWidth(1, 250) # minimum column width
		layout.setColumnMinimumWidth(2, 80) # minimum column width

		layout.addWidget(self.label_2, 0, 0)
		layout.addWidget(self.lineDataFolder, 0, 1)
		layout.addWidget(self.btnDataFolder, 0, 2)

		layout.addWidget(self.label_3, 1, 0)
		layout.addWidget(self.comboBoxCamera, 1, 1)

		layout.addWidget(self.btnClose, 2, 2)
		layout.addWidget(self.btnSave, 2, 1)

		self.setLayout(layout)

		QtCore.QObject.connect(self.btnDataFolder, QtCore.SIGNAL("clicked()"), self.dataFolderChange)
		QtCore.QObject.connect(self.btnSave, QtCore.SIGNAL("clicked()"), self.saveSettingsDialog)
		QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))

		self.exec()

	def dataFolderChange(self):
		foldeData = Metashape.app.getExistingDirectory("Data folder")
		self.lineDataFolder.setText(foldeData)

	def saveSettingsDialog(self):
		if autoftg_main.projectOpened == False:
			# settings.folderProject = self.lineProjFolder.text()
			autoftg_main.appCfg.set('APP SETTINGS', 'folder_data', self.lineDataFolder.text())
			autoftg_main.appCfg.set('APP SETTINGS', 'default_camera', self.comboBoxCamera.currentText())
			with open(autoftg_main.appCfgFilePath, 'w') as configfile:
				autoftg_main.projCfg.write(configfile)
			autoftg_main.appCfgLoad()
		else:
			autoftg_main.projCfg.set('PROJECT SETTINGS', 'folder_data', self.lineDataFolder.text())
			autoftg_main.projCfg.set('PROJECT SETTINGS', 'default_camera', self.comboBoxCamera.currentText())
			with open(autoftg_main.projCfgFilePath, 'w') as configfile:
				autoftg_main.projCfg.write(configfile)
			autoftg_main.projCfgLoad
		
		print("New settings stored.")
		self.close()


