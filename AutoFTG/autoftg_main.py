# AutoFTG - Scripts for Agisoft Metashape Pro
#
# This is an assembly of python scripts for process automation, and some existing scripts from other users
#
# Scripts were written for use in work process on project 2TDK, construction of railroad tunnels in Slovenia,
# but were later modified to support any kind of project where lots of processing is needed.
# 
# Author: Boris Bilc
# 
# Script repository (GitHub):
# ---------------------------
# URL: https://github.com/bilkos/AutoFTG-Scripts_Metashape-Pro
# 
# 
# References:
# -----------
# 
# Copy Bounding Box Script:
# - https://github.com/agisoft-llc/metashape-scripts/blob/master/src/copy_bounding_box_dialog.py
#   Copies bounding boxes from chunk to other chunks.
# 
#
# If you add or change resorces (icons, images, etc... in qtresorces.qrc), then you need to re-compile qtresorces.qrc file.
# To do that you need to navigate to script folder and run following command:
# 
# pyside2-rcc -o resource.py qtresources.qrc
# 
# If you are using VSCode that you can modify and compile UI elements with PySide2-VSC extension.
# 
# Scripts are free to use for commercial or non-commercial use.
# 
# Please use 'Issues' page in GitHub repository to report any bugs, and suggestions for improvements.
# Link to issues page: https://github.com/bilkos/AutoFTG-Scripts_Metashape-Pro/issues



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

from AutoFTG.autoftg_batch import *
from AutoFTG.autoftg_chunkquickadd import *
from AutoFTG.autoftg_settingscamedit import *
from AutoFTG.autoftg_settingschunk import *
from AutoFTG.autoftg_settingsmain import *
from AutoFTG.autoftg_copyregion import *
from AutoFTG.qtresources import *

# App info
app_name = "AutoFTG"
app_ver = "2.6.3"
appsettings_ver = "6"
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


# Load icons settings
icoCfg = ConfigParser()
icoCfgFile = 'settings_icons.ini'
icoCfgPath = os.path.expanduser('~\AppData\Local\Agisoft\Metashape Pro\scripts\AutoFTG\\').replace("\\", "/")
icoCfgFilePath =  icoCfgPath + icoCfgFile
icons_list = []


def loadIcoSettings():
	global icons_list
	icoCfgFileExists = os.path.isfile(icoCfgFilePath)	# Check if settings file exists
	if icoCfgFileExists == False:
		icoCfg.add_section("ICONS")
		icoCfg.set("ICONS", "ico-0", "icons8-xbox-cross-96.png")
		icoCfg.set("ICONS", "ico-1", "icons8-product-documents-50.png")
		icoCfg.set("ICONS", "ico-2", "icons8-documents-folder-50-2.png")
		icoCfg.set("ICONS", "ico-3", "icons8-documents-folder-50.png")
		icoCfg.set("ICONS", "ico-4", "icons8-dossier-50.png")
		icoCfg.set("ICONS", "ico-5", "icons8-pictures-folder-50-2.png")
		icoCfg.set("ICONS", "ico-6", "icons8-folded-booklet-50.png")
		icoCfg.set("ICONS", "ico-7", "icons8-images-folder-50.png")
		icoCfg.set("ICONS", "ico-8", "icons8-full-image-50.png")
		icoCfg.set("ICONS", "ico-9", "icons8-video-folder-50.png")
		icoCfg.set("ICONS", "ico-10", "icons8-ftp-50.png")
		icoCfg.set("ICONS", "ico-11", "icons8-web-camera-50.png")
		icoCfg.set("ICONS", "ico-12", "icons8-camera-on-tripod-96.png")
		icoCfg.set("ICONS", "ico-13", "icons8-sd-50.png")
		icoCfg.set("ICONS", "ico-14", "icons8-quadcopter-50.png")
		icoCfg.set("ICONS", "ico-15", "icons8-plane-48.png")
		icoCfg.set("ICONS", "ico-16", "icons8-national-park-48.png")
		icoCfg.set("ICONS", "ico-17", "icons8-ground-48.png")
		icoCfg.set("ICONS", "ico-18", "icons8-country-48.png")
		icoCfg.set("ICONS", "ico-19", "icons8-subway-50.png")
		icoCfg.set("ICONS", "ico-20", "icons8-underground-50.png")
		icoCfg.set("ICONS", "ico-21", "icons8-land-surveying-48.png")
		icoCfg.set("ICONS", "ico-22", "icons8-drawing-compass-48.png")
		icoCfg.set("ICONS", "ico-23", "icons8-camera-50.png")
		icoCfg.set("ICONS", "ico-24", "menu_kalota-modra.png")
		icoCfg.set("ICONS", "ico-25", "menu_kalota-oranzna.png")
		icoCfg.set("ICONS", "ico-26", "template_kalota-modra.png")
		icoCfg.set("ICONS", "ico-27", "template_kalota-oranzna.png")
		icoCfg.set("ICONS", "ico-28", "template_kalota-rdeca.png")
		icoCfg.set("ICONS", "ico-29", "template_kalota-vijola.png")
		icoCfg.set("ICONS", "ico-30", "template_kalota-zelena.png")
		icoCfg.set("ICONS", "ico-31", "template_stopnica-modra.png")
		icoCfg.set("ICONS", "ico-32", "template_stopnica-oranzna.png")
		icoCfg.set("ICONS", "ico-33", "template_stopnica-rdeca.png")
		icoCfg.set("ICONS", "ico-34", "template_stopnica-vijola.png")
		icoCfg.set("ICONS", "ico-35", "template_stopnica-zelena.png")

		with open(icoCfgFilePath, 'w') as icoconfig:
			camCfg.write(icoconfig)
		
		icoCfgFileExists = True

	icoCfg.read(icoCfgFilePath)
	icons_list = icoCfg.options("ICONS")
	print("Loading chunk definition icons... OK.")


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

