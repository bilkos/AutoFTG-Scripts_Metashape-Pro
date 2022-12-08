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
from easygui import EgStore
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QIcon
from AutoFTG import resource

# VERZIJA APLIKACIJE
app_name = "AutoFTG"
app_ver = "2.0.1-beta"
app_author = "Boris Bilc, Slovenia"
app_repo = "URL: https://github.com/bilkos/AutoFTG-Scripts_Metashape-Pro"
ref_repo = "Agisoft GitHub repository - https://github.com/agisoft-llc/metashape-scripts"
ref_scripts = "Copy Bounding Box Script - https://github.com/agisoft-llc/metashape-scripts/blob/master/src/copy_bounding_box_dialog.py"
app_about = "AutoFTG - Scripts for process automation in Agisoft Metashape Pro\n This is an assembly of existing scripts from other users, and some additional scripts written for use in work process at project 2TIR, tunnel T8-KP in Slovenia."

def appAbout():
	app_aboutmsg = app_name + "\n" + app_ver + "\n" + app_author + app_about + "\n\n" + app_repo + "\n\n" + ref_repo + "\n" + ref_scripts + "\n"
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

if settingsFilenameExists == False:
	print("\n\nInicializacija osnovnih nastavitev.\nUstvari nov AvtoFTG propjekt za uporabo nastavitev za posamezen projekt. Menu: <AutoFTG>")
	settings.store()    # persist the settings
else:
	print("\n\nNalozene so osnovne nastavitve.\nUstvari nov AvtoFTG propjekt za uporabo nastavitev za posamezen projekt. Menu: <AutoFTG>")
	print("Projekt: " + str(settings.fileProject))
	print("Mapa projekta: " + str(settings.folderProject))
	print("Mapa podatki: " + str(settings.foldeData))
	print("Privzeta kalibracija (ID): " + str(cameraList[int(settings.defaultCamera)]))
	print("\nUrejanje nastavitev je dostopno preko menija <AutoFTG>.")


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
		print("\n\nInicializacija nastavitev za projekt...")
		settings.fileProject = fileProject
		settings.folderProject = os.getcwd().replace('\\', '/')
		Metashape.app.messageBox("Pokazi mapo z delovnimi podatki...")
		settings.foldeData = Metashape.app.getExistingDirectory("Mapa z podatki")
		cam_calibrationSettings()
		settings.store()
		print("Izbrana delovna mapa: " + str(settings.foldeData))
		print("Inicializacija nastavitev za AutoFTG končana.")
		Metashape.app.messageBox("Inicializacija nastavitev za projekt koncana.\n\n"
			+ "Datoteka z nastavitvami: " + str(settingsFilename) + "\n"
			+ "Projekt: " + str(settings.fileProject) + "\n"
			+ "Mapa projekta: " + str(settings.folderProject) + "\n"
			+ "Mapa podatki: " + str(settings.foldeData) + "\n"
			+ "Privzeta kalibracija (ID): " + str(cameraList[int(settings.defaultCamera)])
			)
		fileDoc.save(fileProject)
		projectOpened = True

	else:
		print("\n\nNastavitve projekta nalozene...")
		print("Projekt: " + str(settings.fileProject))
		print("Mapa projekta: " + str(settings.folderProject))
		print("Mapa podatki: " + str(settings.foldeData))
		print("Privzeta kalibracija (ID): " + str(cameraList[int(settings.defaultCamera)]))
		settings.store()
		Metashape.app.messageBox("Nastavitve nalozene.\n\n"
			+ "Datoteka z nastavitvami: " + str(settingsFilename) + "\n"
			+ "Projekt: " + str(settings.fileProject) + "\n"
			+ "Mapa projekta: " + str(settings.folderProject) + "\n"
			+ "Mapa podatki: " + str(settings.foldeData) + "\n"
			+ "Privzeta kalibracija (ID): " + str(cameraList[int(settings.defaultCamera)])
			)
		projectOpened = True


def checkProject():
	global projectOpened
	fileProject = str(Metashape.app.document).replace("<Document '", "").replace("'>", "")
	if fileProject == '':
		Metashape.app.messageBox("Prazen projekt!\n\nNajprej shrani ali odpri obstojec projekt (datoteka *.psx).")
		novProjekt()
	else:
		initAutoFtgProjekt()
		projectOpened = True


# def initMain():
# 	if uporabiProjekt == True:
# 		initAutoFtgProjekt()
# 	else:
# 		initAutoFtg()


