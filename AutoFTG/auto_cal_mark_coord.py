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
app_ver = "2.4.1-beta"
appsettings_ver = "5"
app_author = "Author: Boris Bilc\n\n"
app_repo = "Repository URL:\nhttps://github.com/bilkos-Scripts_Metashape-Pro"
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


settingsFilename = os.path.expanduser('~\AppData\Local\Agisoft\Metashape Pro\scripts\AutoFTG\AutoFTG_settings.txt').replace("\\", "/")
settingsFilenameExists = os.path.isfile(settingsFilename)	# Check if settings file exists
settings = Settings(settingsFilename)	# Init settings
projectOpened = False
settingsRebuild = False


# Init configparser for camera settings. Set empty camera variables for global use.
cam_config = ConfigParser()
cam_name = ''
cam_type = ''
cam_res = ''
cam_file = ''


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

	if fileDoc == '':
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
	settingsFilenameExists = os.path.isfile(settingsFilename)	# Preveri, če datoteka z projektom obstaja
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
	global cam_res
	global cam_file

	# Read settings for requested camera
	cam_name = cam_config.get(cam_section, "Name")
	cam_type = cam_config.get(cam_section, "Type")
	cam_res = cam_config.get(cam_section, "Resolution")
	cam_file = cam_config.get(cam_section, "File")
	print("Using camera\n" + "Name: " + cam_name + "\nType: " + cam_type + "n\Resolution: " + cam_res + "\nFile: " + cam_file)
	

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

	# Init calibration and import settings from camera calibration file (Metashape XML)
	chunk_calib = Metashape.Calibration()
	if cam_file != "None":
		chunk_calib.load(path=camera_path, format=Metashape.CalibrationFormatXML)
	chunk_sensor.user_calib = chunk_calib
	
	# Save document and show message with applied settings
	doc.save()
	Metashape.app.messageBox("Camera settings applied.\n\nCamera: " + cam_name + "\nType: " + cam_type + "\nFilename: " + cam_file)
	Metashape.app.update()


# Camera choicebox variables
camcalMsgSet = "Choose default camera to be used when adding new chunks"
camcalTitleSet = "Default Camera"


# Choose default camera routine
def cam_calibrationSettings(msg=camcalMsgSet, title=camcalTitleSet, callback=None, run=True):
	readIniConf()
	mb = easygui.choicebox(msg, title, choices=cam_list, preselect=cam_list.index(settings.defaultCamera), callback=callback)
	if run:
		if mb == None:
			print("No camera chosen. Nothing has changed...")
		else:
#			replyindex = choices.index(mb)
#			readCameraSettings(replyindex)
			settings.defaultCamera = str(mb)
			settings.store()
			print("Default camera settings saved.\nDefault Camera: " + mb)
	else:
		print("\nCamera settings loaded....\n")
		return mb


camcalMsg = "Choose camera to be used in this chunk"
camcalTitle = "Custom Camera"


def cam_calibrationChunk(msg=camcalMsg, title=camcalTitle, callback=None, run=True):
	readIniConf()
	cambox = easygui.choicebox(msg, title, choices=cam_list, preselect=cam_list.index(settings.defaultCamera), callback=callback)
	if run:
		if cambox == None:
			print("No camera chosen. Using default camera.")
		else:
#			camboxindex = choices.index(cambox)
			readCameraSettings(cambox)
			useCameraSettings()
			print("\n\nApplied custom camera: " + cambox)
	else:
		print("\nCamera settings loaded....\n")
		return cambox


