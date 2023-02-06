# Class for Copy Region UI
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
from AutoFTG.autoftg_settingschunk import *
from AutoFTG.autoftg_settingsmain import *
from AutoFTG.qtresources import *


class CopyBoundingBoxDlg(QtWidgets.QDialog):

	def __init__(self, parent):

		QtWidgets.QDialog.__init__(self, parent)
		self.setWindowTitle("Copy Region (Bounding Box)")
		appIcon = QIcon()
		appIcon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(appIcon)

		self.labelFrom = QtWidgets.QLabel("From")
		self.labelTo = QtWidgets.QLabel("To")

		self.fromChunk = QtWidgets.QComboBox()
		for chunk in Metashape.app.document.chunks:
			self.fromChunk.addItem(chunk.label)

		self.toChunks = QtWidgets.QListWidget()
		self.toChunks.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
		for chunk in Metashape.app.document.chunks:
			self.toChunks.addItem(chunk.label)

		self.btnOk = QtWidgets.QPushButton("Copy")
		self.btnOk.setFixedSize(120, 36)
		self.btnOk.setToolTip("Copy region from one chunk to multiple chunks.:")

		self.btnQuit = QtWidgets.QPushButton("Cancel")
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
		

