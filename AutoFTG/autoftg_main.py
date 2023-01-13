# AutoFTG - Scripts for Agisoft Metashape Pro
# Scripts for process automation
# This is an assembly of existing scripts from other users, and some additional 
# scripts written for use in work process at project 2TIR, tunnel T8-KP in Slovenia.
# 
# Author: Boriws Bilc
# 
# Script repository (GitHub):
# ---------------------------
# URL: https://github.com/bilkos/AutoFTG-Scripts_Metashape-Pro
# 
# 
# References:
# -----------
# 
# Copy Bounding Box Script
#  https://github.com/agisoft-llc/metashape-scripts/blob/master/src/copy_bounding_box_dialog.py
#  Copies bounding boxes from chunk to other chunks.
# 
#
# If you add or change resorces (icons, images, etc... in qtresorces.qrc), then you need to re-compile resorces.py file
# To do that you need to navigate to script folder and run following command:
# 
# pyside2-rcc -o resource.py qtresources.qrc
# 


import os
import sys
import time
import shutil
from os import path

import Metashape

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from configparser import ConfigParser

from AutoFTG import qtresources

# App info
app_name = "AutoFTG"
app_ver = "2.5.0"
appsettings_ver = "5"
app_author = "Author: Boris Bilc\n\n"
app_repo = "Repository URL:\nhttps://github.com/bilkos/AutoFTG-Scripts_Metashape-Pro"
ref_repo = "Agisoft GitHub repository:\nhttps://github.com/agisoft-llc/metashape-scripts"
ref_scripts = "Copy Bounding Box Script:\nhttps://github.com/agisoft-llc/metashape-scripts/blob/master/src/copy_bounding_box_dialog.py"
app_about = "Scripts for process automation in Agisoft Metashape Pro\n\nThis is an assembly of existing scripts from other users,\nand some additional scripts written for use in work process at project 2TIR, tunnel T8-KP in Slovenia."


# Check compatibility with Metashape
compatible_major_version = "2.0"
found_major_version = ".".join(Metashape.app.version.split('.')[:2])
if found_major_version != compatible_major_version:
	raise Exception("Incompatible Metashape version: {} != {}".format(found_major_version, compatible_major_version))


projectOpened = False
settingsRebuild = False
selected_data_folder = ''
selected_camera = "No Calibration - Frame (Default)"
selected_pre = ''
selected_suf = ''
selected_menu = ''

# Load main app settings
appCfg = ConfigParser()
appCfgFile = 'settings_autoftg.ini'
appCfgPath = os.path.expanduser('~\AppData\Local\Agisoft\Metashape Pro\scripts\AutoFTG\\').replace("\\", "/")
appCfgFilePath =  appCfgPath + appCfgFile
appCfgFileExists = os.path.isfile(appCfgFilePath)	# Check if settings file exists


# Load custom menu settings
menuCfg = ConfigParser()
menuCfgFile = "settings_newchunk.ini"
menuCfgPath = os.path.expanduser('~\AppData\Local\Agisoft\Metashape Pro\scripts\AutoFTG').replace("\\", "/")
menuCfgFilePath =  menuCfgPath + "/" + menuCfgFile
menuCfgFilePathExists = os.path.isfile(menuCfgFilePath)
chunk_sections = []


# Init configparser for camera settings. Set empty camera variables for global use.
camCfg = ConfigParser()
cam_name = ''
cam_desc = ''
cam_type = ''
cam_subtype = ''
cam_res = ''
cam_file = ''

cameraXmlSource = ''
cameraXmlDest = ''

camCfgFile = "settings_cam.ini"
camCfgPath = os.path.expanduser('~\AppData\Local\Agisoft\Metashape Pro\scripts\AutoFTG\cameras\\').replace("\\", "/")
camCfgFilePath =  camCfgPath + camCfgFile
camCfgFilePathExists = os.path.isfile(camCfgFilePath)
cam_list = []


# Check settings version
def checkSettingsVer():
	global settingsRebuild
	if appCfg.get("SETTINGS", "settings_version") != appsettings_ver:
		settingsReset(True)
		

# Routine to check if project exists before initializing settings
def projectOpenedCheck():
	global projectOpened
	doc = Metashape.app.document
	#fileDoc = str(doc).replace("<Document '", "").replace("'>", "")

	if doc == "<Document ''>" or doc == None:
		projectOpened = False
		Metashape.app.messageBox("Empty project?\n\nSave project first, or open an existing project. (*.psx).")
		appCfgLoad()
	else:
		projectOpened = True
		projCfgLoad()


def appCfgLoad():
	global selected_data_folder
	global selected_camera
	appCfgFileExists = os.path.isfile(appCfgFilePath)	# Check if settings file exists
	if appCfgFileExists == False:
		print("\nSettings initialization...\nPlease choose data folder, and default camera.")
		Metashape.app.messageBox("Settings initialization...\nPlease choose data folder, and default camera.")
		foldeData = str(Metashape.app.getExistingDirectory("Working data folder"))
		#selectCamDefault()
		diaSelectCamera()
		appCfg.add_section('SETTINGS')
		appCfg.set('SETTINGS', 'settings_version', appsettings_ver)
		appCfg.set('SETTINGS', 'folder_data', foldeData)
		appCfg.set('SETTINGS', 'default_camera', selected_camera)

		# Writing our configuration file to 'example.cfg'
		with open(appCfgFilePath, 'w') as configfile:
			appCfg.write(configfile)

	appCfg.read(appCfgFilePath)
	selected_data_folder = appCfg.get('SETTINGS', 'folder_data')
	selected_camera = appCfg.get('SETTINGS', 'default_camera')


def menuCfgLoad():
	global chunk_sections
	if menuCfgFilePathExists == False:
		menu_section_m = "GENERAL"
		menuCfg.add_section(menu_section_m)
		menuCfg.set(menu_section_m, "menu_category", "")
		menuCfg.set(menu_section_m, "menu_icon", ":/icons/icons8-add-50.png")
		menuCfg.set(menu_section_m, "chunk_name_prefix", "")
		menuCfg.set(menu_section_m, "chunk_name_suffix", "")
		menuCfg.set(menu_section_m, "work_folder", "")
	
		with open(menuCfgFilePath, 'w') as menuconfig:
			menuCfg.write(menuconfig)

	menuCfg.read(menuCfgFilePath)
	chunk_sections = menuCfg.sections()
	print("Custom chunk settings loaded...\nFile: " + menuCfgFile)


def camCfgLoad():
	global cam_list

	if camCfgFilePathExists == False:
		defcam_name = 'No Calibration - Frame (Default)'
		defcam_description = 'Default Metashape camera settings for type FRAME. Calibration is calculated On-The-Fly.'
		defcam_type = 'Frame'
		defcam_subtype = 'Standard'
		defcam_resolution = '0'
		defcam_file = 'None'

		defcam2_name = 'No Calibration - Fisheye'
		defcam2_description = 'Default Metashape camera settings for type FISHEYE. Calibration is calculated On-The-Fly.'
		defcam2_type = 'Fisheye'
		defcam2_subtype = 'Standard'
		defcam2_resolution = '0'
		defcam2_file = 'None'

		camCfg.add_section(defcam_name)
		camCfg.set(defcam_name, "description", defcam_description)
		camCfg.set(defcam_name, "type", defcam_type)
		camCfg.set(defcam_name, "subtype", defcam_subtype)
		camCfg.set(defcam_name, "resolution", defcam_resolution)
		camCfg.set(defcam_name, "file", defcam_file)
		camCfg.add_section(defcam2_name)
		camCfg.set(defcam2_name, "description", defcam2_description)
		camCfg.set(defcam2_name, "type", defcam2_type)
		camCfg.set(defcam2_name, "subtype", defcam2_subtype)
		camCfg.set(defcam2_name, "resolution", defcam2_resolution)
		camCfg.set(defcam2_name, "file", defcam2_file)

		with open(camCfgFilePath, 'w') as camconfigfile:
			camCfg.write(camconfigfile)

	camCfg.read(camCfgFilePath)
	cam_list = camCfg.sections()
	print("Camera settings loaded...\nFile: " + camCfgFile)


# Project settings initialization (used when .psx project is loaded)
def projCfgLoad():
	global settingsRebuild
	global projDoc
	global projCfgFilePath
	global projCfgFilePathExists
	global projCfg
	global projectOpened
	global selected_camera
	global selected_data_folder

	projDoc = Metashape.app.document
	projDocFile = str(projDoc).replace("<Document '", "").replace("'>", "")
	projCfg = ConfigParser()	# INICALIZACIJA NASTAVITEV
	projCfgFilePath = projDocFile.replace(".psx", "_settings.ini")	# Datoteka z nastavitvami projekta
	projCfgFilePathExists = os.path.isfile(projCfgFilePath)	# Preveri, če datoteka z projektom obstaja
	
	if projCfgFilePathExists == False:
		print("\nProject settings initialization...\nPlease choose data folder, and default camera.")
		Metashape.app.messageBox("Settings initialization...\nPlease choose data folder, and default camera.")
		proj_data = Metashape.app.getExistingDirectory("Project data folder")
		diaSelectCamera()
		projCfg.add_section('SETTINGS')
		projCfg.set('SETTINGS', 'settings_version', appsettings_ver)
		projCfg.set('SETTINGS', 'folder_data', str(proj_data))
		projCfg.set('SETTINGS', 'default_camera', selected_camera)
		
		# Writing our configuration file to 'example.cfg'
		with open(projCfgFilePath, 'w') as configfile:
			projCfg.write(configfile)

	projCfg.read(projCfgFilePath)
	checkSettingsVer()
	selected_data_folder = projCfg.get('SETTINGS', 'folder_data')
	selected_camera = projCfg.get('SETTINGS', 'default_camera')
	readCameraSettings(selected_camera)
	projectOpened = True
	Metashape.app.messageBox("Project settings loaded.\n\n"
			+ "Data Folder: " + str(selected_data_folder) + "\n"
			+ "Default Camera: " + str(selected_camera))


# Reset settings
def settingsReset(settingsRebuild):
	if settingsRebuild == True:
		if projectOpened == True:
			os.remove(appCfgFilePath)
			os.remove(projCfgFilePath)
			settingsRebuild = False
			projCfgLoad()
		else:
			os.remove(appCfgFilePath)
			settingsRebuild = False
			appCfgLoad()


# Read camera settings from INI config file
def readCameraSettings(cam_section):
	global cam_name
	global cam_desc
	global cam_type
	global cam_subtype
	global cam_res
	global cam_file

	# Read settings for requested camera
	cam_name = cam_section
	cam_desc = camCfg.get(cam_section, "Description")
	cam_type = camCfg.get(cam_section, "Type")
	cam_subtype = camCfg.get(cam_section, "SubType")
	cam_res = camCfg.get(cam_section, "Resolution")
	cam_file = camCfg.get(cam_section, "File")
	print("Using camera\n" + "Name: " + cam_name + "\nDesc.: " + cam_desc + "\nType: " + cam_type + "\nSubType: " + cam_subtype + "\nResolution: " + cam_res + "\nFile: " + cam_file)
	

# Called to apply camera settings when creating new chunk
def useCameraSettings():
	# Init document
	doc = Metashape.app.document
	chunk = doc.chunk
	# readCameraSettings(settings.defaultCamera)
	camera_path = camCfgPath + cam_file
	
	# Sensor to which we will apply settings
	chunk_sensor = chunk.sensors[0]
	
	# Set sensor type from camera
	if cam_type == "Fisheye":
		chunk_sensor.type = Metashape.Sensor.Type.Fisheye
	elif cam_type == "Frame":
		chunk_sensor.type = Metashape.Sensor.Type.Frame
	elif cam_type == "Spherical":
			chunk_sensor.type = Metashape.Sensor.Type.Spherical
	elif cam_type == "Cylindrical":
			chunk_sensor.type = Metashape.Sensor.Type.Cylindrical
	elif cam_type == "RPC":
			chunk_sensor.type = Metashape.Sensor.Type.RPC
	else:
		Metashape.app.messagBox("Camera Type not recognized.\nPlease check camera settings...")

	# Init calibration and import settings from camera calibration file (Metashape XML)
	chunk_calib = Metashape.Calibration()
	if cam_file != "None":
		chunk_calib.load(path=camera_path, format=Metashape.CalibrationFormatXML)
	chunk_sensor.user_calib = chunk_calib
	
	# Save document and show message with applied settings
	doc.save()
	# Metashape.app.messageBox("Camera settings applied.\n\nCamera: " + cam_name + "\nType: " + cam_type + "\nFilename: " + cam_file)
	Metashape.app.update()


