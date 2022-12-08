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
# References:
# -----------
# Agisoft GitHub repository - https://github.com/agisoft-llc/metashape-scripts
# 
# Scripts used:
# -------------
# Copy Bounding Box Script
#  https://github.com/agisoft-llc/metashape-scripts/blob/master/src/copy_bounding_box_dialog.py
#  Copies bounding boxes from chunk to other chunks.
# 


import os
import sys
import time
from os import path

import easygui
import Metashape
from AutoFTG import resource
from easygui import EgStore
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


# VERZIJA APLIKACIJE
app_name = "AutoFTG"
app_ver = "2.1.0-beta"
app_author = "Author: Boris Bilc (Slovenia)"
app_repo = "Repository URL: https://github.com/bilkos/AutoFTG-Scripts_Metashape-Pro"
ref_repo = "Agisoft GitHub repository:https://github.com/agisoft-llc/metashape-scripts"
ref_scripts = "Copy Bounding Box Script: https://github.com/agisoft-llc/metashape-scripts/blob/master/src/copy_bounding_box_dialog.py"
app_about = "Scripts for process automation in Agisoft Metashape Pro\n\nThis is an assembly of existing scripts from other users, and some additional scripts written for use in work process at project 2TIR, tunnel T8-KP in Slovenia."

def appAbout():
	app_aboutmsg = app_name + " (" + app_ver + ")\n\n" + app_author + "\n\n" + app_about + "\n\n" + app_repo + "\n\nReferences:\n" + ref_repo + "\n\n" + ref_scripts + "\n"
	Metashape.app.messageBox(app_aboutmsg)

# Checking compatibility
compatible_major_version = "2.0"
found_major_version = ".".join(Metashape.app.version.split('.')[:2])
if found_major_version != compatible_major_version:
	raise Exception("Incompatible Metashape version: {} != {}".format(found_major_version, compatible_major_version))

cameraList = [								# Seznam kamer, ki so prednastavljene [Variable LIST]
	"NULL: Frame",							# ID: 0
	"NULL: Fisheye",						# ID: 1
	"HH3_031-1 by dibit: Fisheye",			# ID: 2
	"HH3_031-2 by dibit: Fisheye",			# ID: 3
	"HH3_031-3 by dibit: Fisheye",			# ID: 4
	"DJI Phantom 4 Pro 2.0 (CELU)",			# ID: 5
	"DJI Phantom 4 Advanced (2B)"			# ID: 6
	]

# Class for settings initialization
class Settings(EgStore):
	# Privzete vrednosti nastavitev - inicializacija nastavitev pri prvem zagonu
	def __init__(self, filename):  # filename is required
		self.settingsVersion = app_ver
		self.fileProject = ''
		self.folderProject = ''
		self.foldeData = ''
		self.defaultCamera = '0'
		self.filename = filename  # this is required - init settings
		self.restore()


# Main settings initialization
settingsFilename = "C:/AutoFTG_settings.txt"    # Main settings file (used when no project is loaded)
settingsFilenameExists = os.path.isfile(settingsFilename)	# Check if settings file exists
settings = Settings(settingsFilename)	# Init settings
projectOpened = False
resetSettings = False


def initAutoFtg():
	if settingsFilenameExists == False:
		print("\n\nInicializacija osnovnih nastavitev.\nUstvari nov AvtoFTG propjekt za uporabo nastavitev za posamezen projekt. Menu: <AutoFTG>")
		settings.store()    # persist the settings
	else:
		checkSettingsVer() 
		print("\n\nNalozene so osnovne nastavitve.\nUstvari nov AvtoFTG propjekt za uporabo nastavitev za posamezen projekt. Menu: <AutoFTG>")
		print("Project File: " + str(settings.fileProject))
		print("Export Folder: " + str(settings.folderProject))
		print("Data Folder: " + str(settings.foldeData))
		print("Default Camera: " + str(cameraList[int(settings.defaultCamera)]))
		print("\nUrejanje nastavitev je dostopno preko menija <AutoFTG>.")


def checkSettingsVer():
	global resetSettings
	if settings.settingsVersion == app_ver:
		resetSettings = False
	else:
		resetSettings = True
		settingsReset(resetSettings)
		