projCfg = ConfigParser()	# INICALIZACIJA NASTAVITEV
	

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
	print("Camera settings loaded...")


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
		Metashape.app.messageBox("Camera Updated\n\n" + "Name: " + camname + "\nDesc.: " + camdesc + "\nType: " + camtype + "\nSubType: " + camsub + "\nRes.:: " + camres + " MP\nFile: " + camfile)
	else:
		camCfg.add_section(camname)
		camCfg.set(camname, "Description", camdesc)
		camCfg.set(camname, "Type", camtype)
		camCfg.set(camname, "SubType", camsub)
		camCfg.set(camname, "Resolution", camres)
		camCfg.set(camname, "File", camfile)
		Metashape.app.messageBox("Camera Created\n\n" + "Name: " + camname + "\nDesc.: " + camdesc + "\nType: " + camtype + "\nSubType: " + camsub + "\nRes.:: " + camres + " MP\nFile: " + camfile)

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


def chunksCfgLoad():
	global chunk_sections
	if menuCfgFilePathExists == False:
		menu_section_m = "GENERAL"
		menuCfg.add_section(menu_section_m)
		menuCfg.set(menu_section_m, "menu_icon", "ico-0")
		menuCfg.set(menu_section_m, "chunk_name_format", "metashape")
		menuCfg.set(menu_section_m, "chunk_name_prefix", "")
		menuCfg.set(menu_section_m, "chunk_name_suffix", "")
		menuCfg.set(menu_section_m, "work_folder", str(Metashape.app.getExistingDirectory("Project data folder (batch)")))
		menuCfg.set(menu_section_m, "export_folder", str(Metashape.app.getExistingDirectory("Project data export folder (batch)")))
		
		with open(menuCfgFilePath, 'w') as menuconfig:
			menuCfg.write(menuconfig)

	menuCfg.read(menuCfgFilePath)
	chunk_sections = menuCfg.sections()
	print("Custom chunk settings loaded...\nFile: " + menuCfgFile)