def project_folder_change():
	settings.foldeData = Metashape.app.getExistingDirectory("Mapa z podatki")
	settings.store()
	print("Izbrana delovna mapa: " + str(settings.foldeData))


def novProjekt():
	global projectOpened
	doc = Metashape.app.document
	docPath = Metashape.app.getSaveFileName("Ustvari nov projekt", "",  "Metashape Project (*.psx)")
	try:
		doc.save(docPath)
		Metashape.app.messageBox("Projerkt shranjen.\n")
		initAutoFtgProjekt()
		projectOpened = True
	except RuntimeError:
		Metashape.app.messageBox("Napaka! Projerkt ni shranjen.")
		projectOpened = False
	
	Metashape.app.update()

#	settingsProjekt = docPath.replace(".psx", "_settings.txt")		# Dattoteka z nastavitvami
#	settingsProjektExists = os.path.isfile(settingsProjekt)	# Preveri, če datoteka z nastavitvami obstaja
#	settings = Settings(settingsFilename)	# INICALIZACIJA NASTAVITEV
#	
#	if settingsProjektExists == False:
#		print("\n\nInicializacija nastavitev AutoFTG za projekt...")
#		settings.fileProject = docPath
#		settings.foldeData = Metashape.app.getExistingDirectory("Izberi mapo z podatki...")
#		cam_calibrationSettings()
#		settings.store()    # persist the settings
#		print("Projekt = " + str(settings.projectsFile))
#		print("Podatki = " + str(settings.dataFolder))
#		print("Privzeta kalibracija (ID) = " + str(settings.defaultCamera))


camcalMsg = "Izberi privzeto kalibracijo za uporabo pri dodajanju novih chunkov"
camcalTitle = "Privzeta Kalibracija"
camcalPreselect = int(settings.defaultCamera)


# Funkcija za izbiro privzete kalibracije
def cam_calibrationSettings(msg=camcalMsg, title=camcalTitle, choices=cameraList, preselect=camcalPreselect, callback=None, run=True):

	mb = easygui.choicebox(msg, title, choices=choices, preselect=preselect, callback=callback)

	if run:
		# reply = mb.run()
		if mb == None:
			print("Nastavitev za kamero nespremenjena.")
			settings.store()
		else:
			replyindex = choices.index(mb)
			settings.defaultCamera = str(replyindex)
			settings.store()
			print("Nastavitve shranjene...\nPrivzeta kalibracija: " + mb)
		# return reply
	else:
		print("\nNastavitev za kamero nalozena....\n")
		settings.store()
		return mb


# # Izbira ps
# def def_pointsample():
# 	current_ps = settings.defaulfPointSample
# 	new_ps = Metashape.app.getString("Default point sample spacing (m):", current_ps)
# 	
# 	if new_ps == current_ps:
# 		print("No changes... Old point sampling value kept (" + str(current_ps) + "m)")
# 	elif (float(new_ps) > 0):
# 		settings.defaulfPointSample = new_ps
# 		settings.store()
# 		print("Settings changed..." + str(settings.defaulfPointSample))
# 	else:
# 		print("Wrong value. Noting changed.")
# 
# # Izbira filter
# def def_pointfilter():
# 	current_pf = settings.defaultPointFilter
# 	new_pf = Metashape.app.getString("Default point sample spacing (m):", current_pf)
# 	
# 	if new_pf == current_pf:
# 		print("No changes... Old point filtering value kept (" + str(current_pf) + "m)")
# 	elif (float(new_pf) > 0):
# 		settings.defaultPointFilter = new_pf
# 		settings.store()
# 		print("Settings changed..." + str(settings.defaultPointFilter))
# 	else:
# 		print("Wrong value. Noting changed.")


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
		print("Kopiranje regije...")

		doc = Metashape.app.document

		fromChunk = doc.chunks[self.fromChunk.currentIndex()]

		toChunks = []
		for i in range(self.toChunks.count()):
			if self.toChunks.item(i).isSelected():
				toChunks.append(doc.chunks[i])

		print("Kopiram regije iz chunka: '" + fromChunk.label + "' v " + str(len(toChunks)))

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
		
		print("RKopiranje končano!\Iz: " + fromChunk.label + "\V: " + str(len(toChunks)) + "\n")
		self.reject()
		

def copy_bbox():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()

	dlg = CopyBoundingBoxDlg(parent)


def progress_print(p):
		print('Izvedeno: {:.2f}%'.format(p))

image_folder = settings.foldeData