def settingsReset(reset):
	if reset == True:
		settings.settingsVersion = app_ver
		settings.fileProject = ''
		settings.folderProject = ''
		settings.foldeData = ''
		settings.defaultCamera = '0'
		settings.store()
		

def initAutoFtgProjekt():
	global settingsFilename
	global settingsFilenameExists
	global settings
	global projectOpened

	fileDoc = Metashape.app.document
	fileProject = str(fileDoc).replace("<Document '", "").replace("'>", "")
	settingsFilename = fileProject.replace(".psx", "_settings.txt")    # Datoteka z nastavitvami projekta
	settingsFilenameExists = os.path.isfile(settingsFilename)	# Preveri, če datoteka z projektom obstaja
	settings = Settings(settingsFilename)	# INICALIZACIJA NASTAVITEV
	
	if settingsFilenameExists == False:
		print("\n\nInitializing project settings...")
		settings.fileProject = fileProject
		Metashape.app.messageBox("Show folder for data export")
		settings.folderProject = Metashape.app.getExistingDirectory("Choose Export Folder")
		Metashape.app.messageBox("Show folder with working data")
		settings.foldeData = Metashape.app.getExistingDirectory("Choose Data Folder")
		cam_calibrationSettings()
		settings.store()
		print("\n\nProject settings saved.")
		print("Settings File: " + str(settingsFilename))
		print("Project File: " + str(settings.fileProject))
		print("Export Folder: " + str(settings.folderProject))
		print("Data Folder: " + str(settings.foldeData))
		print("Default Camera: " + str(cameraList[int(settings.defaultCamera)]))
		print("\nInitialization complete!")
		Metashape.app.messageBox("Initialization complete.\nProject settings saved...\n\n"
			+ "Settings File: " + str(settingsFilename) + "\n"
			+ "Project File: " + str(settings.fileProject) + "\n"
			+ "Export Folder: " + str(settings.folderProject) + "\n"
			+ "Data Folder: " + str(settings.foldeData) + "\n"
			+ "Default Camera: " + str(cameraList[int(settings.defaultCamera)])
			)
		fileDoc.save(fileProject)
		projectOpened = True

	else:
		checkSettingsVer()
		print("\n\nProject settings loaded.")
		print("Settings File: " + str(settingsFilename))
		print("Project File: " + str(settings.fileProject))
		print("Export Folder: " + str(settings.folderProject))
		print("Data Folder: " + str(settings.foldeData))
		print("Default Camera: " + str(cameraList[int(settings.defaultCamera)]))
		settings.store()
		Metashape.app.messageBox("Project settings loaded.\n\n"
			+ "Settings File: " + str(settingsFilename) + "\n"
			+ "Project File: " + str(settings.fileProject) + "\n"
			+ "Export Folder: " + str(settings.folderProject) + "\n"
			+ "Data Folder: " + str(settings.foldeData) + "\n"
			+ "Default Camera: " + str(cameraList[int(settings.defaultCamera)])
			)
		projectOpened = True


def checkProject():
	global projectOpened
	fileProject = str(Metashape.app.document).replace("<Document '", "").replace("'>", "")
	if fileProject == '':
		Metashape.app.messageBox("Project not saved!\n\nSave project or open an existing one first (Filetype *.psx).")
		novProjekt()
	else:
		initAutoFtgProjekt()
		projectOpened = True


# def initMain():
# 	if uporabiProjekt == True:
# 		initAutoFtgProjekt()
# 	else:
# 		initAutoFtg()


def projFolderChange():
	settings.foldeData = Metashape.app.getExistingDirectory("Data export folder")
	settings.store()
	print("Export Folder: " + str(settings.folderProject))


def dataFolderChange():
	settings.foldeData = Metashape.app.getExistingDirectory("Working data folder")
	settings.store()
	print("Working Folder: " + str(settings.foldeData))


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


camcalMsg = "Choose default camera to be used when adding new chunks"
camcalTitle = "Default Camera"
camcalPreselect = int(settings.defaultCamera)