# Routine for adding/editing camera configuration
def saveCamConfig(camorig, camname, camtype, camfile):
	if cam_config.has_section(camorig) == True:
		cam_config.remove_section(camorig)
		cam_config.add_section(camname)
		cam_config.set(camname, "Name", camname)
		cam_config.set(camname, "Type", camtype)
		cam_config.set(camname, "File", camfile)
		Metashape.app.messageBox("Camera settings saved...\n" + "Name: " + camname + "\nType: " + camtype + "\nFile: " + camfile)
	else:
		cam_config.add_section(camname)
		cam_config.set(camname, "Name", camname)
		cam_config.set(camname, "Type", camtype)
		cam_config.set(camname, "File", camfile)
		Metashape.app.messageBox("Camera added...\n" + "Name: " + camname + "\nType: " + camtype + "\nFile: " + camfile)

	with open(script_ini_path, 'w') as configfile:
		cam_config.write(configfile)

	readIniConf()


# Routine for adding/editing camera configuration
def removeCamConfig(camname):
	if cam_config.has_section(camname) == True:
		cameraXml = script_path + cam_config.get(camname, "File")
		
		if os.path.exists(cameraXml):
			os.remove(cameraXml)
			print("Camera XML file " + cameraXml + " deleted...")
		else:
			print("File not found!")
		
		cam_config.remove_section(camname)
		
		with open(script_ini_path, 'w') as configfile:
			cam_config.write(configfile)
		
		readIniConf()
		
		Metashape.app.messageBox("Camera settings and XML file removed...")
	else:
		Metashape.app.messageBox("Error! No camera named (" + str(camname) + ") was found.\n\nDid you manualy edit comaera configuration?")


# Change chunk name prefix STOPNICA IZKOP
def changeNameStIzPre():
	current_name = 'STOPNICA (IZKOP)'
	current_setting = str(settings.chunkNameStIzPre)
	current_append = 'prefix'
		
	new_append = Metashape.app.getString(label='Modify ' + current_append + ' for ' + current_name, value=current_setting)

	settings.chunkNameStIzPre = str(new_append)
	
	settings.store()

	Metashape.app.messageBox("New " + current_append + " for " + current_name + " changed to: " + str(new_append))


# Change chunk name prefix STOPNICA IZKOP
def changeNameStIzSuf():
	current_name = 'STOPNICA (IZKOP)'
	current_setting = str(settings.chunkNameStIzSuf)
	current_append = 'suffix'
		
	new_append = Metashape.app.getString(label='Modify ' + current_append + ' for ' + current_name, value=current_setting)

	settings.chunkNameStIzSuf = str(new_append)
	
	settings.store()

	Metashape.app.messageBox("New " + current_append + " for " + current_name + " changed to: " + str(new_append))


# Change chunk name prefix STOPNICA IZKOP
def changeNameStBbPre():
	current_name = 'STOPNICA (B.BET.)'
	current_setting = str(settings.chunkNameStBbPre)
	current_append = 'prefix'
		
	new_append = Metashape.app.getString(label='Modify ' + current_append + ' for ' + current_name, value=current_setting)

	settings.chunkNameStBbPre = str(new_append)
	
	settings.store()

	Metashape.app.messageBox("New " + current_append + " for " + current_name + " changed to: " + str(new_append))


# Change chunk name prefix STOPNICA IZKOP
def changeNameStBbSuf():
	current_name = 'STOPNICA (B.BET.)'
	current_setting = str(settings.chunkNameStBbSuf)
	current_append = 'suffix'
		
	new_append = Metashape.app.getString(label='Modify ' + current_append + ' for ' + current_name, value=current_setting)

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
	easygui.msgbox("Settings currently in use...\n\nSettings file: " + str(settingsFilename) + "\n"
							+ "Settings version: " + str(settings.settingsVersion) + "\n"
							+ "Project folder: " + str(settings.folderProject) + "\n"
							+ "Data folder: " + str(settings.foldeData) + "\n"
							+ "Default camera: " + str(settings.defaultCamera) + "\n"
							 , title="Current settings")


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
		# icon1 = QIcon()
		# icon1.addFile(u":/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
		# self.btnClose.setIcon(icon1)

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


