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
import textwrap

import Metashape

from AutoFTG import qtresources

import easygui
from easygui import EgStore

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore
from configparser import ConfigParser


# App info
app_name = "AutoFTG"
app_ver = "2.4.5-RC"
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


# Create About message dialog
def appAbout():
	app_aboutmsg = app_name + "\n\nVersion: " + app_ver + "\n" + app_author + "\n" + app_about + "\n\n" + app_repo + "\n\nReferences:\n" + ref_repo + "\n\n" + ref_scripts + "\n"
	message_box = QMessageBox()
	message_box.setMinimumSize(600,500)
	message_box.setTextFormat(Qt.PlainText)
	message_box.setText(app_aboutmsg)

	message_box.exec_()



# Class for program and project settings initialization
class Settings(EgStore):
	def __init__(self, filename):  # filename is required
		self.settingsVersion = appsettings_ver
		self.folderProject = ''
		self.foldeData = ''
		self.defaultCamera = 'NULL - Frame (Default)'
		self.chunkNameKlPre = ''
		self.chunkNameKlSuf = ''
		self.chunkNameStIzPre = ''
		self.chunkNameStBbPre = ''
		self.chunkNameStIzSuf = '_IZ'
		self.chunkNameStBbSuf = '_ST_BB'
		self.filename = filename  # this is required - init settings
		self.restore()

appCfg = ConfigParser()
settingsFilename = os.path.expanduser('~\AppData\Local\Agisoft\Metashape Pro\scripts\AutoFTG\AutoFTG_settings.txt').replace("\\", "/")
settingsFilenameExists = os.path.isfile(settingsFilename)	# Check if settings file exists
settings = Settings(settingsFilename)	# Init settings
projectOpened = False
settingsRebuild = False


# Init configparser for camera settings. Set empty camera variables for global use.
cam_config = ConfigParser()
cam_name = ''
cam_type = ''
cam_subtype = ''
cam_res = ''
cam_file = ''
selected_camera = None
cameraXmlSource = ''
cameraXmlDest = ''


# Load custom menu config
menuCfg = ConfigParser()
menuCfgPath = os.path.expanduser('~\AppData\Local\Agisoft\Metashape Pro\scripts\AutoFTG').replace("\\", "/")
menuCfgFile = "newchunk_settings.ini"
menuCfgFilePath =  menuCfgPath + "/" + menuCfgFile
menuCfgFilePathExists = os.path.isfile(menuCfgFilePath)
if menuCfgFilePathExists == False:
	menu_section_m = "GENERAL"
	menuCfg.add_section(menu_section_m)
	menuCfg.set(menu_section_m, "menu_category", "")
	menuCfg.set(menu_section_m, "menu_icon", ":/icons/icons8-add-50.png")
	menuCfg.set(menu_section_m, "chunk_name_prefix", "")
	menuCfg.set(menu_section_m, "chunk_name_suffix", "")
	
	with open(menuCfgFilePath, 'w') as menuconfig:
		menuCfg.write(menuconfig)

menuCfg.read(menuCfgFilePath)

chunk_sections = menuCfg.sections()


# Set path to camera settings INI file. Use the same location as scripts for Metashape.
script_path = os.path.expanduser('~\AppData\Local\Agisoft\Metashape Pro\scripts\AutoFTG\cameras\\').replace("\\", "/")
script_ini_file = "cam_settings.ini"
script_ini_path =  script_path + script_ini_file


def readIniConf():
	global cam_list
	# Read INI settings file
	cam_config.read(script_ini_path)
	# Create list with cameras read from INI file. Each section is one camera.
	cam_list = cam_config.sections()

	for camera in cam_list:
		print("\n------------------")
		cam_item = cam_config.items(camera, raw=False)
		for item in cam_item:
			print(item[0].capitalize() + ": " + item[1])
		
	print("Loaded camera settings...\n File: " + script_ini_file)


# Check settings version
def checkSettingsVer():
	global settingsRebuild
	if settings.settingsVersion != appsettings_ver:
		settingsRebuild = True
		settingsReset()
		

# Reset settings
def settingsReset():
	global settingsRebuild
	if settingsRebuild == True:
		os.remove(settingsFilename)
		if projectOpened == True:
			settingsRebuild = False
			initAutoFtgProjekt()
		else:
			settingsRebuild = False
			initAutoFtg()