def cam_calibration():
	calsetting = int(settings.defaultCamera)
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


# Nalozi kalibracijo kamere / Nulta / Tip: Fisheye
def cam_calibrationDefault():
	doc = Metashape.app.document
	chunk = doc.chunk
	
	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Frame
#	my_calib = Metashape.Calibration()
#	my_calib.load(path="\\\\Stroj\\1_ftg_t8-kp\\100_T8-KP_OBDELAVA\\dibit-kamera_HH3_031_Fisheye.xml", format=Metashape.CalibrationFormatXML)
#	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Kalibracija nastavljena.\n\Kamera: null\nTip: Frame\nDatoteka: ---")
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
	Metashape.app.messageBox("Kalibracija nastavljena.\n\Kamera: null\nTip: Fisheye\nDatoteka: ---")
	Metashape.app.update()


# Nalozi kalibracijo kamere / HH3_031 by dibit / Tip: Fisheye
def cam_calibration1a():
	doc = Metashape.app.document
	chunk = doc.chunk	

	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Fisheye
	my_calib = Metashape.Calibration()
	my_calib.load(path="\\\\Stroj\\1_ftg_t8-kp\\100_T8-KP_OBDELAVA\\dibit-kamera_HH3_031_Fisheye.xml", format=Metashape.CalibrationFormatXML)
	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Kalibracija nastavljena.\n\Kamera:  1: HH3_031 by dibit\nTip: Fisheye\nDatoteka: dibit-kamera_HH3_031_Fisheye.xml")
	Metashape.app.update()


# Nalozi kalibracijo kamere / HH3 KAMERA 2 by dibit / Tip: Fisheye
def cam_calibration1b():
	doc = Metashape.app.document
	chunk = doc.chunk	

	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Fisheye
	my_calib = Metashape.Calibration()
	my_calib.load(path="\\\\Stroj\\1_ftg_t8-kp\\100_T8-KP_OBDELAVA\\dibit-kamera-2_HH3_Fisheye.xml", format=Metashape.CalibrationFormatXML)
	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Kalibracija nastavljena.\n\Kamera:  2: HH3 by dibit\nTip: Fisheye\nDatoteka: dibit-kamera-2_HH3_Fisheye.xml")
	Metashape.app.update()


# Nalozi kalibracijo kamere / HH3 KAMERA 2 by dibit / Tip: Fisheye
def cam_calibration1c():
	doc = Metashape.app.document
	chunk = doc.chunk	

	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Fisheye
	my_calib = Metashape.Calibration()
	my_calib.load(path="\\\\Stroj\\1_ftg_t8-kp\\100_T8-KP_OBDELAVA\\dibit-kamera-3_HH3_Fisheye.xml", format=Metashape.CalibrationFormatXML)
	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Kalibracija nastavljena.\n\Kamera: HH3 by dibit\nTip: Fisheye\nDatoteka: dibit-kamera-3_HH3_Fisheye.xml")
	Metashape.app.update()


# Nalozi kalibracijo kamere / DJI Phantom 4 Pro 2 (CELU) / Tip: Frame
def cam_calibration2():
	doc = Metashape.app.document
	chunk = doc.chunk	

	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Frame
	my_calib = Metashape.Calibration()
	my_calib.load(path="\\\\STROJ\\AeroProjekti-Arhiv\\_KalibracijeKamer\\DJI-Phantom-4-Pro2_20MP_2022-01_CELU.xml", format=Metashape.CalibrationFormatXML)
	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Kalibracija nastavljena.\n\Kamera: DJI Phantom 4 Pro 2.0 (CELU)\nTip: Frame\nDatoteka: DJI-Phantom-4-Pro2_20MP_2022-01_CELU.xml")
	Metashape.app.update()


# Nalozi kalibracijo kamere / DJI Phantom 4 Advanced (2B) / Tip: Frame
def cam_calibration3():
	doc = Metashape.app.document
	chunk = doc.chunk	

	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Frame
	my_calib = Metashape.Calibration()
	my_calib.load(path="\\\\STROJ\\AeroProjekti-Arhiv\\_KalibracijeKamer\\DJI-Phantom-4-Advanced_20MP_2022-01_2B.xml", format=Metashape.CalibrationFormatXML)
	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Kalibracija nastavljena.\n\Kamera: DJI Phantom 4 Advanced (2B)\nTip: Frame\nDatoteka: DJI-Phantom-4-Advanced_20MP_2022-01_2B.xml")
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
		Metashape.app.messageBox("Detkcija markerjev končana.\n\nNaslednje je na vrsti uvoz koordinat.\nDatoeka mora imeti glavo, koordinate bodo brane od vrstice 7 in naprej.")
		
		# Uvoz koordinat za markerje
		path_ref = Metashape.app.getOpenFileName("Uvoz koordinat za " + chunk.label, netroot, "Text file (*.txt)")
		chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)

		# Posodobi pogled
		chunk.updateTransform()
		
		Metashape.app.messageBox("Target coordinates imported.\n\nNext step: Workflow > Align Photos")
		Metashape.app.update()
		
		# Shrani projekt
		doc.save()