# Class for camera edit dialog
class Ui_DialogCameras(QtWidgets.QDialog):
	def __init__(self, parent, camnew, camname, camtype, camfile):
		global camOrigName
		camOrigName = camname
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"DialogCameras")
		self.resize(400, 170)
		self.setWindowTitle(u"AutoFTG Edit Cameras")
		
		layout = QtWidgets.QGridLayout()  # creating layout
		
		self.gridLayout = QtWidgets.QGridLayout()
		self.gridLayout.setObjectName(u"gridLayout")
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.btnBrowseXML = QtWidgets.QPushButton()
		self.btnBrowseXML.setObjectName(u"btnBrowseXML")
		self.btnBrowseXML.setText(u" Browse")
		icon = QIcon()
		icon.addFile(u":/icons/icons8-opened-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.btnBrowseXML.setIcon(icon)

		layout.addWidget(self.btnBrowseXML, 4, 3, 1, 1)

		self.comboBoxType = QtWidgets.QComboBox()
		self.comboBoxType.addItem(u"Frame")
		self.comboBoxType.addItem(u"Fisheye")
		self.comboBoxType.addItem(u"Spherical")
		self.comboBoxType.addItem(u"Cylindrical")
		self.comboBoxType.setObjectName(u"comboBoxType")
		self.comboBoxType.setCurrentText(camtype)

		layout.addWidget(self.comboBoxType, 2, 1, 1, 1)

		self.label_3 = QtWidgets.QLabel()
		self.label_3.setObjectName(u"label_3")
		self.label_3.setText(u"Name:")

		layout.addWidget(self.label_3, 3, 0, 1, 1)

		self.btnSaveCam = QtWidgets.QPushButton()
		self.btnSaveCam.setObjectName(u"btnSaveCam")
		if camnew == True:
			self.btnSaveCam.setText(u" Save")
		else:
			self.btnSaveCam.setText(u" Update")
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons8-save-as-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.btnSaveCam.setIcon(icon1)
		self.btnSaveCam.setIconSize(QSize(12, 12))

		layout.addWidget(self.btnSaveCam, 6, 3, 1, 1)

		self.line_2 = QtWidgets.QFrame()
		self.line_2.setObjectName(u"line_2")
		self.line_2.setFrameShape(QFrame.HLine)
		self.line_2.setFrameShadow(QFrame.Sunken)

		layout.addWidget(self.line_2, 5, 0, 1, 4)

		self.line = QtWidgets.QFrame()
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)

		layout.addWidget(self.line, 1, 0, 1, 4)

		self.label_4 = QtWidgets.QLabel()
		self.label_4.setObjectName(u"label_4")
		self.label_4.setText(u"Type:")

		layout.addWidget(self.label_4, 2, 0, 1, 1)

		self.label_5 = QtWidgets.QLabel()
		self.label_5.setObjectName(u"label_5")
		self.label_5.setText(u"File:")

		layout.addWidget(self.label_5, 4, 0, 1, 1)

		self.btnCloseCamDialog = QtWidgets.QPushButton()
		self.btnCloseCamDialog.setObjectName(u"btnCloseCamDialog")
		self.btnCloseCamDialog.setText(u"Close")
		# icon2 = QIcon()
		# icon2.addFile(u":/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
		# self.btnCloseCamDialog.setIcon(icon2)

		layout.addWidget(self.btnCloseCamDialog, 6, 2, 1, 1)

		self.lineEditFile = QtWidgets.QLineEdit()
		self.lineEditFile.setObjectName(u"lineEditFile")
		self.lineEditFile.setInputMask(u"")
		self.lineEditFile.setText(camfile)
		self.lineEditFile.setClearButtonEnabled(True)

		layout.addWidget(self.lineEditFile, 4, 1, 1, 2)

		self.lineEditName = QtWidgets.QLineEdit()
		self.lineEditName.setObjectName(u"lineEditName")
		self.lineEditName.setInputMask(u"")
		self.lineEditName.setText(camname)
		self.lineEditName.setClearButtonEnabled(True)

		layout.addWidget(self.lineEditName, 3, 1, 1, 2)

		self.label_2 = QtWidgets.QLabel()
		self.label_2.setObjectName(u"label_2")
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(10)
		self.label_2.setFont(font)
		self.label_2.setText(u"Add Camera Calibration")

		layout.addWidget(self.label_2, 0, 0, 1, 4)
		
		self.setLayout(layout)

		QtCore.QObject.connect(self.btnBrowseXML, QtCore.SIGNAL("clicked()"), self.selectCameraFile)
		QtCore.QObject.connect(self.btnSaveCam, QtCore.SIGNAL("clicked()"), self.saveCamera)
		QtCore.QObject.connect(self.btnCloseCamDialog, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))

		self.exec()

	cameraXmlSource = ''

	def selectCameraFile(self):
		global cameraXmlSource
		global cameraXmlDest
		cameraXmlSource = Metashape.app.getOpenFileName(hint="Select Camera Calibration", dir=str(settings.folderProject), filter="Metashape Camera Calibration (*.xml)")
		camXmlFile = os.path.basename(cameraXmlSource)
		cameraXmlDest = script_path + camXmlFile
		self.lineEditFile.setText(camXmlFile)


	def saveCamera(self):