# Routine to check if project exists before initializing settings
def checkProject():
	global projectOpened
	doc = Metashape.app.document
	fileDoc = str(doc).replace("<Document '", "").replace("'>", "")

	if fileDoc == '' or fileDoc == None:
		projectOpened = False
		Metashape.app.messageBox("Project not saved!\n\nSave project or open an existing (Filetype *.psx).")
		# novProjekt()
	else:
		projectOpened = True
		initAutoFtgProjekt()


# Main settings file initialization (used when no project is loaded)
def initAutoFtg():
	global settingsFilename
	global settingsFilenameExists
	global settings
	global projectOpened
	global settingsRebuild

	settingsFilename = os.path.expanduser('~\AppData\Local\Agisoft\Metashape Pro\scripts\AutoFTG\AutoFTG_settings.txt').replace("\\", "/")
	settingsFilenameExists = os.path.isfile(settingsFilename)	# Check if settings file exists
	settings = Settings(settingsFilename)	# Init settings
	readIniConf()
	projectOpened = False
	
	if settingsFilenameExists == False:
		print("\n\nInicializacija osnovnih nastavitev.\nUstvari nov AvtoFTG propjekt za uporabo nastavitev za posamezen projekt. Menu: <AutoFTG>")
		Metashape.app.messageBox("Show folder for exported data...\n\nFolder where exported data will be sotred.")
		projFolderChange()
		Metashape.app.messageBox("Show folder with working data ...\nThis should be a folder where raw data to process is located.)")
		dataFolderChange()
		Metashape.app.messageBox("Choose project default camera...")
		cam_calibrationSettings()
		settings.store()	# persist the settings
	else:
		checkSettingsVer()
		print("\n\nNalozene so osnovne nastavitve.\nUstvari nov AvtoFTG propjekt za uporabo nastavitev za posamezen projekt. Menu: <AutoFTG>")
		print("Export Folder: " + str(settings.folderProject))
		print("Data Folder: " + str(settings.foldeData))
		print("Default Camera: " + str(settings.defaultCamera))
		print("\nUrejanje nastavitev je dostopno preko menija <AutoFTG>.")


# Project settings initialization (used when .psx project is loaded)
def initAutoFtgProjekt():
	global settingsFilename
	global settingsFilenameExists
	global settings
	global projectOpened
	global settingsRebuild
	global fileProject

	fileDoc = Metashape.app.document
	fileProject = str(fileDoc).replace("<Document '", "").replace("'>", "")
	settingsFilename = fileProject.replace(".psx", "_settings.txt")	# Datoteka z nastavitvami projekta
	settingsFilenameExists = os.path.isfile(settingsFilename)	# Preveri, ??e datoteka z projektom obstaja
	settings = Settings(settingsFilename)	# INICALIZACIJA NASTAVITEV
	
	if settingsFilenameExists == False:
		print("\n\nInitializing project settings...")
		Metashape.app.messageBox("Show folder for data export")
		settings.folderProject = Metashape.app.getExistingDirectory("Choose Export Folder")
		Metashape.app.messageBox("Show folder with working data")
		settings.foldeData = Metashape.app.getExistingDirectory("Choose Data Folder")
		cam_calibrationSettings()
		readCameraSettings(settings.defaultCamera)
		settings.store()
		print("\n\nProject settings saved.")
		print("Settings File: " + str(settingsFilename))
		print("Export Folder: " + str(settings.folderProject))
		print("Data Folder: " + str(settings.foldeData))
		print("Default Camera: " + str(cam_name))
		print("\nInitialization complete!")
		Metashape.app.messageBox("Initialization complete.\nProject settings saved...\n\n"
			+ "Settings File: " + str(settingsFilename) + "\n"
			+ "Export Folder: " + str(settings.folderProject) + "\n"
			+ "Data Folder: " + str(settings.foldeData) + "\n"
			+ "Default Camera: " + str(cam_name)
			)
		fileDoc.save(fileProject)
		projectOpened = True

	else:
		checkSettingsVer()
		readCameraSettings(settings.defaultCamera)
		Metashape.app.messageBox("Project settings loaded.\n\n"
			+ "Settings File: " + str(settingsFilename) + "\n"
			+ "Export Folder: " + str(settings.folderProject) + "\n"
			+ "Data Folder: " + str(settings.foldeData) + "\n"
			+ "Default Camera: " + str(cam_name)
			)
		projectOpened = True