#def run_samplepoints():
#	doc = Metashape.app.document
#	chunk = doc.chunk
#	# sample_int = 0.025
#	sampling = Metashape.app.getBool("Start Point Sampling?")
#	
#	if sampling == True:
#		chunk.dense_cloud.copy()
#		# Sample points
#		chunk.samplePoints(source_data=Metashape.ModelData, uniform_sampling=False)
#		Metashape.app.messageBox("Sample Points process complete!")
#		doc.save()
#		Metashape.app.update()


#def run_samplepointsuni():
#	doc = Metashape.app.document
#	chunk = doc.chunk
#	sample_int = float(settings.defaulfPointSample)
#	sampling = Metashape.app.getBool("Start Uniform Point Sampling?\nChoose (No) to change point spacing value.")
#	
#	if sampling == True:
#		chunk.dense_cloud.copy()
#		# Sample points
#		chunk.samplePoints(source_data=Metashape.ModelData, uniform_sampling=True, points_spacing=sample_int)
#		Metashape.app.messageBox("Sample Points process complete!")
#		doc.save()
#		Metashape.app.update()
#	else:
#		sample_int = Metashape.app.getFloat("New spacing (m):", sample_int)
#		chunk.dense_cloud.copy()
#		chunk.samplePoints(source_data=Metashape.ModelData, uniform_sampling=True, points_spacing=sample_int)
#		Metashape.app.messageBox("Sample Points process complete!")
#		doc.save()
#		Metashape.app.update()	


#def run_filterpoints():
#	doc = Metashape.app.document
#	chunk = doc.chunk
#	filter_int = float(settings.defaultPointFilter)
#	filtering = Metashape.app.getBool("Start process with default settings? To change values choose 'No'.\n\nMode: Uniform sampling\nDefault spacing: " + str(filter_int) + "m")
# 	
#	if filtering == True:
#		chunk.dense_cloud.copy()
#		# Sample points
#		chunk.filterDenseCloud(point_spacing=filter_int)
#		Metashape.app.messageBox("Filtering process complete!\n\nNew point spacing: " + filter_int + "m")
#		doc.save()
#		Metashape.app.update()
#	else:
#		filter_int = Metashape.app.getFloat("Enter point spacing (m):", filter_int)
#		chunk.dense_cloud.copy()
#		chunk.filterDenseCloud(point_spacing=filter_int)
#		Metashape.app.messageBox("Filtering process complete!\n\nNew point spacing: " + filter_int + "m")
#		doc.save()
#		Metashape.app.update()


def find_files(folder, types):
    return [entry.path for entry in os.scandir(folder) if (entry.is_file() and os.path.splitext(entry.name)[1].lower() in types)]


def newchunk_kalota_auto():
	global projectOpened
	doc = Metashape.app.document
	docPath = Metashape.app.document.path
	# netroot = path.dirname(netpath)
	if projectOpened == True:
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

def newchunk_stizk_auto():
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


def newchunk_stbbet_auto():
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


def newchunk_aero():
	if projectOpened == True:
		doc = Metashape.app.document
		netpath = Metashape.app.document.path
		# netroot = path.dirname(netpath)
		netroot = settings.foldeData
		image_folder = Metashape.app.getExistingDirectory("Select photos folder (KALOTA)", netroot)
		photos = find_files(image_folder, [".jpg", ".jpeg", ".JPG", ".JPEG"])
		chunk = doc.addChunk()
		chunk.addPhotos(photos)
		chunk_nameraw = os.path.basename(image_folder)
		chunk.label = Metashape.app.getString("Chunk Name", chunk_nameraw)
		doc.chunk = chunk
		doc.save()
		Metashape.app.messageBox("New chunk created!\n\nChunk Name = " + chunk_nameraw)
		addcalib = Metashape.app.getBool("Import default camera calibration?\n\nCamera: NULL - Fisheye")
		if addcalib == True:
			cam_calibration()
			doc.save()
		nadaljujem = Metashape.app.getBool("Continue with marker detection and coordinates import?")
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