#		global cameraXmlSource
		cameraXmlDestExists = os.path.isfile(cameraXmlDest)
		if cameraXmlDestExists == False:
			try:
				shutil.copy2(cameraXmlSource, cameraXmlDest)
				cameraNameAdd = self.lineEditName.text()
				cameraTypeAdd = self.comboBoxType.currentText()
				cameraFileAdd = self.lineEditFile.text()
				saveCamConfig(cameraNameAdd, cameraNameAdd, cameraTypeAdd, cameraFileAdd)
			except:
				Metashape.app.messageBox("Error! No camera added...")
		else:
			cameraNameAdd = self.lineEditName.text()
			cameraTypeAdd = self.comboBoxType.currentText()
			cameraFileAdd = self.lineEditFile.text()
			saveCamConfig(camOrigName, cameraNameAdd, cameraTypeAdd, cameraFileAdd)
			Metashape.app.messageBox("Camera settings saved.\n" + "Name: " + cameraNameAdd + "\nType: " + cameraTypeAdd + "\nFile: " + cameraFileAdd)

		readIniConf()

		self.close()

# Routine for calling Edit Settings UI - called when user want's to edit settings
def addCameraDialog(camnew, camname, camtype, camfile):
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	if camnew == False:
		cameraDialog = Ui_DialogCameras(parent, camnew, camname, camtype, camfile)
	else:
		cameraDialog = Ui_DialogCameras(parent, camnew, "New Camera", "Frame", "")