# Change project export folder
def projFolderChange():
	settings.folderProject = Metashape.app.getExistingDirectory("Data export folder")
	settings.store()
	print("Export Folder: " + str(settings.folderProject))


# Change project data folder
def dataFolderChange():
	settings.foldeData = Metashape.app.getExistingDirectory("Working data folder")
	settings.store()
	print("Working Folder: " + str(settings.foldeData))


# Create new project routine - used when no project is present when user tries to add new chunk
def novProjekt():
	global projectOpened
	doc = Metashape.app.document
	docPath = Metashape.app.getSaveFileName("Save new project", "",  "Metashape Project (*.psx)")
	try:
		doc.save(docPath)
		Metashape.app.messageBox("New project saved.\n")
		initAutoFtgProjekt()
		projectOpened = True
	except RuntimeError:
		Metashape.app.messageBox("Process canceled...")
		projectOpened = False
	
	Metashape.app.update()


# Read camera settings from INI config file
def readCameraSettings(cam_section):
	global cam_name
	global cam_type
	global cam_subtype
	global cam_res
	global cam_file

	# Read settings for requested camera
	cam_name = cam_config.get(cam_section, "Name")
	cam_type = cam_config.get(cam_section, "Type")
	cam_subtype = cam_config.get(cam_section, "SubType")
	cam_res = cam_config.get(cam_section, "Resolution")
	cam_file = cam_config.get(cam_section, "File")
	print("Using camera\n" + "Name: " + cam_name + "\nType: " + cam_type + "\nSubType: " + cam_subtype + "\nResolution: " + cam_res + "\nFile: " + cam_file)
	

# Called to apply camera settings when creating new chunk
def useCameraSettings():
	# Init document
	doc = Metashape.app.document
	chunk = doc.chunk
	# readCameraSettings(settings.defaultCamera)
	camera_path = script_path + cam_file
	
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
	Metashape.app.messageBox("Camera settings applied.\n\nCamera: " + cam_name + "\nType: " + cam_type + "\nFilename: " + cam_file)
	Metashape.app.update()


# Choose default camera routine
def cam_calibrationSettings():
	readIniConf()
	diaSelectCamera()
	if selected_camera == None:
		print("No camera chosen. Nothing has changed...")
	else:
		settings.defaultCamera = str(selected_camera)
		settings.store()
		print("Default camera settings saved.\nDefault Camera: " + selected_camera)


def cam_calibrationChunk():
	readIniConf()
	diaSelectCamera()
	if selected_camera == None:
		print("No camera chosen. Using default camera.")
	else:
		readCameraSettings(selected_camera)
		useCameraSettings()
		print("\n\nApplied custom camera: " + selected_camera)


# Routine for adding/editing camera configuration
def saveCamConfig(camorig, camname, camtype, camsub, camres, camfile):
	if cam_config.has_section(camorig) == True:
		cam_config.remove_section(camorig)
		cam_config.add_section(camname)
		cam_config.set(camname, "Name", camname)
		cam_config.set(camname, "Type", camtype)
		cam_config.set(camname, "SubType", camsub)
		cam_config.set(camname, "Resolution", camres)
		cam_config.set(camname, "File", camfile)
		Metashape.app.messageBox("Camera added...\n" + "Name: " + camname + "\nType: " + camtype + "\nSubType: " + camsub + "\nRes.:: " + camres + " MP\nFile: " + camfile)
	else:
		cam_config.add_section(camname)
		cam_config.set(camname, "Name", camname)
		cam_config.set(camname, "Type", camtype)
		cam_config.set(camname, "SubType", camsub)
		cam_config.set(camname, "Resolution", camres)
		cam_config.set(camname, "File", camfile)
		Metashape.app.messageBox("Camera added...\n" + "Name: " + camname + "\nType: " + camtype + "\nSubType: " + camsub + "\nRes.:: " + camres + " MP\nFile: " + camfile)

	with open(script_ini_path, 'w') as configfile:
		cam_config.write(configfile)

	readIniConf()