# def newchunk_stizk():
# 	doc = Metashape.app.document
# 	netpath = Metashape.app.document.path
# 	# netroot = path.dirname(netpath)
# 	netroot = settings.foldeData
# 	image_folder = Metashape.app.getExistingDirectory("Select photos folder (STOPNICA - IZKOP)", netroot)
# 	photos = find_files(image_folder, [".jpg", ".jpeg", ".JPG", ".JPEG"])
# 	chunk = doc.addChunk()
# 	chunk.addPhotos(photos)
# 	chunk_nameraw = os.path.basename(image_folder)
# 	chunk_name = "ST_IZ_" + chunk_nameraw
# 	chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
# 	doc.chunk = chunk
# 	doc.save()
# 	Metashape.app.messageBox("New chunk created!\n\nChunk Name = " + chunk_name)
# 	addcalib = Metashape.app.getBool("Import default camera calibration?\n\nCamera: NULL - Fisheye")
# 	if addcalib == True:
# 		cam_calibration()
# 		doc.save()
# 	nadaljujem = Metashape.app.getBool("Continue with marker detection and coordinates import?")
# 	if nadaljujem == True:
# 		chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
# 		Metashape.app.messageBox("Marker Detection complete!\n\nNext step: Choose file with target coordinates.\nPoint file must have header.\nImport starts at line 7.")
# 		path_ref = Metashape.app.getOpenFileName("Import Target Coordinates", image_folder, "Text file (*.txt)")
# 		chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
# 		chunk.updateTransform()
# 		Metashape.app.messageBox("Target coordinates imported.\n\nNext step: Workflow > Align Photos")
# 		Metashape.app.update()
# 		doc.save()


# def newchunk_stbbet():
# 	doc = Metashape.app.document
# 	netpath = Metashape.app.document.path
# 	# netroot = path.dirname(netpath)
# 	netroot = settings.foldeData
# 	image_folder = Metashape.app.getExistingDirectory("Select photos folder (STOPNICA - B.BET.)", netroot)
# 	photos = find_files(image_folder, [".jpg", ".jpeg", ".JPG", ".JPEG"])
# 	chunk = doc.addChunk()
# 	chunk.addPhotos(photos)
# 	chunk_nameraw = os.path.basename(image_folder)
# 	chunk_name = "ST_BB_" + chunk_nameraw
# 	chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
# 	doc.chunk = chunk
# 	doc.save()
# 	Metashape.app.messageBox("New chunk created!\n\nChunk Name = " + chunk_name)
# 	addcalib = Metashape.app.getBool("Import default camera calibration?\n\nCamera: NULL - Fisheye")
# 	if addcalib == True:
# 		cam_calibration()
# 		doc.save()
# 	nadaljujem = Metashape.app.getBool("Continue with marker detection and coordinates import?")
# 	if nadaljujem == True:
# 		chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
# 		Metashape.app.messageBox("Marker Detection complete!\n\nNext step: Choose file with target coordinates.\nPoint file must have header.\nImport starts at line 7.")
# 		path_ref = Metashape.app.getOpenFileName("Import Target Coordinates", image_folder, "Text file (*.txt)")
# 		chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
# 		chunk.updateTransform()
# 		Metashape.app.messageBox("Target coordinates imported.\n\nNext step: Workflow > Align Photos")
# 		Metashape.app.update()
# 		doc.save()


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

# Menu items
#labelMain = "<Auto FTG>"
#Metashape.app.addMenuSeparator(labelMain)

label1a = "<Auto FTG>/Nov chunk"
Metashape.app.addMenuItem(label1a, newchunk_aero, icon=iconimg4)

labelNewChunk = "<Auto FTG>/Nov chunk (Predor)"
Metashape.app.addMenuSeparator(labelNewChunk)

label0a = "<Auto FTG>/Nov chunk (Predor)/KALOTA"
Metashape.app.addMenuItem(label0a, newchunk_kalota_auto, icon=iconimg10)

label0b = "<Auto FTG>/Nov chunk (Predor)/STOPNICA (IZKOP)"
Metashape.app.addMenuItem(label0b, newchunk_stizk_auto, icon=iconimg11)

label0c = "<Auto FTG>/Nov chunk (Predor)/STOPNICA (B.BET)"
Metashape.app.addMenuItem(label0c, newchunk_stbbet_auto, icon=iconimg12)