# Funkcija za izbiro privzete kalibracije
def cam_calibrationSettings(msg=camcalMsg, title=camcalTitle, choices=cameraList, preselect=camcalPreselect, callback=None, run=True):

	mb = easygui.choicebox(msg, title, choices=choices, preselect=preselect, callback=callback)

	if run:
		if mb == None:
			print("No camera chosen. Nothing has changed...")
		else:
			replyindex = choices.index(mb)
			settings.defaultCamera = str(replyindex)
			settings.store()
			print("Default camera settings saved.\nDefault Camera: " + mb)
	else:
		print("\nCamera settings loaded....\n")
		return mb


def showSettings():
	Metashape.app.messageBox("Settings currently in use:\n\n"
							+ "Settings file: " + str(settingsFilename) + "\n"
							+ "Settings version: " + str(settings.settingsVersion) + "\n\n"
							+ "Project file: " + str(settings.fileProject) + "\n"
							+ "Project folder: " + str(settings.folderProject) + "\n"
							+ "Data folder: " + str(settings.foldeData) + "\n\n"
							+ "Default camera: " + str(cameraList[int(settings.defaultCamera)]) + "\n"
							 )


class Ui_settingsDialog(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"settingsDialog")
		self.resize(390, 210)
		self.setWindowTitle(u"AutoFTG Settings")
		icon = QIcon()
		icon.addFile(u":/AutoFTG/openfolder.png", QSize(), QIcon.Normal, QIcon.Off)

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
		self.btnProjFolder.setText(u"Browse")
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
		self.btnDataFolder.setText(u"Browse")
		self.btnDataFolder.setIcon(icon)
		self.btnDataFolder.setIconSize(QSize(21, 21))
		
		self.label_3 = QtWidgets.QLabel()
		self.label_3.setObjectName(u"label_3")
		self.label_3.setGeometry(QRect(10, 70, 90, 16))
		self.label_3.setText("Default Camera:")
		self.comboBoxCamera = QtWidgets.QComboBox()
		self.comboBoxCamera.setObjectName(u"comboBoxCamera")
		self.comboBoxCamera.setGeometry(QRect(10, 70, 280, 24))
		for camera in cameraList:
			self.comboBoxCamera.addItem(camera)
		self.comboBoxCamera.setCurrentIndex(int(settings.defaultCamera))
		
		self.btnClose = QtWidgets.QPushButton()
		self.btnClose.setObjectName(u"btnClose")
		self.btnClose.setGeometry(QRect(220, 90, 75, 23))
		self.btnClose.setText(u"Close")
		self.btnSave = QtWidgets.QPushButton()
		self.btnSave.setObjectName(u"btnSave")
		self.btnSave.setGeometry(QRect(300, 90, 75, 23))
		self.btnSave.setText(u"Save")
		
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
		settings.defaultCamera = self.comboBoxCamera.currentIndex()
		settings.store()
		print("New settings stored.")


def editSettings():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	editDialog = Ui_settingsDialog(parent)


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
		

def copy_bbox():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()

	dlg = CopyBoundingBoxDlg(parent)


def progress_print(p):
		print('Completed: {:.2f}%'.format(p))


def cam_calibration(calsetting):
	if calsetting == 0:
		cam_calibrationDefault()
	elif calsetting == 1:
		cam_calibration0()
	elif calsetting == 2:
		cam_calibration1a()
	elif calsetting == 3:
		cam_calibration1b()
	elif calsetting == 4:
		cam_calibration1c()
	elif calsetting == 5:
		cam_calibration2()
	elif calsetting == 6:
		cam_calibration3()
	else:
		cam_calibrationDefault()


# Nalozi kalibracijo kamere / Nulta / Type: Fisheye
def cam_calibrationDefault():
	doc = Metashape.app.document
	chunk = doc.chunk
	
	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Frame
#	my_calib = Metashape.Calibration()
#	my_calib.load(path="\\\\Stroj\\1_ftg_t8-kp\\100_T8-KP_OBDELAVA\\dibit-kamera_HH3_031_Fisheye.xml", format=Metashape.CalibrationFormatXML)
#	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Camera settings applied.\n\nCamera: null\nType: Frame\nFilename: ---")
	Metashape.app.update()


def cam_calibration0():
	doc = Metashape.app.document
	chunk = doc.chunk
	
	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Fisheye
