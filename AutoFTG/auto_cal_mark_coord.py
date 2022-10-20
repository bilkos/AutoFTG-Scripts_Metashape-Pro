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

   
import Metashape
import os, sys, time
from os import path
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtGui import QIcon
import easygui
from easygui import EgStore

app_ver = "1.7.4"

# Checking compatibility
compatible_major_version = "2.0"
found_major_version = ".".join(Metashape.app.version.split('.')[:2])
if found_major_version != compatible_major_version:
	raise Exception("Incompatible Metashape version: {} != {}".format(found_major_version, compatible_major_version))



# NALAGANJE NASTAVITEV
class Settings(EgStore):

	def __init__(self, filename):  # filename is required
		# Privzete vrednosti nastavitev - inicializacija nastavitev pri prvem zagonu
		self.defaultCalibration = "0"
		self.defaulfPointSample = "0.02"
		self.defaultPointFilter = "0.02"
		self.projectsFolder = ""
		# Inicializacija
		self.filename = filename  # this is required
		self.restore()

settingsFilename = "C:/Program Files/Agisoft/Metashape Pro/AutoFTGconfig.txt"		# Dattoteka z nastavitvami
settingsFilenameExists = os.path.isfile(settingsFilename)	# Preveri, če datoteka z nastavitvami obstaja
settings = Settings(settingsFilename)	# INICALIZACIJA NASTAVITEV

if settingsFilenameExists == False:
	settings.projectsFolder = Metashape.app.getExistingDirectory("Select projects folder...")
	settings.store()    # persist the settings
	print("Initializing default settings for AutoFTG...")
else:
	print("Initializing settings for AutoFTG...\nLoaded settings:")
	print("Calibration: " + str(settings.defaultCalibration))
	print("Point sample spacing: " + str(settings.defaulfPointSample) + "m")
	print("Point filter spacing: " + str(settings.defaultPointFilter) + "m")
	print("To change settings use <AutoFTG> menu.")

# Izbira privzete kalibracije
def cam_calibrationSettings(msg="Choose default calibration that will be\nused when creating new chunk.", title="Default Calibration", 
				choices=["0 - NULL: Frame", "1 - NULL: Fisheye", "2 - HH3_031-1 by dibit: Fisheye", "3 - HH3_031-2 by dibit: Fisheye", "4 - HH3_031-3 by dibit: Fisheye", "5 - DJI Phantom 4 Pro 2.0 (CELU)", "6 - DJI Phantom 4 Advanced (2B)"], 
				preselect=int(settings.defaultCalibration), callback=None, run=True):

	mb = easygui.choicebox(msg, title, choices=choices, preselect=preselect, callback=callback)

	if run:
		# reply = mb.run()
		if mb == None:
			print("Noting changed.")
		else:
			replyindex = choices.index(mb)
			settings.defaultCalibration = replyindex
			settings.store()
			print("New settings applied...\nDefault cal.: " + mb)
		# return reply
	else:
		print("Noting changed.")
		return mb


# Izbira ps
def def_pointsample():
	current_ps = settings.defaulfPointSample
	new_ps = Metashape.app.getString("Default point sample spacing (m):", current_ps)
	
	if new_ps == current_ps:
		print("No changes... Old point sampling value kept (" + str(current_ps) + "m)")
	elif (float(new_ps) > 0):
		settings.defaulfPointSample = new_ps
		settings.store()
		print("Settings changed..." + str(settings.defaulfPointSample))
	else:
		print("Wrong value. Noting changed.")

# Izbira filter
def def_pointfilter():
	current_pf = settings.defaultPointFilter
	new_pf = Metashape.app.getString("Default point sample spacing (m):", current_pf)
	
	if new_pf == current_pf:
		print("No changes... Old point filtering value kept (" + str(current_pf) + "m)")
	elif (float(new_pf) > 0):
		settings.defaultPointFilter = new_pf
		settings.store()
		print("Settings changed..." + str(settings.defaultPointFilter))
	else:
		print("Wrong value. Noting changed.")