#label1b = "<Auto FTG>/New Chunk/Add Chunk: STOPNICA - IZKOP"
#Metashape.app.addMenuItem(label1b, newchunk_stizk)
#
#label1c = "<Auto FTG>/New Chunk/Add Chunk: STOPNICA - B.BET."
#Metashape.app.addMenuItem(label1c, newchunk_stbbet)

#labelsep4 = "<Auto FTG>/Camera Calibration"
#Metashape.app.addMenuSeparator(labelsep4)

labelsep2 = "<Auto FTG>/--------------------"
Metashape.app.addMenuSeparator(labelsep2)

labelNewChunk = "<Auto FTG>/Kalibracija Kamere/"
Metashape.app.addMenuSeparator(labelNewChunk)

labelset1 = "<Auto FTG>/Kalibracija Kamere/Privzeta kalibracija..."
Metashape.app.addMenuItem(labelset1, cam_calibrationSettings, icon=iconimg3)

label2 = "<Auto FTG>/Kalibracija Kamere/Druge Kalibracije/(0) Initial: NULL (Frame)"
Metashape.app.addMenuItem(label2, cam_calibrationDefault)

label2a = "<Auto FTG>/Kalibracija Kamere/Druge Kalibracije/(1) Initial: NULL (Fisheye)"
Metashape.app.addMenuItem(label2a, cam_calibration0)

label2b = "<Auto FTG>/Kalibracija Kamere/Druge Kalibracije/(2) Camera 1: HH3 by dibit (Fisheye)"
Metashape.app.addMenuItem(label2b, cam_calibration1a)

label2c = "<Auto FTG>/Kalibracija Kamere/Druge Kalibracije/(3) Camera 2: HH3 by dibit (Fisheye)"
Metashape.app.addMenuItem(label2c, cam_calibration1b)

label2cc = "<Auto FTG>/Kalibracija Kamere/Druge Kalibracije/(4) Camera 3: HH3 by dibit (Fisheye)"
Metashape.app.addMenuItem(label2cc, cam_calibration1c)

label2d = "<Auto FTG>/Kalibracija Kamere/Druge Kalibracije/(5) DJI Phantom 4 Pro 2.0 (CELU)"
Metashape.app.addMenuItem(label2d, cam_calibration2)

label2e = "<Auto FTG>/Kalibracija Kamere/Druge Kalibracije/(6) DJI Phantom 4 Advanced (2B)"
Metashape.app.addMenuItem(label2e, cam_calibration3)

labelsep3 = "<Auto FTG>/--------------------"
Metashape.app.addMenuItem(labelsep3, prazno)

label3a = "<Auto FTG>/Detekcija matkertjev + Uvoz koordinat"
Metashape.app.addMenuItem(label3a, marker_targets, icon=iconimg6)

labelsep2 = "<Auto FTG>/--------------------"
Metashape.app.addMenuSeparator(labelsep2)

label4 = "<Auto FTG>/Kopiranje regije za procesiranje (Med chunki)"
Metashape.app.addMenuItem(label4, copy_bbox)

labelsep1 = "<Auto FTG>/--------------------"
Metashape.app.addMenuItem(labelsep1, prazno)

#label6 = "<Auto FTG>/Filter Points (Uniform - Region oriented)"
#Metashape.app.addMenuItem(label6, run_filterpoints)

#labelsep3 = "<Auto FTG>/--------------------"
#Metashape.app.addMenuItem(labelsep3, prazno)

#label5a = "<Auto FTG>/Sample Points (Surface Detail)"
#Metashape.app.addMenuItem(label5a, run_samplepoints)

#label5b = "<Auto FTG>/Sample Points (Uniform Spacing)"
#Metashape.app.addMenuItem(label5b, run_samplepointsuni)

#labelsep4 = "<Auto FTG>/--------------------"
#Metashape.app.addMenuItem(labelsep4, prazno)

labelset0 = "<Auto FTG>/Nastavi privzeto delovno mapo..."
Metashape.app.addMenuItem(labelset0, project_folder_change)

labelset2 = "<Auto FTG>/Nalozi nastavitve za projekt..."
Metashape.app.addMenuItem(labelset2, checkProject)

# labelset3 = "<Auto FTG>/Change default sampling spacing..."
# Metashape.app.addMenuItem(labelset3, def_pointsample)

labelabout = "<Auto FTG>/About AutoFTG..."
Metashape.app.addMenuItem(labelabout, appAbout)