#	my_calib = Metashape.Calibration()
#	my_calib.load(path="\\\\Stroj\\1_ftg_t8-kp\\100_T8-KP_OBDELAVA\\dibit-kamera_HH3_031_Fisheye.xml", format=Metashape.CalibrationFormatXML)
#	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Camera settings applied.\n\nCamera: null\nType: Fisheye\nFilename: ---")
	Metashape.app.update()


# Nalozi kalibracijo kamere / HH3_031 by dibit / Type: Fisheye
def cam_calibration1a():
	doc = Metashape.app.document
	chunk = doc.chunk	

	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Fisheye
	my_calib = Metashape.Calibration()
	my_calib.load(path="\\\\Stroj\\1_ftg_t8-kp\\100_T8-KP_OBDELAVA\\dibit-kamera_HH3_031_Fisheye.xml", format=Metashape.CalibrationFormatXML)
	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Camera settings applied.\n\nCamera: #1 HH3 by dibit\nType: Fisheye\nFilename: dibit-kamera_HH3_031_Fisheye.xml")
	Metashape.app.update()


# Nalozi kalibracijo kamere / HH3 KAMERA 2 by dibit / Type: Fisheye
def cam_calibration1b():
	doc = Metashape.app.document
	chunk = doc.chunk	

	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Fisheye
	my_calib = Metashape.Calibration()
	my_calib.load(path="\\\\Stroj\\1_ftg_t8-kp\\100_T8-KP_OBDELAVA\\dibit-kamera-2_HH3_Fisheye.xml", format=Metashape.CalibrationFormatXML)
	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Camera settings applied.\n\nCamera: #2 HH3 by dibit\nType: Fisheye\nFilename: dibit-kamera-2_HH3_Fisheye.xml")
	Metashape.app.update()


# Nalozi kalibracijo kamere / HH3 KAMERA 2 by dibit / Type: Fisheye
def cam_calibration1c():
	doc = Metashape.app.document
	chunk = doc.chunk	

	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Fisheye
	my_calib = Metashape.Calibration()
	my_calib.load(path="\\\\Stroj\\1_ftg_t8-kp\\100_T8-KP_OBDELAVA\\dibit-kamera-3_HH3_Fisheye.xml", format=Metashape.CalibrationFormatXML)
	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Camera settings applied.\n\nCamera: HH3 by dibit\nType: Fisheye\nFilename: dibit-kamera-3_HH3_Fisheye.xml")
	Metashape.app.update()


# Nalozi kalibracijo kamere / DJI Phantom 4 Pro 2 (CELU) / Type: Frame
def cam_calibration2():
	doc = Metashape.app.document
	chunk = doc.chunk	

	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Frame
	my_calib = Metashape.Calibration()
	my_calib.load(path="\\\\STROJ\\AeroProjekti-Arhiv\\_KalibracijeKamer\\DJI-Phantom-4-Pro2_20MP_2022-01_CELU.xml", format=Metashape.CalibrationFormatXML)
	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Camera settings applied.\n\nCamera: DJI Phantom 4 Pro 2.0 (CELU)\nType: Frame\nFilename: DJI-Phantom-4-Pro2_20MP_2022-01_CELU.xml")
	Metashape.app.update()


# Nalozi kalibracijo kamere / DJI Phantom 4 Advanced (2B) / Type: Frame
def cam_calibration3():
	doc = Metashape.app.document
	chunk = doc.chunk	

	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Frame
	my_calib = Metashape.Calibration()
	my_calib.load(path="\\\\STROJ\\AeroProjekti-Arhiv\\_KalibracijeKamer\\DJI-Phantom-4-Advanced_20MP_2022-01_2B.xml", format=Metashape.CalibrationFormatXML)
	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Camera settings applied.\n\nCamera: DJI Phantom 4 Advanced (2B)\nType: Frame\nFilename: DJI-Phantom-4-Advanced_20MP_2022-01_2B.xml")
	Metashape.app.update()