class CopyBoundingBoxDlg(QtWidgets.QDialog):

	def __init__(self, parent):

		QtWidgets.QDialog.__init__(self, parent)
		self.setWindowTitle("Copy bounding box")

		self.labelFrom = QtWidgets.QLabel("From Chunk")
		self.labelTo = QtWidgets.QLabel("To Chunk")

		self.fromChunk = QtWidgets.QComboBox()
		for chunk in Metashape.app.document.chunks:
			self.fromChunk.addItem(chunk.label)

		self.toChunks = QtWidgets.QListWidget()
		self.toChunks.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
		for chunk in Metashape.app.document.chunks:
			self.toChunks.addItem(chunk.label)

		self.btnOk = QtWidgets.QPushButton("Ok")
		self.btnOk.setFixedSize(120, 36)
		self.btnOk.setToolTip("Copy bounding box to all selected chunks")

		self.btnQuit = QtWidgets.QPushButton("Close")
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
		print("Script started...")

		doc = Metashape.app.document

		fromChunk = doc.chunks[self.fromChunk.currentIndex()]

		toChunks = []
		for i in range(self.toChunks.count()):
			if self.toChunks.item(i).isSelected():
				toChunks.append(doc.chunks[i])

		print("Copying bounding box from chunk '" + fromChunk.label + "' to " + str(len(toChunks)) + " chunks...")

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
		
		print("Region copied!\nFrom: " + fromChunk.label + "\nTo: " + str(len(toChunks)) + "\n\nDone!")
		self.reject()
		

def copy_bbox():
	app = QtWidgets.QApplication.instance()
	parent = app.activeWindow()

	dlg = CopyBoundingBoxDlg(parent)


def progress_print(p):
		print('Task progress: {:.2f}%'.format(p))

image_folder = settings.projectsFolder

def cam_calibration():
	calsetting = int(settings.defaultCalibration)
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
	Metashape.app.messageBox("Camera Calibration configured.\n\nCamera: null\nType: Frame\nFile: ---")
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
	Metashape.app.messageBox("Camera Calibration configured.\n\nCamera: null\nType: Fisheye\nFile: ---")
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
	Metashape.app.messageBox("Camera Calibration imported.\n\nCamera: Kamera 1: HH3_031 by dibit\nType: Fisheye\nFile: dibit-kamera_HH3_031_Fisheye.xml")
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
	Metashape.app.messageBox("Camera Calibration imported.\n\nCamera: Kamera 2: HH3 by dibit\nType: Fisheye\nFile: dibit-kamera-2_HH3_Fisheye.xml")
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
	Metashape.app.messageBox("Camera Calibration imported.\n\nCamera: Kamera 3: HH3 by dibit\nType: Fisheye\nFile: dibit-kamera-3_HH3_Fisheye.xml")
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
	Metashape.app.messageBox("Camera Calibration imported.\n\nCamera: DJI Phantom 4 Pro 2.0 (CELU)\nType: Frame\nFile: DJI-Phantom-4-Pro2_20MP_2022-01_CELU.xml")
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
	Metashape.app.messageBox("Camera Calibration imported.\n\nCamera: DJI Phantom 4 Advanced (2B)\nType: Frame\nFile: DJI-Phantom-4-Advanced_20MP_2022-01_2B.xml")
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
		Metashape.app.messageBox("Marker Detection complete!\n\nNext step: Choose file with target coordinates.\nPoint file must have header.\nImport starts at line 7.")
		
		# Uvoz koordinat za markerje
		path_ref = Metashape.app.getOpenFileName("Import Target Coordinates", netroot, "Text file (*.txt)")
		chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)

		# Posodobi pogled
		chunk.updateTransform()
		
		Metashape.app.messageBox("Target coordinates imported.\n\nNext step: Workflow > Align Photos")
		Metashape.app.update()
		
		# Shrani projekt
		doc.save()


def run_samplepoints():
	doc = Metashape.app.document
	chunk = doc.chunk
	# sample_int = 0.025
	sampling = Metashape.app.getBool("Start Point Sampling?")
	
	if sampling == True:
		chunk.dense_cloud.copy()
		# Sample points
		chunk.samplePoints(source_data=Metashape.ModelData, uniform_sampling=False)
		Metashape.app.messageBox("Sample Points process complete!")
		doc.save()
		Metashape.app.update()