# Routine for adding/editing camera configuration
def removeCamConfig(camname):
	cam_xmlmsg = ''
	if cam_config.has_section(camname) == True:
		if cam_config.get(camname, "File") != "":
			cameraXml = script_path + cam_config.get(camname, "File")
			if os.path.isfile(cameraXml):
				os.remove(cameraXml)
				cam_xmlmsg = "\nXML file " + cameraXml + " deleted."

		cam_config.remove_section(camname)
		cam_secmsg = "Camera [" + camname + "] removed from settings." + cam_xmlmsg
		
		with open(script_ini_path, 'w') as configfile:
			cam_config.write(configfile)
		
		readIniConf()
		
		Metashape.app.messageBox(cam_secmsg)
	else:
		Metashape.app.messageBox("Error! No camera named (" + str(camname) + ") was found.\n\nDid you manualy edit comaera configuration?")


# Change chunk name prefix STOPNICA IZKOP
def changeNameStIzPre():
	current_name = 'STOPNICA (IZKOP)'
	current_setting = str(settings.chunkNameStIzPre)
	current_append = 'prefix'
	
	new_append = Metashape.app.getString(label='Modify ' + current_append + ' for ' + current_name, value=current_setting)
	if new_append != None:
		settings.chunkNameStIzPre = str(new_append)
		settings.store()
		Metashape.app.messageBox("New " + current_append + " for " + current_name + " changed to: " + str(new_append))


# Change chunk name prefix STOPNICA IZKOP
def changeNameStIzSuf():
	current_name = 'STOPNICA (IZKOP)'
	current_setting = str(settings.chunkNameStIzSuf)
	current_append = 'suffix'
		
	new_append = Metashape.app.getString(label='Modify ' + current_append + ' for ' + current_name, value=current_setting)

	if new_append != None:
		settings.chunkNameStIzSuf = str(new_append)
		settings.store()
		Metashape.app.messageBox("New " + current_append + " for " + current_name + " changed to: " + str(new_append))


# Change chunk name prefix STOPNICA IZKOP
def changeNameStBbPre():
	current_name = 'STOPNICA (B.BET.)'
	current_setting = str(settings.chunkNameStBbPre)
	current_append = 'prefix'
		
	new_append = Metashape.app.getString(label='Modify ' + current_append + ' for ' + current_name, value=current_setting)

	if new_append != None:
		settings.chunkNameStBbPre = str(new_append)
		settings.store()
		Metashape.app.messageBox("New " + current_append + " for " + current_name + " changed to: " + str(new_append))


# Change chunk name prefix STOPNICA IZKOP
def changeNameStBbSuf():
	current_name = 'STOPNICA (B.BET.)'
	current_setting = str(settings.chunkNameStBbSuf)
	current_append = 'suffix'
		
	new_append = Metashape.app.getString(label='Modify ' + current_append + ' for ' + current_name, value=current_setting)

	if new_append != None:
		settings.chunkNameStBbSuf = str(new_append)
		settings.store()
		Metashape.app.messageBox("New " + current_append + " for " + current_name + " changed to: " + str(new_append))


# Change chunk name suffix
def changeChunkAppend(setting_name, append_type):
	if setting_name == 0 & append_type == 0:
		current_name = 'STOPNICA (IZKOP)'
		current_setting = str(settings.chunkNameStIzPre)
	elif setting_name == 1 & append_type == 0:
		current_name = 'STOPNICA (B.BET.)'
		current_setting = str(settings.chunkNameStBbPre)
	elif setting_name == 0 & append_type == 1:
		current_name = 'STOPNICA (IZKOP)'
		current_setting = str(settings.chunkNameStIzSuf)
	elif setting_name == 1 & append_type == 1:
		current_name = 'STOPNICA (B.BET.)'
		current_setting = str(settings.chunkNameStBbSuf)
	
	if append_type == 0:
		current_append = 'prefix'
	elif append_type == 1:
		current_append = 'suffix'
		
	new_append = Metashape.app.getString(label='Modify ' + current_append + ' for ' + current_name, value=current_setting)

	if setting_name == 0 & append_type == 0:
		settings.chunkNameStIzPre = str(new_append)
	elif setting_name == 1 & append_type == 0:
		settings.chunkNameStBbPre = str(new_append)
	elif setting_name == 0 & append_type == 1:
		settings.chunkNameStIzSuf = str(new_append)
	elif setting_name == 1 & append_type == 1:
		settings.chunkNameStBbSuf = str(new_append)
	
	settings.store()

	Metashape.app.messageBox("New " + current_append + " for " + current_name + " changed to: " + str(new_append))