# Choose default camera routine
def selectCamDefault():
	camCfgLoad()
	diaSelectCamera()
	if selected_camera == None:
		Metashape.app.messageBox("No camera selected. Nothing has changed...")
	else:
		if projectOpened == True:
			projCfg.set('SETTINGS', 'default_camera', selected_camera)
			with open(projCfgFilePath, 'w') as configfile:
				projCfg.write(configfile)
			projCfg.read(projCfgFilePath)
		else:
			appCfg.set('SETTINGS', 'default_camera', selected_camera)
			with open(appCfgFilePath, 'w') as configfile:
				appCfg.write(configfile)
			appCfg.read(appCfgFilePath)
		
		print("Default camera settings saved.\nDefault Camera: " + selected_camera)


def selectCamChunk():
	camCfgLoad()
	diaSelectCamera()
	if selected_camera == None:
		print("No camera chosen. Using default camera.")
	else:
		readCameraSettings(selected_camera)
		useCameraSettings()
		print("\n\nApplied custom camera: " + selected_camera)


# Routine for adding/editing camera configuration
def saveCamConfig(camorig, camname, camdesc, camtype, camsub, camres, camfile):
	if camCfg.has_section(camorig) == True:
		camCfg.remove_section(camorig)
		camCfg.add_section(camname)
		camCfg.set(camname, "Description", camdesc)
		camCfg.set(camname, "Type", camtype)
		camCfg.set(camname, "SubType", camsub)
		camCfg.set(camname, "Resolution", camres)
		camCfg.set(camname, "File", camfile)
		Metashape.app.messageBox("Camera added...\n" + "Name: " + camname + "\nDesc.: " + camdesc + "\nType: " + camtype + "\nSubType: " + camsub + "\nRes.:: " + camres + " MP\nFile: " + camfile)
	else:
		camCfg.add_section(camname)
		camCfg.set(camname, "Description", camdesc)
		camCfg.set(camname, "Type", camtype)
		camCfg.set(camname, "SubType", camsub)
		camCfg.set(camname, "Resolution", camres)
		camCfg.set(camname, "File", camfile)
		Metashape.app.messageBox("Camera added...\n" + "Name: " + camname + "\nDesc.: " + camdesc + "\nType: " + camtype + "\nSubType: " + camsub + "\nRes.:: " + camres + " MP\nFile: " + camfile)

	with open(camCfgFilePath, 'w') as configfile:
		camCfg.write(configfile)

	camCfgLoad()


# Routine for adding/editing camera configuration
def removeCamConfig(camname):
	cam_xmlmsg = ''
	if camCfg.has_section(camname) == True:
		if camCfg.get(camname, "File") != "":
			cameraXml = camCfgPath + camCfg.get(camname, "File")
			if os.path.isfile(cameraXml):
				os.remove(cameraXml)
				cam_xmlmsg = "\nXML file " + cameraXml + " deleted."

		camCfg.remove_section(camname)
		cam_secmsg = "Camera [" + camname + "] removed from settings." + cam_xmlmsg
		
		with open(camCfgFilePath, 'w') as configfile:
			camCfg.write(configfile)
		
		camCfgLoad()
		
		Metashape.app.messageBox(cam_secmsg)
	else:
		Metashape.app.messageBox("Error! No camera named (" + str(camname) + ") was found.\n\nDid you manualy edit comaera configuration?")


# # Change project data folder
# def dataFolderChange():
# 	settings.foldeData = Metashape.app.getExistingDirectory("Working data folder")
# 	settings.store()
# 	print("Working Folder: " + str(settings.foldeData))


# # Create new project routine - used when no project is present when user tries to add new chunk
# def novProjekt():
# 	global projectOpened
# 	doc = Metashape.app.document
# 	docPath = Metashape.app.getSaveFileName("Save new project", "",  "Metashape Project (*.psx)")
# 	try:
# 		doc.save(docPath)
# 		Metashape.app.messageBox("New project saved.\n")
# 		projCfgLoad()
# 		projectOpened = True
# 	except RuntimeError:
# 		Metashape.app.messageBox("Process canceled...")
# 		projectOpened = False
# 	
# 	Metashape.app.update()


# Class for settings editing UI
class Ui_settingsDialog(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"settingsDialog")
		self.resize(300, 100)
		self.setWindowTitle(u"AutoFTG Settings")
		
		icon = QIcon()
		icon.addFile(u":/icons/icons8-opened-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)

		# self.label = QtWidgets.QLabel()
		# self.label.setObjectName(u"label")
		# self.label.setGeometry(QRect(10, 10, 80, 16))
		# self.label.setText("Project Folder:")
		# self.lineProjFolder = QtWidgets.QLineEdit()
		# self.lineProjFolder.setObjectName(u"lineProjFolder")
		# self.lineProjFolder.setGeometry(QRect(10, 10, 280, 24))
		# self.lineProjFolder.setText(str(selected_data_folder))
		# self.lineProjFolder.setClearButtonEnabled(True)
		# self.btnProjFolder = QtWidgets.QPushButton()
		# self.btnProjFolder.setObjectName(u"btnProjFolder")
		# self.btnProjFolder.setGeometry(QRect(300, 10, 80, 24))
		# self.btnProjFolder.setText(u" Browse")
		# self.btnProjFolder.setIcon(icon)
		# self.btnProjFolder.setIconSize(QSize(21, 21))
		
		self.label_2 = QtWidgets.QLabel()
		self.label_2.setObjectName(u"label_2")
		self.label_2.setGeometry(QRect(10, 40, 80, 16))
		self.label_2.setText("Data Folder:")
		self.lineDataFolder = QtWidgets.QLineEdit()
		self.lineDataFolder.setObjectName(u"lineDataFolder")
		self.lineDataFolder.setGeometry(QRect(10, 40, 280, 24))
		self.lineDataFolder.setText(str(selected_data_folder))
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
		for camera in cam_list:
			self.comboBoxCamera.addItem(camera)
		self.comboBoxCamera.setCurrentText(str(selected_camera))
		
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
		# layout.setRowMinimumHeight(3, 24)
		layout.setVerticalSpacing(1)

		layout.setColumnMinimumWidth(1, 250) # minimum column width
		layout.setColumnMinimumWidth(2, 80) # minimum column width

		# layout.addWidget(self.label, 0, 0)
		# layout.addWidget(self.lineProjFolder, 0, 1)
		# layout.addWidget(self.btnProjFolder, 0, 2)

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

	# def projFolderChange(self):
	# 	folderExport = Metashape.app.getExistingDirectory("Export folder")
	# 	self.lineProjFolder.setText(folderExport)

	def dataFolderChange(self):
		foldeData = Metashape.app.getExistingDirectory("Data folder")
		self.lineDataFolder.setText(foldeData)

	def saveSettingsDialog(self):
		if projectOpened == False:
			# settings.folderProject = self.lineProjFolder.text()
			appCfg.set('SETTINGS', 'folder_data', self.lineDataFolder.text())
			appCfg.set('SETTINGS', 'default_camera', self.comboBoxCamera.currentText())
			with open(appCfgFilePath, 'w') as configfile:
				projCfg.write(configfile)
			appCfgLoad()
		else:
			projCfg.set('SETTINGS', 'folder_data', self.lineDataFolder.text())
			projCfg.set('SETTINGS', 'default_camera', self.comboBoxCamera.currentText())
			with open(projCfgFilePath, 'w') as configfile:
				projCfg.write(configfile)
			projCfgLoad
		
		print("New settings stored.")
		self.close()

# Routine for calling Edit Settings UI - called when user want's to edit settings
def editSettings():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	editDialog = Ui_settingsDialog(parent)


class Ui_DialogAddEditCam(QtWidgets.QDialog):
	def __init__(self, parent, camnew, camname):
		global cameraXmlSource
		global cameraXmlDest
		global camOrigName
		camOrigName = camname
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"DialogAddEditCam")
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
		icon = QIcon()
		icon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(icon)
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
			cameraXmlSource = ''
			cameraXmlDest = ''
			self.setWindowTitle(u"Add New Camera")
			self.pushButton_2.setText(u"Add Camera")
		else:
			selCamType = camCfg.get(camname, "Description")
			selCamType = camCfg.get(camname, "Type")
			selCamSubType = camCfg.get(camname, "SubType")
			selCamRes = camCfg.get(camname, "Resolution")
			selCamFile = camCfg.get(camname, "File")
			cameraXmlSource = selCamFile
			cameraXmlDest = selCamFile
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
		global cameraXmlSource
		global cameraXmlDest
		cameraXmlSource = Metashape.app.getOpenFileName(hint="Select Camera Calibration", dir=str(selected_data_folder), filter="Metashape Camera Calibration (*.xml)")
		camXmlFile = os.path.basename(cameraXmlSource)
		cameraXmlDest = camCfgPath + camXmlFile
		self.lineEdit_3.setText(camXmlFile)


	def saveCamera(self):
		global cameraXmlSource
		global cameraXmlDest
		cameraNameAdd = self.lineEdit_2.text()
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
			saveCamConfig(camOrigName, cameraNameAdd, cameraTypeAdd, cameraSubTypeAdd, cameraResAdd, cameraFileAdd)
			Metashape.app.messageBox("Camera settings saved.\n" + "Name: " + cameraNameAdd + "\nType: " + cameraTypeAdd + "\nFile: " + cameraFileAdd)
			camCfgLoad()
			cameraXmlSource = ''
			cameraXmlDest = ''
			self.close()


	def copyXml(self):
		if cameraXmlSource != cameraXmlDest:
			cameraXmlDestExists = os.path.isfile(cameraXmlDest)
			if cameraXmlDestExists == False:
				try:
					shutil.copy2(cameraXmlSource, cameraXmlDest)
				except:
					Metashape.app.messageBox("Error! Could not copy calibration file...")
			else:
				try:
					os.remove(cameraXmlDest)
				except:
					Metashape.app.messageBox("Error! Failed to remove old calibration file...")

				try:
					shutil.copy2(cameraXmlSource, cameraXmlDest)
				except:
					Metashape.app.messageBox("Error! Failed to copy calibration file...")


	def closeCameraDialog(self):
		camCfgLoad()
		self.close()


# Routine for calling Edit Settings UI - called when user want's to edit settings
def addCameraDialog(camnew, camname):
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	if camnew == False:
		dia = Ui_DialogAddEditCam(parent, camnew, camname)
	else:
		dia = Ui_DialogAddEditCam(parent, camnew, camname="")