def run_samplepointsuni():
	doc = Metashape.app.document
	chunk = doc.chunk
	sample_int = float(settings.defaulfPointSample)
	sampling = Metashape.app.getBool("Start Uniform Point Sampling?\nChoose (No) to change point spacing value.")
	
	if sampling == True:
		chunk.dense_cloud.copy()
		# Sample points
		chunk.samplePoints(source_data=Metashape.ModelData, uniform_sampling=True, points_spacing=sample_int)
		Metashape.app.messageBox("Sample Points process complete!")
		doc.save()
		Metashape.app.update()
	else:
		sample_int = Metashape.app.getFloat("New spacing (m):", sample_int)
		chunk.dense_cloud.copy()
		chunk.samplePoints(source_data=Metashape.ModelData, uniform_sampling=True, points_spacing=sample_int)
		Metashape.app.messageBox("Sample Points process complete!")
		doc.save()
		Metashape.app.update()	


def run_filterpoints():
	doc = Metashape.app.document
	chunk = doc.chunk
	filter_int = float(settings.defaultPointFilter)
	filtering = Metashape.app.getBool("Start process with default settings? To change values choose 'No'.\n\nMode: Uniform sampling\nDefault spacing: " + str(filter_int) + "m")
 	
	if filtering == True:
		chunk.dense_cloud.copy()
		# Sample points
		chunk.filterDenseCloud(point_spacing=filter_int)
		Metashape.app.messageBox("Filtering process complete!\n\nNew point spacing: " + filter_int + "m")
		doc.save()
		Metashape.app.update()
	else:
		filter_int = Metashape.app.getFloat("Enter point spacing (m):", filter_int)
		chunk.dense_cloud.copy()
		chunk.filterDenseCloud(point_spacing=filter_int)
		Metashape.app.messageBox("Filtering process complete!\n\nNew point spacing: " + filter_int + "m")
		doc.save()
		Metashape.app.update()


def find_files(folder, types):
    return [entry.path for entry in os.scandir(folder) if (entry.is_file() and os.path.splitext(entry.name)[1].lower() in types)]


def newchunk_kalota_auto():
	doc = Metashape.app.document
	netpath = Metashape.app.document.path
	netroot = path.dirname(netpath)
	image_folder = Metashape.app.getExistingDirectory("Select photos folder (KALOTA)", netroot)
	photos = find_files(image_folder, [".jpg", ".jpeg", ".JPG", ".JPEG"])
	chunk = doc.addChunk()
	chunk.addPhotos(photos)
	chunk_name = os.path.basename(image_folder)
	chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
	doc.chunk = chunk
	doc.save()
	Metashape.app.update()
	Metashape.app.messageBox("Loading images... press OK to continue.")
	cam_calibration()
	time.sleep(3)
	chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
	path_ref = Metashape.app.getOpenFileName("Import Target Coordinates", image_folder, "Text file (*.txt)")
	chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
	chunk.updateTransform()
	Metashape.app.update()
	doc.save()


def newchunk_stizk_auto():
	doc = Metashape.app.document
	netpath = Metashape.app.document.path
	# netroot = path.dirname(netpath)
	netroot = settings.projectsFolder
	image_folder = Metashape.app.getExistingDirectory("Select photos folder (STOPNICA - IZKOP)", netroot)
	photos = find_files(image_folder, [".jpg", ".jpeg", ".JPG", ".JPEG"])
	chunk = doc.addChunk()
	chunk.addPhotos(photos)
	chunk_name = os.path.basename(image_folder)
	chunk_name = "ST_IZ_" + chunk_name
	chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
	doc.chunk = chunk
	doc.save()
	Metashape.app.update()
	Metashape.app.messageBox("Loading images... press OK to continue.")
	cam_calibration()
	time.sleep(3)
	chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
	path_ref = Metashape.app.getOpenFileName("Import Target Coordinates", image_folder, "Text file (*.txt)")
	chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
	chunk.updateTransform()
	Metashape.app.update()
	doc.save()


