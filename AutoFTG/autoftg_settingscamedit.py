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
from AutoFTG.qtresources_rc2 import *

selected_camera = None

class Ui_DialogAddEditCam(QtWidgets.QDialog):
	def __init__(self, parent, camnew, camname):
		global camOrigName
		camOrigName = camname
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"DialogAddEditCam")
		appIcon = QIcon()
		appIcon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(appIcon)
		self.resize(480, 270)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)
		self.setMinimumSize(QSize(480, 270))
		self.setMaximumSize(QSize(480, 270))
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(10)
		self.setFont(font)
		self.setWindowTitle(u"Add/Edit Camera")
		appIcon = QIcon()
		appIcon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(appIcon)
		self.gridLayoutWidget = QWidget(self)
		self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
		self.gridLayoutWidget.setGeometry(QRect(10, 10, 461, 251))
		self.gridLayout = QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setSpacing(5)
		self.gridLayout.setContentsMargins(10, 10, 10, 10)
		self.gridLayout.setObjectName(u"gridLayout")
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.comboBox_2 = QComboBox(self.gridLayoutWidget)
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons8-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon1, u"Standard")
		icon2 = QIcon()
		icon2.addFile(u":/icons/icons8-slr-small-lens-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon2, u"DSLR")
		icon3 = QIcon()
		icon3.addFile(u":/icons/icons8-camera-on-tripod-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon3, u"Special")
		icon4 = QIcon()
		icon4.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon4, u"Drone")
		icon5 = QIcon()
		icon5.addFile(u":/icons/icons8-touchscreen-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon5, u"SmartPhone")
		icon6 = QIcon()
		icon6.addFile(u":/icons/icons8-gopro-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon6, u"SportCam")
		self.comboBox_2.setObjectName(u"comboBox_2")
		self.comboBox_2.setFont(font)
		self.comboBox_2.setIconSize(QSize(24, 24))

		self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)

		self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
		self.lineEdit_2.setObjectName(u"lineEdit_2")
		self.lineEdit_2.setFont(font)
		self.lineEdit_2.setPlaceholderText(u"Camera name")

		self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)

		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setSpacing(5)
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
		self.lineEdit_3.setObjectName(u"lineEdit_3")
		sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		sizePolicy1.setHorizontalStretch(0)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
		self.lineEdit_3.setSizePolicy(sizePolicy1)
		self.lineEdit_3.setMinimumSize(QSize(0, 28))
		self.lineEdit_3.setMaximumSize(QSize(16777215, 28))
		font1 = QFont()
		font1.setFamily(u"Segoe UI")
		font1.setPointSize(8)
		self.lineEdit_3.setFont(font1)
		self.lineEdit_3.setPlaceholderText(u"Choose calibration XML file...")

		self.horizontalLayout_2.addWidget(self.lineEdit_3)

		self.pushButton_3 = QPushButton(self.gridLayoutWidget)
		self.pushButton_3.setObjectName(u"pushButton_3")
		sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
		sizePolicy2.setHorizontalStretch(0)
		sizePolicy2.setVerticalStretch(0)
		sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
		self.pushButton_3.setSizePolicy(sizePolicy2)
		self.pushButton_3.setFont(font1)
		self.pushButton_3.setToolTip(u"Choose XML calibration file...")
		self.pushButton_3.setText(u"Browse")
		icon7 = QIcon()
		icon7.addFile(u":/icons/icons8-images-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_3.setIcon(icon7)
		self.pushButton_3.setIconSize(QSize(24, 24))

		self.horizontalLayout_2.addWidget(self.pushButton_3)


		self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)

		self.label_3 = QLabel(self.gridLayoutWidget)
		self.label_3.setObjectName(u"label_3")
		sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
		sizePolicy3.setHorizontalStretch(0)
		sizePolicy3.setVerticalStretch(0)
		sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
		self.label_3.setSizePolicy(sizePolicy3)
		font2 = QFont()
		font2.setFamily(u"Segoe UI")
		font2.setPointSize(10)
		font2.setBold(True)
		font2.setWeight(75)
		self.label_3.setFont(font2)
		self.label_3.setText(u"Camera Name")

		self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setSpacing(5)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.pushButton = QPushButton(self.gridLayoutWidget)
		self.pushButton.setObjectName(u"pushButton")
		sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
		self.pushButton.setSizePolicy(sizePolicy)
		self.pushButton.setMinimumSize(QSize(0, 0))
		self.pushButton.setMaximumSize(QSize(90, 30))
		self.pushButton.setText(u"Cancel")
		icon8 = QIcon()
		icon8.addFile(u":/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton.setIcon(icon8)
		self.pushButton.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton)

		self.pushButton_2 = QPushButton(self.gridLayoutWidget)
		self.pushButton_2.setObjectName(u"pushButton_2")
		sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
		self.pushButton_2.setSizePolicy(sizePolicy)
		self.pushButton_2.setMinimumSize(QSize(0, 0))
		self.pushButton_2.setMaximumSize(QSize(90, 30))
		self.pushButton_2.setText(u"Save")
		icon9 = QIcon()
		icon9.addFile(u":/icons/icons8-save-all-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_2.setIcon(icon9)
		self.pushButton_2.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton_2)


		self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 2)

		self.label = QLabel(self.gridLayoutWidget)
		self.label.setObjectName(u"label")
		sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy3)
		self.label.setFont(font)
		self.label.setText(u"Type")

		self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

		self.label_4 = QLabel(self.gridLayoutWidget)
		self.label_4.setObjectName(u"label_4")
		sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
		self.label_4.setSizePolicy(sizePolicy3)
		font3 = QFont()
		font3.setFamily(u"Segoe UI")
		font3.setPointSize(9)
		self.label_4.setFont(font3)
		self.label_4.setText(u"Resolution")

		self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

		self.label_7 = QLabel(self.gridLayoutWidget)
		self.label_7.setObjectName(u"label_7")
		self.label_7.setFont(font3)
		self.label_7.setText(u"Description")

		self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

		self.line = QFrame(self.gridLayoutWidget)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.gridLayout.addWidget(self.line, 6, 0, 1, 2)

		self.comboBox = QComboBox(self.gridLayoutWidget)
		icon10 = QIcon()
		icon10.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox.addItem(icon10, u"Frame")
		icon11 = QIcon()
		icon11.addFile(u":/icons/icons8-video-wall-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox.addItem(icon11, u"Fisheye")
		icon12 = QIcon()
		icon12.addFile(u":/icons/icons8-live-photos-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox.addItem(icon12, u"Spherical")
		icon13 = QIcon()
		icon13.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox.addItem(icon13, u"Cylindical")
		icon14 = QIcon()
		icon14.addFile(u":/icons/icons8-ios-application-placeholder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox.addItem(icon14, u"RPC")
		self.comboBox.setObjectName(u"comboBox")
		self.comboBox.setFont(font)
		self.comboBox.setIconSize(QSize(24, 24))

		self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)

		self.label_5 = QLabel(self.gridLayoutWidget)
		self.label_5.setObjectName(u"label_5")
		sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
		self.label_5.setSizePolicy(sizePolicy3)
		self.label_5.setText(u"Callibration")

		self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

		self.label_2 = QLabel(self.gridLayoutWidget)
		self.label_2.setObjectName(u"label_2")
		sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
		self.label_2.setSizePolicy(sizePolicy3)
		self.label_2.setFont(font3)
		self.label_2.setText(u"Sub-Type")

		self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

		self.horizontalLayout_3 = QHBoxLayout()
		self.horizontalLayout_3.setSpacing(5)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.lineEdit = QLineEdit(self.gridLayoutWidget)
		self.lineEdit.setObjectName(u"lineEdit")
		self.lineEdit.setMaximumSize(QSize(50, 16777215))
		self.lineEdit.setFont(font)
		self.lineEdit.setText(u"0")

		self.horizontalLayout_3.addWidget(self.lineEdit)

		self.label_6 = QLabel(self.gridLayoutWidget)
		self.label_6.setObjectName(u"label_6")
		self.label_6.setText(u"MP")

		self.horizontalLayout_3.addWidget(self.label_6)


		self.gridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)

		self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
		self.lineEdit_4.setObjectName(u"lineEdit_4")
		self.lineEdit_4.setFont(font)
		self.lineEdit_4.setPlaceholderText(u"Description of camera (optional)")

		self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)

		QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_4)
		QWidget.setTabOrder(self.lineEdit_4, self.comboBox)
		QWidget.setTabOrder(self.comboBox, self.comboBox_2)
		QWidget.setTabOrder(self.comboBox_2, self.lineEdit)
		QWidget.setTabOrder(self.lineEdit, self.lineEdit_3)
		QWidget.setTabOrder(self.lineEdit_3, self.pushButton_3)
		QWidget.setTabOrder(self.pushButton_3, self.pushButton_2)
		QWidget.setTabOrder(self.pushButton_2, self.pushButton)

		if camnew == True:
			autoftg_main.cameraXmlSource = ''
			autoftg_main.cameraXmlDest = ''
			self.setWindowTitle(u"Add New Camera")
			self.pushButton_2.setText(u"Add Camera")
		else:
			selCamType = autoftg_main.camCfg.get(camname, "Description")
			selCamType = autoftg_main.camCfg.get(camname, "Type")
			selCamSubType = autoftg_main.camCfg.get(camname, "SubType")
			selCamRes = autoftg_main.camCfg.get(camname, "Resolution")
			selCamFile = autoftg_main.camCfg.get(camname, "File")
			autoftg_main.cameraXmlSource = selCamFile
			autoftg_main.cameraXmlDest = selCamFile
			self.lineEdit_2.setText(camname)
			self.comboBox.setCurrentText(selCamType)
			self.comboBox_2.setCurrentText(selCamSubType)
			self.lineEdit.setText(selCamRes)
			self.lineEdit_3.setText(selCamFile)
			self.setWindowTitle(u"Edit Camera")
			self.pushButton_2.setText(u"Save Changes")
		
		QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.selectCameraFile)
		QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.saveCamera)
		QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))

		self.exec()

	
	def selectCameraFile(self):
		autoftg_main.cameraXmlSource = Metashape.app.getOpenFileName(hint="Select Camera Calibration", dir=str(autoftg_main.selected_data_folder), filter="Metashape Camera Calibration (*.xml)")
		camXmlFile = os.path.basename(autoftg_main.cameraXmlSource)
		autoftg_main.cameraXmlDest = autoftg_main.camCfgPath + camXmlFile
		self.lineEdit_3.setText(camXmlFile)


	def saveCamera(self):
		cameraNameAdd = self.lineEdit_2.text()
		camDesc = self.lineEdit_4.text()
		cameraTypeAdd = self.comboBox.currentText()
		cameraSubTypeAdd = self.comboBox_2.currentText()
		cameraResAdd = self.lineEdit.text()
		cameraFileAdd = self.lineEdit_3.text()
		if cameraNameAdd == "" or cameraNameAdd == None:
			Metashape.app.messageBox("Error! No camera name entered...")
		else:
			if self.lineEdit_3.text() != "" or self.lineEdit_3.text() != None:
				self.copyXml()
			else:
				cameraFileAdd = "None"
			autoftg_main.saveCamConfig(camOrigName, cameraNameAdd, camDesc, cameraTypeAdd, cameraSubTypeAdd, cameraResAdd, cameraFileAdd)
			autoftg_main.camCfgLoad()
			autoftg_main.cameraXmlSource = ''
			autoftg_main.cameraXmlDest = ''
			self.close()


	def copyXml(self):
		if autoftg_main.cameraXmlSource != autoftg_main.cameraXmlDest:
			cameraXmlDestExists = os.path.isfile(autoftg_main.cameraXmlDest)
			if cameraXmlDestExists == False:
				try:
					shutil.copy2(autoftg_main.cameraXmlSource, autoftg_main.cameraXmlDest)
				except:
					Metashape.app.messageBox("Error! Could not copy calibration file...")
			else:
				try:
					os.remove(autoftg_main.cameraXmlDest)
				except:
					Metashape.app.messageBox("Error! Failed to remove old calibration file...")

				try:
					shutil.copy2(autoftg_main.cameraXmlSource, autoftg_main.cameraXmlDest)
				except:
					Metashape.app.messageBox("Error! Failed to copy calibration file...")


	def closeCameraDialog(self):
		autoftg_main.camCfgLoad()
		self.close()