class Ui_dialogCamGui(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"dialogCamGui")
		self.resize(350, 300)
		self.setWindowTitle(u"Cameras Editor")

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
		for camera in cam_list:
			cam_type = str(camCfg.get(camera, 'Type'))
			cam_stype = str(camCfg.get(camera, "SubType"))
			cam_res = str(camCfg.get(camera, 'Resolution'))
			self.listWidgetCamItem = QListWidgetItem(camera, self.listWidgetCam)
			self.listWidgetCamItem.setText(str(camera))
			if cam_stype == "Drone":
				self.listWidgetCamItem.setIcon(menuico5)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")
			elif cam_stype == "SmartPhone":
				self.listWidgetCamItem.setIcon(menuico4)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")
			elif cam_type == "Fisheye":
				self.listWidgetCamItem.setIcon(menuico1)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")
			elif cam_type == "Cylindrical":
				self.listWidgetCamItem.setIcon(menuico2)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")
			elif cam_type == "Spherical":
				self.listWidgetCamItem.setIcon(menuico3)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")
			elif cam_type == "RPC":
				self.listWidgetCamItem.setIcon(menuico9)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")
			else:
				self.listWidgetCamItem.setIcon(menuico00)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")

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
		# # for camera in cam_list:
		# # 	self.listWidgetCam.addItem(camera)
		for camera in cam_list:
			cam_type = str(camCfg.get(camera, 'Type'))
			cam_stype = str(camCfg.get(camera, "SubType"))
			cam_res = str(camCfg.get(camera, 'Resolution'))
			self.listWidgetCamItem = QListWidgetItem(camera, self.listWidgetCam)
			self.listWidgetCamItem.setText(str(camera))
			if cam_stype == "Drone":
				menuico5 = QIcon()
				menuico5.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
				self.listWidgetCamItem.setIcon(menuico5)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")
			elif cam_stype == "SmartPhone":
				menuico4 = QIcon()
				menuico4.addFile(u":/icons/icons8-touchscreen-48.png", QSize(), QIcon.Normal, QIcon.Off)
				self.listWidgetCamItem.setIcon(menuico4)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")
			elif cam_type == "Fisheye":
				menuico1 = QIcon()
				menuico1.addFile(u":/icons/icons8-panorama-50.png", QSize(), QIcon.Normal, QIcon.Off)
				self.listWidgetCamItem.setIcon(menuico1)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")
			elif cam_type == "Cylindrical":
				menuico2 = QIcon()
				menuico2.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
				self.listWidgetCamItem.setIcon(menuico2)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")
			elif cam_type == "Spherical":
				menuico3 = QIcon()
				menuico3.addFile(u":/icons/icons8-video-stabilization-50.png", QSize(), QIcon.Normal, QIcon.Off)
				self.listWidgetCamItem.setIcon(menuico3)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")
			elif cam_type == "RPC":
				menuico9 = QIcon()
				menuico9.addFile(u":/icons/icons8-ios-application-placeholder-50.png", QSize(), QIcon.Normal, QIcon.Off)
				self.listWidgetCamItem.setIcon(menuico9)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")
			else:
				menuico00 = QIcon()
				menuico00.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
				self.listWidgetCamItem.setIcon(menuico00)
				self.listWidgetCamItem.setToolTip("Type: " + cam_type + "\nSubType: " + cam_stype + "\nRes.: " + cam_res + "MP")


	def addNewCam(self):
		addCameraDialog(camnew=True, camname="")
		self.refreshCamList()


	def editSelCamera(self):
		# defaultItem = self.listWidgetCam.isItemSelected("Default")
		if self.listWidgetCam.currentRow() > 1:
			selCamName = self.listWidgetCam.currentItem().text()
			addCameraDialog(camnew=False, camname=selCamName)
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
				removeCamConfig(del_cam)
			self.refreshCamList()

		elif self.listWidgetCam.currentRow() <= 1:
			Metashape.app.messageBox("Default cameras can not be removed.")

		else:
			Metashape.app.messageBox("No camera selected...")


# Routine for calling Edit Settings UI - called when user want's to edit settings
def camerasEditor():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	camEditDialog = Ui_dialogCamGui(parent)


class Ui_dialogChooseCamera(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"dialogChooseCamera")
		self.resize(320, 300)
		self.setWindowTitle(u"Choose Camera")
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
		font1 = QFont()
		font1.setPointSize(10)
		for cam in cam_list:
			icon_type = camCfg.get(cam, "Type")
			icon_subtype = camCfg.get(cam, "SubType")
			self.listwidget = QListWidgetItem(self.listWidget)
			self.listwidget.setText(cam)
			if icon_subtype == "SmartPhone":
				self.listwidget.setIcon(icon4)
			elif icon_subtype == "Drone":
				self.listwidget.setIcon(icon5)
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

		self.listWidget.setCurrentRow(cam_list.index(selected_camera))

		self.listWidget.setSortingEnabled(False)

		QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.selectCam)
		QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))

		self.exec()

	def selectCam(self):
		global selected_camera
		selected_camera = self.listWidget.currentItem().text()
		self.close()


# Routine for calling Edit Settings UI - called when user want's to edit settings
def diaSelectCamera():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	diaChCam = Ui_dialogChooseCamera(parent)


# Class for Copy Region UI
class CopyBoundingBoxDlg(QtWidgets.QDialog):

	def __init__(self, parent):

		QtWidgets.QDialog.__init__(self, parent)
		self.setWindowTitle("Kopiranje Regije")

		self.labelFrom = QtWidgets.QLabel("Iz Chunk")
		self.labelTo = QtWidgets.QLabel("V Chunk")

		self.fromChunk = QtWidgets.QComboBox()
		for chunk in Metashape.app.document.chunks:
			self.fromChunk.addItem(chunk.label)

		self.toChunks = QtWidgets.QListWidget()
		self.toChunks.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
		for chunk in Metashape.app.document.chunks:
			self.toChunks.addItem(chunk.label)

		self.btnOk = QtWidgets.QPushButton("Kopiraj")
		self.btnOk.setFixedSize(120, 36)
		self.btnOk.setToolTip("Kopiranje regije na vse izbrane chunke:")

		self.btnQuit = QtWidgets.QPushButton("Prekini")
		self.btnQuit.setFixedSize(80, 36)

		layout = QtWidgets.QGridLayout()  # creating layout
		layout.setColumnMinimumWidth(0, 80) # minimum column width
		layout.setColumnMinimumWidth(1, 180) # minimum column width
		layout.addWidget(self.labelFrom, 0, 0)
		layout.addWidget(self.fromChunk, 0, 1)

		layout.addWidget(self.labelTo, 1, 0)
		layout.addWidget(self.toChunks, 1, 1, 20, 2)

		layout.addWidget(self.btnQuit, 30, 0)
		layout.addWidget(self.btnOk, 30, 1)

		self.setLayout(layout)

		QtCore.QObject.connect(self.btnOk, QtCore.SIGNAL("clicked()"), self.copyBoundingBox)
		QtCore.QObject.connect(self.btnQuit, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))

		self.exec()


	def copyBoundingBox(self):
		print("Copy region bounding box...")

		doc = Metashape.app.document

		fromChunk = doc.chunks[self.fromChunk.currentIndex()]

		toChunks = []
		for i in range(self.toChunks.count()):
			if self.toChunks.item(i).isSelected():
				toChunks.append(doc.chunks[i])

		print("Copy region from/to: '" + fromChunk.label + "' to " + str(len(toChunks)))

		T0 = fromChunk.transform.matrix

		region = fromChunk.region
		R0 = region.rot
		C0 = region.center
		s0 = region.size

		for chunk in toChunks:

			if chunk == fromChunk:
				continue

			T = chunk.transform.matrix.inv() * T0

			R = Metashape.Matrix([[T[0, 0], T[0, 1], T[0, 2]],
								  [T[1, 0], T[1, 1], T[1, 2]],
								  [T[2, 0], T[2, 1], T[2, 2]]])

			scale = R.row(0).norm()
			R = R * (1 / scale)
			
			new_region = Metashape.Region()
			new_region.rot = R * R0
			c = T.mulp(C0)
			new_region.center = c
			new_region.size = s0 * scale / 1.

			chunk.region = new_region
		
		print("Process complete!\n\nFrom: " + fromChunk.label + " / To: " + str(len(toChunks)) + "\n")
		self.reject()
		

# Routine for calling Copy Regions UI
def copy_bbox():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()

	dlg = CopyBoundingBoxDlg(parent)


# Show progress of processing
def progress_print(p):
		print('Completed: {:.2f}%'.format(p))


# Detect markers and import coords
def marker_targets():
	doc = Metashape.app.document
	chunk = doc.chunk
	netpath = Metashape.app.document.path
	netroot = path.dirname(netpath)
	nadaljujem = Metashape.app.getBool("Start marker detection?")

	if nadaljujem == True:
		chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
		Metashape.app.messageBox("Marker detection finished.\n\nIn next step choose file containing marker coordinates.\n\nFile must contain header, coordinates are expected starting at line 7.")
		path_ref = Metashape.app.getOpenFileName("Import coordinates " + chunk.label, netroot, "Text file (*.txt)")
		chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
		chunk.updateTransform()	
		Metashape.app.messageBox("Target coordinates imported.\n\nNext step: Workflow > Align Photos")
		Metashape.app.update()
		doc.save()


# Routine for finding files - used when creating new chunk
def find_files(folder, types):
	return [entry.path for entry in os.scandir(folder) if (entry.is_file() and os.path.splitext(entry.name)[1].lower() in types)]


class Ui_DialogAddChunkQuick(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"DialogAddChunkQuick")
		self.resize(310, 155)
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
		for section in chunk_sections:
			menu_icon = menuCfg.get(section, "menu_icon")
			seticon = QIcon()
			seticon.addFile(menu_icon, QSize(), QIcon.Normal, QIcon.Off)
			self.cbChunkSettings.addItem(seticon, section)
		
		
		self.cbChunkSettings.setObjectName(u"cbChunkSettings")
		sizePolicy.setHeightForWidth(self.cbChunkSettings.sizePolicy().hasHeightForWidth())
		self.cbChunkSettings.setSizePolicy(sizePolicy)
		font2 = QFont()
		font2.setFamily(u"Segoe UI")
		font2.setPointSize(11)
		self.cbChunkSettings.setFont(font2)
		self.cbChunkSettings.setCursor(QCursor(Qt.PointingHandCursor))

		self.cbChunkSettings.setCurrentText(u"Default")
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
		selected_pre = menuCfg.get(selected_menu, "chunk_name_prefix")
		selected_suf = menuCfg.get(selected_menu, "chunk_name_suffix")
		selected_workfolder = menuCfg.get(selected_menu, "work_folder")

		if self.checkBoxAutoProc.isChecked == False:
			self.accept()
			newchunk_manual(selected_pre, selected_suf, selected_workfolder)
		else:
			self.accept()
			newchunk_auto(selected_pre, selected_suf, selected_workfolder)		


def diaAddChunkQuick():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	dia = Ui_DialogAddChunkQuick(parent)