def appCfgLoad():
	global selected_data_folder
	global selected_camera
	appCfgFileExists = os.path.isfile(appCfgFilePath)	# Check if settings file exists
	if appCfgFileExists == False:
		print("\nSettings initialization...\nPlease choose data folder, and default camera.")
		Metashape.app.messageBox("Settings file not found...\nPlease choose default data folder, and default camera.")
		foldeData = str(Metashape.app.getExistingDirectory("Working data folder"))
		#selectCamDefault()
		diaSelectCamera()
		appCfg.add_section('APP SETTINGS')
		appCfg.set('APP SETTINGS', 'settings_version', appsettings_ver)
		appCfg.set('APP SETTINGS', 'folder_data', foldeData)
		appCfg.set('APP SETTINGS', 'default_camera', selected_camera)
		appCfg.set('APP SETTINGS', 'default_chunk_def', "GENERAL")

		# Writing our configuration file to 'example.cfg'
		with open(appCfgFilePath, 'w') as configfile:
			appCfg.write(configfile)

	appCfg.read(appCfgFilePath)
	checkSettingsVer()
	selected_data_folder = appCfg.get('APP SETTINGS', 'folder_data')
	selected_camera = appCfg.get('APP SETTINGS', 'default_camera')


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
	projCfgFilePath = projDocFile.replace(".psx", "_settings.ini")	# Datoteka z nastavitvami projekta
	projCfgFilePathExists = os.path.isfile(projCfgFilePath)	# Preveri, če datoteka z projektom obstaja
	
	if projCfgFilePathExists == False:
		print("\nProject settings initialization...\nPlease choose data folder, and default camera.")
		Metashape.app.messageBox("Settings initialization...\nPlease choose data folder, and default camera.")
		proj_data = Metashape.app.getExistingDirectory("Project data folder")
		diaSelectCamera()
		if projCfg.has_section('PROJECT SETTINGS') == True:
			projCfg.remove_section('PROJECT SETTINGS')
			
		projCfg.add_section('PROJECT SETTINGS')
		projCfg.set('PROJECT SETTINGS', 'settings_version', appsettings_ver)
		projCfg.set('PROJECT SETTINGS', 'folder_data', str(proj_data))
		projCfg.set('PROJECT SETTINGS', 'default_camera', selected_camera)
		projCfg.set('PROJECT SETTINGS', 'default_chunk_def', "GENERAL")
		
		# Writing our configuration file to 'example.cfg'
		with open(projCfgFilePath, 'w') as configfile:
			projCfg.write(configfile)
	
	projCfg.read(projCfgFilePath)
	checkSettingsVer()
	selected_data_folder = projCfg.get('PROJECT SETTINGS', 'folder_data')
	selected_camera = projCfg.get('PROJECT SETTINGS', 'default_camera')
	selected_chunk_def = projCfg.get('PROJECT SETTINGS', 'default_chunk_def')
	readCameraSettings(selected_camera)
	projectOpened = True
	Metashape.app.messageBox("Project settings loaded.\n\n"
			+ "Data Folder: " + str(selected_data_folder) + "\n"
			+ "Default Camera: " + str(selected_camera) + "\n"
			+ "Def. Chunk Definition: " + str(selected_chunk_def))


# Check settings version
def checkSettingsVer():
	global settingsRebuild
	if appCfg.get("APP SETTINGS", "settings_version") != appsettings_ver:
		settingsReset()
		

# Reset settings
def settingsReset():
	if projectOpened == True:
		os.remove(projCfgFilePath)
		projCfgLoad()
	else:
		os.remove(appCfgFilePath)
		appCfgLoad()


# Routine to check if project exists before initializing settings
def projectOpenedCheck():
	global projectOpened
	doc = Metashape.app.document
	#fileDoc = str(doc).replace("<Document '", "").replace("'>", "")

	if doc == "<Document ''>" or doc == None:
		projectOpened = False
		appCfgLoad()
		Metashape.app.messageBox("Empty project?\n\nSave project first, or open an existing project. (*.psx).")
	else:
		projectOpened = True
		projCfgLoad()


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


def newchunk_manual(name_prefix, name_suffix, work_folder):
	global projectOpened
	if projectOpened == True:
		doc = Metashape.app.document
		# netroot = path.dirname(netpath)
		netroot = work_folder
		try:
			image_folder = Metashape.app.getExistingDirectory("Select data folder", netroot)

		except:
			print("Add Chunk cancelled...")
			
		else:
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
		try:
			image_folder = Metashape.app.getExistingDirectory("Select data folder", netroot)

		except:
			print("Add Chunk cancelled...")
			
		else:	
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


# Choose default camera routine
def selectCamDefault():
	camCfgLoad()
	diaSelectCamera()
	if selected_camera == None:
		Metashape.app.messageBox("No camera selected. Nothing has changed...")
	else:
		if projectOpened == True:
			projCfg.set('PROJECT SETTINGS', 'default_camera', selected_camera)
			with open(projCfgFilePath, 'w') as configfile:
				projCfg.write(configfile)
			projCfg.read(projCfgFilePath)
		else:
			appCfg.set('APP SETTINGS', 'default_camera', selected_camera)
			with open(appCfgFilePath, 'w') as configfile:
				appCfg.write(configfile)
			appCfg.read(appCfgFilePath)
		
		print("Default camera settings saved.\nDefault Camera: " + selected_camera)


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


