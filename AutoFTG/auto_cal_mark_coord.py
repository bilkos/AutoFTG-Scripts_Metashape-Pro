# AutoFTG - Scripts for Agisoft Metashape Pro
# Scripts for process automation
# This is an assembly of existing scripts from other users, and some additional 
# scripts written for use in work process at project 2TIR, tunnel T8-KP in Slovenia.
# 
# Author: Boriws Bilc
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

# Checking compatibility
compatible_major_version = "1.8"
found_major_version = ".".join(Metashape.app.version.split('.')[:2])
if found_major_version != compatible_major_version:
	raise Exception("Incompatible Metashape version: {} != {}".format(found_major_version, compatible_major_version))


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
		self.btnOk.setFixedSize(200, 36)
		self.btnOk.setToolTip("Copy bounding box to all selected chunks")

		self.btnQuit = QtWidgets.QPushButton("Close")
		self.btnQuit.setFixedSize(80, 36)

		layout = QtWidgets.QGridLayout()  # creating layout
		layout.setColumnMinimumWidth(0, 80) # minimum column width
		layout.setColumnMinimumWidth(1, 200) # minimum column width
		layout.addWidget(self.labelFrom, 0, 0)
		layout.addWidget(self.fromChunk, 0, 1)

		layout.addWidget(self.labelTo, 1, 0)
		layout.addWidget(self.toChunks, 1, 1)

		layout.addWidget(self.btnQuit, 3, 0)
		layout.addWidget(self.btnOk, 3, 1)

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


# Nalozi kalibracijo kamere / Nulta / Tip: Fisheye
def cam_calibration0():
	doc = Metashape.app.document
	chunk = doc.chunk
	
	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Fisheye
#	my_calib = Metashape.Calibration()
#	my_calib.load(path="\\\\Stroj\\1_ftg_t8-kp\\100_T8-KP_OBDELAVA\\dibit-kamera_HH3_031_Fisheye.xml", format=Metashape.CalibrationFormatXML)
#	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Camera Calibration settings changed.\n\nCamera: none\nType: Fisheye\nFile: ---")
	Metashape.app.update()


# Nalozi kalibracijo kamere / HH3_031 by dibit / Tip: Fisheye
def cam_calibration1():
	doc = Metashape.app.document
	chunk = doc.chunk	

	my_sensor = chunk.sensors[0]
	my_sensor.type = Metashape.Sensor.Type.Fisheye
	my_calib = Metashape.Calibration()
	my_calib.load(path="\\\\Stroj\\1_ftg_t8-kp\\100_T8-KP_OBDELAVA\\dibit-kamera_HH3_031_Fisheye.xml", format=Metashape.CalibrationFormatXML)
	my_sensor.user_calib = my_calib
	doc.save()
	Metashape.app.messageBox("Camera Calibration imported.\n\nCamera: HH3_031 by dibit\nType: Fisheye\nFile: dibit-kamera_HH3_031_Fisheye.xml")
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
	sample_int = 0.10
	sampling = Metashape.app.getBool("Start with default settings?\nTo change values choose 'No'.\n\nMode: Uniform sampling\nDefault spacing: 0.05m\n\n*Default Dense Cloud will be replaced!")
	
	if sampling == True:
		# Sample points
		chunk.samplePoints(source_data=Metashape.ModelData, uniform_sampling=True, points_spacing=sample_int)
		Metashape.app.messageBox("Sample Points process complete!\n\nNew point spacing: " + sample_int + "m")
		doc.save()
		Metashape.app.update()
	else:
		sample_int = Metashape.app.getFloat("Enter point spacing (m):", sample_int)
		chunk.samplePoints(source_data=Metashape.ModelData, uniform_sampling=True, points_spacing=sample_int)
		Metashape.app.messageBox("Sample Points process complete!\n\nNew point spacing: " + sample_int + "m")
		doc.save()
		Metashape.app.update()	


def find_files(folder, types):
    return [entry.path for entry in os.scandir(folder) if (entry.is_file() and os.path.splitext(entry.name)[1].lower() in types)]