def marker_targets():
	doc = Metashape.app.document
	chunk = doc.chunk
	netpath = Metashape.app.document.path
	netroot = path.dirname(netpath)
	nadaljujem = Metashape.app.getBool("Start marker detection?")

	if nadaljujem == True:
		# Poisci markerje
		chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
		Metashape.app.messageBox("Marker detection finished.\n\nIn next step choose file containing marker coordinates.\n\nFile must contain header, coordinates are expected starting at line 7.")
		
		# Uvoz koordinat za markerje
		path_ref = Metashape.app.getOpenFileName("Import coordinates " + chunk.label, netroot, "Text file (*.txt)")
		chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)

		# Posodobi pogled
		chunk.updateTransform()
		
		Metashape.app.messageBox("Target coordinates imported.\n\nNext step: Workflow > Align Photos")
		Metashape.app.update()
		
		# Shrani projekt
		doc.save()


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
		
		addcalib = Metashape.app.getBool("Confirm to import default camera calibration.\n\nDefault Camera: " + cameraList[int(settings.defaultCamera)])
		
		if addcalib == True:
			cam_calibration(int(settings.defaultCamera))
			doc.save()
		else:
			cam_choice = easygui.choicebox("Choose Camra", title="Choose Camera", choices=cameraList, preselect=settings.defaultCamera, callback=None)
			cam_choice_index = cameraList.index(cam_choice)
			cam_calibration(cam_choice_index)

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
		newchunk_aero()


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
		cam_calibration()
		doc.save(docPath)
		chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
		path_ref = Metashape.app.getOpenFileName("Uvoz koordinat markerjev", image_folder, "Text file (*.txt)")
		chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
		chunk.updateTransform()
		Metashape.app.update()
		doc.save(docPath)
	else:
		checkProject()
		newchunk_kalota_auto()

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
		chunk_name = "ST_IZ_" + chunk_nameraw
		chunk.label = Metashape.app.getString("Naziv chunka", chunk_name)
		doc.chunk = chunk
		doc.save(netpath)
		Metashape.app.update()
		Metashape.app.messageBox("Nalaganje slik...")
		cam_calibration()
		chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
		path_ref = Metashape.app.getOpenFileName("Import Target Coordinates", image_folder, "Text file (*.txt)")
		chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
		chunk.updateTransform()
		Metashape.app.update()
		doc.save(netpath)
	else:
		checkProject()
		newchunk_stizk_auto()


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
		chunk_name = "ST_BB_" + chunk_nameraw
		chunk.label = Metashape.app.getString("Naziv chunkae", chunk_name)
		doc.chunk = chunk
		doc.save()
		Metashape.app.update()
		Metashape.app.messageBox("Nalaganje slik...")
		cam_calibration()
		chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
		path_ref = Metashape.app.getOpenFileName("Import Target Coordinates", image_folder, "Text file (*.txt)")
		chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
		chunk.updateTransform()
		Metashape.app.update()
		doc.save()
	else:
		checkProject()
		newchunk_stbbet_auto()


def navodila_proces():
	Metashape.app.messageBox("Osnovni koraki postopka obdelave:\n\n1. Ustvari nov chunk - Menu: AtuoFTG -> Create Chunk\n*2. Nastavi kalibracijo kamere\n*3. Detekcija markerjev in uvoz tock\n\n4. Align Photos\n\n5. Preveri markerje\n6. Copy Region\n\n7. Build Dense Cloud\n\n8. Pocisti tocke na celu izkopa oz.\n   obrezi tocke na bokih stopnice.\n\n9. Build Mesh\n10. Sample Points\n11. Razrez dense cloud-a (izkop/b.bet.)\n12. Izvoz podatkov\n\nAvtor skripte: Boris Bilc / Verzija: " + app_ver)


def prazno():
	print("Prazna vrstica")

iconimg1 = ":/AutoFTG/AutoFTG-appicon.png"
iconimg2 = ":/AutoFTG/openfolder.png"
iconimg3 = ":/AutoFTG/pic_lib.png"
iconimg4 = ":/AutoFTG/picfileicon.png"
iconimg5 = ":/AutoFTG/picture-folder.png"
iconimg6 = ":/AutoFTG/target_icon_129425.png"
iconimg7 = ":/AutoFTG/target_icon_224983.png"
iconimg8 = ":/AutoFTG/target_icon_224995.png"
iconimg9 = ":/AutoFTG/kalota_m.png"
iconimg10 = ":/AutoFTG/kalota.png"
iconimg11 = ":/AutoFTG/stopnca_o.png"
iconimg12 = ":/AutoFTG/stopnca_s.png"
iconimg13 = ":/AutoFTG/ABOUTmESSAGE.png"
iconimg14 = ":/AutoFTG/CAMScreenCap.png"
iconimg15 = ":/AutoFTG/CAMVideoStudio.png"
iconimg16 = ":/AutoFTG/DeviceManager.png"
iconimg17 = ":/AutoFTG/Screenshot.png"
iconimg18 = ":/AutoFTG/CamImages.png"
iconimg19 = ":/AutoFTG/pencil-writing_107734.png"
iconimg20 = ":/AutoFTG/picture_file_image_icon_219497.png"