# Show current settings
def showSettings():
	show_settings_text = ("Settings currently in use...\n\nSettings file: " + str(settingsFilename) + "\n"
							+ "Settings version: " + str(settings.settingsVersion) + "\n"
							+ "Project folder: " + str(settings.folderProject) + "\n"
							+ "Data folder: " + str(settings.foldeData) + "\n"
							+ "Default camera: " + str(settings.defaultCamera) + "\n")
	show_settings = QMessageBox()
	show_settings.setMinimumSize(600,500)
	show_settings.setTextFormat(Qt.PlainText)
	show_settings.setText(show_settings_text)
	show_settings.setWindowTitle("Current Settings")

	show_settings.exec_()

# Class for settings editing UI
class Ui_settingsDialog(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"settingsDialog")
		self.resize(400, 170)
		self.setWindowTitle(u"AutoFTG Settings")
		
		icon = QIcon()
		icon.addFile(u":/icons/icons8-opened-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)

		self.label = QtWidgets.QLabel()
		self.label.setObjectName(u"label")
		self.label.setGeometry(QRect(10, 10, 80, 16))
		self.label.setText("Project Folder:")
		self.lineProjFolder = QtWidgets.QLineEdit()
		self.lineProjFolder.setObjectName(u"lineProjFolder")
		self.lineProjFolder.setGeometry(QRect(10, 10, 280, 24))
		self.lineProjFolder.setText(str(settings.folderProject))
		self.lineProjFolder.setClearButtonEnabled(True)
		self.btnProjFolder = QtWidgets.QPushButton()
		self.btnProjFolder.setObjectName(u"btnProjFolder")
		self.btnProjFolder.setGeometry(QRect(300, 10, 80, 24))
		self.btnProjFolder.setText(u" Browse")
		self.btnProjFolder.setIcon(icon)
		self.btnProjFolder.setIconSize(QSize(21, 21))
		
		self.label_2 = QtWidgets.QLabel()
		self.label_2.setObjectName(u"label_2")
		self.label_2.setGeometry(QRect(10, 40, 80, 16))
		self.label_2.setText("Data Folder:")
		self.lineDataFolder = QtWidgets.QLineEdit()
		self.lineDataFolder.setObjectName(u"lineDataFolder")
		self.lineDataFolder.setGeometry(QRect(10, 40, 280, 24))
		self.lineDataFolder.setText(str(settings.foldeData))
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
		self.comboBoxCamera.setCurrentText(str(settings.defaultCamera))
		
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
		layout.setRowMinimumHeight(3, 24)
		layout.setVerticalSpacing(1)

		layout.setColumnMinimumWidth(1, 300) # minimum column width
		layout.setColumnMinimumWidth(2, 50) # minimum column width

		layout.addWidget(self.label, 0, 0)
		layout.addWidget(self.lineProjFolder, 0, 1)
		layout.addWidget(self.btnProjFolder, 0, 2)

		layout.addWidget(self.label_2, 1, 0)
		layout.addWidget(self.lineDataFolder, 1, 1)
		layout.addWidget(self.btnDataFolder, 1, 2)

		layout.addWidget(self.label_3, 2, 0)
		layout.addWidget(self.comboBoxCamera, 2, 1)

		layout.addWidget(self.btnClose, 3, 2)
		layout.addWidget(self.btnSave, 3, 1)

		self.setLayout(layout)

		QtCore.QObject.connect(self.btnProjFolder, QtCore.SIGNAL("clicked()"), self.projFolderChange)
		QtCore.QObject.connect(self.btnDataFolder, QtCore.SIGNAL("clicked()"), self.dataFolderChange)
		QtCore.QObject.connect(self.btnSave, QtCore.SIGNAL("clicked()"), self.saveSettingsDialog)
		QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))

		self.exec()

	def projFolderChange(self):
		folderExport = Metashape.app.getExistingDirectory("Export folder")
		self.lineProjFolder.setText(folderExport)

	def dataFolderChange(self):
		foldeData = Metashape.app.getExistingDirectory("Data folder")
		self.lineDataFolder.setText(foldeData)

	def saveSettingsDialog(self):
		settings.folderProject = self.lineProjFolder.text()
		settings.foldeData = self.lineDataFolder.text()
		settings.defaultCamera = self.comboBoxCamera.currentText()
		settings.store()
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
		self.resize(480, 240)
		self.setWindowTitle(u"Add/Edit Camera")
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		self.setSizePolicy(sizePolicy)
		self.setMinimumSize(QSize(480, 240))
		self.setMaximumSize(QSize(480, 240))
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(9)
		self.setFont(font)
		icon = QIcon()
		icon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(icon)
		self.gridLayoutWidget = QWidget(self)
		self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
		self.gridLayoutWidget.setGeometry(QRect(10, 10, 461, 220))
		self.gridLayout = QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setSpacing(5)
		self.gridLayout.setContentsMargins(10, 10, 10, 10)
		self.gridLayout.setObjectName(u"gridLayout")
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.label = QLabel(self.gridLayoutWidget)
		self.label.setObjectName(u"label")
		sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy)
		font1 = QFont()
		font1.setFamily(u"Segoe UI")
		font1.setPointSize(10)
		self.label.setFont(font1)
		self.label.setText(u"Camera Type")

		self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

		self.line = QFrame(self.gridLayoutWidget)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.gridLayout.addWidget(self.line, 5, 0, 1, 2)

		self.label_4 = QLabel(self.gridLayoutWidget)
		self.label_4.setObjectName(u"label_4")
		sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
		self.label_4.setSizePolicy(sizePolicy)
		self.label_4.setText(u"Resolution")

		self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

		self.label_5 = QLabel(self.gridLayoutWidget)
		self.label_5.setObjectName(u"label_5")
		sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
		self.label_5.setSizePolicy(sizePolicy)
		self.label_5.setText(u"Callibration File")

		self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

		self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
		self.lineEdit_2.setObjectName(u"lineEdit_2")
		sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		sizePolicy1.setHorizontalStretch(0)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
		self.lineEdit_2.setSizePolicy(sizePolicy1)
		self.lineEdit_2.setMaximumSize(QSize(200, 16777215))
		font2 = QFont()
		font2.setFamily(u"Segoe UI")
		font2.setPointSize(11)
		self.lineEdit_2.setFont(font2)
		self.lineEdit_2.setPlaceholderText(u"Camera name")

		self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)

		self.comboBox = QComboBox(self.gridLayoutWidget)
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox.addItem(icon1, u"Frame")
		icon2 = QIcon()
		icon2.addFile(u":/icons/icons8-video-wall-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox.addItem(icon2, u"Fisheye")
		icon3 = QIcon()
		icon3.addFile(u":/icons/icons8-live-photos-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox.addItem(icon3, u"Spherical")
		icon4 = QIcon()
		icon4.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox.addItem(icon4, u"Cylindrical")
		icon12 = QIcon()
		icon12.addFile(u":/icons/icons8-ios-application-placeholder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox.addItem(icon12, u"RPC")
		self.comboBox.setObjectName(u"comboBox")
		sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
		sizePolicy2.setHorizontalStretch(0)
		sizePolicy2.setVerticalStretch(0)
		sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
		self.comboBox.setSizePolicy(sizePolicy2)
		self.comboBox.setFont(font1)
		self.comboBox.setIconSize(QSize(24, 24))

		self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)

		self.horizontalLayout_3 = QHBoxLayout()
		self.horizontalLayout_3.setSpacing(5)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.lineEdit = QLineEdit(self.gridLayoutWidget)
		self.lineEdit.setObjectName(u"lineEdit")
		sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
		self.lineEdit.setSizePolicy(sizePolicy1)
		self.lineEdit.setMaximumSize(QSize(50, 16777215))
		self.lineEdit.setFont(font)
		self.lineEdit.setCursorPosition(0)
		self.lineEdit.setPlaceholderText(u"0.0")

		self.horizontalLayout_3.addWidget(self.lineEdit)

		self.label_6 = QLabel(self.gridLayoutWidget)
		self.label_6.setObjectName(u"label_6")
		sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
		self.label_6.setSizePolicy(sizePolicy)
		self.label_6.setText(u"MP")

		self.horizontalLayout_3.addWidget(self.label_6)


		self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)

		self.label_3 = QLabel(self.gridLayoutWidget)
		self.label_3.setObjectName(u"label_3")
		sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
		self.label_3.setSizePolicy(sizePolicy)
		self.label_3.setFont(font2)
		self.label_3.setText(u"Camera Name:")

		self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

		self.label_2 = QLabel(self.gridLayoutWidget)
		self.label_2.setObjectName(u"label_2")
		sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
		self.label_2.setSizePolicy(sizePolicy)
		self.label_2.setFont(font1)
		self.label_2.setText(u"Camera Sub-Type")

		self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

		self.comboBox_2 = QComboBox(self.gridLayoutWidget)
		icon5 = QIcon()
		icon5.addFile(u":/icons/icons8-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon5, u"Standard")
		icon6 = QIcon()
		icon6.addFile(u":/icons/icons8-slr-small-lens-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon6, u"DSLR")
		icon7 = QIcon()
		icon7.addFile(u":/icons/icons8-camera-on-tripod-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon7, u"Special")
		icon8 = QIcon()
		icon8.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon8, u"Drone")
		icon9 = QIcon()
		icon9.addFile(u":/icons/icons8-touchscreen-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon9, u"SmartPhone")
		icon10 = QIcon()
		icon10.addFile(u":/icons/icons8-gopro-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon10, u"SportCam")
		self.comboBox_2.setObjectName(u"comboBox_2")
		sizePolicy2.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
		self.comboBox_2.setSizePolicy(sizePolicy2)
		self.comboBox_2.setFont(font1)
		self.comboBox_2.setIconSize(QSize(24, 24))

		self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)

		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setSpacing(5)
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
		self.lineEdit_3.setObjectName(u"lineEdit_3")
		self.lineEdit_3.setPlaceholderText(u"Choose calibration XML file...")

		self.horizontalLayout_2.addWidget(self.lineEdit_3)

		self.pushButton_3 = QPushButton(self.gridLayoutWidget)
		self.pushButton_3.setObjectName(u"pushButton_3")
		sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
		sizePolicy3.setHorizontalStretch(0)
		sizePolicy3.setVerticalStretch(0)
		sizePolicy3.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
		self.pushButton_3.setSizePolicy(sizePolicy3)
		self.pushButton_3.setText(u"Browse")
		icon9 = QIcon()
		icon9.addFile(u":/icons/icons8-images-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_3.setIcon(icon9)
		self.pushButton_3.setIconSize(QSize(24, 24))
		self.pushButton_3.setFlat(True)

		self.horizontalLayout_2.addWidget(self.pushButton_3)


		self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setSpacing(5)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.pushButton = QPushButton(self.gridLayoutWidget)
		self.pushButton.setObjectName(u"pushButton")
		sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
		self.pushButton.setSizePolicy(sizePolicy1)
		self.pushButton.setMinimumSize(QSize(0, 0))
		self.pushButton.setMaximumSize(QSize(110, 30))
		self.pushButton.setText(u"Cancel")
		icon10 = QIcon()
		icon10.addFile(u":/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton.setIcon(icon10)
		self.pushButton.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton)

		self.pushButton_2 = QPushButton(self.gridLayoutWidget)
		self.pushButton_2.setObjectName(u"pushButton_2")
		sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
		self.pushButton_2.setSizePolicy(sizePolicy1)
		self.pushButton_2.setMinimumSize(QSize(0, 0))
		self.pushButton_2.setMaximumSize(QSize(110, 30))
		self.pushButton_2.setText(u"Save")
		icon11 = QIcon()
		icon11.addFile(u":/icons/icons8-save-all-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_2.setIcon(icon11)
		self.pushButton_2.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton_2)


		self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 2)

		QWidget.setTabOrder(self.lineEdit_2, self.comboBox)
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
			selCamType = cam_config.get(camname, "Type")
			selCamSubType = cam_config.get(camname, "SubType")
			selCamRes = cam_config.get(camname, "Resolution")
			selCamFile = cam_config.get(camname, "File")
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
		cameraXmlSource = Metashape.app.getOpenFileName(hint="Select Camera Calibration", dir=str(settings.folderProject), filter="Metashape Camera Calibration (*.xml)")
		camXmlFile = os.path.basename(cameraXmlSource)
		cameraXmlDest = script_path + camXmlFile
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
			readIniConf()
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
		readIniConf()
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
		self.resize(340, 240)
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
		self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 321, 151))
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
			cam_type = str(cam_config.get(camera, 'Type'))
			cam_stype = str(cam_config.get(camera, "SubType"))
			cam_res = str(cam_config.get(camera, 'Resolution'))
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
			cam_type = str(cam_config.get(camera, 'Type'))
			cam_stype = str(cam_config.get(camera, "SubType"))
			cam_res = str(cam_config.get(camera, 'Resolution'))
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
		self.resize(280, 280)
		self.setWindowTitle(u"Choose Camera")
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		self.setSizePolicy(sizePolicy)
		self.setMinimumSize(QSize(280, 280))
		self.setMaximumSize(QSize(280, 280))
		self.setWindowTitle(u"Choose Camera")
		self.verticalLayoutWidget = QWidget(self)
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
			icon_type = cam_config.get(cam, "Type")
			icon_subtype = cam_config.get(cam, "SubType")
			self.listwidget = QListWidgetItem(self.listWidget)
			self.listwidget.setText(cam)
			if icon_subtype == "Smartphone":
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

		self.listWidget.setCurrentRow(cam_list.index(settings.defaultCamera))

		__sortingEnabled = self.listWidget.isSortingEnabled()
		self.listWidget.setSortingEnabled(False)
		self.listWidget.setSortingEnabled(__sortingEnabled)

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
		self.btnCancel.setText(u"Cancel")
		icon6 = QIcon()
		icon6.addFile(u":/icons/icons8-cancel-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.btnCancel.setIcon(icon6)
		self.btnCancel.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.btnCancel)

		self.verticalLayout.addLayout(self.horizontalLayout)


		QtCore.QObject.connect(self.btnCreate, QtCore.SIGNAL("clicked()"), self.startProcess)
		QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))			
		
		self.exec()


	def startProcess(self):
		selected_menu = self.cbChunkSettings.currentText()
		self.name_prefix = menuCfg.get(selected_menu, "chunk_name_prefix")
		self.name_suffix = menuCfg.get(selected_menu, "chunk_name_suffix")

		if self.checkBoxAutoProc.isChecked == False:
			newchunk_manual(self.name_prefix, self.name_suffix)
		else:
			newchunk_auto(self.name_prefix, self.name_suffix)
		
		self.close()