def newchunk_kalota():
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
	Metashape.app.messageBox("New chunk created!\n\nChunk Name = " + chunk_name)
	addcalib = Metashape.app.getBool("Import camera calibration?\n\nCamera: HH3_031 by dibit")
	if addcalib == True:
		cam_calibration1()
		marker_targets()


def newchunk_stizk():
	doc = Metashape.app.document
	netpath = Metashape.app.document.path
	netroot = path.dirname(netpath)
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
	addcalib = Metashape.app.getBool("Import camera calibration?\n\nCamera: HH3_031 by dibit")
	if addcalib == True:
		cam_calibration1()
	startmarkerdet =  Metashape.app.getBool("Continue with marker detection?")
	if startmarkerdet == True:
		marker_targets()

def newchunk_stbbet():
	doc = Metashape.app.document
	netpath = Metashape.app.document.path
	netroot = path.dirname(netpath)
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
	addcalib = Metashape.app.getBool("Import camera calibration?\n\nCamera: HH3_031 by dibit")
	if addcalib == True:
		cam_calibration1()
	startmarkerdet =  Metashape.app.getBool("Continue with marker detection?")
	if startmarkerdet == True:
		marker_targets()

def navodila_proces():
	Metashape.app.messageBox("Osnovni koraki postopka obdelave:\n\n1. Ustvari nov chunk - Menu: AtuoFTG -> Create Chunk\n*2. Nastavi kalibracijo kamere\n*3. Detekcija markerjev in uvoz tock\n\n4. Align Photos\n\n5. Preveri markerje\n6. Copy Region\n\n7. Build Dense Cloud\n\n8. Pocisti tocke na celu izkopa oz.\n   obrezi tocke na bokih stopnice.\n\n9. Build Mesh\n10. Sample Points\n11. Razrez dense cloud-a (izkop/b.bet.)\n12. Izvoz podatkov\n\nAvtor skripte: Boris Bilc")


def prazno():
	print("Prazna vrstica")


# Menu items
label1a = "< AutoFTG >/Create Chunk/> KALOTA | Drugo"
Metashape.app.addMenuItem(label1a, newchunk_kalota)

label1b = "< AutoFTG >/Create Chunk/> STOPNICA - IZKOP"
Metashape.app.addMenuItem(label1b, newchunk_stizk)

label1c = "< AutoFTG >/Create Chunk/> STOPNICA - B.BET."
Metashape.app.addMenuItem(label1c, newchunk_stbbet)

label2a = "< AutoFTG >/- Camera Calibration/(Default) HH3_031 by dibit > T8-KP"
Metashape.app.addMenuItem(label2a, cam_calibration1)

label2b = "< AutoFTG >/- Camera Calibration/NULL Cal. - Fisheye"
Metashape.app.addMenuItem(label2b, cam_calibration0)

label2c = "< AutoFTG >/- Camera Calibration/DJI Phantom 4 Pro 2.0 (CELU)"
Metashape.app.addMenuItem(label2c, cam_calibration2)

label2d = "< AutoFTG >/- Camera Calibration/DJI Phantom 4 Advanced (2B)"
Metashape.app.addMenuItem(label2d, cam_calibration3)

label3a = "< AutoFTG >/- Detect Markers + Import Points"
Metashape.app.addMenuItem(label3a, marker_targets)

labelsep2 = "< AutoFTG >/----------"
Metashape.app.addMenuItem(labelsep2, prazno)

label4 = "< AutoFTG >/Copy Region (Between Chunks)"
Metashape.app.addMenuItem(label4, copy_bbox)

labelsep1 = "< AutoFTG >/----------"
Metashape.app.addMenuItem(labelsep1, prazno)

label5 = "< AutoFTG >/Sample Points (Uniform)"
Metashape.app.addMenuItem(label5, run_samplepoints)

labelsep3 = "< AutoFTG >/--------------------"
Metashape.app.addMenuItem(labelsep3, prazno)

labelhelp = "< AutoFTG >/( i ) Kratka navodila za FTG"
Metashape.app.addMenuItem(labelhelp, navodila_proces)