def newchunk_stbbet_auto():
	doc = Metashape.app.document
	netpath = Metashape.app.document.path
	# netroot = path.dirname(netpath)
	netroot = settings.projectsFolder
	image_folder = Metashape.app.getExistingDirectory("Select photos folder (STOPNICA - B.BET.)", netroot)
	photos = find_files(image_folder, [".jpg", ".jpeg", ".JPG", ".JPEG"])
	chunk = doc.addChunk()
	chunk.addPhotos(photos)
	chunk_name = os.path.basename(image_folder)
	chunk_name = "ST_BB_" + chunk_name
	chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
	doc.chunk = chunk
	doc.save()
	Metashape.app.update()
	Metashape.app.messageBox("Loading images... press OK to continue.")
	cam_calibration()
	time.sleep(3)
	chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
	path_ref = Metashape.app.getOpenFileName("Import Target Coordinates", image_folder, "Text file (*.txt)")
	chunk.importReference(path_ref, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
	chunk.updateTransform()
	Metashape.app.update()
	doc.save()


def newchunk_kalota():
	doc = Metashape.app.document
	netpath = Metashape.app.document.path
	# netroot = path.dirname(netpath)
	netroot = settings.projectsFolder
	image_folder = Metashape.app.getExistingDirectory("Select photos folder (KALOTA)", netroot)
	photos = find_files(image_folder, [".jpg", ".jpeg", ".JPG", ".JPEG"])
	chunk = doc.addChunk()
	chunk.addPhotos(photos)
	chunk_name = os.path.basename(image_folder)
	chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
	doc.chunk = chunk
	doc.save()
	Metashape.app.messageBox("New chunk created!\n\nChunk Name = " + chunk_name)
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


def newchunk_stizk():
	doc = Metashape.app.document
	netpath = Metashape.app.document.path
	# netroot = path.dirname(netpath)
	netroot = settings.projectsFolder
	image_folder = Metashape.app.getExistingDirectory("Select photos folder (STOPNICA - IZKOP)", netroot)
	photos = find_files(image_folder, [".jpg", ".jpeg", ".JPG", ".JPEG"])
	chunk = doc.addChunk()
	chunk.addPhotos(photos)
	chunk_name = os.path.basename(image_folder)
	chunk_name = "ST_IZ_" + chunk_name
	chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
	doc.chunk = chunk
	doc.save()
	Metashape.app.messageBox("New chunk created!\n\nChunk Name = " + chunk_name)
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


def newchunk_stbbet():
	doc = Metashape.app.document
	netpath = Metashape.app.document.path
	# netroot = path.dirname(netpath)
	netroot = settings.projectsFolder
	image_folder = Metashape.app.getExistingDirectory("Select photos folder (STOPNICA - B.BET.)", netroot)
	photos = find_files(image_folder, [".jpg", ".jpeg", ".JPG", ".JPEG"])
	chunk = doc.addChunk()
	chunk.addPhotos(photos)
	chunk_name = os.path.basename(image_folder)
	chunk_name = "ST_BB_" + chunk_name
	chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
	doc.chunk = chunk
	doc.save()
	Metashape.app.messageBox("New chunk created!\n\nChunk Name = " + chunk_name)
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


def navodila_proces():
	Metashape.app.messageBox("Osnovni koraki postopka obdelave:\n\n1. Ustvari nov chunk - Menu: AtuoFTG -> Create Chunk\n*2. Nastavi kalibracijo kamere\n*3. Detekcija markerjev in uvoz tock\n\n4. Align Photos\n\n5. Preveri markerje\n6. Copy Region\n\n7. Build Dense Cloud\n\n8. Pocisti tocke na celu izkopa oz.\n   obrezi tocke na bokih stopnice.\n\n9. Build Mesh\n10. Sample Points\n11. Razrez dense cloud-a (izkop/b.bet.)\n12. Izvoz podatkov\n\nAvtor skripte: Boris Bilc / Verzija: " + app_ver)


def prazno():
	print("Prazna vrstica")


# Menu items
label0a = "< AutoFTG >/New Chunk (Auto) ->/Add Chunk: KALOTA | Drugo"
Metashape.app.addMenuItem(label0a, newchunk_kalota_auto)

label0b = "< AutoFTG >/New Chunk (Auto) ->/Add Chunk: STOPNICA - IZKOP"
Metashape.app.addMenuItem(label0b, newchunk_stizk_auto)

label0c = "< AutoFTG >/New Chunk (Auto) ->/Add Chunk: STOPNICA - B.BET."
Metashape.app.addMenuItem(label0c, newchunk_stbbet_auto)

label1a = "< AutoFTG >/New Chunk ->/Add Chunk: KALOTA | Drugo"
Metashape.app.addMenuItem(label1a, newchunk_kalota)

label1b = "< AutoFTG >/New Chunk ->/Add Chunk: STOPNICA - IZKOP"
Metashape.app.addMenuItem(label1b, newchunk_stizk)

label1c = "< AutoFTG >/New Chunk ->/Add Chunk: STOPNICA - B.BET."
Metashape.app.addMenuItem(label1c, newchunk_stbbet)

labelsep4 = "< AutoFTG >/--------------------"
Metashape.app.addMenuItem(labelsep4, prazno)

label2 = "< AutoFTG >/- Camera Calibration/(0) Initial: NULL (Frame)"
Metashape.app.addMenuItem(label2, cam_calibrationDefault)

label2a = "< AutoFTG >/- Camera Calibration/(1) Initial: NULL (Fisheye)"
Metashape.app.addMenuItem(label2a, cam_calibration0)

label2b = "< AutoFTG >/- Camera Calibration/(2) Camera 1: HH3 by dibit (Fisheye)"
Metashape.app.addMenuItem(label2b, cam_calibration1a)

label2c = "< AutoFTG >/- Camera Calibration/(3) Camera 2: HH3 by dibit (Fisheye)"
Metashape.app.addMenuItem(label2c, cam_calibration1b)

label2cc = "< AutoFTG >/- Camera Calibration/(4) Camera 3: HH3 by dibit (Fisheye)"
Metashape.app.addMenuItem(label2cc, cam_calibration1c)

label2d = "< AutoFTG >/- Camera Calibration/(5) DJI Phantom 4 Pro 2.0 (CELU)"
Metashape.app.addMenuItem(label2d, cam_calibration2)

label2e = "< AutoFTG >/- Camera Calibration/(6) DJI Phantom 4 Advanced (2B)"
Metashape.app.addMenuItem(label2e, cam_calibration3)

label2set = "< AutoFTG >/- Camera Calibration/Change default calibration..."
Metashape.app.addMenuItem(label2set, cam_calibrationSettings)

label3a = "< AutoFTG >/- Detect Markers + Import Points"
Metashape.app.addMenuItem(label3a, marker_targets)

labelsep2 = "< AutoFTG >/--------------------"
Metashape.app.addMenuItem(labelsep2, prazno)

label4 = "< AutoFTG >/Copy Region (Between Chunks)"
Metashape.app.addMenuItem(label4, copy_bbox)

labelsep1 = "< AutoFTG >/--------------------"
Metashape.app.addMenuItem(labelsep1, prazno)

label6 = "< AutoFTG >/Filter Points (Uniform - Region oriented)"
Metashape.app.addMenuItem(label6, run_filterpoints)

label6z = "< AutoFTG >/Change default filter spacing..."
Metashape.app.addMenuItem(label6z, def_pointfilter)

labelsep3 = "< AutoFTG >/--------------------"
Metashape.app.addMenuItem(labelsep3, prazno)

label5a = "< AutoFTG >/Sample Points (Surface Detail)"
Metashape.app.addMenuItem(label5a, run_samplepoints)

label5b = "< AutoFTG >/Sample Points (Uniform Spacing)"
Metashape.app.addMenuItem(label5b, run_samplepointsuni)

label5z = "< AutoFTG >/Change default sampling spacing..."
Metashape.app.addMenuItem(label5z, def_pointsample)

# labelhelp = "< AutoFTG >/( i ) Kratka navodila za FTG"
# Metashape.app.addMenuItem(labelhelp, navodila_proces)