def diaAddChunkQuick():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	dia = Ui_DialogAddChunkQuick(parent)


def newchunk_manual(name_prefix, name_suffix):
	global projectOpened
	if projectOpened == True:
		doc = Metashape.app.document
		# netroot = path.dirname(netpath)
		netroot = settings.foldeData
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
			readCameraSettings(settings.defaultCamera)
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
		checkProject()


# Create chunk AUTO - automaticaly use predefined options
def newchunk_auto(name_prefix, name_suffix):
	global projectOpened
	if projectOpened == True:
		doc = Metashape.app.document
		netpath = Metashape.app.document.path
		netroot = settings.foldeData
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
		time.sleep(3)
		readCameraSettings(settings.defaultCamera)
		useCameraSettings()
		chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
		# path_ref = Metashape.app.getOpenFileName("Import marker coordinates", image_folder, "Text file (*.txt)")
		points_file = image_folder + "\\" + chunk_nameraw + ".txt"
		chunk.importReference(points_file, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
		chunk.updateTransform()
		Metashape.app.update()
		doc.save(netpath)
	else:
		checkProject()


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

labelAddChQuick = "Add New Chunk"
Metashape.app.addMenuItem(label=labelAddChQuick, func=diaAddChunkQuick, icon=iconadd)


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


labelset2 = "AutoFTG/Load Project Settings..."
Metashape.app.addMenuItem(labelset2, checkProject, icon=iconloads)

labelsep3a = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep3a, prazno)