class Ui_DialogBatchChunk(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.sel_items = []
		self.setObjectName(u"DialogBatchChunk")
		self.setWindowTitle(u"Batch Chunk Creator")
		self.resize(680, 520)
		self.verticalLayoutWidget = QWidget(self)
		self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
		self.verticalLayoutWidget.setGeometry(QRect(10, 0, 661, 511))
		self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setSpacing(5)
		self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_2.setObjectName(u"verticalLayout_2")
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_9 = QHBoxLayout()
		self.horizontalLayout_9.setSpacing(5)
		self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
		self.label_15 = QLabel(self.verticalLayoutWidget)
		self.label_15.setObjectName(u"label_15")
		sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
		self.label_15.setSizePolicy(sizePolicy)
		self.label_15.setMaximumSize(QSize(32, 32))
		self.label_15.setPixmap(QPixmap(u":/icons/icons8-apps-tab-50.png"))
		self.label_15.setScaledContents(True)

		self.horizontalLayout_9.addWidget(self.label_15)

		self.label_3 = QLabel(self.verticalLayoutWidget)
		self.label_3.setObjectName(u"label_3")
		sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		sizePolicy1.setHorizontalStretch(0)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
		self.label_3.setSizePolicy(sizePolicy1)
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(16)
		self.label_3.setFont(font)
		self.label_3.setText(u"Batch Chunk Creator")

		self.horizontalLayout_9.addWidget(self.label_3)


		self.verticalLayout_2.addLayout(self.horizontalLayout_9)

		self.line_4 = QFrame(self.verticalLayoutWidget)
		self.line_4.setObjectName(u"line_4")
		self.line_4.setFrameShape(QFrame.HLine)
		self.line_4.setFrameShadow(QFrame.Sunken)

		self.verticalLayout_2.addWidget(self.line_4)

		self.gridLayout = QGridLayout()
		self.gridLayout.setSpacing(5)
		self.gridLayout.setObjectName(u"gridLayout")
		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setSpacing(5)
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.label_2 = QLabel(self.verticalLayoutWidget)
		self.label_2.setObjectName(u"label_2")
		sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
		sizePolicy2.setHorizontalStretch(0)
		sizePolicy2.setVerticalStretch(0)
		sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
		self.label_2.setSizePolicy(sizePolicy2)
		font1 = QFont()
		font1.setFamily(u"Segoe UI")
		font1.setPointSize(11)
		font1.setBold(True)
		font1.setWeight(75)
		self.label_2.setFont(font1)
		self.label_2.setText(u"Data location")

		self.horizontalLayout_2.addWidget(self.label_2)

		self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_4.setObjectName(u"checkBox_4")
		sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
		sizePolicy3.setHorizontalStretch(0)
		sizePolicy3.setVerticalStretch(0)
		sizePolicy3.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
		self.checkBox_4.setSizePolicy(sizePolicy3)
#if QT_CONFIG(statustip)
		self.checkBox_4.setToolTip(u"Disable to set custom location for data. Enable to use project default data location settings.")
#endif // QT_CONFIG(statustip)
		self.checkBox_4.setText(u"Use Project Data Location")
		icon = QIcon()
		icon.addFile(u":/icons/icons8-copy-to-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_4.setIcon(icon)
		self.checkBox_4.setIconSize(QSize(20, 20))
		self.checkBox_4.setChecked(True)

		self.horizontalLayout_2.addWidget(self.checkBox_4)


		self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

		self.gridLayout_3 = QGridLayout()
		self.gridLayout_3.setSpacing(5)
		self.gridLayout_3.setObjectName(u"gridLayout_3")
		self.horizontalLayout_3 = QHBoxLayout()
		self.horizontalLayout_3.setSpacing(5)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.label_10 = QLabel(self.verticalLayoutWidget)
		self.label_10.setObjectName(u"label_10")
		sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
		sizePolicy4.setHorizontalStretch(0)
		sizePolicy4.setVerticalStretch(0)
		sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
		self.label_10.setSizePolicy(sizePolicy4)
		font2 = QFont()
		font2.setFamily(u"Segoe UI")
		font2.setPointSize(9)
		font2.setBold(True)
		font2.setWeight(75)
		self.label_10.setFont(font2)
		self.label_10.setText(u"Suffix:")

		self.horizontalLayout_3.addWidget(self.label_10)

		self.label_7 = QLabel(self.verticalLayoutWidget)
		self.label_7.setObjectName(u"label_7")
		sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
		self.label_7.setSizePolicy(sizePolicy2)
		self.label_7.setFrameShape(QFrame.StyledPanel)
		self.label_7.setText(u"Suffix...")

		self.horizontalLayout_3.addWidget(self.label_7)


		self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

		self.horizontalLayout_6 = QHBoxLayout()
		self.horizontalLayout_6.setSpacing(5)
		self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
		self.label_9 = QLabel(self.verticalLayoutWidget)
		self.label_9.setObjectName(u"label_9")
		sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
		self.label_9.setSizePolicy(sizePolicy4)
		self.label_9.setFont(font2)
		self.label_9.setFrameShape(QFrame.NoFrame)
		self.label_9.setText(u"Type:	  ")

		self.horizontalLayout_6.addWidget(self.label_9)

		self.label_12 = QLabel(self.verticalLayoutWidget)
		self.label_12.setObjectName(u"label_12")
		sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
		self.label_12.setSizePolicy(sizePolicy2)
		self.label_12.setFrameShape(QFrame.StyledPanel)
		self.label_12.setText(u"TextLabel")

		self.horizontalLayout_6.addWidget(self.label_12)


		self.gridLayout_3.addLayout(self.horizontalLayout_6, 7, 0, 1, 1)

		self.horizontalLayout_5 = QHBoxLayout()
		self.horizontalLayout_5.setSpacing(5)
		self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
		self.label_11 = QLabel(self.verticalLayoutWidget)
		self.label_11.setObjectName(u"label_11")
		sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
		self.label_11.setSizePolicy(sizePolicy4)
		self.label_11.setFont(font2)
		self.label_11.setText(u"Prefix:")

		self.horizontalLayout_5.addWidget(self.label_11)

		self.label_6 = QLabel(self.verticalLayoutWidget)
		self.label_6.setObjectName(u"label_6")
		sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
		self.label_6.setSizePolicy(sizePolicy2)
		self.label_6.setFrameShape(QFrame.StyledPanel)
		
		self.horizontalLayout_5.addWidget(self.label_6)


		self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

		self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
		self.comboBox_2.setObjectName(u"comboBox_2")
		
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
		for cam in cam_list:
			icon_type = camCfg.get(cam, "Type")
			icon_subtype = camCfg.get(cam, "SubType")
			#self.listwidget = QListWidgetItem(self.listWidget)
			#self.listwidget.setText(cam)
			if icon_subtype == "SmartPhone":
				self.comboBox_2.addItem(icon4, cam)
			elif icon_subtype == "Drone":
				self.comboBox_2.addItem(icon5, cam)
			else:
				if icon_type == "Fisheye":
					self.comboBox_2.addItem(icon1, cam)
				elif icon_type == "Spherical":
					self.comboBox_2.addItem(icon3, cam)
				elif icon_type == "Cylindrical":
					self.comboBox_2.addItem(icon2, cam)
				elif icon_type == "RPC":
					self.comboBox_2.addItem(icon5a, cam)
				else:
					self.comboBox_2.addItem(icon, cam)

		self.comboBox_2.setCurrentText(selected_camera)
		sizePolicy2.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
		self.comboBox_2.setSizePolicy(sizePolicy2)
		font3 = QFont()
		font3.setFamily(u"Segoe UI")
		font3.setPointSize(11)
		self.comboBox_2.setFont(font3)
		self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.comboBox_2.setToolTip(u"Choose camera settings to be applied when creating new chunk...")
#endif // QT_CONFIG(statustip)
		self.comboBox_2.setIconSize(QSize(20, 20))

		self.gridLayout_3.addWidget(self.comboBox_2, 6, 0, 1, 1)

		self.checkBox = QCheckBox(self.verticalLayoutWidget)
		self.checkBox.setObjectName(u"checkBox")
		sizePolicy2.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
		self.checkBox.setSizePolicy(sizePolicy2)
		font4 = QFont()
		font4.setFamily(u"Segoe UI")
		font4.setPointSize(9)
		self.checkBox.setFont(font4)
		self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Marker coordinates will be imported after target detection. <span style=\" font-weight:600;\">*</span></p><p><span style=\" font-weight:600;\">Disabled:</span> Coordinates are not imported. User must manually import coordinates.</p><p><span style=\" font-weight:600;\">*</span> Automatic importing of marker coordinates only works if point file name is the same as it's parent folder name, and contains a header with metadata. Point coordinates should start at row #7.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox.setText(u"Import Marker Coordinates")
		icon7 = QIcon()
		icon7.addFile(u":/icons/icons8-map-marker-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox.setIcon(icon7)
		self.checkBox.setIconSize(QSize(20, 20))
		self.checkBox.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox, 12, 0, 1, 1)

		self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_2.setObjectName(u"checkBox_2")
		sizePolicy2.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
		self.checkBox_2.setSizePolicy(sizePolicy2)
		self.checkBox_2.setFont(font4)
		self.checkBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_2.setToolTip(u"<html><head/><body><p>Enable automatic target detection when new chunk is created...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_2.setText(u"Automatic Target Detection")
		icon8 = QIcon()
		icon8.addFile(u":/icons/icons8-my-location-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_2.setIcon(icon8)
		self.checkBox_2.setIconSize(QSize(20, 20))
		self.checkBox_2.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox_2, 11, 0, 1, 1)

		self.cbChunkSettings = QComboBox(self.verticalLayoutWidget)
		for section in chunk_sections:
			menu_icon = menuCfg.get(section, "menu_icon")
			seticon = QIcon()
			seticon.addFile(menu_icon, QSize(), QIcon.Normal, QIcon.Off)
			self.cbChunkSettings.addItem(seticon, section)
		# icon9 = QIcon()
		# icon9.addFile(u":/icons/icons8-add-tab-50.png", QSize(), QIcon.Normal, QIcon.Off)
		# self.cbChunkSettings.addItem(icon9, u"Default")
		# icon10 = QIcon()
		# icon10.addFile(u":/icons/kalota_m.png", QSize(), QIcon.Normal, QIcon.Off)
		# self.cbChunkSettings.addItem(icon10, u"T8 GC - KALOTA")
		# icon11 = QIcon()
		# icon11.addFile(u":/icons/stopnca_o.png", QSize(), QIcon.Normal, QIcon.Off)
		# self.cbChunkSettings.addItem(icon11, u"STOPNICA - IZKOP")
		# icon12 = QIcon()
		# icon12.addFile(u":/icons/stopnca_s.png", QSize(), QIcon.Normal, QIcon.Off)
		# self.cbChunkSettings.addItem(icon12, u"STOPNICA - B.BET.")
		self.cbChunkSettings.setObjectName(u"cbChunkSettings")
		sizePolicy2.setHeightForWidth(self.cbChunkSettings.sizePolicy().hasHeightForWidth())
		self.cbChunkSettings.setSizePolicy(sizePolicy2)
		self.cbChunkSettings.setFont(font3)
		self.cbChunkSettings.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.cbChunkSettings.setToolTip(u"Choose settings used for chunk creation...")
#endif // QT_CONFIG(statustip)
		self.cbChunkSettings.setIconSize(QSize(20, 20))
		self.cbChunkSettings.setCurrentIndex(0)

		self.gridLayout_3.addWidget(self.cbChunkSettings, 1, 0, 1, 1)

		self.label_4 = QLabel(self.verticalLayoutWidget)
		self.label_4.setObjectName(u"label_4")
		sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
		self.label_4.setSizePolicy(sizePolicy2)
		self.label_4.setMaximumSize(QSize(16777215, 25))
		self.label_4.setFont(font1)
		self.label_4.setText(u"Camera")
		self.label_4.setAlignment(Qt.AlignCenter)

		self.gridLayout_3.addWidget(self.label_4, 5, 0, 1, 1)

		self.line_6 = QFrame(self.verticalLayoutWidget)
		self.line_6.setObjectName(u"line_6")
		self.line_6.setFrameShape(QFrame.HLine)
		self.line_6.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line_6, 4, 0, 1, 1)

		self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_3.setObjectName(u"checkBox_3")
		font5 = QFont()
		font5.setFamily(u"Segoe UI")
		font5.setPointSize(10)
		self.checkBox_3.setFont(font5)
		self.checkBox_3.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_3.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Automatic chunk creation with predefined settings</p><p><span style=\" font-weight:600;\">Disabled:</span> Manual confirmation of intermediate steps</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_3.setText(u"Automatic Processing")
		icon13 = QIcon()
		icon13.addFile(u":/icons/icons8-in-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_3.setIcon(icon13)
		self.checkBox_3.setIconSize(QSize(20, 20))
		self.checkBox_3.setCheckable(True)
		self.checkBox_3.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox_3, 14, 0, 1, 1)

		self.label_5 = QLabel(self.verticalLayoutWidget)
		self.label_5.setObjectName(u"label_5")
		sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
		self.label_5.setSizePolicy(sizePolicy2)
		self.label_5.setMaximumSize(QSize(16777215, 25))
		self.label_5.setFont(font1)
		self.label_5.setText(u"Markers")
		self.label_5.setAlignment(Qt.AlignCenter)

		self.gridLayout_3.addWidget(self.label_5, 10, 0, 1, 1)

		self.horizontalLayout_7 = QHBoxLayout()
		self.horizontalLayout_7.setSpacing(5)
		self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
		self.label_13 = QLabel(self.verticalLayoutWidget)
		self.label_13.setObjectName(u"label_13")
		sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
		self.label_13.setSizePolicy(sizePolicy4)
		self.label_13.setFont(font2)
		self.label_13.setText(u"SubType:")

		self.horizontalLayout_7.addWidget(self.label_13)

		self.label_14 = QLabel(self.verticalLayoutWidget)
		self.label_14.setObjectName(u"label_14")
		sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
		self.label_14.setSizePolicy(sizePolicy2)
		self.label_14.setFrameShape(QFrame.StyledPanel)
		self.label_14.setText(u"TextLabel")
		
		self.horizontalLayout_7.addWidget(self.label_14)


		self.gridLayout_3.addLayout(self.horizontalLayout_7, 8, 0, 1, 1)

		self.label = QLabel(self.verticalLayoutWidget)
		self.label.setObjectName(u"label")
		sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy2)
		self.label.setMaximumSize(QSize(16777215, 25))
		self.label.setFont(font1)
		self.label.setText(u"Chunk Creation")
		self.label.setAlignment(Qt.AlignCenter)

		self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

		self.line = QFrame(self.verticalLayoutWidget)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line, 9, 0, 1, 1)

		self.line_3 = QFrame(self.verticalLayoutWidget)
		self.line_3.setObjectName(u"line_3")
		self.line_3.setFrameShape(QFrame.HLine)
		self.line_3.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line_3, 13, 0, 1, 1)


		self.gridLayout.addLayout(self.gridLayout_3, 0, 2, 3, 1)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setSpacing(5)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.lineEdit = QLineEdit(self.verticalLayoutWidget)
		self.lineEdit.setObjectName(u"lineEdit")
		self.lineEdit.setEnabled(False)
		sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy5.setHorizontalStretch(0)
		sizePolicy5.setVerticalStretch(0)
		sizePolicy5.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
		self.lineEdit.setSizePolicy(sizePolicy5)
		self.lineEdit.setFont(font5)
		self.lineEdit.setToolTip(u"Path to main folder with data sub-folders...")
		self.lineEdit.setWhatsThis(u"Path to main folder with data sub-folders...")
		self.lineEdit.setPlaceholderText(u"Data location...")

		self.horizontalLayout.addWidget(self.lineEdit)

		self.pushButton = QPushButton(self.verticalLayoutWidget)
		self.pushButton.setObjectName(u"pushButton")
		self.pushButton.setEnabled(False)
		sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
		self.pushButton.setSizePolicy(sizePolicy3)
		self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton.setToolTip(u"Data location (root folder with sub-folders containing data)")
		self.pushButton.setText(u"Browse")
		icon14 = QIcon()
		icon14.addFile(u":/icons/icons8-images-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton.setIcon(icon14)
		self.pushButton.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton)


		self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

		self.horizontalLayout_4 = QHBoxLayout()
		self.horizontalLayout_4.setSpacing(5)
		self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
		self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_3.setObjectName(u"pushButton_3")
		self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_3.setToolTip(u"Press [Ctrl+P] to start processing")
		self.pushButton_3.setToolTip(u"Process selected folders, and create new chunks...")
		self.pushButton_3.setText(u"Process")
		icon15 = QIcon()
		icon15.addFile(u":/icons/icons8-synchronize-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_3.setIcon(icon15)
		self.pushButton_3.setIconSize(QSize(24, 24))
		self.pushButton_3.setShortcut(u"P")
		self.pushButton_3.setChecked(False)

		self.horizontalLayout_4.addWidget(self.pushButton_3)

		self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_2.setObjectName(u"pushButton_2")
		self.pushButton_2.setToolTip(u"Exit chunk creator...")
		self.pushButton_2.setText(u"Exit")
		icon16 = QIcon()
		icon16.addFile(u":/icons/icons8-enter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_2.setIcon(icon16)
		self.pushButton_2.setIconSize(QSize(24, 24))
		self.pushButton_2.setShortcut(u"X")

		self.horizontalLayout_4.addWidget(self.pushButton_2)


		self.gridLayout.addLayout(self.horizontalLayout_4, 3, 2, 1, 1)

		self.line_5 = QFrame(self.verticalLayoutWidget)
		self.line_5.setObjectName(u"line_5")
		self.line_5.setFrameShape(QFrame.VLine)
		self.line_5.setFrameShadow(QFrame.Sunken)

		self.gridLayout.addWidget(self.line_5, 0, 1, 4, 1)

		self.label_8 = QLabel(self.verticalLayoutWidget)
		self.label_8.setObjectName(u"label_8")
		self.label_8.setFrameShape(QFrame.StyledPanel)
		self.label_8.setText(u"Selected: ")
		self.label_8.setIndent(5)

		self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

		self.treeWidget = QTreeWidget(self.verticalLayoutWidget)
		icon17 = QIcon()
		icon17.addFile(u":/icons/icons8-folder-tree-50.png", QSize(), QIcon.Normal, QIcon.Off)
		font6 = QFont()
		font6.setBold(True)
		font6.setWeight(75)
		__qtreewidgetitem = QTreeWidgetItem()
		__qtreewidgetitem.setText(0, u"Folders");
		__qtreewidgetitem.setFont(0, font6);
		__qtreewidgetitem.setIcon(0, icon17);
		self.treeWidget.setHeaderItem(__qtreewidgetitem)
		icon18 = QIcon()
		icon18.addFile(u":/icons/icons8-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		font7 = QFont()
		font7.setFamily(u"Segoe UI")
		self.treeWidget.setObjectName(u"treeWidget")
		sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
		sizePolicy6.setHorizontalStretch(0)
		sizePolicy6.setVerticalStretch(0)
		#sizePolicy6.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
		self.treeWidget.setSizePolicy(sizePolicy6)
		self.treeWidget.setMinimumSize(QSize(380, 0))
		#self.treeWidget.setMaximumSize(QSize(400, 16777215))
		self.treeWidget.setAutoScrollMargin(20)
		self.treeWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
		self.treeWidget.setTabKeyNavigation(True)
		self.treeWidget.setProperty("showDropIndicator", False)
		self.treeWidget.setAlternatingRowColors(True)
		self.treeWidget.setSelectionMode(QAbstractItemView.MultiSelection)
		self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
		self.treeWidget.setUniformRowHeights(True)
		self.treeWidget.setSortingEnabled(True)
		self.treeWidget.setAllColumnsShowFocus(True)
		self.treeWidget.header().setVisible(True)
		self.treeWidget.header().setDefaultSectionSize(200)

		self.gridLayout.addWidget(self.treeWidget, 2, 0, 1, 1)

		self.verticalLayout_2.addLayout(self.gridLayout)
		
		defChk = self.cbChunkSettings.currentText()
		self.label_6.setText(menuCfg.get(defChk, "chunk_name_prefix"))
		self.label_7.setText(menuCfg.get(defChk, "chunk_name_suffix"))

		defCam = self.comboBox_2.currentText()
		self.label_12.setText(camCfg.get(defCam, "type"))
		self.label_14.setText(camCfg.get(defCam, "subtype"))
		
		self.checkBox_4.toggled.connect(self.pushButton.setDisabled)
		self.checkBox_4.toggled.connect(self.lineEdit.setDisabled)
		self.checkBox_2.toggled.connect(self.checkBox.toggle)
		self.cbChunkSettings.currentTextChanged.connect(self.setCurrentSettings)
		self.comboBox_2.currentTextChanged.connect(self.setCurrentCamera)
		self.lineEdit.textChanged.connect(self.updateFolders)
		self.pushButton_2.clicked.connect(self.quitChunkBatch)
		self.pushButton_3.clicked.connect(self.processBatch)
		self.pushButton.clicked.connect(self.browseFolder)
		self.treeWidget.itemSelectionChanged.connect(self.updateSelected)

		# QtCore.QObject.connect(self.cbChunkSettings, QtCore.SIGNAL("currentTextChanged()"), self.lineEdit, QtCore.SLOT("setText()"))
		# QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.startProcess)
		# QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.startProcess)
		# QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))			
		
		self.exec()

	def browseFolder(self):
		defFolder = Metashape.app.getExistingDirectory("Data folder")
		self.lineEdit.setText(defFolder)


	def setCurrentSettings(self):
		chunkSet = self.cbChunkSettings.currentText()
		if chunkSet == "Default":
			self.lineEdit.clear()
			self.pushButton.setEnabled
			self.lineEdit.setEnabled
			self.checkBox_4.setChecked(False)
			self.label_6.setText(menuCfg.get(chunkSet, "chunk_name_prefix"))
			self.label_7.setText(menuCfg.get(chunkSet, "chunk_name_suffix"))
		else:
			self.lineEdit.setText(str(menuCfg.get(chunkSet, "work_folder")))
			self.pushButton.setDisabled
			self.lineEdit.setDisabled
			self.checkBox_4.setChecked(True)
			self.label_6.setText(menuCfg.get(chunkSet, "chunk_name_prefix"))
			self.label_7.setText(menuCfg.get(chunkSet, "chunk_name_suffix"))


	def setCurrentCamera(self):
		chunkCam = self.comboBox_2.currentText()
		self.label_12.setText(camCfg.get(chunkCam, "type"))
		self.label_14.setText(camCfg.get(chunkCam, "subtype"))
		

	def updateFolders(self):
		self.treeWidget.clear()
		open_folder = self.lineEdit.text()
		if open_folder != "":
			open_folder = self.lineEdit.text().replace("\\", "/") + "/"
			icon17 = QIcon()
			icon17.addFile(u":/icons/icons8-folder-tree-50.png", QSize(), QIcon.Normal, QIcon.Off)
			icon18 = QIcon()
			icon18.addFile(u":/icons/icons8-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
			font6 = QFont()
			font6.setBold(True)
			font6.setWeight(75)
			__qtreewidgetitem = QTreeWidgetItem()
			__qtreewidgetitem.setText(0, u"Folders");
			__qtreewidgetitem.setFont(0, font6);
			__qtreewidgetitem.setIcon(0, icon17);
			self.treeWidget.setHeaderItem(__qtreewidgetitem)
			folder_list = next(os.walk(open_folder))[1]
			
			for folder in folder_list:
				__qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
				__qtreewidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
				__qtreewidgetitem1.setText(0, folder);
				__qtreewidgetitem1.setIcon(0, icon18);

		else:
			icon17 = QIcon()
			icon17.addFile(u":/icons/icons8-folder-tree-50.png", QSize(), QIcon.Normal, QIcon.Off)
			font6 = QFont()
			font6.setBold(True)
			font6.setWeight(75)
			__qtreewidgetitem = QTreeWidgetItem()
			__qtreewidgetitem.setText(0, u"Folders");
			__qtreewidgetitem.setFont(0, font6);
			__qtreewidgetitem.setIcon(0, icon17);
			self.treeWidget.setHeaderItem(__qtreewidgetitem)
		

	def updateSelected(self):
		sel_items = self.treeWidget.selectedItems()
		sel_count = len(sel_items)
		self.label_8.setText(u"Selected: " + str(sel_count))


	def processBatch(self):
		self.sel_items = self.treeWidget.selectedItems()
		sel_count = len(self.sel_items)
		item_menu = self.cbChunkSettings.currentText()
		item_pre = menuCfg.get(item_menu, "chunk_name_prefix")
		item_suf = menuCfg.get(item_menu, "chunk_name_suffix")
		item_cam = self.comboBox_2.currentText()
		if sel_count > 0:
			i_cnt = 1
			for item in self.sel_items:
				print("Processing item: " + str(i_cnt) + "/" + str(sel_count) + " - " + str(item.text(0)))
				doc = Metashape.app.document
				netpath = Metashape.app.document.path
				netroot = self.lineEdit.text()
				image_folder = str(netroot).replace("\\", "/") + "/" + item.text(0)
				photos = find_files(image_folder, [".jpg", ".jpeg", ".png", ".tif", ".tiff"])
				chunk = doc.addChunk()
				chunk.addPhotos(photos)
				chunk_name = item_pre + item.text(0) + item_suf
				# chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
				chunk.label = chunk_name
				doc.chunk = chunk
				doc.save(netpath)
				Metashape.app.update()
				# Metashape.app.messageBox("Nalaganje slik...")
				time.sleep(3)
				readCameraSettings(item_cam)
				useCameraSettings()
				chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
				# path_ref = Metashape.app.getOpenFileName("Import marker coordinates", image_folder, "Text file (*.txt)")
				points_file = image_folder + "/" + item.text(0) + ".txt"
				chunk.importReference(points_file, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
				chunk.updateTransform()
				doc.save(netpath)
				Metashape.app.update()
				i_cnt = i_cnt + 1


	def quitChunkBatch(self):
		self.reject()


def diaAddChunkBatch():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	dia2 = Ui_DialogBatchChunk(parent)


class Ui_DialogBatchChunk(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.sel_items = []
		self.setObjectName(u"DialogBatchChunk")
		self.setWindowTitle(u"Batch Chunk Creator")
		self.resize(680, 520)
		self.verticalLayoutWidget = QWidget(self)
		self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
		self.verticalLayoutWidget.setGeometry(QRect(10, 0, 661, 511))
		self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setSpacing(5)
		self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_2.setObjectName(u"verticalLayout_2")
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_9 = QHBoxLayout()
		self.horizontalLayout_9.setSpacing(5)
		self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
		self.label_15 = QLabel(self.verticalLayoutWidget)
		self.label_15.setObjectName(u"label_15")
		sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
		self.label_15.setSizePolicy(sizePolicy)
		self.label_15.setMaximumSize(QSize(32, 32))
		self.label_15.setPixmap(QPixmap(u":/icons/icons8-apps-tab-50.png"))
		self.label_15.setScaledContents(True)

		self.horizontalLayout_9.addWidget(self.label_15)

		self.label_3 = QLabel(self.verticalLayoutWidget)
		self.label_3.setObjectName(u"label_3")
		sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		sizePolicy1.setHorizontalStretch(0)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
		self.label_3.setSizePolicy(sizePolicy1)
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(16)
		self.label_3.setFont(font)
		self.label_3.setText(u"Batch Chunk Creator")

		self.horizontalLayout_9.addWidget(self.label_3)


		self.verticalLayout_2.addLayout(self.horizontalLayout_9)

		self.line_4 = QFrame(self.verticalLayoutWidget)
		self.line_4.setObjectName(u"line_4")
		self.line_4.setFrameShape(QFrame.HLine)
		self.line_4.setFrameShadow(QFrame.Sunken)

		self.verticalLayout_2.addWidget(self.line_4)

		self.gridLayout = QGridLayout()
		self.gridLayout.setSpacing(5)
		self.gridLayout.setObjectName(u"gridLayout")
		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setSpacing(5)
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.label_2 = QLabel(self.verticalLayoutWidget)
		self.label_2.setObjectName(u"label_2")
		sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
		sizePolicy2.setHorizontalStretch(0)
		sizePolicy2.setVerticalStretch(0)
		sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
		self.label_2.setSizePolicy(sizePolicy2)
		font1 = QFont()
		font1.setFamily(u"Segoe UI")
		font1.setPointSize(11)
		font1.setBold(True)
		font1.setWeight(75)
		self.label_2.setFont(font1)
		self.label_2.setText(u"Data location")

		self.horizontalLayout_2.addWidget(self.label_2)

		self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_4.setObjectName(u"checkBox_4")
		sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
		sizePolicy3.setHorizontalStretch(0)
		sizePolicy3.setVerticalStretch(0)
		sizePolicy3.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
		self.checkBox_4.setSizePolicy(sizePolicy3)
#if QT_CONFIG(statustip)
		self.checkBox_4.setToolTip(u"Disable to set custom location for data. Enable to use project default data location settings.")
#endif // QT_CONFIG(statustip)
		self.checkBox_4.setText(u"Use Project Data Location")
		icon = QIcon()
		icon.addFile(u":/icons/icons8-copy-to-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_4.setIcon(icon)
		self.checkBox_4.setIconSize(QSize(20, 20))
		self.checkBox_4.setChecked(True)

		self.horizontalLayout_2.addWidget(self.checkBox_4)


		self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

		self.gridLayout_3 = QGridLayout()
		self.gridLayout_3.setSpacing(5)
		self.gridLayout_3.setObjectName(u"gridLayout_3")
		self.horizontalLayout_3 = QHBoxLayout()
		self.horizontalLayout_3.setSpacing(5)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.label_10 = QLabel(self.verticalLayoutWidget)
		self.label_10.setObjectName(u"label_10")
		sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
		sizePolicy4.setHorizontalStretch(0)
		sizePolicy4.setVerticalStretch(0)
		sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
		self.label_10.setSizePolicy(sizePolicy4)
		font2 = QFont()
		font2.setFamily(u"Segoe UI")
		font2.setPointSize(9)
		font2.setBold(True)
		font2.setWeight(75)
		self.label_10.setFont(font2)
		self.label_10.setText(u"Suffix:")

		self.horizontalLayout_3.addWidget(self.label_10)

		self.label_7 = QLabel(self.verticalLayoutWidget)
		self.label_7.setObjectName(u"label_7")
		sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
		self.label_7.setSizePolicy(sizePolicy2)
		self.label_7.setFrameShape(QFrame.StyledPanel)
		self.label_7.setText(u"Suffix...")

		self.horizontalLayout_3.addWidget(self.label_7)


		self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

		self.horizontalLayout_6 = QHBoxLayout()
		self.horizontalLayout_6.setSpacing(5)
		self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
		self.label_9 = QLabel(self.verticalLayoutWidget)
		self.label_9.setObjectName(u"label_9")
		sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
		self.label_9.setSizePolicy(sizePolicy4)
		self.label_9.setFont(font2)
		self.label_9.setFrameShape(QFrame.NoFrame)
		self.label_9.setText(u"Type:	  ")

		self.horizontalLayout_6.addWidget(self.label_9)

		self.label_12 = QLabel(self.verticalLayoutWidget)
		self.label_12.setObjectName(u"label_12")
		sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
		self.label_12.setSizePolicy(sizePolicy2)
		self.label_12.setFrameShape(QFrame.StyledPanel)
		self.label_12.setText(u"TextLabel")

		self.horizontalLayout_6.addWidget(self.label_12)


		self.gridLayout_3.addLayout(self.horizontalLayout_6, 7, 0, 1, 1)

		self.horizontalLayout_5 = QHBoxLayout()
		self.horizontalLayout_5.setSpacing(5)
		self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
		self.label_11 = QLabel(self.verticalLayoutWidget)
		self.label_11.setObjectName(u"label_11")
		sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
		self.label_11.setSizePolicy(sizePolicy4)
		self.label_11.setFont(font2)
		self.label_11.setText(u"Prefix:")

		self.horizontalLayout_5.addWidget(self.label_11)

		self.label_6 = QLabel(self.verticalLayoutWidget)
		self.label_6.setObjectName(u"label_6")
		sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
		self.label_6.setSizePolicy(sizePolicy2)
		self.label_6.setFrameShape(QFrame.StyledPanel)
		
		self.horizontalLayout_5.addWidget(self.label_6)


		self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

		self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
		self.comboBox_2.setObjectName(u"comboBox_2")
		
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
		for cam in cam_list:
			icon_type = camCfg.get(cam, "Type")
			icon_subtype = camCfg.get(cam, "SubType")
			#self.listwidget = QListWidgetItem(self.listWidget)
			#self.listwidget.setText(cam)
			if icon_subtype == "SmartPhone":
				self.comboBox_2.addItem(icon4, cam)
			elif icon_subtype == "Drone":
				self.comboBox_2.addItem(icon5, cam)
			else:
				if icon_type == "Fisheye":
					self.comboBox_2.addItem(icon1, cam)
				elif icon_type == "Spherical":
					self.comboBox_2.addItem(icon3, cam)
				elif icon_type == "Cylindrical":
					self.comboBox_2.addItem(icon2, cam)
				elif icon_type == "RPC":
					self.comboBox_2.addItem(icon5a, cam)
				else:
					self.comboBox_2.addItem(icon, cam)

		self.comboBox_2.setCurrentText(selected_camera)
		sizePolicy2.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
		self.comboBox_2.setSizePolicy(sizePolicy2)
		font3 = QFont()
		font3.setFamily(u"Segoe UI")
		font3.setPointSize(11)
		self.comboBox_2.setFont(font3)
		self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.comboBox_2.setToolTip(u"Choose camera settings to be applied when creating new chunk...")
#endif // QT_CONFIG(statustip)
		self.comboBox_2.setIconSize(QSize(20, 20))

		self.gridLayout_3.addWidget(self.comboBox_2, 6, 0, 1, 1)

		self.checkBox = QCheckBox(self.verticalLayoutWidget)
		self.checkBox.setObjectName(u"checkBox")
		sizePolicy2.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
		self.checkBox.setSizePolicy(sizePolicy2)
		font4 = QFont()
		font4.setFamily(u"Segoe UI")
		font4.setPointSize(9)
		self.checkBox.setFont(font4)
		self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Marker coordinates will be imported after target detection. <span style=\" font-weight:600;\">*</span></p><p><span style=\" font-weight:600;\">Disabled:</span> Coordinates are not imported. User must manually import coordinates.</p><p><span style=\" font-weight:600;\">*</span> Automatic importing of marker coordinates only works if point file name is the same as it's parent folder name, and contains a header with metadata. Point coordinates should start at row #7.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox.setText(u"Import Marker Coordinates")
		icon7 = QIcon()
		icon7.addFile(u":/icons/icons8-map-marker-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox.setIcon(icon7)
		self.checkBox.setIconSize(QSize(20, 20))
		self.checkBox.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox, 12, 0, 1, 1)

		self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_2.setObjectName(u"checkBox_2")
		sizePolicy2.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
		self.checkBox_2.setSizePolicy(sizePolicy2)
		self.checkBox_2.setFont(font4)
		self.checkBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_2.setToolTip(u"<html><head/><body><p>Enable automatic target detection when new chunk is created...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_2.setText(u"Automatic Target Detection")
		icon8 = QIcon()
		icon8.addFile(u":/icons/icons8-my-location-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_2.setIcon(icon8)
		self.checkBox_2.setIconSize(QSize(20, 20))
		self.checkBox_2.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox_2, 11, 0, 1, 1)

		self.cbChunkSettings = QComboBox(self.verticalLayoutWidget)
		for section in chunk_sections:
			menu_icon = menuCfg.get(section, "menu_icon")
			seticon = QIcon()
			seticon.addFile(menu_icon, QSize(), QIcon.Normal, QIcon.Off)
			self.cbChunkSettings.addItem(seticon, section)
		# icon9 = QIcon()
		# icon9.addFile(u":/icons/icons8-add-tab-50.png", QSize(), QIcon.Normal, QIcon.Off)
		# self.cbChunkSettings.addItem(icon9, u"Default")
		# icon10 = QIcon()
		# icon10.addFile(u":/icons/kalota_m.png", QSize(), QIcon.Normal, QIcon.Off)
		# self.cbChunkSettings.addItem(icon10, u"T8 GC - KALOTA")
		# icon11 = QIcon()
		# icon11.addFile(u":/icons/stopnca_o.png", QSize(), QIcon.Normal, QIcon.Off)
		# self.cbChunkSettings.addItem(icon11, u"STOPNICA - IZKOP")
		# icon12 = QIcon()
		# icon12.addFile(u":/icons/stopnca_s.png", QSize(), QIcon.Normal, QIcon.Off)
		# self.cbChunkSettings.addItem(icon12, u"STOPNICA - B.BET.")
		self.cbChunkSettings.setObjectName(u"cbChunkSettings")
		sizePolicy2.setHeightForWidth(self.cbChunkSettings.sizePolicy().hasHeightForWidth())
		self.cbChunkSettings.setSizePolicy(sizePolicy2)
		self.cbChunkSettings.setFont(font3)
		self.cbChunkSettings.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.cbChunkSettings.setToolTip(u"Choose settings used for chunk creation...")
#endif // QT_CONFIG(statustip)
		self.cbChunkSettings.setIconSize(QSize(20, 20))
		self.cbChunkSettings.setCurrentIndex(0)

		self.gridLayout_3.addWidget(self.cbChunkSettings, 1, 0, 1, 1)

		self.label_4 = QLabel(self.verticalLayoutWidget)
		self.label_4.setObjectName(u"label_4")
		sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
		self.label_4.setSizePolicy(sizePolicy2)
		self.label_4.setMaximumSize(QSize(16777215, 25))
		self.label_4.setFont(font1)
		self.label_4.setText(u"Camera")
		self.label_4.setAlignment(Qt.AlignCenter)

		self.gridLayout_3.addWidget(self.label_4, 5, 0, 1, 1)

		self.line_6 = QFrame(self.verticalLayoutWidget)
		self.line_6.setObjectName(u"line_6")
		self.line_6.setFrameShape(QFrame.HLine)
		self.line_6.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line_6, 4, 0, 1, 1)

		self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_3.setObjectName(u"checkBox_3")
		font5 = QFont()
		font5.setFamily(u"Segoe UI")
		font5.setPointSize(10)
		self.checkBox_3.setFont(font5)
		self.checkBox_3.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_3.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Automatic chunk creation with predefined settings</p><p><span style=\" font-weight:600;\">Disabled:</span> Manual confirmation of intermediate steps</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_3.setText(u"Automatic Processing")
		icon13 = QIcon()
		icon13.addFile(u":/icons/icons8-in-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_3.setIcon(icon13)
		self.checkBox_3.setIconSize(QSize(20, 20))
		self.checkBox_3.setCheckable(True)
		self.checkBox_3.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox_3, 14, 0, 1, 1)

		self.label_5 = QLabel(self.verticalLayoutWidget)
		self.label_5.setObjectName(u"label_5")
		sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
		self.label_5.setSizePolicy(sizePolicy2)
		self.label_5.setMaximumSize(QSize(16777215, 25))
		self.label_5.setFont(font1)
		self.label_5.setText(u"Markers")
		self.label_5.setAlignment(Qt.AlignCenter)

		self.gridLayout_3.addWidget(self.label_5, 10, 0, 1, 1)

		self.horizontalLayout_7 = QHBoxLayout()
		self.horizontalLayout_7.setSpacing(5)
		self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
		self.label_13 = QLabel(self.verticalLayoutWidget)
		self.label_13.setObjectName(u"label_13")
		sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
		self.label_13.setSizePolicy(sizePolicy4)
		self.label_13.setFont(font2)
		self.label_13.setText(u"SubType:")

		self.horizontalLayout_7.addWidget(self.label_13)

		self.label_14 = QLabel(self.verticalLayoutWidget)
		self.label_14.setObjectName(u"label_14")
		sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
		self.label_14.setSizePolicy(sizePolicy2)
		self.label_14.setFrameShape(QFrame.StyledPanel)
		self.label_14.setText(u"TextLabel")
		
		self.horizontalLayout_7.addWidget(self.label_14)


		self.gridLayout_3.addLayout(self.horizontalLayout_7, 8, 0, 1, 1)

		self.label = QLabel(self.verticalLayoutWidget)
		self.label.setObjectName(u"label")
		sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy2)
		self.label.setMaximumSize(QSize(16777215, 25))
		self.label.setFont(font1)
		self.label.setText(u"Chunk Creation")
		self.label.setAlignment(Qt.AlignCenter)

		self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

		self.line = QFrame(self.verticalLayoutWidget)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line, 9, 0, 1, 1)

		self.line_3 = QFrame(self.verticalLayoutWidget)
		self.line_3.setObjectName(u"line_3")
		self.line_3.setFrameShape(QFrame.HLine)
		self.line_3.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line_3, 13, 0, 1, 1)


		self.gridLayout.addLayout(self.gridLayout_3, 0, 2, 3, 1)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setSpacing(5)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.lineEdit = QLineEdit(self.verticalLayoutWidget)
		self.lineEdit.setObjectName(u"lineEdit")
		self.lineEdit.setEnabled(False)
		sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy5.setHorizontalStretch(0)
		sizePolicy5.setVerticalStretch(0)
		sizePolicy5.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
		self.lineEdit.setSizePolicy(sizePolicy5)
		self.lineEdit.setFont(font5)
		self.lineEdit.setToolTip(u"Path to main folder with data sub-folders...")
		self.lineEdit.setWhatsThis(u"Path to main folder with data sub-folders...")
		self.lineEdit.setPlaceholderText(u"Data location...")

		self.horizontalLayout.addWidget(self.lineEdit)

		self.pushButton = QPushButton(self.verticalLayoutWidget)
		self.pushButton.setObjectName(u"pushButton")
		self.pushButton.setEnabled(False)
		sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
		self.pushButton.setSizePolicy(sizePolicy3)
		self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton.setToolTip(u"Data location (root folder with sub-folders containing data)")
		self.pushButton.setText(u"Browse")
		icon14 = QIcon()
		icon14.addFile(u":/icons/icons8-images-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton.setIcon(icon14)
		self.pushButton.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton)


		self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

		self.horizontalLayout_4 = QHBoxLayout()
		self.horizontalLayout_4.setSpacing(5)
		self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
		self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_3.setObjectName(u"pushButton_3")
		self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_3.setToolTip(u"Press [Ctrl+P] to start processing")
		self.pushButton_3.setToolTip(u"Process selected folders, and create new chunks...")
		self.pushButton_3.setText(u"Process")
		icon15 = QIcon()
		icon15.addFile(u":/icons/icons8-synchronize-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_3.setIcon(icon15)
		self.pushButton_3.setIconSize(QSize(24, 24))
		self.pushButton_3.setShortcut(u"P")
		self.pushButton_3.setChecked(False)

		self.horizontalLayout_4.addWidget(self.pushButton_3)

		self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_2.setObjectName(u"pushButton_2")
		self.pushButton_2.setToolTip(u"Exit chunk creator...")
		self.pushButton_2.setText(u"Exit")
		icon16 = QIcon()
		icon16.addFile(u":/icons/icons8-enter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_2.setIcon(icon16)
		self.pushButton_2.setIconSize(QSize(24, 24))
		self.pushButton_2.setShortcut(u"X")

		self.horizontalLayout_4.addWidget(self.pushButton_2)


		self.gridLayout.addLayout(self.horizontalLayout_4, 3, 2, 1, 1)

		self.line_5 = QFrame(self.verticalLayoutWidget)
		self.line_5.setObjectName(u"line_5")
		self.line_5.setFrameShape(QFrame.VLine)
		self.line_5.setFrameShadow(QFrame.Sunken)

		self.gridLayout.addWidget(self.line_5, 0, 1, 4, 1)

		self.label_8 = QLabel(self.verticalLayoutWidget)
		self.label_8.setObjectName(u"label_8")
		self.label_8.setFrameShape(QFrame.StyledPanel)
		self.label_8.setText(u"Selected: ")
		self.label_8.setIndent(5)

		self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

		self.treeWidget = QTreeWidget(self.verticalLayoutWidget)
		icon17 = QIcon()
		icon17.addFile(u":/icons/icons8-folder-tree-50.png", QSize(), QIcon.Normal, QIcon.Off)
		font6 = QFont()
		font6.setBold(True)
		font6.setWeight(75)
		__qtreewidgetitem = QTreeWidgetItem()
		__qtreewidgetitem.setText(0, u"Folders");
		__qtreewidgetitem.setFont(0, font6);
		__qtreewidgetitem.setIcon(0, icon17);
		self.treeWidget.setHeaderItem(__qtreewidgetitem)
		icon18 = QIcon()
		icon18.addFile(u":/icons/icons8-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		font7 = QFont()
		font7.setFamily(u"Segoe UI")
		self.treeWidget.setObjectName(u"treeWidget")
		sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
		sizePolicy6.setHorizontalStretch(0)
		sizePolicy6.setVerticalStretch(0)
		#sizePolicy6.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
		self.treeWidget.setSizePolicy(sizePolicy6)
		self.treeWidget.setMinimumSize(QSize(380, 0))
		#self.treeWidget.setMaximumSize(QSize(400, 16777215))
		self.treeWidget.setAutoScrollMargin(20)
		self.treeWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
		self.treeWidget.setTabKeyNavigation(True)
		self.treeWidget.setProperty("showDropIndicator", False)
		self.treeWidget.setAlternatingRowColors(True)
		self.treeWidget.setSelectionMode(QAbstractItemView.MultiSelection)
		self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
		self.treeWidget.setUniformRowHeights(True)
		self.treeWidget.setSortingEnabled(True)
		self.treeWidget.setAllColumnsShowFocus(True)
		self.treeWidget.header().setVisible(True)
		self.treeWidget.header().setDefaultSectionSize(200)

		self.gridLayout.addWidget(self.treeWidget, 2, 0, 1, 1)

		self.verticalLayout_2.addLayout(self.gridLayout)
		
		defChk = self.cbChunkSettings.currentText()
		self.label_6.setText(menuCfg.get(defChk, "chunk_name_prefix"))
		self.label_7.setText(menuCfg.get(defChk, "chunk_name_suffix"))

		defCam = self.comboBox_2.currentText()
		self.label_12.setText(camCfg.get(defCam, "type"))
		self.label_14.setText(camCfg.get(defCam, "subtype"))
		
		self.checkBox_4.toggled.connect(self.pushButton.setDisabled)
		self.checkBox_4.toggled.connect(self.lineEdit.setDisabled)
		self.checkBox_2.toggled.connect(self.checkBox.toggle)
		self.cbChunkSettings.currentTextChanged.connect(self.setCurrentSettings)
		self.comboBox_2.currentTextChanged.connect(self.setCurrentCamera)
		self.lineEdit.textChanged.connect(self.updateFolders)
		self.pushButton_2.clicked.connect(self.quitChunkBatch)
		self.pushButton_3.clicked.connect(self.processBatch)
		self.pushButton.clicked.connect(self.browseFolder)
		self.treeWidget.itemSelectionChanged.connect(self.updateSelected)

		# QtCore.QObject.connect(self.cbChunkSettings, QtCore.SIGNAL("currentTextChanged()"), self.lineEdit, QtCore.SLOT("setText()"))
		# QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.startProcess)
		# QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.startProcess)
		# QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))			
		
		self.exec()

	def browseFolder(self):
		defFolder = Metashape.app.getExistingDirectory("Data folder")
		self.lineEdit.setText(defFolder)


	def setCurrentSettings(self):
		chunkSet = self.cbChunkSettings.currentText()
		if chunkSet == "Default":
			self.lineEdit.clear()
			self.pushButton.setEnabled
			self.lineEdit.setEnabled
			self.checkBox_4.setChecked(False)
			self.label_6.setText(menuCfg.get(chunkSet, "chunk_name_prefix"))
			self.label_7.setText(menuCfg.get(chunkSet, "chunk_name_suffix"))
		else:
			self.lineEdit.setText(str(menuCfg.get(chunkSet, "work_folder")))
			self.pushButton.setDisabled
			self.lineEdit.setDisabled
			self.checkBox_4.setChecked(True)
			self.label_6.setText(menuCfg.get(chunkSet, "chunk_name_prefix"))
			self.label_7.setText(menuCfg.get(chunkSet, "chunk_name_suffix"))


	def setCurrentCamera(self):
		chunkCam = self.comboBox_2.currentText()
		self.label_12.setText(camCfg.get(chunkCam, "type"))
		self.label_14.setText(camCfg.get(chunkCam, "subtype"))
		

	def updateFolders(self):
		self.treeWidget.clear()
		open_folder = self.lineEdit.text()
		if open_folder != "":
			open_folder = self.lineEdit.text().replace("\\", "/") + "/"
			icon17 = QIcon()
			icon17.addFile(u":/icons/icons8-folder-tree-50.png", QSize(), QIcon.Normal, QIcon.Off)
			icon18 = QIcon()
			icon18.addFile(u":/icons/icons8-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
			font6 = QFont()
			font6.setBold(True)
			font6.setWeight(75)
			__qtreewidgetitem = QTreeWidgetItem()
			__qtreewidgetitem.setText(0, u"Folders");
			__qtreewidgetitem.setFont(0, font6);
			__qtreewidgetitem.setIcon(0, icon17);
			self.treeWidget.setHeaderItem(__qtreewidgetitem)
			folder_list = next(os.walk(open_folder))[1]
			
			for folder in folder_list:
				__qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
				__qtreewidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
				__qtreewidgetitem1.setText(0, folder);
				__qtreewidgetitem1.setIcon(0, icon18);

		else:
			icon17 = QIcon()
			icon17.addFile(u":/icons/icons8-folder-tree-50.png", QSize(), QIcon.Normal, QIcon.Off)
			font6 = QFont()
			font6.setBold(True)
			font6.setWeight(75)
			__qtreewidgetitem = QTreeWidgetItem()
			__qtreewidgetitem.setText(0, u"Folders");
			__qtreewidgetitem.setFont(0, font6);
			__qtreewidgetitem.setIcon(0, icon17);
			self.treeWidget.setHeaderItem(__qtreewidgetitem)
		

	def updateSelected(self):
		sel_items = self.treeWidget.selectedItems()
		sel_count = len(sel_items)
		self.label_8.setText(u"Selected: " + str(sel_count))


	def processBatch(self):
		self.sel_items = self.treeWidget.selectedItems()
		sel_count = len(self.sel_items)
		item_menu = self.cbChunkSettings.currentText()
		item_pre = menuCfg.get(item_menu, "chunk_name_prefix")
		item_suf = menuCfg.get(item_menu, "chunk_name_suffix")
		item_cam = self.comboBox_2.currentText()
		if sel_count > 0:
			i_cnt = 1
			for item in self.sel_items:
				print("Processing item: " + str(i_cnt) + "/" + str(sel_count) + " - " + str(item.text(0)))
				doc = Metashape.app.document
				netpath = Metashape.app.document.path
				netroot = self.lineEdit.text()
				image_folder = str(netroot).replace("\\", "/") + "/" + item.text(0)
				photos = find_files(image_folder, [".jpg", ".jpeg", ".png", ".tif", ".tiff"])
				chunk = doc.addChunk()
				chunk.addPhotos(photos)
				chunk_name = item_pre + item.text(0) + item_suf
				# chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
				chunk.label = chunk_name
				doc.chunk = chunk
				doc.save(netpath)
				Metashape.app.update()
				# Metashape.app.messageBox("Nalaganje slik...")
				time.sleep(3)
				readCameraSettings(item_cam)
				useCameraSettings()
				chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
				# path_ref = Metashape.app.getOpenFileName("Import marker coordinates", image_folder, "Text file (*.txt)")
				points_file = image_folder + "/" + item.text(0) + ".txt"
				chunk.importReference(points_file, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
				chunk.updateTransform()
				doc.save(netpath)
				Metashape.app.update()
				i_cnt = i_cnt + 1


	def quitChunkBatch(self):
		self.reject()


def diaAddChunkBatch():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	dia2 = Ui_DialogBatchChunk(parent)


def newchunk_manual(name_prefix, name_suffix, work_folder):
	global projectOpened
	if projectOpened == True:
		doc = Metashape.app.document
		# netroot = path.dirname(netpath)
		netroot = work_folder
		image_folder = Metashape.app.getExistingDirectory("Select data folder", netroot)
		photos = find_files(image_folder, [".jpg", ".jpeg", ".png", ".tif", ".tiff"])
		chunk = doc.addChunk()
		chunk_nameraw = os.path.basename(image_folder)
		chunk_name = name_prefix + chunk_nameraw + name_suffix
		chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
		chunk.addPhotos(photos)
		doc.chunk = chunk
		doc.save()
		Metashape.app.messageBox("New chunk added!\n\nChunk Name: " + chunk_name)
		addcalib = Metashape.app.getBool("Confirm to import default camera calibration.\n\nDefault Camera: " + cam_name)
		if addcalib == True:
			readCameraSettings(selected_camera)
			useCameraSettings()
			doc.save()
		else:
			diaSelectCamera()
			readCameraSettings(selected_camera)
			useCameraSettings()
		nadaljujem = Metashape.app.getBool("Camera set...\nUsing Camera: " + str(selected_camera) + "\n\nContinue with marker detection and coordinates import?")
		if nadaljujem == True:
			chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
			Metashape.app.messageBox("Marker Detection complete!\n\nNext step: Choose file with target coordinates.\nPoint file must have header.\nImport starts at line 7.")
			path_ref = Metashape.app.getOpenFileName("Import Target Coordinates", image_folder, "Text file (*.txt)")
			chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
			chunk.updateTransform()
			Metashape.app.messageBox("Target coordinates imported.\n\nNext step: Workflow > Align Photos")
			Metashape.app.update()
			doc.save()
	else:
		projectOpenedCheck()


# Create chunk AUTO - automaticaly use predefined options
def newchunk_auto(name_prefix, name_suffix, work_folder):
	global projectOpened
	if projectOpened == True:
		doc = Metashape.app.document
		netpath = Metashape.app.document.path
		netroot = work_folder
		image_folder = Metashape.app.getExistingDirectory("Select data folder", netroot)
		photos = find_files(image_folder, [".jpg", ".jpeg", ".png", ".tif", ".tiff"])
		chunk = doc.addChunk()
		chunk.addPhotos(photos)
		chunk_nameraw = os.path.basename(image_folder)
		chunk_name = name_prefix + chunk_nameraw + name_suffix
		# chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
		chunk.label = chunk_name
		doc.chunk = chunk
		doc.save(netpath)
		Metashape.app.update()
		# Metashape.app.messageBox("Nalaganje slik...")
		# time.sleep(3)
		readCameraSettings(selected_camera)
		useCameraSettings()
		chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
		# path_ref = Metashape.app.getOpenFileName("Import marker coordinates", image_folder, "Text file (*.txt)")
		points_file = image_folder + "/" + chunk_nameraw + ".txt"
		chunk.importReference(points_file, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
		chunk.updateTransform()
		doc.save(netpath)
		Metashape.app.update()
	else:
		projectOpenedCheck()


# Create About message dialog
def appAbout():
	app_aboutmsg = app_name + "\n\nVersion: " + app_ver + "\n" + app_author + "\n" + app_about + "\n\n" + app_repo + "\n\nReferences:\n" + ref_repo + "\n\n" + ref_scripts + "\n"
	message_box = QMessageBox()
	message_box.setMinimumSize(600,500)
	message_box.setTextFormat(Qt.PlainText)
	message_box.setText(app_aboutmsg)

	message_box.exec_()


def prazno():
	print("Prazna vrstica")


icon_app = ":/icons/AutoFTG-appicon.png"
icon0 = ":/icons/icons8-about-50.png"
iconadd = ":/icons/icons8-add-50.png"
icon2 = ":/icons/icons8-add-camera-50.png"
icon3 = ":/icons/icons8-add-list-50.png"
icon4 = ":/icons/icons8-add-new-50.png"
icon5 = ":/icons/icons8-aperture-50.png"
icon6 = ":/icons/icons8-apps-tab-50.png"
icon7 = ":/icons/icons8-bursts-50.png"
icon8 = ":/icons/icons8-camera-50.png"
icon9 = ":/icons/icons8-cameras-50.png"
icon10 = ":/icons/icons8-cancel-50.png"
icon11 = ":/icons/icons8-christmas-star-50.png"
icon12 = ":/icons/icons8-close-50.png"
icon13 = ":/icons/icons8-close-window-50.png"
icon14 = ":/icons/icons8-design-50.png"
icon15 = ":/icons/icons8-drag-and-drop-50.png"
icon16 = ":/icons/icons8-edit-50.png"
icon17 = ":/icons/icons8-full-page-view-50.png"
icon18 = ":/icons/icons8-images-folder-50.png"
icon19 = ":/icons/icons8-ios-application-placeholder-50.png"
icon20 = ":/icons/icons8-my-location-50.png"
icon21 = ":/icons/icons8-opened-folder-50.png"
icon22 = ":/icons/icons8-overscan-settings-50.png"
icon23 = ":/icons/icons8-panorama-50.png"
icon24 = ":/icons/icons8-quadcopter-50.png"
icon25 = ":/icons/icons8-restore-50.png"
icon26 = ":/icons/icons8-save-50.png"
icon27 = ":/icons/icons8-save-as-50.png"
icon28 = ":/icons/icons8-services-50.png"
icon29 = ":/icons/icons8-settings-50.png"
icon30 = ":/icons/icons8-slr-back-side-50.png"
icon31 = ":/icons/icons8-slr-camera-50.png"
icon32 = ":/icons/icons8-tools-50.png"
icon33 = ":/icons/icons8-video-stabilization-50.png"
icon34 = ":/icons/icons8-video-wall-50.png"
icon35 = ":/icons/icons8-vintage-camera-50.png"
icon36 = ":/icons/icons8-wallpaper-50.png"
icon37 = ":/icons/icons8-web-camera-50.png"
icon38 = ":/icons/icons8-map-marker-50.png"
icon40 = ":/icons/icons8-toolbox-50.png"
iconaddc = ":/icons/icons8-plus-50.png"
iconloads = ":/icons/icons8-share-50.png"
iconimg28 = ":/icons/kalota.png"
iconimg29 = ":/icons/kalota_m.png"
iconimg59 = ":/icons/stopnca_o.png"
iconimg60 = ":/icons/stopnca_s.png"


# Add Main Menu to start with
labelmenu= "About Auto FTG"
Metashape.app.addMenuItem(labelmenu, appAbout, icon=icon_app)

labelAddChQuick = "AutoFTG/Add New Chunk"
Metashape.app.addMenuItem(label=labelAddChQuick, func=diaAddChunkQuick, icon=iconadd)

labelAddChBatch = "AutoFTG/Add New Chunk (Batch)"
Metashape.app.addMenuItem(label=labelAddChBatch, func=diaAddChunkBatch, icon=iconaddc)

labelset2 = "AutoFTG/Load Project Settings"
Metashape.app.addMenuItem(labelset2, projectOpenedCheck, icon=icon40)

labelsep3a = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep3a, prazno)

label3a = "AutoFTG/Detect markers + Import coordinates"
Metashape.app.addMenuItem(label3a, marker_targets, icon=icon38)

label4 = "AutoFTG/Copy Region (Bounding Box)"
Metashape.app.addMenuItem(label4, copy_bbox, icon=icon15)

labelsep1 = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep1, prazno)

label2 = "AutoFTG/Change Camera (Current Chunk)"
Metashape.app.addMenuItem(label2, selectCamChunk, icon=icon8)

label2aaa = "AutoFTG/Set Default Camera"
Metashape.app.addMenuItem(label2aaa, selectCamDefault, icon=icon35)

label2cccc = "AutoFTG/Cameras Editor"
Metashape.app.addMenuItem(label2cccc, camerasEditor, icon=icon9)

labelsep55 = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep55, prazno)

labelset4 = "AutoFTG/Edit Settings"
Metashape.app.addMenuItem(labelset4, editSettings, icon=icon32)

labelAddChQuicki = "Add New Chunk"
Metashape.app.addMenuItem(label=labelAddChQuicki, func=diaAddChunkQuick, icon=iconadd)

labelset2i = "Load Project Settings"
Metashape.app.addMenuItem(labelset2i, projectOpenedCheck, icon=icon40)

# labelsep3 = "AutoFTG/New Chunk (2TIR)/--------------------"
# Metashape.app.addMenuItem(labelsep3, prazno)
# 
# labelNewStIz = "AutoFTG/New Chunk (2TIR)/STOPNICA (IZKOP) Pefix\Suffix"
# Metashape.app.addMenuSeparator(labelNewStIz)
# 
# label0c = "AutoFTG/New Chunk (2TIR)/STOPNICA (IZKOP) Pefix\Suffix/< Modify prefix"
# Metashape.app.addMenuItem(label0c, changeNameStIzPre)
# 
# label0d = "AutoFTG/New Chunk (2TIR)/STOPNICA (IZKOP) Pefix\Suffix/> Modify suffix"
# Metashape.app.addMenuItem(label0d, changeNameStIzSuf)
# 
# labelNewStBb = "AutoFTG/New Chunk (2TIR)/STOPNICA (B.BET.) Pefix\Suffix"
# Metashape.app.addMenuSeparator(labelNewStBb)
# 
# label0f = "AutoFTG/New Chunk (2TIR)/STOPNICA (B.BET.) Pefix\Suffix/< Modify prefix"
# Metashape.app.addMenuItem(label0f, changeNameStBbPre)
# 
# label0g = "AutoFTG/New Chunk (2TIR)/STOPNICA (B.BET.) Pefix\Suffix/> Modify suffix"
# Metashape.app.addMenuItem(label0g, changeNameStBbSuf)

# changeChunkAppend(setting_name, append_type)

# labelsep2 = "Cameras"
# Metashape.app.addMenuSeparator(labelsep2)

# labelsep5 = "AutoFTG/--------------------"
# Metashape.app.addMenuItem(labelsep5, prazno)

# Initialize setting for AutoFTG


# Main settings file initialization (used when no project is loaded)
class main():
	global projectOpened
	projectOpened = False
	camCfgLoad()
	projectOpenedCheck()
	# appCfgLoad()
	checkSettingsVer()
	menuCfgLoad()
	#print("\n\nAutoFTG Settings loaded...\nSettings version: " + str(appCfg.get('SETTINGS', 'settings_version')))
	#print("Data Folder: " + str(appCfg.get('SETTINGS', 'folder_data')))
	#print("Default Camera: " + str(appCfg.get('SETTINGS', 'default_camera')))


# initAutoFtg()