class Ui_dialogCamGui(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"dialogCamGui")
		self.resize(350, 300)
		self.setWindowTitle(u"Cameras Editor")
		appIcon = QIcon()
		appIcon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(appIcon)
		layoutMain = QtWidgets.QVBoxLayout()  # creating layout
		menuico00 = QIcon()
		menuico00.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico1 = QIcon()
		menuico1.addFile(u":/icons/icons8-panorama-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico2 = QIcon()
		menuico2.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico3 = QIcon()
		menuico3.addFile(u":/icons/icons8-video-stabilization-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico4 = QIcon()
		menuico4.addFile(u":/icons/icons8-touchscreen-48.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico5 = QIcon()
		menuico5.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico6 = QIcon()
		menuico6.addFile(u":/icons/icons8-add-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico7 = QIcon()
		menuico7.addFile(u":/icons/icons8-design-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico8 = QIcon()
		menuico8.addFile(u":/icons/icons8-no-camera-96.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico9 = QIcon()
		menuico9.addFile(u":/icons/icons8-ios-application-placeholder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icoTripod = QIcon()
		icoTripod.addFile(u":/icons/icons8-camera-on-tripod-96.png", QSize(), QIcon.Normal, QIcon.Off)
		font1 = QFont()
		font1.setPointSize(10)
		self.verticalLayoutWidget_2 = QWidget()
		self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
		self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 331, 211))
		self.vLayout_Main = QVBoxLayout(self.verticalLayoutWidget_2)
		self.vLayout_Main.setObjectName(u"vLayout_Main")
		self.vLayout_Main.setContentsMargins(0, 0, 0, 0)
		self.hLayoutCamEdit = QHBoxLayout()
		self.hLayoutCamEdit.setObjectName(u"hLayoutCamEdit")
		self.listWidgetCam = QListWidget(self.verticalLayoutWidget_2)
		self.listWidgetCam.setObjectName(u"listWidgetCam")
		self.listWidgetCam.setFont(font1)
		self.listWidgetCam.setFrameShape(QFrame.StyledPanel)
		self.listWidgetCam.setFrameShadow(QFrame.Plain)
		self.listWidgetCam.setDefaultDropAction(Qt.IgnoreAction)
		self.listWidgetCam.setIconSize(QSize(20, 20))
		for camera in autoftg_main.cam_list:
			lcam_type = str(autoftg_main.camCfg.get(camera, 'Type'))
			lcam_stype = str(autoftg_main.camCfg.get(camera, "SubType"))
			lcam_res = str(autoftg_main.camCfg.get(camera, 'Resolution'))
			lcam_desc = str(autoftg_main.camCfg.get(camera, 'Description'))
			self.listWidgetCamItem = QListWidgetItem(camera, self.listWidgetCam)
			self.listWidgetCamItem.setText(str(camera))
   #	<html><head/><body><p><b>Processing error!</span></p></body></html>
			if lcam_stype == "Drone":
				self.listWidgetCamItem.setIcon(menuico5)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			elif lcam_stype == "SmartPhone":
				self.listWidgetCamItem.setIcon(menuico4)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			elif lcam_stype == "Special":
				self.listWidgetCamItem.setIcon(icoTripod)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			elif lcam_type == "Fisheye":
				self.listWidgetCamItem.setIcon(menuico1)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			elif lcam_type == "Cylindrical":
				self.listWidgetCamItem.setIcon(menuico2)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			elif lcam_type == "Spherical":
				self.listWidgetCamItem.setIcon(menuico3)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			elif lcam_type == "RPC":
				self.listWidgetCamItem.setIcon(menuico9)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			else:
				self.listWidgetCamItem.setIcon(menuico00)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)

		self.hLayoutCamEdit.addWidget(self.listWidgetCam)

		self.vLayout_CamBtn = QVBoxLayout()
		self.vLayout_CamBtn.setObjectName(u"vLayout_CamBtn")
		sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		
		self.btnRemoveCam = QPushButton(self.verticalLayoutWidget_2)
		self.btnRemoveCam.setObjectName(u"btnRemoveCam")
		sizePolicy.setHeightForWidth(self.btnRemoveCam.sizePolicy().hasHeightForWidth())
		self.btnRemoveCam.setSizePolicy(sizePolicy)
		self.btnRemoveCam.setText(u" Remove")
		self.btnRemoveCam.setIcon(menuico8)
		self.btnRemoveCam.setIconSize(QSize(24, 24))

		self.vLayout_CamBtn.addWidget(self.btnRemoveCam)

		self.btnEditCam = QPushButton(self.verticalLayoutWidget_2)
		self.btnEditCam.setObjectName(u"btnEditCam")
		sizePolicy.setHeightForWidth(self.btnEditCam.sizePolicy().hasHeightForWidth())
		self.btnEditCam.setSizePolicy(sizePolicy)
		self.btnEditCam.setText(u" Edit")
		self.btnEditCam.setIcon(menuico7)
		self.btnEditCam.setIconSize(QSize(24, 24))

		self.vLayout_CamBtn.addWidget(self.btnEditCam)

		self.btnAddNewCam = QPushButton(self.verticalLayoutWidget_2)
		self.btnAddNewCam.setObjectName(u"btnAddNewCam")
		sizePolicy.setHeightForWidth(self.btnAddNewCam.sizePolicy().hasHeightForWidth())
		self.btnAddNewCam.setSizePolicy(sizePolicy)
		self.btnAddNewCam.setText(u" Add")
		self.btnAddNewCam.setIcon(menuico6)
		self.btnAddNewCam.setIconSize(QSize(24, 24))

		self.vLayout_CamBtn.addWidget(self.btnAddNewCam)

		self.hLayoutCamEdit.addLayout(self.vLayout_CamBtn)

		layoutMain.addLayout(self.hLayoutCamEdit)

		self.hLayout_MainBtn = QHBoxLayout()
		self.hLayout_MainBtn.setObjectName(u"hLayout_MainBtn")
		self.btnMainClose = QPushButton(self.verticalLayoutWidget_2)
		self.btnMainClose.setObjectName(u"btnMainClose")
		sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
		sizePolicy1.setHorizontalStretch(0)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.btnMainClose.sizePolicy().hasHeightForWidth())
		self.btnMainClose.setSizePolicy(sizePolicy1)
		self.btnMainClose.setText(u"Close")

		self.hLayout_MainBtn.addWidget(self.btnMainClose)

		layoutMain.addLayout(self.hLayout_MainBtn)

		self.setLayout(layoutMain)

		QtCore.QObject.connect(self.btnAddNewCam, QtCore.SIGNAL("clicked()"), self.addNewCam)
		QtCore.QObject.connect(self.btnEditCam, QtCore.SIGNAL("clicked()"), self.editSelCamera)
		QtCore.QObject.connect(self.btnRemoveCam, QtCore.SIGNAL("clicked()"), self.removeSelCamera)
		QtCore.QObject.connect(self.btnMainClose, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))

		self.exec()


	def refreshCamList(self):
		self.listWidgetCam.clear()
		menuico00 = QIcon()
		menuico00.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico1 = QIcon()
		menuico1.addFile(u":/icons/icons8-panorama-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico2 = QIcon()
		menuico2.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico3 = QIcon()
		menuico3.addFile(u":/icons/icons8-video-stabilization-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico4 = QIcon()
		menuico4.addFile(u":/icons/icons8-touchscreen-48.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico5 = QIcon()
		menuico5.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico6 = QIcon()
		menuico6.addFile(u":/icons/icons8-add-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico7 = QIcon()
		menuico7.addFile(u":/icons/icons8-design-50.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico8 = QIcon()
		menuico8.addFile(u":/icons/icons8-no-camera-96.png", QSize(), QIcon.Normal, QIcon.Off)
		menuico9 = QIcon()
		menuico9.addFile(u":/icons/icons8-ios-application-placeholder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icoTripod = QIcon()
		icoTripod.addFile(u":/icons/icons8-camera-on-tripod-96.png", QSize(), QIcon.Normal, QIcon.Off)
		for camera in autoftg_main.cam_list:
			lcam_type = str(autoftg_main.camCfg.get(camera, 'Type'))
			lcam_stype = str(autoftg_main.camCfg.get(camera, "SubType"))
			lcam_res = str(autoftg_main.camCfg.get(camera, 'Resolution'))
			lcam_desc = str(autoftg_main.camCfg.get(camera, 'Description'))
			self.listWidgetCamItem = QListWidgetItem(camera, self.listWidgetCam)
			self.listWidgetCamItem.setText(str(camera))
   #	<html><head/><body><p><b>Processing error!</span></p></body></html>
			if lcam_stype == "Drone":
				self.listWidgetCamItem.setIcon(menuico5)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			elif lcam_stype == "SmartPhone":
				self.listWidgetCamItem.setIcon(menuico4)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			elif lcam_stype == "Special":
				self.listWidgetCamItem.setIcon(icoTripod)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			elif lcam_type == "Fisheye":
				self.listWidgetCamItem.setIcon(menuico1)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			elif lcam_type == "Cylindrical":
				self.listWidgetCamItem.setIcon(menuico2)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			elif lcam_type == "Spherical":
				self.listWidgetCamItem.setIcon(menuico3)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			elif lcam_type == "RPC":
				self.listWidgetCamItem.setIcon(menuico9)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)
			else:
				self.listWidgetCamItem.setIcon(menuico00)
				self.listWidgetCamItem.setToolTip("<html><head/><body><p><b>Type: " + lcam_type + "</b><br>SubType: " + lcam_stype + "<br>Res.: " + lcam_res + "MP" + "<br>Desc.: " + lcam_desc)

		

	def addNewCam(self):
		autoftg_main.addCameraDialog(camnew=True, camname="")
		self.refreshCamList()


	def editSelCamera(self):
		# defaultItem = self.listWidgetCam.isItemSelected("Default")
		if self.listWidgetCam.currentRow() > 1:
			selCamName = self.listWidgetCam.currentItem().text()
			autoftg_main.addCameraDialog(camnew=False, camname=selCamName)
			self.refreshCamList()

		elif self.listWidgetCam.currentRow() <= 1:
			Metashape.app.messageBox("Default cameras can not be edited.")

		else:
			Metashape.app.messageBox("No camera selected...")


	def removeSelCamera(self):
		if self.listWidgetCam.currentRow() > 1:
			del_cam = self.listWidgetCam.currentItem().text()
			remove_confirm = Metashape.app.getBool("Remove selected camera?\n\nSelected: " + del_cam)
			if remove_confirm == True:
				autoftg_main.removeCamConfig(del_cam)
			self.refreshCamList()

		elif self.listWidgetCam.currentRow() <= 1:
			Metashape.app.messageBox("Default cameras can not be removed.")

		else:
			Metashape.app.messageBox("No camera selected...")


class Ui_dialogChooseCamera(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"dialogChooseCamera")
		self.resize(320, 300)
		self.setWindowTitle(u"Choose Camera")
		appIcon = QIcon()
		appIcon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(appIcon)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		self.setSizePolicy(sizePolicy)
		self.setMinimumSize(QSize(320, 300))
		self.setMaximumSize(QSize(320, 300))
		self.setWindowTitle(u"Choose Camera")
		self.verticalLayoutWidget = QWidget(self)
		self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
		self.verticalLayoutWidget.setGeometry(QRect(10, 10, 301, 281))
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
		self.label.setText(u"Select Camera")

		self.verticalLayout.addWidget(self.label)

		self.listWidget = QListWidget(self.verticalLayoutWidget)
		icon = QIcon()
		icon.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
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
		font1 = QFont()
		font1.setPointSize(10)
		for cam in autoftg_main.cam_list:
			icon_type = autoftg_main.camCfg.get(cam, "Type")
			icon_subtype = autoftg_main.camCfg.get(cam, "SubType")
			self.listwidget = QListWidgetItem(self.listWidget)
			self.listwidget.setText(cam)
			if icon_subtype == "SmartPhone":
				self.listwidget.setIcon(icon4)
			elif icon_subtype == "Drone":
				self.listwidget.setIcon(icon5)
			elif icon_subtype == "Special":
				self.listwidget.setIcon(icoTripod)
			else:
				if icon_type == "Fisheye":
					self.listwidget.setIcon(icon1)
				elif icon_type == "Spherical":
					self.listwidget.setIcon(icon3)
				elif icon_type == "Cylindrical":
					self.listwidget.setIcon(icon2)
				elif icon_type == "RPC":
					self.listwidget.setIcon(icon5a)
				else:
					self.listwidget.setIcon(icon)

		self.listWidget.setObjectName(u"listWidget")
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
		self.pushButton_2.setText(u"Cancel")

		self.horizontalLayout_2.addWidget(self.pushButton_2)

		self.pushButton = QPushButton(self.verticalLayoutWidget)
		self.pushButton.setObjectName(u"pushButton")
		icon6 = QIcon()
		icon6.addFile(u":/icons/icons8-done-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton.setIcon(icon6)
		self.pushButton.setText(u"Ok")

		self.horizontalLayout_2.addWidget(self.pushButton)
		
		self.verticalLayout.addLayout(self.horizontalLayout_2)

		self.listWidget.setCurrentRow(autoftg_main.cam_list.index(autoftg_main.selected_camera))

		self.listWidget.setSortingEnabled(False)

		QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.selectCam)
		QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))

		self.exec()

	def selectCam(self):
		autoftg_main.selected_camera = self.listWidget.currentItem().text()
		self.close()