label3a = "AutoFTG/Detect markers + Import coordinates"
Metashape.app.addMenuItem(label3a, marker_targets, icon=icon38)

label4 = "AutoFTG/Copy Region (Bounding Box)"
Metashape.app.addMenuItem(label4, copy_bbox, icon=icon15)

# labelsep2 = "Cameras"
# Metashape.app.addMenuSeparator(labelsep2)

labelsep1 = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep1, prazno)

label2 = "AutoFTG/Change Camera (Current Chunk)"
Metashape.app.addMenuItem(label2, cam_calibrationChunk, icon=icon8)

labelsep5 = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep5, prazno)

label2cccc = "AutoFTG/Settings/Cameras Editor"
Metashape.app.addMenuItem(label2cccc, camerasEditor, icon=icon9)

labelsep55 = "AutoFTG/Settings/--------------------"
Metashape.app.addMenuItem(labelsep55, prazno)

label2aaa = "AutoFTG/Settings/Set Default Camera"
Metashape.app.addMenuItem(label2aaa, cam_calibrationSettings, icon=icon35)

labelset4 = "AutoFTG/Settings/Edit Settings"
Metashape.app.addMenuItem(labelset4, editSettings, icon=icon32)

# Initialize setting for AutoFTG
initAutoFtg()