# Menu items
labelmenu= "Auto FTG"
Metashape.app.addMenuItem(labelmenu, appAbout, icon=iconimg1)

label1a = "AutoFTG/New Chunk"
Metashape.app.addMenuItem(label1a, newchunk_aero, icon=iconimg20)

labelNewChunk = "AutoFTG/New Chunk (2TIR)"
Metashape.app.addMenuSeparator(labelNewChunk)

label0a = "AutoFTG/New Chunk (2TIR)/KALOTA"
Metashape.app.addMenuItem(label0a, newchunk_kalota_auto, icon=iconimg10)

label0b = "AutoFTG/New Chunk (2TIR)/STOPNICA (IZKOP)"
Metashape.app.addMenuItem(label0b, newchunk_stizk_auto, icon=iconimg11)

label0c = "AutoFTG/New Chunk (2TIR)/STOPNICA (B.BET)"
Metashape.app.addMenuItem(label0c, newchunk_stbbet_auto, icon=iconimg12)

labelsep3 = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep3, prazno)

label3a = "AutoFTG/Detect markers + Import coordinates"
Metashape.app.addMenuItem(label3a, marker_targets, icon=iconimg6)

label4 = "AutoFTG/Copy Region (Bounding Box)"
Metashape.app.addMenuItem(label4, copy_bbox, icon=iconimg17)

labelsep2 = "AutoFTG/--------------------"
Metashape.app.addMenuSeparator(labelsep2)

labelset1 = "AutoFTG/Default Camera..."
Metashape.app.addMenuItem(labelset1, cam_calibrationSettings, icon=iconimg18)

label2 = "AutoFTG/Change camera/(0) Initial: NULL (Frame)"
Metashape.app.addMenuItem(label2, cam_calibrationDefault)

label2a = "AutoFTG/Change camera/(1) Initial: NULL (Fisheye)"
Metashape.app.addMenuItem(label2a, cam_calibration0)

label2b = "AutoFTG/Change camera/(2) Camera 1: HH3 by dibit (Fisheye)"
Metashape.app.addMenuItem(label2b, cam_calibration1a)

label2c = "AutoFTG/Change camera/(3) Camera 2: HH3 by dibit (Fisheye)"
Metashape.app.addMenuItem(label2c, cam_calibration1b)

label2f = "AutoFTG/Change camera/(4) Camera 3: HH3 by dibit (Fisheye)"
Metashape.app.addMenuItem(label2f, cam_calibration1c)

label2d = "AutoFTG/Change camera/(5) DJI Phantom 4 Pro 2.0 (CELU)"
Metashape.app.addMenuItem(label2d, cam_calibration2)

label2e = "AutoFTG/Change camera/(6) DJI Phantom 4 Advanced (2B)"
Metashape.app.addMenuItem(label2e, cam_calibration3)

labelsep1 = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep1, prazno)

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

labelset2 = "AutoFTG/Load project settings"
Metashape.app.addMenuItem(labelset2, checkProject, icon=iconimg16)

# labelset3 = "AutoFTG/Show current settings."
# Metashape.app.addMenuItem(labelset3, showSettings, icon=iconimg15)

labelset4 = "AutoFTG/Edit current settings"
Metashape.app.addMenuItem(labelset4, editSettings, icon=iconimg19)

labelsep5 = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep5, prazno)

labelabout = "AutoFTG/About AutoFTG..."
Metashape.app.addMenuItem(labelabout, appAbout, icon=iconimg1)

# Initialize setting for AutoFTG
initAutoFtg()