# Routine for calling Edit Settings UI - called when user want's to edit settings
def editSettings():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	editDialog = Ui_settingsDialog(parent)


# Routine for calling Edit Settings UI - called when user want's to edit settings
def addCameraDialog(camnew, camname):
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	if camnew == False:
		dia = Ui_DialogAddEditCam(parent, camnew, camname)
	else:
		dia = Ui_DialogAddEditCam(parent, camnew, camname="")


# Routine for calling Edit Settings UI - called when user want's to edit settings
def diaSelectCamera():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	diaChCam = Ui_dialogChooseCamera(parent)


# Routine for calling Edit Settings UI - called when user want's to edit settings
def camerasEditor():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	camEditDialog = Ui_dialogCamGui(parent)


# Routine for calling Copy Regions UI
def copy_bbox():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	dlg = CopyBoundingBoxDlg(parent)


def diaAddChunkSingle():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	dia = Ui_DialogAddChunkQuick(parent)


def diaAddChunkBatch():
	projectOpenedCheck()
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	dia2 = Ui_DialogBatchChunk(parent)


def diaChunkSettings():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()
	dia_cs = Ui_DialogChunkSettings(parent)


icon_app = ":/icons/AutoFTG-appicon.png"
icon_app2 = ":/icons/AUTOFTG-V2.png"
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

labelAddChSingle = "AutoFTG/Add Chunk (Single)"
Metashape.app.addMenuItem(label=labelAddChSingle, func=diaAddChunkSingle, shortcut="Ctrl++", icon=iconadd)

labelAddChBatch = "AutoFTG/Batch Chunk Creator"
Metashape.app.addMenuItem(label=labelAddChBatch, func=diaAddChunkBatch, shortcut="Ctrl+*", icon=icon4)

labelChSet = "AutoFTG/Chunk Definition Settings"
Metashape.app.addMenuItem(label=labelChSet, func=diaChunkSettings, icon=":/icons/icons8-content-50.png")

labelsep1a = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep1a, prazno)

label3a = "AutoFTG/Detect markers && Import coordinates"
Metashape.app.addMenuItem(label3a, marker_targets, icon=icon38)

label4 = "AutoFTG/Copy Region (Bounding Box)"
Metashape.app.addMenuItem(label4, copy_bbox, icon=icon15)

labelsep1 = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep1, prazno)

label2 = "AutoFTG/Change Camera (Chunk)"
Metashape.app.addMenuItem(label2, selectCamChunk, icon=icon8)

label2aaa = "AutoFTG/Set Default Camera (Project)"
Metashape.app.addMenuItem(label2aaa, selectCamDefault, icon=icon35)

label2cccc = "AutoFTG/Cameras Editor"
Metashape.app.addMenuItem(label2cccc, camerasEditor, icon=icon9)

labelsep55 = "AutoFTG/--------------------"
Metashape.app.addMenuItem(labelsep55, prazno)

labelset2 = "AutoFTG/Load Project Settings"
Metashape.app.addMenuItem(labelset2, projectOpenedCheck, icon=icon40)

labelset4 = "AutoFTG/Edit Loaded Settings"
Metashape.app.addMenuItem(labelset4, editSettings, icon=icon32)

labelset2i = "Load Project Settings"
Metashape.app.addMenuItem(labelset2i, projectOpenedCheck, icon=icon40)

labelAddChQui = "Add Chunk (Single)"
Metashape.app.addMenuItem(label=labelAddChQui, func=diaAddChunkSingle, icon=iconadd)

labelAddChBat = "Add Chunk (Multi)"
Metashape.app.addMenuItem(label=labelAddChBat, func=diaAddChunkBatch, icon=icon4)

labelCopyReg = "Copy Region"
Metashape.app.addMenuItem(labelCopyReg, copy_bbox, icon=icon15)

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

# Initialize AutoFTG
def loadAutoftg():
	global projectOpened
	camCfgLoad()
	chunksCfgLoad()
	loadIcoSettings()
	projectOpenedCheck()
	checkSettingsVer()
	print("\n\nAutoFTG initialized...\nApp Version: " + str(app_ver) + "\nSettings Version: " + str(appCfg.get('APP SETTINGS', 'settings_version')))
	print(str(app_author))

# Run
loadAutoftg()