class Ui_dialogCamGui(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"dialogCamGui")
		self.resize(340, 240)
		self.setWindowTitle(u"Cameras Editor")

		layoutMain = QtWidgets.QVBoxLayout()  # creating layout

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
		for camera in cam_list:
			self.listWidgetCamItem = QListWidgetItem(camera, self.listWidgetCam)
			self.listWidgetCamItem.setText(str(camera))
			self.listWidgetCamItem.setToolTip("Type: " + str(cam_config.get(camera, 'type')) + "\nRes.: " + str(cam_config.get(camera, 'resolution')))
			# self.listWidgetCam.addItem(camera)
			# self.listWidgetCam.setToolTip("Type: " + str(cam_config.get(camera, 'type')) + "\nRes.: " + str(cam_config.get(camera, 'resolution')))
			# print(item[0].capitalize() + ": " + item[1])

		self.hLayoutCamEdit.addWidget(self.listWidgetCam)

		self.vLayout_CamBtn = QVBoxLayout()
		self.vLayout_CamBtn.setObjectName(u"vLayout_CamBtn")
		self.btnAddNewCam = QPushButton(self.verticalLayoutWidget_2)
		self.btnAddNewCam.setObjectName(u"btnAddNewCam")
		sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnAddNewCam.sizePolicy().hasHeightForWidth())
		self.btnAddNewCam.setSizePolicy(sizePolicy)
		self.btnAddNewCam.setText(u" Add")
		icon = QIcon()
		icon.addFile(u":/icons/icons8-add-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.btnAddNewCam.setIcon(icon)

		self.vLayout_CamBtn.addWidget(self.btnAddNewCam)

		self.btnEditCam = QPushButton(self.verticalLayoutWidget_2)
		self.btnEditCam.setObjectName(u"btnEditCam")
		sizePolicy.setHeightForWidth(self.btnEditCam.sizePolicy().hasHeightForWidth())
		self.btnEditCam.setSizePolicy(sizePolicy)
		self.btnEditCam.setText(u" Edit")
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons8-edit-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.btnEditCam.setIcon(icon1)

		self.vLayout_CamBtn.addWidget(self.btnEditCam)

		self.btnRemoveCam = QPushButton(self.verticalLayoutWidget_2)
		self.btnRemoveCam.setObjectName(u"btnRemoveCam")
		sizePolicy.setHeightForWidth(self.btnRemoveCam.sizePolicy().hasHeightForWidth())
		self.btnRemoveCam.setSizePolicy(sizePolicy)
		self.btnRemoveCam.setText(u" Remove")
		icon2 = QIcon()
		icon2.addFile(u":/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.btnRemoveCam.setIcon(icon2)

		self.vLayout_CamBtn.addWidget(self.btnRemoveCam)

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

		# self.btnMainSave = QPushButton(self.verticalLayoutWidget_2)
		# self.btnMainSave.setObjectName(u"btnMainSave")
		# sizePolicy1.setHeightForWidth(self.btnMainSave.sizePolicy().hasHeightForWidth())
		# self.btnMainSave.setSizePolicy(sizePolicy1)
		# self.btnMainSave.setText(u"Save")
# 
		# self.hLayout_MainBtn.addWidget(self.btnMainSave)

		layoutMain.addLayout(self.hLayout_MainBtn)

		self.setLayout(layoutMain)

		QtCore.QObject.connect(self.btnAddNewCam, QtCore.SIGNAL("clicked()"), self.addNewCam)
		QtCore.QObject.connect(self.btnEditCam, QtCore.SIGNAL("clicked()"), self.editSelCamera)
		QtCore.QObject.connect(self.btnRemoveCam, QtCore.SIGNAL("clicked()"), self.removeSelCamera)
		# QtCore.QObject.connect(self.btnMainSave, QtCore.SIGNAL("clicked()"), self.saveCameraEdit)
		QtCore.QObject.connect(self.btnMainClose, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("reject()"))

		self.exec()

	def addNewCam(self):
		camNew = True
		addCameraDialog(camNew, "New Camera", "Frame", "")
		self.listWidgetCam.clear()
		for camera in cam_list:
			self.listWidgetCam.addItem(camera)


	def editSelCamera(self):
		# defaultItem = self.listWidgetCam.isItemSelected("Default")
		if self.listWidgetCam.currentRow() > 0:
			camNew = False
			selCamName = self.listWidgetCam.currentItem().text()
			selCamType = cam_config.get(selCamName, "Type")
			selCamFile = cam_config.get(selCamName, "File")
			addCameraDialog(camNew, selCamName, selCamType, selCamFile)
		elif self.listWidgetCam.currentRow() == 0:
			Metashape.app.messageBox("Default camera can not be edited.")
		else:
			Metashape.app.messageBox("No camera selected...")


	def removeSelCamera(self):
		if self.listWidgetCam.isItemSelected() == True:
			camname = self.listWidgetCam.currentItem().text()
			removeCamConfig(camname)
			self.listWidgetCam.takeItem(self.listWidgetCam.currentRow)


	def saveCameraEdit(self):
		print("")


# Routine for calling Edit Settings UI - called when user want's to edit settings
def camerasEditor():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	camEditDialog = Ui_dialogCamGui(parent)




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


# Create new chunk - Options are chosen manually
def newchunk_aero():
	global projectOpened
	if projectOpened == True:
		doc = Metashape.app.document
		netpath = Metashape.app.document.path
		# netroot = path.dirname(netpath)
		netroot = settings.foldeData
		image_folder = Metashape.app.getExistingDirectory("Select folder with photos", netroot)
		photos = find_files(image_folder, [".jpg", ".jpeg", ".png", ".tif", ".tiff"])			# ".JPG", ".JPEG", 
		chunk = doc.addChunk()
		chunk_nameraw = os.path.basename(image_folder)
		chunk.label = Metashape.app.getString("Chunk Name", chunk_nameraw)
		chunk.addPhotos(photos)
		doc.chunk = chunk
		doc.save()
		Metashape.app.messageBox("New chunk added!\n\nChunk Name: " + chunk_nameraw)
		
		addcalib = Metashape.app.getBool("Confirm to import default camera calibration.\n\nDefault Camera: " + cam_name)
		
		if addcalib == True:
			readCameraSettings(settings.defaultCamera)
			useCameraSettings()
			doc.save()
		else:
			cam_choice = easygui.choicebox("Choose Camra", title="Choose Camera", choices=cam_list, preselect=settings.defaultCamera, callback=None)
			cam_choice_index = cam_list.index(cam_choice)
			readCameraSettings(cam_choice)
			useCameraSettings()

		nadaljujem = Metashape.app.getBool("Camera set...\nUsing Camera: " + str(cam_choice) + "\n\nContinue with marker detection and coordinates import?")
		
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
		# newchunk_aero()

#
# Create chunk - custom auto routines
#
def newchunk_kalota_auto():
	global projectOpened
	if projectOpened == True:
		doc = Metashape.app.document
		docPath = Metashape.app.document.path
		netroot = settings.foldeData
		image_folder = Metashape.app.getExistingDirectory("Mapa z podatki za (KALOTA)", netroot)
		photos = find_files(image_folder, [".jpg", ".jpeg", ".JPG", ".JPEG"])
		chunk = doc.addChunk()
		chunk.addPhotos(photos)
		chunk_nameraw = os.path.basename(image_folder)
		chunk.label = Metashape.app.getString("Naziv chunka", chunk_nameraw)
		doc.chunk = chunk
		doc.save(docPath)
		Metashape.app.update()
		Metashape.app.messageBox("Nalaganje slik...")
		readCameraSettings(settings.defaultCamera)
		useCameraSettings()
		doc.save(docPath)
		chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
		path_ref = Metashape.app.getOpenFileName("Uvoz koordinat markerjev", image_folder, "Text file (*.txt)")
		chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
		chunk.updateTransform()
		Metashape.app.update()
		doc.save(docPath)
	else:
		checkProject()
		# newchunk_kalota_auto()


def newchunk_stizk_auto():
	global projectOpened
	if projectOpened == True:
		doc = Metashape.app.document
		netpath = Metashape.app.document.path
		# netroot = path.dirname(netpath)
		netroot = settings.foldeData
		image_folder = Metashape.app.getExistingDirectory("Mapa z podatki za (STOPNICA - IZKOP)", netroot)
		photos = find_files(image_folder, [".jpg", ".jpeg", ".JPG", ".JPEG"])
		chunk = doc.addChunk()
		chunk.addPhotos(photos)
		chunk_nameraw = os.path.basename(image_folder)
		chunk_name = str(settings.chunkNameStIzPre) + chunk_nameraw + str(settings.chunkNameStIzSuf)
		chunk.label = Metashape.app.getString("Naziv chunka", chunk_name)
		doc.chunk = chunk
		doc.save(netpath)
		Metashape.app.update()
		Metashape.app.messageBox("Nalaganje slik...")
		readCameraSettings(settings.defaultCamera)
		useCameraSettings()
		chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
		path_ref = Metashape.app.getOpenFileName("Import Target Coordinates", image_folder, "Text file (*.txt)")
		chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
		chunk.updateTransform()
		Metashape.app.update()
		doc.save(netpath)
	else:
		checkProject()
		# newchunk_stizk_auto()


def newchunk_stbbet_auto():
	global projectOpened
	if projectOpened == True:
		doc = Metashape.app.document
		netpath = Metashape.app.document.path
		# netroot = path.dirname(netpath)
		netroot = settings.foldeData
		image_folder = Metashape.app.getExistingDirectory("Mapa z podatki za (STOPNICA - B.BET)", netroot)
		photos = find_files(image_folder, [".jpg", ".jpeg", ".JPG", ".JPEG"])
		chunk = doc.addChunk()
		chunk.addPhotos(photos)
		chunk_nameraw = os.path.basename(image_folder)
		chunk_name = str(settings.chunkNameStBbPre) + chunk_nameraw + str(settings.chunkNameStBbSuf)
		chunk.label = Metashape.app.getString("Naziv chunkae", chunk_name)
		doc.chunk = chunk
		doc.save()
		Metashape.app.update()
		Metashape.app.messageBox("Nalaganje slik...")
		readCameraSettings(settings.defaultCamera)
		useCameraSettings()
		chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
		path_ref = Metashape.app.getOpenFileName("Import Target Coordinates", image_folder, "Text file (*.txt)")
		chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
		chunk.updateTransform()
		Metashape.app.update()
		doc.save()
	else:
		checkProject()
		# newchunk_stbbet_auto()



def prazno():
	print("Prazna vrstica")


icon_app = ":/icons/AutoFTG-appicon.png"
icon0 = ":/icons/icons8-about-50.png"
icon1 = ":/icons/icons8-add-50.png"
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

iconimg28 = ":/icons/kalota.png"
iconimg29 = ":/icons/kalota_m.png"
iconimg59 = ":/icons/stopnca_o.png"
iconimg60 = ":/icons/stopnca_s.png"


# Menu items
labelmenu= "About Auto FTG"
Metashape.app.addMenuItem(labelmenu, appAbout, icon=icon_app)

label1a = "AutoFTG/New Chunk"
Metashape.app.addMenuItem(label1a, newchunk_aero, icon=icon1)

labelNewChunk = "AutoFTG/New Chunk (2TIR)"
Metashape.app.addMenuSeparator(labelNewChunk)

label0a = "AutoFTG/New Chunk (2TIR)/KALOTA"
Metashape.app.addMenuItem(label0a, newchunk_kalota_auto, icon=iconimg29)

labelsep33 = "AutoFTG/New Chunk (2TIR)/--------------------"
Metashape.app.addMenuItem(labelsep33, prazno)

label0b = "AutoFTG/New Chunk (2TIR)/STOPNICA (IZKOP)"
Metashape.app.addMenuItem(label0b, newchunk_stizk_auto, icon=iconimg59)

label0e = "AutoFTG/New Chunk (2TIR)/STOPNICA (B.BET.)"
Metashape.app.addMenuItem(label0e, newchunk_stbbet_auto, icon=iconimg60)

labelsep3 = "AutoFTG/New Chunk (2TIR)/--------------------"
Metashape.app.addMenuItem(labelsep3, prazno)

labelNewStIz = "AutoFTG/New Chunk (2TIR)/STOPNICA (IZKOP) Pefix\Suffix"
Metashape.app.addMenuSeparator(labelNewStIz)

label0c = "AutoFTG/New Chunk (2TIR)/STOPNICA (IZKOP) Pefix\Suffix/< Modify prefix"
Metashape.app.addMenuItem(label0c, changeNameStIzPre)

label0d = "AutoFTG/New Chunk (2TIR)/STOPNICA (IZKOP) Pefix\Suffix/> Modify suffix"
Metashape.app.addMenuItem(label0d, changeNameStIzSuf)

labelNewStBb = "AutoFTG/New Chunk (2TIR)/STOPNICA (B.BET.) Pefix\Suffix"
Metashape.app.addMenuSeparator(labelNewStBb)

label0f = "AutoFTG/New Chunk (2TIR)/STOPNICA (B.BET.) Pefix\Suffix/< Modify prefix"
Metashape.app.addMenuItem(label0f, changeNameStBbPre)

label0g = "AutoFTG/New Chunk (2TIR)/STOPNICA (B.BET.) Pefix\Suffix/> Modify suffix"
Metashape.app.addMenuItem(label0g, changeNameStBbSuf)

# changeChunkAppend(setting_name, append_type)

labelsep3a = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep3a, prazno)

label3a = "AutoFTG/Detect markers + Import coordinates"
Metashape.app.addMenuItem(label3a, marker_targets, icon=icon38)

label4 = "AutoFTG/Copy Region (Bounding Box)"
Metashape.app.addMenuItem(label4, copy_bbox, icon=icon15)

labelsep2 = "AutoFTG/--------------------"
Metashape.app.addMenuSeparator(labelsep2)

label2 = "AutoFTG/Change Current Camera (Chunk)"
Metashape.app.addMenuItem(label2, cam_calibrationChunk, icon=icon8)

label2a = "AutoFTG/Set Default Camera (Project)"
Metashape.app.addMenuItem(label2a, cam_calibrationSettings, icon=icon35)

# label2b = "AutoFTG/Camera Settings/Add New Camera"
# Metashape.app.addMenuItem(label2b, addCameraDialog, icon=iconimg3)

label2c = "AutoFTG/Cameras Editor"
Metashape.app.addMenuItem(label2c, camerasEditor, icon=icon9)
# 
# label2c = "AutoFTG/Change camera/(3) Camera 2: HH3 by dibit (Fisheye)"
# Metashape.app.addMenuItem(label2c, cam_calibration1b)
# 
# label2f = "AutoFTG/Change camera/(4) Camera 3: HH3 by dibit (Fisheye)"
# Metashape.app.addMenuItem(label2f, cam_calibration1c)
# 
# label2d = "AutoFTG/Change camera/(5) DJI Phantom 4 Pro 2.0 (CELU)"
# Metashape.app.addMenuItem(label2d, cam_calibration2)
# 
# label2e = "AutoFTG/Change camera/(6) DJI Phantom 4 Advanced (2B)"
# Metashape.app.addMenuItem(label2e, cam_calibration3)
# 
# labelsep1 = "AutoFTG/--------------------"
# Metashape.app.addMenuItem(labelsep1, prazno)

# label6 = "AutoFTG/Filter Points (Uniform - Region oriented)"
# Metashape.app.addMenuItem(label6, run_filterpoints)
 
# labelsep3 = "AutoFTG/--------------------"
# Metashape.app.addMenuItem(labelsep3, prazno)
 
# label5a = "AutoFTG/Sample Points (Surface Detail)"
# Metashape.app.addMenuItem(label5a, run_samplepoints)
 
# label5b = "AutoFTG/Sample Points (Uniform Spacing)"
# Metashape.app.addMenuItem(label5b, run_samplepointsuni)
 
# labelsep4 = "AutoFTG/--------------------"
# Metashape.app.addMenuItem(labelsep4, prazno)

# labelset0 = "AutoFTG/Change data folder location"
# Metashape.app.addMenuItem(labelset0, dataFolderChange, icon=iconimg5)

labelsep5 = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep5, prazno)

labelset2 = "AutoFTG/Load Project Settings..."
Metashape.app.addMenuItem(labelset2, checkProject, icon=icon40)

# labelset3 = "AutoFTG/Settings/Show Current Settings."
# Metashape.app.addMenuItem(labelset3, showSettings, icon=iconimg20)

labelset4 = "AutoFTG/Project Settings"
Metashape.app.addMenuItem(labelset4, editSettings, icon=icon32)

# labelsep5 = "AutoFTG/--------------------"
# Metashape.app.addMenuItem(labelsep5, prazno)

# labelabout = "About AutoFTG..."
# Metashape.app.addMenuItem(labelabout, appAbout, icon=iconimg1)

# Initialize setting for AutoFTG
initAutoFtg()
