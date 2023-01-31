import os
import shutil
import sys
import time
import subprocess
import csv
from configparser import ConfigParser
from datetime import datetime
from os import path

#import Metashape
import Metashape
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import AutoFTG.autoftg_main as autoftg_main
from AutoFTG.autoftg_batch_setmesh import *

from AutoFTG.qtresources import *

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

chunkSet = ""
logArchive = []

class Ui_DialogBatchChunk(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.sel_items = []
		self.itemDef = autoftg_main.projCfg.get("PROJECT SETTINGS", "default_chunk_def")
		self.itemDefFolder = autoftg_main.menuCfg.get(self.itemDef, "work_folder")
		self.itemDefFolderName = self.itemDefFolder.split(os.sep)[-1]
		self.setObjectName(u"DialogBatchChunk")
		self.resize(900, 830)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)
		self.setMinimumSize(QSize(900, 800))
		self.setMaximumSize(QSize(900, 800))
		self.setWindowTitle(u"Batch Chunk Creator")
		appIcon = QIcon()
		appIcon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(appIcon)
		self.verticalLayoutWidget = QWidget(self)

		self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
		self.verticalLayoutWidget.setGeometry(QRect(0, 0, 901, 805))
		self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setSpacing(6)
		self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_2.setObjectName(u"verticalLayout_2")
		self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
		self.verticalLayout_2.setContentsMargins(10, 0, 10, 10)
		self.horizontalLayout_9 = QHBoxLayout()
		self.horizontalLayout_9.setSpacing(5)
		self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
		self.horizontalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
		self.label_15 = QLabel(self.verticalLayoutWidget)
		self.label_15.setObjectName(u"label_15")
		sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
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
		sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
		sizePolicy1.setHorizontalStretch(0)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
		self.label_3.setSizePolicy(sizePolicy1)
		self.label_3.setMaximumSize(QSize(16777215, 30))
		font1 = QFont()
		font1.setFamily(u"Segoe UI")
		font1.setPointSize(16)
		font1.setBold(False)
		font1.setItalic(False)
		font1.setUnderline(False)
		font1.setWeight(50)
		self.label_3.setFont(font1)
		self.label_3.setText(u"Batch Chunk Creator")

		self.horizontalLayout_9.addWidget(self.label_3)


		self.verticalLayout_2.addLayout(self.horizontalLayout_9)

		self.line_4 = QFrame(self.verticalLayoutWidget)
		self.line_4.setObjectName(u"line_4")
		sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
		sizePolicy2.setHorizontalStretch(0)
		sizePolicy2.setVerticalStretch(0)
		sizePolicy2.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
		self.line_4.setSizePolicy(sizePolicy2)
		self.line_4.setMaximumSize(QSize(16777215, 10))
		self.line_4.setFrameShadow(QFrame.Plain)
		self.line_4.setFrameShape(QFrame.HLine)

		self.verticalLayout_2.addWidget(self.line_4)

		self.gridLayout = QGridLayout()
		self.gridLayout.setSpacing(5)
		self.gridLayout.setObjectName(u"gridLayout")
		self.treeWidget = QTreeWidget(self.verticalLayoutWidget)
		font2 = QFont()
		font2.setBold(True)
		font2.setWeight(75)
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons8-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.treeWidget.headerItem().setText(1, "")
		icon2 = QIcon()
		icon2.addFile(u":/icons/icons8-map-pin-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.treeWidget.headerItem().setText(2, "")
		icon3 = QIcon()
		icon3.addFile(u":/icons/icons8-sd-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.treeWidget.headerItem().setText(3, "")
		icon4 = QIcon()
		icon4.addFile(u":/icons/icons8-bursts-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.treeWidget.headerItem().setText(4, "")
		icon5 = QIcon()
		icon5.addFile(u":/icons/icons8-mesh-48.png", QSize(), QIcon.Normal, QIcon.Off)
		self.treeWidget.headerItem().setText(5, "")
		icon6 = QIcon()
		icon6.addFile(u":/icons/icons8-cloud-development-48.png", QSize(), QIcon.Normal, QIcon.Off)
		self.treeWidget.headerItem().setText(6, "")
		__qtreewidgetitem = QTreeWidgetItem()
		__qtreewidgetitem.setIcon(6, icon6);
		__qtreewidgetitem.setIcon(5, icon5);
		__qtreewidgetitem.setIcon(4, icon4);
		__qtreewidgetitem.setTextAlignment(3, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem.setIcon(3, icon3);
		__qtreewidgetitem.setTextAlignment(2, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem.setIcon(2, icon2);
		__qtreewidgetitem.setTextAlignment(1, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem.setIcon(1, icon1);
		__qtreewidgetitem.setText(0, u"Folders");
		__qtreewidgetitem.setTextAlignment(0, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem.setFont(0, font2);
#if QT_CONFIG(tooltip)
		__qtreewidgetitem.setToolTip(6, u"Point Cloud");
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
		__qtreewidgetitem.setToolTip(5, u"Mesh Model");
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
		__qtreewidgetitem.setToolTip(4, u"Aligned");
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
		__qtreewidgetitem.setToolTip(3, u"Import");
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
		__qtreewidgetitem.setToolTip(2, u"Points");
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
		__qtreewidgetitem.setToolTip(1, u"Images");
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
		__qtreewidgetitem.setToolTip(0, u"Folders");
#endif // QT_CONFIG(tooltip)
		self.treeWidget.setHeaderItem(__qtreewidgetitem)
		icon7 = QIcon()
		icon7.addFile(u":/icons/icons8-folder-tree-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon8 = QIcon()
		icon8.addFile(u":/icons/icons8-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon9 = QIcon()
		icon9.addFile(u":/icons/icons8-add-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon10 = QIcon()
		icon10.addFile(u":/icons/icons8-location-off-48.png", QSize(), QIcon.Normal, QIcon.Off)
		icon11 = QIcon()
		icon11.addFile(u":/icons/icons8-done-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon12 = QIcon()
		icon12.addFile(u":/icons/icons8-no-camera-96.png", QSize(), QIcon.Normal, QIcon.Off)
		icon13 = QIcon()
		icon13.addFile(u":/icons/icons8-error-48.png", QSize(), QIcon.Normal, QIcon.Off)
		font3 = QFont()
		font3.setFamily(u"Segoe UI")
		icon14 = QIcon()
		icon14.addFile(u":/icons/icons8-check-file-50.png", QSize(), QIcon.Normal, QIcon.Off)
		brush = QBrush(QColor(255, 254, 222, 255))
		brush.setStyle(Qt.SolidPattern)
		icon15 = QIcon()
		icon15.addFile(u":/icons/icons8-my-location-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon16 = QIcon()
		icon16.addFile(u":/icons/icons8-microsoft-todo-2019-48.png", QSize(), QIcon.Normal, QIcon.Off)
		
		self.treeWidget.setObjectName(u"treeWidget")
		sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
		sizePolicy3.setHorizontalStretch(0)
		sizePolicy3.setVerticalStretch(0)
		sizePolicy3.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
		self.treeWidget.setSizePolicy(sizePolicy3)
		self.treeWidget.setMinimumSize(QSize(580, 600))
		self.treeWidget.setMaximumSize(QSize(16777215, 640))
		self.treeWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		self.treeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		self.treeWidget.setAutoScrollMargin(20)
		self.treeWidget.setTabKeyNavigation(True)
		self.treeWidget.setProperty("showDropIndicator", False)
		self.treeWidget.setAlternatingRowColors(True)
		self.treeWidget.setSelectionMode(QAbstractItemView.MultiSelection)
		self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.treeWidget.setIconSize(QSize(20, 20))
		self.treeWidget.setUniformRowHeights(True)
		self.treeWidget.setSortingEnabled(True)
		self.treeWidget.setAllColumnsShowFocus(True)
		self.treeWidget.header().setVisible(True)
		self.treeWidget.header().setDefaultSectionSize(39)
		self.treeWidget.header().setStretchLastSection(True)

		self.gridLayout.addWidget(self.treeWidget, 2, 0, 1, 1)

		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setSpacing(5)
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
		self.label_2 = QLabel(self.verticalLayoutWidget)
		self.label_2.setObjectName(u"label_2")
		sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		sizePolicy4.setHorizontalStretch(0)
		sizePolicy4.setVerticalStretch(0)
		sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
		self.label_2.setSizePolicy(sizePolicy4)
		self.label_2.setMinimumSize(QSize(0, 24))
		self.label_2.setMaximumSize(QSize(16777215, 24))
		font4 = QFont()
		font4.setFamily(u"Segoe UI")
		font4.setPointSize(12)
		font4.setBold(True)
		font4.setWeight(75)
		self.label_2.setFont(font4)
		self.label_2.setText(u"Data Folders")
		self.label_2.setIndent(5)

		self.horizontalLayout_2.addWidget(self.label_2)

		self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_4.setObjectName(u"checkBox_4")
		sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
		sizePolicy5.setHorizontalStretch(0)
		sizePolicy5.setVerticalStretch(0)
		sizePolicy5.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
		self.checkBox_4.setSizePolicy(sizePolicy5)
		self.checkBox_4.setMinimumSize(QSize(0, 24))
		self.checkBox_4.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.checkBox_4.setStatusTip(u"Disable to set custom location for data. Enable to use project default data location settings.")
#endif // QT_CONFIG(statustip)
		self.checkBox_4.setText(u"Use Project Data Location")
		icon17 = QIcon()
		icon17.addFile(u":/icons/icons8-copy-to-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_4.setIcon(icon17)
		self.checkBox_4.setIconSize(QSize(20, 20))
		self.checkBox_4.setChecked(True)

		self.horizontalLayout_2.addWidget(self.checkBox_4)


		self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

		self.horizontalLayout_4 = QHBoxLayout()
		self.horizontalLayout_4.setSpacing(5)
		self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
		self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_3.setObjectName(u"pushButton_3")
		self.pushButton_3.setEnabled(False)
		sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy6.setHorizontalStretch(0)
		sizePolicy6.setVerticalStretch(0)
		sizePolicy6.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
		self.pushButton_3.setSizePolicy(sizePolicy6)
		self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.pushButton_3.setToolTip(u"Press [Ctrl+P] to start processing")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
		self.pushButton_3.setStatusTip(u"Process selected folders, and create new chunks...")
#endif // QT_CONFIG(statustip)
		self.pushButton_3.setText(u"Ready")
		icon18 = QIcon()
		icon18.addFile(u":/icons/icons8-submit-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
		icon18.addFile(u":/icons/icons8-ok-50.png", QSize(), QIcon.Disabled, QIcon.Off)
		self.pushButton_3.setIcon(icon18)
		self.pushButton_3.setIconSize(QSize(24, 24))
#if QT_CONFIG(shortcut)
		self.pushButton_3.setShortcut(u"P")
#endif // QT_CONFIG(shortcut)
		self.pushButton_3.setChecked(False)

		self.horizontalLayout_4.addWidget(self.pushButton_3)

		self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_2.setObjectName(u"pushButton_2")
		sizePolicy5.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
		self.pushButton_2.setSizePolicy(sizePolicy5)
		self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.pushButton_2.setStatusTip(u"Exit chunk creator...")
#endif // QT_CONFIG(statustip)
		self.pushButton_2.setText(u"Close")
		icon19 = QIcon()
		icon19.addFile(u":/icons/icons8-close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_2.setIcon(icon19)
		self.pushButton_2.setIconSize(QSize(24, 24))
#if QT_CONFIG(shortcut)
		self.pushButton_2.setShortcut(u"X")
#endif // QT_CONFIG(shortcut)

		self.horizontalLayout_4.addWidget(self.pushButton_2)


		self.gridLayout.addLayout(self.horizontalLayout_4, 4, 2, 1, 1)

		self.horizontalLayout_17 = QHBoxLayout()
		self.horizontalLayout_17.setSpacing(5)
		self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
		self.label_8 = QLabel(self.verticalLayoutWidget)
		self.label_8.setObjectName(u"label_8")
		sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
		sizePolicy7.setHorizontalStretch(0)
		sizePolicy7.setVerticalStretch(0)
		sizePolicy7.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
		self.label_8.setSizePolicy(sizePolicy7)
		self.label_8.setMaximumSize(QSize(16777215, 20))
		font5 = QFont()
		font5.setFamily(u"Segoe UI")
		font5.setPointSize(10)
		font5.setBold(False)
		font5.setWeight(50)
		self.label_8.setFont(font5)
		self.label_8.setFrameShape(QFrame.NoFrame)
		self.label_8.setText(u"<html><head/><body><p><span style=\" font-weight:600;\">Ready... </span>Select folder(s) to process.</p></body></html>")
		self.label_8.setIndent(10)

		self.horizontalLayout_17.addWidget(self.label_8)

		self.pushButton_10 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_10.setObjectName(u"pushButton_10")
		self.pushButton_10.setEnabled(False)
#if QT_CONFIG(tooltip)
		self.pushButton_10.setToolTip(u"Open selected item in File Explorer")
#endif // QT_CONFIG(tooltip)
		self.pushButton_10.setText(u"")
		icon20 = QIcon()
		icon20.addFile(u":/icons/icons8-file-explorer-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_10.setIcon(icon20)
		self.pushButton_10.setIconSize(QSize(20, 20))
		self.pushButton_10.setAutoDefault(False)
		self.pushButton_10.setFlat(False)

		self.horizontalLayout_17.addWidget(self.pushButton_10)


		self.gridLayout.addLayout(self.horizontalLayout_17, 3, 0, 1, 1)

		self.line = QFrame(self.verticalLayoutWidget)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.VLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.gridLayout.addWidget(self.line, 0, 1, 5, 1)

		self.progressBar = QProgressBar(self.verticalLayoutWidget)
		self.progressBar.setObjectName(u"progressBar")
		self.progressBar.setEnabled(False)
		sizePolicy4.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
		self.progressBar.setSizePolicy(sizePolicy4)
		self.progressBar.setMinimum(0)
		self.progressBar.setMaximum(10)
		self.progressBar.setValue(0)
		self.progressBar.setTextVisible(False)
		self.progressBar.setOrientation(Qt.Horizontal)
		self.progressBar.setTextDirection(QProgressBar.TopToBottom)
		self.progressBar.setFormat(u"%p%")

		self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 1)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setSpacing(5)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.lineEdit = QLineEdit(self.verticalLayoutWidget)
		self.lineEdit.setObjectName(u"lineEdit")
		self.lineEdit.setEnabled(False)
		sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
		self.lineEdit.setSizePolicy(sizePolicy4)
		self.lineEdit.setMaximumSize(QSize(16777215, 24))
		font6 = QFont()
		font6.setFamily(u"Segoe UI")
		font6.setPointSize(10)
		self.lineEdit.setFont(font6)
#if QT_CONFIG(statustip)
		self.lineEdit.setStatusTip(u"Path to main folder with data sub-folders...")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
		self.lineEdit.setWhatsThis(u"Path to main folder with data sub-folders...")
#endif // QT_CONFIG(whatsthis)
		self.lineEdit.setPlaceholderText(u"Data location...")

		self.horizontalLayout.addWidget(self.lineEdit)

		self.pushButton = QPushButton(self.verticalLayoutWidget)
		self.pushButton.setObjectName(u"pushButton")
		self.pushButton.setEnabled(False)
		sizePolicy5.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
		self.pushButton.setSizePolicy(sizePolicy5)
		self.pushButton.setMinimumSize(QSize(0, 30))
		self.pushButton.setMaximumSize(QSize(16777215, 30))
		self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.pushButton.setStatusTip(u"Data location (root folder with sub-folders containing data)")
#endif // QT_CONFIG(statustip)
		self.pushButton.setText(u"Browse")
		icon21 = QIcon()
		icon21.addFile(u":/icons/icons8-browse-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton.setIcon(icon21)
		self.pushButton.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton)

		self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_4.setObjectName(u"pushButton_4")
		sizePolicy5.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
		self.pushButton_4.setSizePolicy(sizePolicy5)
		self.pushButton_4.setMinimumSize(QSize(0, 30))
		self.pushButton_4.setMaximumSize(QSize(16777215, 30))
		self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_4.setText(u"Refresh")
		icon22 = QIcon()
		icon22.addFile(u":/icons/icons8-available-updates-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_4.setIcon(icon22)
		self.pushButton_4.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton_4)


		self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

		self.gridLayout_3 = QGridLayout()
		self.gridLayout_3.setSpacing(5)
		self.gridLayout_3.setObjectName(u"gridLayout_3")
		self.horizontalLayout_5 = QHBoxLayout()
		self.horizontalLayout_5.setSpacing(5)
		self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
		self.label_11 = QLabel(self.verticalLayoutWidget)
		self.label_11.setObjectName(u"label_11")
		font7 = QFont()
		font7.setFamily(u"Segoe UI")
		font7.setPointSize(9)
		font7.setBold(False)
		font7.setWeight(50)
		self.label_11.setFont(font7)
		self.label_11.setText(u"Prefix:")
		self.label_11.setIndent(10)

		self.horizontalLayout_5.addWidget(self.label_11)

		self.label_6 = QLabel(self.verticalLayoutWidget)
		self.label_6.setObjectName(u"label_6")
		sizePolicy7.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
		self.label_6.setSizePolicy(sizePolicy7)
		self.label_6.setMinimumSize(QSize(0, 20))
		self.label_6.setMaximumSize(QSize(16777215, 20))
		font8 = QFont()
		font8.setFamily(u"Segoe UI")
		font8.setPointSize(8)
		self.label_6.setFont(font8)
		self.label_6.setFrameShape(QFrame.NoFrame)
		self.label_6.setText(u"")

		self.horizontalLayout_5.addWidget(self.label_6)


		self.gridLayout_3.addLayout(self.horizontalLayout_5, 9, 0, 1, 1)

		self.checkBox = QCheckBox(self.verticalLayoutWidget)
		self.checkBox.setObjectName(u"checkBox")
		sizePolicy1.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
		self.checkBox.setSizePolicy(sizePolicy1)
		self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Marker coordinates will be imported after target detection. <span style=\" font-weight:600;\">*</span></p><p><span style=\" font-weight:600;\">Disabled:</span> Coordinates are not imported. User must manually import coordinates.</p><p><span style=\" font-weight:600;\">*</span> Automatic importing of marker coordinates only works if point file name is the same as it's parent folder name, and contains a header with metadata. Point coordinates should start at row #7.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox.setText(u"Import Marker Coordinates")
		icon23 = QIcon()
		icon23.addFile(u":/icons/icons8-map-marker-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox.setIcon(icon23)
		self.checkBox.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox, 21, 0, 1, 1)

		self.horizontalLayout_12 = QHBoxLayout()
		self.horizontalLayout_12.setSpacing(5)
		self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
		self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
		icon24 = QIcon()
		icon24.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon25 = QIcon()
		icon25.addFile(u":/icons/icons8-video-wall-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon26 = QIcon()
		icon26.addFile(u":/icons/icons8-live-photos-96.png", QSize(), QIcon.Normal, QIcon.Off)
		icon27 = QIcon()
		icon27.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon28 = QIcon()
		icon28.addFile(u":/icons/icons8-video-stabilization-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon29 = QIcon()
		icon29.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		cicon = QIcon()
		cicon.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
		cicon1 = QIcon()
		cicon1.addFile(u":/icons/icons8-panorama-50.png", QSize(), QIcon.Normal, QIcon.Off)
		cicon2 = QIcon()
		cicon2.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
		cicon3 = QIcon()
		cicon3.addFile(u":/icons/icons8-video-stabilization-50.png", QSize(), QIcon.Normal, QIcon.Off)
		cicon4 = QIcon()
		cicon4.addFile(u":/icons/icons8-touchscreen-48.png", QSize(), QIcon.Normal, QIcon.Off)
		cicon5 = QIcon()
		cicon5.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		cicon5a = QIcon()
		cicon5a.addFile(u":/icons/icons8-ios-application-placeholder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		cicoTripod = QIcon()
		cicoTripod.addFile(u":/icons/icons8-camera-on-tripod-96.png", QSize(), QIcon.Normal, QIcon.Off)
		for cam in autoftg_main.cam_list:
			icon_type = autoftg_main.camCfg.get(cam, "Type")
			icon_subtype = autoftg_main.camCfg.get(cam, "SubType")
			if icon_subtype == "SmartPhone":
				self.comboBox_2.addItem(cicon4, cam)
			elif icon_subtype == "Drone":
				self.comboBox_2.addItem(cicon5, cam)
			elif icon_subtype == "Special":
				self.comboBox_2.addItem(cicoTripod, cam)
			else:
				if icon_type == "Fisheye":
					self.comboBox_2.addItem(cicon1, cam)
				elif icon_type == "Spherical":
					self.comboBox_2.addItem(cicon3, cam)
				elif icon_type == "Cylindrical":
					self.comboBox_2.addItem(cicon2, cam)
				elif icon_type == "RPC":
					self.comboBox_2.addItem(cicon5a, cam)
				else:
					self.comboBox_2.addItem(cicon, cam)
		
		self.comboBox_2.setCurrentText(autoftg_main.selected_camera)
		self.comboBox_2.setObjectName(u"comboBox_2")
		sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
		sizePolicy8.setHorizontalStretch(0)
		sizePolicy8.setVerticalStretch(0)
		sizePolicy8.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
		self.comboBox_2.setSizePolicy(sizePolicy8)
		self.comboBox_2.setMinimumSize(QSize(200, 0))
		self.comboBox_2.setFont(font6)
		self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.comboBox_2.setStatusTip(u"Choose camera settings to be applied when creating new chunk...")
#endif // QT_CONFIG(statustip)
		self.comboBox_2.setIconSize(QSize(20, 20))

		self.horizontalLayout_12.addWidget(self.comboBox_2)

		self.btnDefCam = QPushButton(self.verticalLayoutWidget)
		self.btnDefCam.setObjectName(u"btnDefCam")
		self.btnDefCam.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.btnDefCam.setToolTip(u"Set as default")
#endif // QT_CONFIG(tooltip)
		self.btnDefCam.setText(u"")
		icon30 = QIcon()
		icon30.addFile(u":/icons/icons8-christmas-star-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.btnDefCam.setIcon(icon30)
		self.btnDefCam.setIconSize(QSize(20, 20))
		self.btnDefCam.setAutoDefault(False)
		self.btnDefCam.setFlat(False)

		self.horizontalLayout_12.addWidget(self.btnDefCam)


		self.gridLayout_3.addLayout(self.horizontalLayout_12, 3, 0, 1, 1)

		self.line_2 = QFrame(self.verticalLayoutWidget)
		self.line_2.setObjectName(u"line_2")
		self.line_2.setFrameShadow(QFrame.Plain)
		self.line_2.setFrameShape(QFrame.HLine)

		self.gridLayout_3.addWidget(self.line_2, 22, 0, 1, 1)

		self.horizontalLayout_13 = QHBoxLayout()
		self.horizontalLayout_13.setSpacing(5)
		self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
		self.checkBox_mesh = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_mesh.setObjectName(u"checkBox_mesh")
		self.checkBox_mesh.setEnabled(True)
		sizePolicy6.setHeightForWidth(self.checkBox_mesh.sizePolicy().hasHeightForWidth())
		self.checkBox_mesh.setSizePolicy(sizePolicy6)
		self.checkBox_mesh.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_mesh.setToolTip(u"<html><head/><body><p>Enable to run 'Build Mesh/Build Textures' processing for selected items.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_mesh.setText(u"Build Mesh && Textures")
		icon31 = QIcon()
		icon31.addFile(u":/icons/icons8-national-park-48.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_mesh.setIcon(icon31)
		self.checkBox_mesh.setCheckable(True)
		self.checkBox_mesh.setChecked(False)
		self.checkBox_mesh.setTristate(False)

		self.horizontalLayout_13.addWidget(self.checkBox_mesh)

		self.pushButton_setMesh = QPushButton(self.verticalLayoutWidget)
		self.pushButton_setMesh.setObjectName(u"pushButton_setMesh")
		self.pushButton_setMesh.setEnabled(False)
		sizePolicy5.setHeightForWidth(self.pushButton_setMesh.sizePolicy().hasHeightForWidth())
		self.pushButton_setMesh.setSizePolicy(sizePolicy5)
		self.pushButton_setMesh.setCursor(QCursor(Qt.PointingHandCursor))
		icon32 = QIcon()
		icon32.addFile(u":/icons/icons8-adjust-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_setMesh.setIcon(icon32)
		self.pushButton_setMesh.setFlat(True)

		self.horizontalLayout_13.addWidget(self.pushButton_setMesh)


		self.gridLayout_3.addLayout(self.horizontalLayout_13, 27, 0, 1, 1)

		self.horizontalLayout_16 = QHBoxLayout()
		self.horizontalLayout_16.setSpacing(5)
		self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
		self.checkBox_pcloud = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_pcloud.setObjectName(u"checkBox_pcloud")
		self.checkBox_pcloud.setEnabled(True)
		sizePolicy6.setHeightForWidth(self.checkBox_pcloud.sizePolicy().hasHeightForWidth())
		self.checkBox_pcloud.setSizePolicy(sizePolicy6)
		self.checkBox_pcloud.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_pcloud.setToolTip(u"<html><head/><body><p>Enable to run 'Build Point Cloud' processing for selected items.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_pcloud.setText(u"Build Point Cloud")
		self.checkBox_pcloud.setIcon(icon26)
		self.checkBox_pcloud.setCheckable(True)
		self.checkBox_pcloud.setChecked(False)
		self.checkBox_pcloud.setTristate(False)

		self.horizontalLayout_16.addWidget(self.checkBox_pcloud)

		self.pushButton_setPCloud = QPushButton(self.verticalLayoutWidget)
		self.pushButton_setPCloud.setObjectName(u"pushButton_setPCloud")
		self.pushButton_setPCloud.setEnabled(False)
		sizePolicy5.setHeightForWidth(self.pushButton_setPCloud.sizePolicy().hasHeightForWidth())
		self.pushButton_setPCloud.setSizePolicy(sizePolicy5)
		self.pushButton_setPCloud.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_setPCloud.setIcon(icon32)
		self.pushButton_setPCloud.setFlat(True)

		self.horizontalLayout_16.addWidget(self.pushButton_setPCloud)


		self.gridLayout_3.addLayout(self.horizontalLayout_16, 29, 0, 1, 1)

		self.horizontalLayout_15 = QHBoxLayout()
		self.horizontalLayout_15.setSpacing(5)
		self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
		self.checkBox_export = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_export.setObjectName(u"checkBox_export")
		self.checkBox_export.setEnabled(True)
		sizePolicy6.setHeightForWidth(self.checkBox_export.sizePolicy().hasHeightForWidth())
		self.checkBox_export.setSizePolicy(sizePolicy6)
		self.checkBox_export.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_export.setToolTip(u"<html><head/><body><p>Enable to export data for selected items after build is complete.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_export.setText(u"Data Export")
		icon33 = QIcon()
		icon33.addFile(u":/icons/icons8-share-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_export.setIcon(icon33)
		self.checkBox_export.setCheckable(True)
		self.checkBox_export.setChecked(False)
		self.checkBox_export.setTristate(False)

		self.horizontalLayout_15.addWidget(self.checkBox_export)

		self.pushButton_setExport = QPushButton(self.verticalLayoutWidget)
		self.pushButton_setExport.setObjectName(u"pushButton_setExport")
		self.pushButton_setExport.setEnabled(False)
		sizePolicy5.setHeightForWidth(self.pushButton_setExport.sizePolicy().hasHeightForWidth())
		self.pushButton_setExport.setSizePolicy(sizePolicy5)
		self.pushButton_setExport.setCursor(QCursor(Qt.PointingHandCursor))
		icon34 = QIcon()
		icon34.addFile(u":/icons/icons8-true-false-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_setExport.setIcon(icon34)
		self.pushButton_setExport.setFlat(True)

		self.horizontalLayout_15.addWidget(self.pushButton_setExport)


		self.gridLayout_3.addLayout(self.horizontalLayout_15, 31, 0, 1, 1)

		self.horizontalLayout_8 = QHBoxLayout()
		self.horizontalLayout_8.setSpacing(5)
		self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
		self.cbChunkSettings = QComboBox(self.verticalLayoutWidget)
		icon35 = QIcon()
		icon35.addFile(u":/icons/icons8-add-tab-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon36 = QIcon()
		icon36.addFile(u":/icons/kalota_m.png", QSize(), QIcon.Normal, QIcon.Off)
		icon37 = QIcon()
		icon37.addFile(u":/icons/stopnca_o.png", QSize(), QIcon.Normal, QIcon.Off)
		icon38 = QIcon()
		icon38.addFile(u":/icons/stopnca_s.png", QSize(), QIcon.Normal, QIcon.Off)
		for section in autoftg_main.chunk_sections:
			menu_icon = autoftg_main.menuCfg.get(section, "menu_icon")
			menu_icon_path = u":/icons/" + autoftg_main.icoCfg.get("ICONS", menu_icon)
			setticon = QIcon()
			setticon.addFile(menu_icon_path, QSize(), QIcon.Normal, QIcon.Off)
			self.cbChunkSettings.addItem(setticon, section)

		self.cbChunkSettings.setCurrentText(self.itemDef)
		self.cbChunkSettings.setObjectName(u"cbChunkSettings")
		sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
		sizePolicy9.setHorizontalStretch(0)
		sizePolicy9.setVerticalStretch(0)
		sizePolicy9.setHeightForWidth(self.cbChunkSettings.sizePolicy().hasHeightForWidth())
		self.cbChunkSettings.setSizePolicy(sizePolicy9)
		self.cbChunkSettings.setMinimumSize(QSize(200, 0))
		self.cbChunkSettings.setFont(font6)
		self.cbChunkSettings.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.cbChunkSettings.setStatusTip(u"Choose settings used for chunk creation...")
#endif // QT_CONFIG(statustip)
		self.cbChunkSettings.setIconSize(QSize(20, 20))

		self.horizontalLayout_8.addWidget(self.cbChunkSettings)

		self.btnDefChunk = QPushButton(self.verticalLayoutWidget)
		self.btnDefChunk.setObjectName(u"btnDefChunk")
		self.btnDefChunk.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.btnDefChunk.setToolTip(u"Set as default")
#endif // QT_CONFIG(tooltip)
		self.btnDefChunk.setText(u"")
		self.btnDefChunk.setIcon(icon30)
		self.btnDefChunk.setIconSize(QSize(20, 20))
		self.btnDefChunk.setAutoDefault(False)
		self.btnDefChunk.setFlat(False)

		self.horizontalLayout_8.addWidget(self.btnDefChunk)


		self.gridLayout_3.addLayout(self.horizontalLayout_8, 8, 0, 1, 1)

		self.horizontalLayout_20 = QHBoxLayout()
		self.horizontalLayout_20.setSpacing(5)
		self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
		self.pushButton_resetSet = QPushButton(self.verticalLayoutWidget)
		self.pushButton_resetSet.setObjectName(u"pushButton_resetSet")
		sizePolicy5.setHeightForWidth(self.pushButton_resetSet.sizePolicy().hasHeightForWidth())
		self.pushButton_resetSet.setSizePolicy(sizePolicy5)
#if QT_CONFIG(tooltip)
		self.pushButton_resetSet.setToolTip(u"Reset settings to definition values.")
#endif // QT_CONFIG(tooltip)
		self.pushButton_resetSet.setText(u"Reset")
		icon39 = QIcon()
		icon39.addFile(u":/icons/icons8-rotate-48.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_resetSet.setIcon(icon39)
		self.pushButton_resetSet.setIconSize(QSize(20, 20))

		self.horizontalLayout_20.addWidget(self.pushButton_resetSet)

		self.pushButton_saveSet = QPushButton(self.verticalLayoutWidget)
		self.pushButton_saveSet.setObjectName(u"pushButton_saveSet")
		sizePolicy5.setHeightForWidth(self.pushButton_saveSet.sizePolicy().hasHeightForWidth())
		self.pushButton_saveSet.setSizePolicy(sizePolicy5)
#if QT_CONFIG(tooltip)
		self.pushButton_saveSet.setToolTip(u"Save current settings to selected definition.")
#endif // QT_CONFIG(tooltip)
		self.pushButton_saveSet.setText(u"Save")
		icon40 = QIcon()
		icon40.addFile(u":/icons/icons8-save-all-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_saveSet.setIcon(icon40)
		self.pushButton_saveSet.setIconSize(QSize(20, 20))
		self.pushButton_saveSet.setAutoDefault(False)
		self.pushButton_saveSet.setFlat(False)

		self.horizontalLayout_20.addWidget(self.pushButton_saveSet)


		self.gridLayout_3.addLayout(self.horizontalLayout_20, 32, 0, 1, 1)

		self.line_7 = QFrame(self.verticalLayoutWidget)
		self.line_7.setObjectName(u"line_7")
		self.line_7.setFrameShape(QFrame.HLine)
		self.line_7.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line_7, 30, 0, 1, 1)

		self.line_6 = QFrame(self.verticalLayoutWidget)
		self.line_6.setObjectName(u"line_6")
		self.line_6.setFrameShape(QFrame.HLine)
		self.line_6.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line_6, 25, 0, 1, 1)

		self.horizontalLayout_19 = QHBoxLayout()
		self.horizontalLayout_19.setSpacing(5)
		self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
		self.label_20 = QLabel(self.verticalLayoutWidget)
		self.label_20.setObjectName(u"label_20")
		self.label_20.setFont(font7)
		self.label_20.setText(u"Data Export:")
		self.label_20.setIndent(10)

		self.horizontalLayout_19.addWidget(self.label_20)

		self.label_expFolder = QLabel(self.verticalLayoutWidget)
		self.label_expFolder.setObjectName(u"label_expFolder")
		sizePolicy8.setHeightForWidth(self.label_expFolder.sizePolicy().hasHeightForWidth())
		self.label_expFolder.setSizePolicy(sizePolicy8)
		self.label_expFolder.setMinimumSize(QSize(200, 15))
		self.label_expFolder.setMaximumSize(QSize(16777215, 60))
		self.label_expFolder.setFont(font8)
		self.label_expFolder.setFrameShape(QFrame.NoFrame)
		self.label_expFolder.setText(u"")
		self.label_expFolder.setWordWrap(True)

		self.horizontalLayout_19.addWidget(self.label_expFolder)


		self.gridLayout_3.addLayout(self.horizontalLayout_19, 12, 0, 1, 1)

		self.line_3 = QFrame(self.verticalLayoutWidget)
		self.line_3.setObjectName(u"line_3")
		self.line_3.setFrameShadow(QFrame.Plain)
		self.line_3.setFrameShape(QFrame.HLine)

		self.gridLayout_3.addWidget(self.line_3, 13, 0, 1, 1)

		self.horizontalLayout_11 = QHBoxLayout()
		self.horizontalLayout_11.setSpacing(5)
		self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
		self.checkBox_align = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_align.setObjectName(u"checkBox_align")
		self.checkBox_align.setEnabled(True)
		sizePolicy6.setHeightForWidth(self.checkBox_align.sizePolicy().hasHeightForWidth())
		self.checkBox_align.setSizePolicy(sizePolicy6)
		self.checkBox_align.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_align.setToolTip(u"<html><head/><body><p>Enable to run 'Align Photos' process for selected items.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_align.setText(u"Align Photos")
		self.checkBox_align.setIcon(icon4)
		self.checkBox_align.setCheckable(True)
		self.checkBox_align.setChecked(False)
		self.checkBox_align.setTristate(False)

		self.horizontalLayout_11.addWidget(self.checkBox_align)

		self.pushButton_setAlign = QPushButton(self.verticalLayoutWidget)
		self.pushButton_setAlign.setObjectName(u"pushButton_setAlign")
		self.pushButton_setAlign.setEnabled(False)
		sizePolicy5.setHeightForWidth(self.pushButton_setAlign.sizePolicy().hasHeightForWidth())
		self.pushButton_setAlign.setSizePolicy(sizePolicy5)
		self.pushButton_setAlign.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_setAlign.setIcon(icon32)
		self.pushButton_setAlign.setFlat(True)

		self.horizontalLayout_11.addWidget(self.pushButton_setAlign)


		self.gridLayout_3.addLayout(self.horizontalLayout_11, 26, 0, 1, 1)

		self.horizontalLayout_14 = QHBoxLayout()
		self.horizontalLayout_14.setSpacing(5)
		self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
		self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_3.setObjectName(u"checkBox_3")
		sizePolicy6.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
		self.checkBox_3.setSizePolicy(sizePolicy6)
		self.checkBox_3.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_3.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Checked:</span> Enable new chunk creation and data import.</p><p><span style=\" font-weight:600;\">Not Checked:</span> Disable new chunk creation. Used when processing existing chunks.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_3.setText(u"Auto Import Processing")
		icon41 = QIcon()
		icon41.addFile(u":/icons/icons8-in-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_3.setIcon(icon41)
		self.checkBox_3.setCheckable(True)
		self.checkBox_3.setChecked(True)

		self.horizontalLayout_14.addWidget(self.checkBox_3)


		self.gridLayout_3.addLayout(self.horizontalLayout_14, 24, 0, 1, 1)

		self.label_17 = QLabel(self.verticalLayoutWidget)
		self.label_17.setObjectName(u"label_17")
		sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
		self.label_17.setSizePolicy(sizePolicy1)
		self.label_17.setMaximumSize(QSize(16777215, 30))
		font9 = QFont()
		font9.setFamily(u"Segoe UI")
		font9.setPointSize(11)
		font9.setBold(True)
		font9.setWeight(75)
		self.label_17.setFont(font9)
		self.label_17.setFrameShape(QFrame.NoFrame)
		self.label_17.setText(u"Processing")
		self.label_17.setIndent(5)

		self.gridLayout_3.addWidget(self.label_17, 23, 0, 1, 1)

		self.label_4 = QLabel(self.verticalLayoutWidget)
		self.label_4.setObjectName(u"label_4")
		sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
		self.label_4.setSizePolicy(sizePolicy1)
		self.label_4.setMaximumSize(QSize(16777215, 30))
		self.label_4.setFont(font9)
		self.label_4.setFrameShape(QFrame.NoFrame)
		self.label_4.setText(u"Camera")
		self.label_4.setIndent(5)

		self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

		self.horizontalLayout_10 = QHBoxLayout()
		self.horizontalLayout_10.setSpacing(5)
		self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
		self.label_18 = QLabel(self.verticalLayoutWidget)
		self.label_18.setObjectName(u"label_18")
		self.label_18.setFont(font7)
		self.label_18.setText(u"Name Format:")
		self.label_18.setIndent(10)

		self.horizontalLayout_10.addWidget(self.label_18)

		self.label_19 = QLabel(self.verticalLayoutWidget)
		self.label_19.setObjectName(u"label_19")
		sizePolicy7.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
		self.label_19.setSizePolicy(sizePolicy7)
		self.label_19.setMinimumSize(QSize(0, 20))
		self.label_19.setMaximumSize(QSize(16777215, 20))
		self.label_19.setFont(font8)
		self.label_19.setFrameShape(QFrame.NoFrame)
		self.label_19.setText(u"")

		self.horizontalLayout_10.addWidget(self.label_19)


		self.gridLayout_3.addLayout(self.horizontalLayout_10, 11, 0, 1, 1)

		self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

		self.gridLayout_3.addItem(self.verticalSpacer, 34, 0, 1, 1)

		self.horizontalLayout_6 = QHBoxLayout()
		self.horizontalLayout_6.setSpacing(5)
		self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
		self.label_9 = QLabel(self.verticalLayoutWidget)
		self.label_9.setObjectName(u"label_9")
		self.label_9.setFont(font7)
		self.label_9.setFrameShape(QFrame.NoFrame)
		self.label_9.setText(u"Type:")
		self.label_9.setIndent(10)

		self.horizontalLayout_6.addWidget(self.label_9)

		self.label_12 = QLabel(self.verticalLayoutWidget)
		self.label_12.setObjectName(u"label_12")
		sizePolicy7.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
		self.label_12.setSizePolicy(sizePolicy7)
		self.label_12.setMinimumSize(QSize(0, 20))
		self.label_12.setMaximumSize(QSize(16777215, 20))
		self.label_12.setFont(font8)
		self.label_12.setFrameShape(QFrame.NoFrame)
		self.label_12.setText(u"")

		self.horizontalLayout_6.addWidget(self.label_12)


		self.gridLayout_3.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)

		self.horizontalLayout_7 = QHBoxLayout()
		self.horizontalLayout_7.setSpacing(5)
		self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
		self.label_13 = QLabel(self.verticalLayoutWidget)
		self.label_13.setObjectName(u"label_13")
		self.label_13.setFont(font7)
		self.label_13.setText(u"SubType:")
		self.label_13.setIndent(10)

		self.horizontalLayout_7.addWidget(self.label_13)

		self.label_14 = QLabel(self.verticalLayoutWidget)
		self.label_14.setObjectName(u"label_14")
		sizePolicy7.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
		self.label_14.setSizePolicy(sizePolicy7)
		self.label_14.setMinimumSize(QSize(0, 20))
		self.label_14.setMaximumSize(QSize(16777215, 20))
		self.label_14.setFont(font8)
		self.label_14.setFrameShape(QFrame.NoFrame)
		self.label_14.setText(u"")

		self.horizontalLayout_7.addWidget(self.label_14)


		self.gridLayout_3.addLayout(self.horizontalLayout_7, 5, 0, 1, 1)

		self.line_5 = QFrame(self.verticalLayoutWidget)
		self.line_5.setObjectName(u"line_5")
		self.line_5.setFrameShadow(QFrame.Plain)
		self.line_5.setFrameShape(QFrame.HLine)

		self.gridLayout_3.addWidget(self.line_5, 6, 0, 1, 1)

		self.label_5 = QLabel(self.verticalLayoutWidget)
		self.label_5.setObjectName(u"label_5")
		sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
		self.label_5.setSizePolicy(sizePolicy1)
		self.label_5.setMaximumSize(QSize(16777215, 30))
		self.label_5.setFont(font9)
		self.label_5.setFrameShape(QFrame.NoFrame)
		self.label_5.setText(u"Markers")
		self.label_5.setIndent(5)

		self.gridLayout_3.addWidget(self.label_5, 19, 0, 1, 1)

		self.horizontalLayout_3 = QHBoxLayout()
		self.horizontalLayout_3.setSpacing(5)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.label_10 = QLabel(self.verticalLayoutWidget)
		self.label_10.setObjectName(u"label_10")
		self.label_10.setFont(font7)
		self.label_10.setText(u"Suffix:")
		self.label_10.setIndent(10)

		self.horizontalLayout_3.addWidget(self.label_10)

		self.label_7 = QLabel(self.verticalLayoutWidget)
		self.label_7.setObjectName(u"label_7")
		sizePolicy7.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
		self.label_7.setSizePolicy(sizePolicy7)
		self.label_7.setMinimumSize(QSize(0, 20))
		self.label_7.setMaximumSize(QSize(16777215, 20))
		self.label_7.setFont(font8)
		self.label_7.setFrameShape(QFrame.NoFrame)
		self.label_7.setText(u"")

		self.horizontalLayout_3.addWidget(self.label_7)


		self.gridLayout_3.addLayout(self.horizontalLayout_3, 10, 0, 1, 1)

		self.label = QLabel(self.verticalLayoutWidget)
		self.label.setObjectName(u"label")
		sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy1)
		self.label.setMaximumSize(QSize(16777215, 30))
		self.label.setFont(font9)
		self.label.setFrameShape(QFrame.NoFrame)
		self.label.setText(u"Chunk Creation Settings")
		self.label.setIndent(5)

		self.gridLayout_3.addWidget(self.label, 7, 0, 1, 1)

		self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_2.setObjectName(u"checkBox_2")
		sizePolicy1.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
		self.checkBox_2.setSizePolicy(sizePolicy1)
		self.checkBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_2.setToolTip(u"<html><head/><body><p>Enable automatic target detection when new chunk is created...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_2.setText(u"Automatic Target Detection")
		self.checkBox_2.setIcon(icon15)
		self.checkBox_2.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox_2, 20, 0, 1, 1)


		self.gridLayout.addLayout(self.gridLayout_3, 0, 2, 3, 1)

		self.label_16 = QLabel(self.verticalLayoutWidget)
		self.label_16.setObjectName(u"label_16")
		sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
		self.label_16.setSizePolicy(sizePolicy1)
		self.label_16.setMaximumSize(QSize(16777215, 20))
		self.label_16.setFont(font6)
		self.label_16.setFrameShape(QFrame.NoFrame)
		self.label_16.setText(u"<html><head/><body><p>Selected: <span style=\" font-weight:600;\">0</span></p></body></html>")
		self.label_16.setIndent(10)

		self.gridLayout.addWidget(self.label_16, 3, 2, 1, 1)


		self.verticalLayout_2.addLayout(self.gridLayout)


		self.checkBox_mesh.setEnabled(True)
		self.checkBox_export.setEnabled(True)
		self.checkBox_pcloud.setEnabled(True)

		defChk = self.cbChunkSettings.currentText()
		self.label_6.setText(autoftg_main.menuCfg.get(defChk, "chunk_name_prefix"))
		self.label_7.setText(autoftg_main.menuCfg.get(defChk, "chunk_name_suffix"))

		defCam = self.comboBox_2.currentText()
		self.label_12.setText(autoftg_main.camCfg.get(defCam, "type"))
		self.label_14.setText(autoftg_main.camCfg.get(defCam, "subtype"))
		
		self.checkBox_4.toggled.connect(self.pushButton.setDisabled)
		self.checkBox_4.toggled.connect(self.lineEdit.setDisabled)
		self.checkBox_2.toggled.connect(self.checkBox.toggle)
		self.cbChunkSettings.currentTextChanged.connect(self.setCurrentSettings)
		self.cbChunkSettings.currentTextChanged.connect(self.updateFolders)
		self.comboBox_2.currentTextChanged.connect(self.setCurrentCamera)
		self.pushButton_2.clicked.connect(self.quitChunkBatch)
		self.pushButton_3.clicked.connect(self.progressBar.reset)
		self.pushButton_3.clicked.connect(self.processBatch)
		self.pushButton_4.clicked.connect(self.updateFolders)
		self.pushButton.clicked.connect(self.browseFolder)
		self.treeWidget.itemSelectionChanged.connect(self.updateSelected)
		self.btnDefChunk.clicked.connect(self.setDefaultChunk)
		self.btnDefCam.clicked.connect(self.setDefaultCam)
		self.pushButton_10.clicked.connect(self.openFileExplorer)
		# self.pushButton_setAlign.clicked.connect()
		self.pushButton_setMesh.setEnabled(True)
		self.pushButton_setMesh.clicked.connect(self.diaSettingsMesh)
		# self.pushButton_setPCloud.clicked.connect()
		# self.pushButton_setExport.clicked.connect()
		self.pushButton_saveSet.clicked.connect(self.saveCurrentSettings)
		self.pushButton_resetSet.clicked.connect(self.resetCurrentSettings)
		
		

		projDoc = Metashape.app.document
		self.projDocFile = str(projDoc).replace("<Document '", "").replace("'>", "")
		self.logFilenamePath = self.projDocFile.replace(".psx", ".csv")	# Datoteka z nastavitvami projekta
		
		self.setCurrentSettings()
		self.setCurrentCamera()
		self.updateFolders()
		
		
		self.exec_()


	def logReadArchive(self):
		global logArchive
		logFilenameExists = os.path.isfile(self.logFilenamePath)
		if logFilenameExists == False:
			with open(self.logFilenamePath, mode='w', newline='') as csvlog_file:
				ms_header = ['Date', 'Time', 'Chunk Name', 'Key', 'Photos', 'Point File', 'Camera', 'Align', 'Mesh', 'Point Cloud', 'Data Path', 'Export Folder', 'Model File', 'P.Cloud File']
				logInit = csv.DictWriter(csvlog_file, fieldnames = ms_header, dialect = 'excel')
				logInit.writeheader()

		with open(self.logFilenamePath, mode='r') as csvlog_file:
			logArchive = csv.reader(csvlog_file, dialect='excel')
			for row in logArchive:
				print(row[2] + " (" + row[7] + ", " + row[8] + ", " + row[9] + ")")
		

	def logWriteArchive(self, data):
		logFilenameExists = os.path.isfile(self.logFilenamePath)
		if logFilenameExists == False:
			with open(self.logFilenamePath, mode='w', newline='') as csvlog_file:
				ms_header = ['Date', 'Time', 'Chunk Name', 'Key', 'Photos', 'Point File', 'Camera', 'Align', 'Mesh', 'Point Cloud', 'Data Path', 'Export Folder', 'Model File', 'P.Cloud File']
				logInit = csv.DictWriter(csvlog_file, fieldnames = ms_header, dialect = 'excel')
				logInit.writeheader()
		else:
			print(str(data))
			with open(self.logFilenamePath, mode='a', newline='') as csvlog_file:
				logWrite = csv.writer(csvlog_file, dialect='excel')
				logWrite.writerow(data)


	def selectChunkFormat(self, chunkDef):
		chunkNameFormat = autoftg_main.menuCfg.get(chunkDef, "chunk_name_format")

		if chunkNameFormat == "metashape":
			self.label_19.setText(u"Metashape Default (Chunk 1, Chunk 2,...)")
		elif chunkNameFormat == "data":
			self.label_19.setText(u"Data Folder Name")
		elif chunkNameFormat == "point":
			self.label_19.setText(u"Point File Metadata")
		elif chunkNameFormat == "creation":
			self.label_19.setText(u"Creation date-time")
		elif chunkNameFormat == "image":
			self.label_19.setText(u"Image date-time")
		elif chunkNameFormat == "custom":
			self.label_19.setText(u"Custom date-time")
		

	def setCurrentSettings(self):
		global chunkSet
		chunkSet = self.cbChunkSettings.currentText()
		autoftg_main.menuCfg.read(autoftg_main.menuCfgFilePath)

		if chunkSet != "" or chunkSet != None:
			self.lineEdit.clear()
			self.pushButton.setEnabled(True)
			self.lineEdit.setEnabled(True)
			self.lineEdit.setText(str(autoftg_main.menuCfg.get(chunkSet, "work_folder")))
			self.label_6.setText(autoftg_main.menuCfg.get(chunkSet, "chunk_name_prefix"))
			self.label_7.setText(autoftg_main.menuCfg.get(chunkSet, "chunk_name_suffix"))
			self.selectChunkFormat(chunkSet)
			self.label_expFolder.setText(str(autoftg_main.menuCfg.get(chunkSet, "export_folder")))
			self.checkBox_4.setChecked(True)
			self.checkBox_2.setChecked(autoftg_main.menuCfg.getboolean(chunkSet, "target_detection"))
			self.checkBox.setChecked(autoftg_main.menuCfg.getboolean(chunkSet, "import_markers"))
			self.checkBox_3.setChecked(autoftg_main.menuCfg.getboolean(chunkSet, "auto_process"))
			self.checkBox_align.setChecked(autoftg_main.menuCfg.getboolean(chunkSet, "align_photos"))
			self.checkBox_mesh.setChecked(autoftg_main.menuCfg.getboolean(chunkSet, "mesh_build"))
			self.checkBox_pcloud.setChecked(autoftg_main.menuCfg.getboolean(chunkSet, "pointcloud_build"))
			self.checkBox_export.setChecked(autoftg_main.menuCfg.getboolean(chunkSet, "export_data"))
			self.mesh_type = (autoftg_main.menuCfg.get(chunkSet, "mesh_type"))
			self.mesh_face_count = (autoftg_main.menuCfg.get(chunkSet, "mesh_face_count"))
			self.mesh_face_count_custom = (autoftg_main.menuCfg.getint(chunkSet, "mesh_face_count_custom"))
			self.mesh_depthmaps = (autoftg_main.menuCfg.get(chunkSet, "mesh_depthmaps"))
			self.mesh_depthfilter = (autoftg_main.menuCfg.get(chunkSet, "mesh_depthfilter"))
			self.mesh_interpolation = (autoftg_main.menuCfg.getboolean(chunkSet, "mesh_interpolation"))
			self.mesh_vertex_color = (autoftg_main.menuCfg.getboolean(chunkSet, "mesh_vertex_color"))
			self.mesh_vertex_confidence = (autoftg_main.menuCfg.getboolean(chunkSet, "mesh_vertex_confidence"))
			self.texture_build = (autoftg_main.menuCfg.getboolean(chunkSet, "texture_build"))
			self.texture_size = (autoftg_main.menuCfg.get(chunkSet, "texture_size"))
			self.texture_levels = (autoftg_main.menuCfg.get(chunkSet, "texture_levels"))
			self.texture_fill = (autoftg_main.menuCfg.getboolean(chunkSet, "texture_fill"))
			self.texture_ghosting = (autoftg_main.menuCfg.getboolean(chunkSet, "texture_ghosting"))
			self.label_8.setText(u"<html><head/><body><p>Chunk definition settings loaded...</p></body></html>")



	def setCurrentCamera(self):
		chunkCam = self.comboBox_2.currentText()
		self.label_12.setText(autoftg_main.camCfg.get(chunkCam, "type"))
		self.label_14.setText(autoftg_main.camCfg.get(chunkCam, "subtype"))
		

	def updateFolders(self):
		self.setCurrentSettings()
		self.logReadArchive()
		
		iconReload = QIcon()
		iconReload.addFile(u":/icons/icons8-update-left-rotation-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconLoading = QIcon()
		iconLoading.addFile(u":/icons/icons8-loading-96.png", QSize(), QIcon.Normal, QIcon.Off)
		font6 = QFont()
		font6.setBold(True)
		font6.setWeight(75)
		iconFolderTree = QIcon()
		iconFolderTree.addFile(u":/icons/icons8-folder-tree-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconFolder = QIcon()
		iconFolder.addFile(u":/icons/icons8-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconDone = QIcon()
		iconDone.addFile(u":/icons/icons8-done-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconDoneFile = QIcon()
		iconDoneFile.addFile(u":/icons/icons8-check-file-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconNoCam = QIcon()
		iconNoCam.addFile(u":/icons/icons8-no-camera-96.png", QSize(), QIcon.Normal, QIcon.Off)
		font7 = QFont()
		font7.setFamily(u"Segoe UI")
		iconClose = QIcon()
		iconClose.addFile(u":/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconAddCam = QIcon()
		iconAddCam.addFile(u":/icons/icons8-add-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconStart = QIcon()
		iconStart.addFile(u":/icons/icons8-synchronize-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconProcess = QIcon()
		iconProcess.addFile(u":/icons/icons8-loading-96.png", QSize(), QIcon.Normal, QIcon.Off)
		iconProcess.addFile(u":/icons/icons8-loading-96.png", QSize(), QIcon.Disabled, QIcon.Off)
		iconError = QIcon()
		iconError.addFile(u":/icons/icons8-error-48.png", QSize(), QIcon.Normal, QIcon.Off)
		iconError.addFile(u":/icons/icons8-error-48.png", QSize(), QIcon.Disabled, QIcon.Off)
		iconOk = QIcon()
		iconOk.addFile(u":/icons/icons8-ok-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconOk.addFile(u":/icons/icons8-ok-50.png", QSize(), QIcon.Disabled, QIcon.Off)
		iconLocOff = QIcon()
		iconLocOff.addFile(u":/icons/icons8-location-off-48.png", QSize(), QIcon.Normal, QIcon.Off)
		iconToDo = QIcon()
		iconToDo.addFile(u":/icons/icons8-microsoft-todo-2019-48.png", QSize(), QIcon.Normal, QIcon.Off)
		iconProgDone = QIcon()
		iconProgDone.addFile(u":/icons/icons8-in-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
		iconReadyProc = QIcon()
		iconReadyProc.addFile(u":/icons/icons8-submit-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
		
		self.pushButton_4.setIcon(iconLoading)
		
		self.treeWidget.clear()
		
		itemCurFolder = str(self.lineEdit.text()).split("/")[-1]

		open_folder = self.lineEdit.text() + "\\"
		
		qtreewidgetitem_top = QTreeWidgetItem(self.treeWidget)
		qtreewidgetitem_top.setText(0, itemCurFolder)
		qtreewidgetitem_top.setFont(0, font6)
		qtreewidgetitem_top.setIcon(0, iconFolderTree)
		qtreewidgetitem_top.setExpanded(True)

		folder_list = []
		folder_list = next(os.walk(open_folder))[1];
		
		# chunks_list = Metashape.app.document.chunks
		# chunks_list.replace("<Chunk '", "").replace("'>'", "")

		for folder in folder_list:
			__qtreewidgetitem1 = QTreeWidgetItem(qtreewidgetitem_top);
			image_folder = str(open_folder).replace("\\", "/") + "/" + folder
			photos_count = len(autoftg_main.find_files(image_folder, [".jpg", ".jpeg", ".png", ".tif", ".tiff"]));
			folder_chunk = self.label_6.text() + folder + self.label_7.text()
			with open(self.logFilenamePath, mode='r') as csvlog_file:
				logArchive = csv.reader(csvlog_file, dialect='excel')
				for row in logArchive:
					print(row[2] + " (" + row[7] + ", " + row[8] + ", " + row[9] + ")")
					if row[2] == folder_chunk:
						__qtreewidgetitem1.setIcon(3, iconDone);
						if row[9] == 'PC':
							__qtreewidgetitem1.setIcon(6, iconToDo);
						if row[8] == 'M' or row[8] == 'M+T':
							__qtreewidgetitem1.setIcon(5, iconToDo);
						if row[7] == 'A':
							__qtreewidgetitem1.setIcon(4, iconToDo);

			points_file = image_folder + "/" + folder + ".txt"
			points_file_exists = os.path.isfile(points_file);
			if points_file_exists == True:
				__qtreewidgetitem1.setIcon(2, iconDoneFile);
				__qtreewidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
				__qtreewidgetitem1.setText(2, u"OK");
			else:
				__qtreewidgetitem1.setIcon(2, iconClose);
				__qtreewidgetitem1.setText(2, u"N/A");
				__qtreewidgetitem1.setFlags(Qt.ItemIsEnabled);
			if photos_count > 0:
				__qtreewidgetitem1.setText(1, str(photos_count));
				__qtreewidgetitem1.setIcon(1, iconAddCam);
				__qtreewidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
			else:
				__qtreewidgetitem1.setText(1, "N/A");
				__qtreewidgetitem1.setIcon(1, iconNoCam);
				__qtreewidgetitem1.setFlags(Qt.ItemIsEnabled);
			
			__qtreewidgetitem1.setText(0, folder);
			__qtreewidgetitem1.setIcon(0, iconFolder);
			__qtreewidgetitem1.setSizeHint(0, QSize(165, 0))
			

		self.pushButton_3.setIcon(iconStart)
		self.pushButton_3.setText(u"Ready")
		self.pushButton_3.setDisabled(True)
		self.label_8.setText(u"<html><head/><body><p>Folder contents reloaded...</p></body></html>")
		self.progressBar.setMinimum(1)
		self.progressBar.setMaximum(1)
		self.progressBar.setValue(0)
		self.progressBar.setTextVisible(False)
		self.progressBar.setDisabled(True)
		self.treeWidget.resizeColumnToContents(0)
		self.treeWidget.resizeColumnToContents(1)
		self.treeWidget.resizeColumnToContents(2)
		self.treeWidget.resizeColumnToContents(3)
		self.treeWidget.resizeColumnToContents(4)
		self.treeWidget.resizeColumnToContents(5)
		self.treeWidget.resizeColumnToContents(6)
		self.treeWidget.sortItems(0, Qt.AscendingOrder)
		self.treeWidget.scrollToBottom()
		self.pushButton_4.setIcon(iconReload)
		

	def setDefaultChunk(self):
		current_chunkdef = self.cbChunkSettings.currentText()
		autoftg_main.projCfg.set("PROJECT SETTINGS", "default_chunk_def", current_chunkdef)
		with open(autoftg_main.projCfgFilePath, 'w') as configfile:
			autoftg_main.projCfg.write(configfile)

		self.label_8.setText(u"<html><head/><body><p>Default definition set to: " + current_chunkdef + "</p></body></html>")


	def setDefaultCam(self):
		current_cam = self.comboBox_2.currentText()
		autoftg_main.projCfg.set("PROJECT SETTINGS", "default_camera", current_cam)
		with open(autoftg_main.projCfgFilePath, 'w') as configfile:
			autoftg_main.projCfg.write(configfile)

		self.label_8.setText(u"<html><head/><body><p>Default camera set to: " + current_cam + "</p></body></html>")


	def saveCurrentSettings(self):
		autoftg_main.menuCfg.set(self.cbChunkSettings.currentText(), "auto_process", str(self.checkBox_3.isChecked()))
		autoftg_main.menuCfg.set(self.cbChunkSettings.currentText(), "align_photos", str(self.checkBox_align.isChecked()))
		autoftg_main.menuCfg.set(self.cbChunkSettings.currentText(), "mesh_build", str(self.checkBox_mesh.isChecked()))
		autoftg_main.menuCfg.set(self.cbChunkSettings.currentText(), "pointcloud_build", str(self.checkBox_pcloud.isChecked()))
		autoftg_main.menuCfg.set(self.cbChunkSettings.currentText(), "export_data", str(self.checkBox_export.isChecked()))
		
		with open(autoftg_main.menuCfgFilePath, 'w') as configfile:
			autoftg_main.menuCfg.write(configfile)

		print("Settings saved...\nChunk def.: " + self.cbChunkSettings.currentText())


	def resetCurrentSettings(self):
		self.checkBox_3.setChecked(autoftg_main.menuCfg.getboolean(self.cbChunkSettings.currentText(), "auto_process"))
		self.checkBox_align.setChecked(autoftg_main.menuCfg.getboolean(self.cbChunkSettings.currentText(), "align_photos"))
		self.checkBox_mesh.setChecked(autoftg_main.menuCfg.getboolean(self.cbChunkSettings.currentText(), "mesh_build"))
		self.checkBox_pcloud.setChecked(autoftg_main.menuCfg.getboolean(self.cbChunkSettings.currentText(), "pointcloud_build"))
		self.checkBox_export.setChecked(autoftg_main.menuCfg.getboolean(self.cbChunkSettings.currentText(), "export_data"))
		
		print("Settings reset...")


	def browseFolder(self):
		defFolder = Metashape.app.getExistingDirectory("Data folder")
		self.lineEdit.setText(defFolder)
		self.updateFolders()


	def updateSelected(self):
		iconStart = QIcon()
		iconStart.addFile(u":/icons/icons8-synchronize-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_3.setIcon(iconStart)
		self.pushButton_3.setEnabled(True)
		sel_items = self.treeWidget.selectedItems()
		sel_count = len(sel_items)
		if sel_count > 0:
			self.pushButton_3.setEnabled(True)
			self.pushButton_3.setText(u"Process")
			self.pushButton_10.setEnabled(True)
			self.label_16.setText(u"<html><head/><body><p>Selected: <span style=\" font-weight:600;\">" + str(sel_count) + "</span></p></body></html>")
		else:
			self.pushButton_3.setDisabled(True)
			self.pushButton_3.setText(u"Ready")
			self.pushButton_10.setDisabled(True)
			self.label_16.setText(u"<html><head/><body><p><b>Select items to process...</b</p></body></html>")
		

	def openFileExplorer(self):
		selected_path = self.lineEdit.text() + "\\" + self.treeWidget.currentItem().text(0)

		# explorer would choke on forward slashes
		path = os.path.normpath(selected_path)

		if os.path.isdir(path):
			subprocess.run([FILEBROWSER_PATH, path])
		else:
			print("Nothing selected?!?")


	# Process selected folders automatically (no user interaction)
	def processBatchAuto(self):
		self.sel_items = self.treeWidget.selectedItems()
		sel_count = len(self.sel_items)
		item_menu = self.cbChunkSettings.currentText()
		item_pre = autoftg_main.menuCfg.get(item_menu, "chunk_name_prefix")
		item_suf = autoftg_main.menuCfg.get(item_menu, "chunk_name_suffix")
		item_cam = self.comboBox_2.currentText()
		output_folder = autoftg_main.menuCfg.get(item_menu, "export_folder").replace("\\", "/")
		

		iconStart = QIcon()
		iconStart.addFile(u":/icons/icons8-synchronize-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconProcess = QIcon()
		iconProcess.addFile(u":/icons/icons8-loading-96.png", QSize(), QIcon.Normal, QIcon.Off)
		iconProcess.addFile(u":/icons/icons8-loading-96.png", QSize(), QIcon.Disabled, QIcon.Off)
		iconError = QIcon()
		iconError.addFile(u":/icons/icons8-error-48.png", QSize(), QIcon.Normal, QIcon.Off)
		iconError.addFile(u":/icons/icons8-error-48.png", QSize(), QIcon.Disabled, QIcon.Off)
		iconOk = QIcon()
		iconOk.addFile(u":/icons/icons8-ok-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconOk.addFile(u":/icons/icons8-ok-50.png", QSize(), QIcon.Disabled, QIcon.Off)
		iconDone = QIcon()
		iconDone.addFile(u":/icons/icons8-done-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconToDo = QIcon()
		iconToDo.addFile(u":/icons/icons8-microsoft-todo-2019-48.png", QSize(), QIcon.Normal, QIcon.Off)
		iconProgDone = QIcon()
		iconProgDone.addFile(u":/icons/icons8-in-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
		
		if sel_count > 0:
			i_cnt = 0
			self.progressBar.setEnabled(True)
			self.progressBar.setMinimum(i_cnt)
			self.progressBar.setMaximum(sel_count)
			self.progressBar.setValue(i_cnt)
			self.progressBar.setTextVisible(True)
			self.progressBar.setAlignment(Qt.AlignCenter)
			self.pushButton_3.setEnabled(False)
			self.pushButton_3.setIcon(iconProcess)
			self.pushButton_3.setText(u"Processing...")
			
			for item in self.sel_items:
				i_cnt = i_cnt + 1
				self.progressBar.setFormat(u"Completed %v of %m")
				self.pushButton_3.setEnabled(False)
				self.pushButton_3.setIcon(iconProcess)
				self.pushButton_3.setText(u"Processing...")
				
				updItem = QTreeWidgetItem
				
				doc = Metashape.app.document
				netpath = Metashape.app.document.path
				netroot = self.lineEdit.text()
				image_folder = str(netroot).replace("\\", "/") + "/" + item.text(0)
				photos = autoftg_main.find_files(image_folder, [".jpg", ".jpeg", ".png", ".tif", ".tiff"])
				chunk = doc.addChunk()
				chunk_key = str(chunk.key)
				self.label_8.setText(u"Processing folder " + str(i_cnt) + " of " + str(sel_count) + " | Current: <b>" + str(item.text(0)) + " (" + chunk_key + ")</b> - Data Import...")
				chunk.addPhotos(photos)
				chunk_name = item_pre + item.text(0) + item_suf
				chunk.label = chunk_name
				doc.chunk = chunk
				doc.save(netpath)
				Metashape.app.update()
				time.sleep(3)
				autoftg_main.readCameraSettings(item_cam)
				autoftg_main.useCameraSettings()
				if self.checkBox_2.isChecked() == True:
					self.label_8.setText(u"Processing folder " + str(i_cnt) + " of " + str(sel_count) + " | Current: <b>" + str(item.text(0)) + " (" + chunk_key + ")</b> - Processing Markers...")
					chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
					Metashape.app.update()

				if self.checkBox.isChecked() == True:
					self.label_8.setText(u"Processing folder " + str(i_cnt) + " of " + str(sel_count) + " | Current: <b>" + str(item.text(0)) + " (" + chunk_key + ")</b> - Coordinates Import...")
					points_file = image_folder + "/" + item.text(0) + ".txt"
					points_file_exists = os.path.isfile(points_file)
					if points_file_exists == True:
						chunk.importReference(points_file, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
						chunk.updateTransform()
						ms_pntfile = item.text(0) + ".txt"
					else:
						ms_pntfile = "None"
					
					Metashape.app.update()
					doc.save(netpath)
					updItem.setIcon(item, 3, iconProgDone)


				align_done = ""
				# Metashape.ReferencePreselectionMode.[ReferencePreselectionSource, ReferencePreselectionEstimated, ReferencePreselectionSequential]
				if self.checkBox_align.isChecked() == True:
					align_quality = 0
					align_genPresel = False
					align_refPresel = False
					align_refPreselMode = Metashape.ReferencePreselectionMode.ReferencePreselectionSource
					align_keyLimit = 40000
					align_tieLimit = 10000
					align_filterMask = False
					align_maskTie = False
					align_filterSta = False
					align_keepKey = False
					align_guidedMatching = False
					align_resetCurrent = True

					self.label_8.setText(u"Processing folder " + str(i_cnt) + " of " + str(sel_count) + " | Current: <b>" + str(item.text(0)) + " (" + chunk_key + ")</b> - Align Photos...")
					chunk.matchPhotos(downscale=align_quality, keypoint_limit=align_keyLimit, tiepoint_limit=align_tieLimit, generic_preselection=align_genPresel, reference_preselection=align_refPresel, reference_preselection_mode=align_refPreselMode, filter_mask=align_filterMask, mask_tiepoints=align_maskTie, filter_stationary_points=align_filterSta, keep_keypoints=align_keepKey, guided_matching=align_guidedMatching, reset_matches=align_resetCurrent, subdivide_task=True)
					doc.save(netpath)
					chunk.alignCameras(subdivide_task = True)
					doc.save(netpath)
					align_done = "A"
					updItem.setIcon(item, 4, iconToDo)
					Metashape.app.update()


				mesh_done = ''
				if self.checkBox_mesh.isChecked() == True:
					self.label_8.setText(u"Processing folder " + str(i_cnt) + " of " + str(sel_count) + " | Current: <b>" + str(item.text(0)) + " (" + chunk_key + ")</b> - Building Model...")
					
					if self.mesh_depthmaps == "Ultra High":
						depth_quality = 0
					elif self.mesh_depthmaps == "High":
						depth_quality = 2
					elif self.mesh_depthmaps == "Medium":
						depth_quality = 4
					elif self.mesh_depthmaps == "Low":
						depth_quality = 8
					elif self.mesh_depthmaps == "Lowest":
						depth_quality = 16
					else:
						depth_quality = 4
					
					if self.mesh_depthfilter == "Aggressive":
						filter_mode = Metashape.AggressiveFiltering
					elif self.mesh_depthfilter == "Moderate":
						filter_mode = Metashape.ModerateFiltering
					elif self.mesh_depthfilter == "Mild":
						filter_mode = Metashape.MildFiltering
					else:
						filter_mode = Metashape.NoFiltering


					chunk.buildDepthMaps(downscale=depth_quality, filter_mode=filter_mode)
					
					doc.save(netpath)

					if self.mesh_interpolation == True:
						mesh_int = Metashape.Interpolation.EnabledInterpolation
					else:
						mesh_int = Metashape.Interpolation.DisabledInterpolation

					mesh_facecount = ""
					mesh_facecount_custom = 0
					if self.mesh_face_count == "High":
						mesh_facecount = Metashape.FaceCount.HighFaceCount
					elif self.mesh_face_count == "Medium":
						mesh_facecount = Metashape.FaceCount.MediumFaceCount
					elif self.mesh_face_count == "Low":
						mesh_facecount = Metashape.FaceCount.LowFaceCount
					elif self.mesh_face_count == "Custom":
						mesh_facecount = Metashape.FaceCount.CustomFaceCount
						mesh_facecount_custom = int(self.mesh_face_count_custom)
					
					if self.mesh_type == "Arbitrary":
						mesh_type = Metashape.SurfaceType.Arbitrary
					else:
						mesh_type = Metashape.SurfaceType.HeightField

					chunk.buildModel(surface_type=mesh_type, interpolation=mesh_int, face_count=mesh_facecount, face_count_custom=mesh_facecount_custom, source_data=Metashape.DepthMapsData, vertex_colors =self.mesh_vertex_color, vertex_confidence=self.mesh_vertex_confidence, subdivide_task=True)
					
					mesh_buildModel = 'M'
					doc.save(netpath)

					model_buildTex = ''
					if self.texture_build == True:
						self.label_8.setText(u"Processing folder " + str(i_cnt) + " of " + str(sel_count) + " | Current: <b>" + str(item.text(0)) + " (" + chunk_key + ")</b> - Building Texture...")
						chunk.buildUV(page_count = self.texture_levels, texture_size = int(self.texture_size))
						doc.save(netpath)
						chunk.buildTexture(texture_size = int(self.texture_size), fill_holes = self.texture_fill, ghosting_filter = self.texture_ghosting)
						
						model_buildTex = '+T'
						doc.save(netpath)

					mesh_done = mesh_buildModel + model_buildTex
					updItem.setIcon(item, 5, iconToDo)
					Metashape.app.update()


				ptcloud_done = ""
				if self.checkBox_pcloud.isChecked() == True:
					source_data = Metashape.DataSource.DepthMapsData
					point_colors = True
					point_confidence = False
					keep_depth = True
					max_neighbors = 100
					uniform_sampling = False
					points_spacing = 0.02
					subdivide_task = True

					self.label_8.setText(u"Processing folder " + str(i_cnt) + " of " + str(sel_count) + " | Current: <b>" + str(item.text(0)) + " (" + chunk_key + ")</b> - Building Point Cloud...")
					chunk.buildPointCloud(source_data=source_data, point_color=point_colors, point_confidence=point_confidence, keep_depth=keep_depth, max_neighbors=max_neighbors, uniform_sampling=uniform_sampling, points_spacing=points_spacing, subdivide_task=subdivide_task)
					doc.save(netpath)
					ptcloud_done = 'PC'
					updItem.setIcon(item, 6, iconToDo)
					Metashape.app.update()


				chunk_emodel = ""
				chunk_eptc = ""
				if self.checkBox_export.isChecked() == True:
					self.label_8.setText(u"Processing folder " + str(i_cnt) + " of " + str(sel_count) + " | Current: <b>" + str(item.text(0)) + " (" + chunk_key + ")</b> - Exporting Data...")
					if chunk.model:
						chunk.exportModel(path=output_folder + "/" + chunk_name + ".obj", binary=True, precision=4, texture_format=Metashape.ImageFormat.ImageFormatJPEG, save_texture=True, save_uv=True, save_normals=True, save_colors=True, save_confidence=False, save_cameras=True, save_markers=True, save_udim=False, save_alpha=False, embed_texture=False, strip_extensions=False, colors_rgb_8bit=True, comment=chunk_name, save_comment=True)
						chunk_emodel = chunk_name + ".obj"
						Metashape.app.update()

					if chunk.point_cloud:
						chunk.exportPointCloud(path=output_folder + "/" + chunk_name + ".laz", source_data=Metashape.PointCloudData, save_point_color=True, save_point_normal=True, save_point_confidence=True)
						chunk_eptc = chunk_name + ".laz"
						Metashape.app.update()

					
				now = datetime.now()
				dt_string = now.strftime("%d.%m.%Y")
				tm_string = now.strftime("%H:%M")
				ms_data = [dt_string, tm_string, chunk_name, chunk_key, str(len(photos)), ms_pntfile, item_cam, align_done, mesh_done, ptcloud_done, image_folder, output_folder, chunk_emodel, chunk_eptc]
				self.logWriteArchive(ms_data)
				updItem.setIcon(item, 3, iconDone);
				self.label_8.setText(u"Processing folder " + str(i_cnt) + " of " + str(sel_count) + " | Current: <b>" + str(item.text(0)) + " (" + chunk_key + ")</b> - Done.")
				self.treeWidget.setItemSelected(item, False)
				self.progressBar.setValue(i_cnt)
				Metashape.app.update()
				doc.save(netpath)
				time.sleep(1)


			if i_cnt < sel_count:
				updItem.setIcon(item, 3, iconError)
				self.pushButton_3.setIcon(iconError)
				self.pushButton_3.setText(u"Error!")
				self.label_8.setText(u"<html><head/><body><p><b>Processing error!</b> / Imported " + str(i_cnt) + " of " + str(sel_count) + " / Could not import <b>" + str(item.text(0)) + "</b></p></body></html>")
			else:
				self.pushButton_3.setIcon(iconOk)
				self.pushButton_3.setText(u"Finished")
				self.label_8.setText(u"<html><head/><body><p><b>Processing Finished!</b> / Imported " + str(i_cnt) + " of " + str(sel_count) + "</p></body></html>")


			Metashape.app.update()
			doc.save(netpath)
			

			

	# Process selected folders manually (user must confirm chunk name, camera settings, marker detection, and show point file)
#	def processBatchManual(self):
#		self.sel_items = self.treeWidget.selectedItems()
#		sel_count = len(self.sel_items)
#		item_menu = self.cbChunkSettings.currentText()
#		item_pre = autoftg_main.menuCfg.get(item_menu, "chunk_name_prefix")
#		item_suf = autoftg_main.menuCfg.get(item_menu, "chunk_name_suffix")
#		item_cam = self.comboBox_2.currentText()
#		output_folder = autoftg_main.menuCfg.get(item_menu, "export_folder").replace("\\", "/")
#
#		iconStart = QIcon()
#		iconStart.addFile(u":/icons/icons8-synchronize-50.png", QSize(), QIcon.Normal, QIcon.Off)
#		iconProcess = QIcon()
#		iconProcess.addFile(u":/icons/icons8-loading-96.png", QSize(), QIcon.Normal, QIcon.Off)
#		iconProcess.addFile(u":/icons/icons8-loading-96.png", QSize(), QIcon.Disabled, QIcon.Off)
#		iconError = QIcon()
#		iconError.addFile(u":/icons/icons8-error-48.png", QSize(), QIcon.Normal, QIcon.Off)
#		iconError.addFile(u":/icons/icons8-error-48.png", QSize(), QIcon.Disabled, QIcon.Off)
#		iconOk = QIcon()
#		iconOk.addFile(u":/icons/icons8-ok-50.png", QSize(), QIcon.Normal, QIcon.Off)
#		iconOk.addFile(u":/icons/icons8-ok-50.png", QSize(), QIcon.Disabled, QIcon.Off)
#		iconDone = QIcon()
#		iconDone.addFile(u":/icons/icons8-done-50.png", QSize(), QIcon.Normal, QIcon.Off)
#		iconToDo = QIcon()
#		iconToDo.addFile(u":/icons/icons8-microsoft-todo-2019-48.png", QSize(), QIcon.Normal, QIcon.Off)
##		
#		if sel_count > 0:
#			i_cnt = 0
#			self.progressBar.setEnabled(True)
#			self.progressBar.setMinimum(i_cnt)
#			self.progressBar.setMaximum(sel_count)
#			self.progressBar.setValue(i_cnt)
#			self.pushButton_3.setDisabled(True)
#			self.pushButton_3.setIcon(iconProcess)
#			self.pushButton_3.setText(u"Processing...")
#			
#			for item in self.sel_items:
#				i_cnt = i_cnt + 1
#				self.progressBar.setFormat(u"Completed %v/%m")
#				self.label_8.setText(u"Processing folder " + str(i_cnt) + " of " + str(sel_count) + " | Current: <b>" + str(item.text(0)) + "</b>")
#				updItem = QTreeWidgetItem
#				doc = Metashape.app.document
#				netpath = Metashape.app.document.path
#				netroot = self.lineEdit.text()
#				image_folder = str(netroot).replace("\\", "/") + "/" + item.text(0)
#				photos = autoftg_main.find_files(image_folder, [".jpg", ".jpeg", ".png", ".tif", ".tiff"])
#				chunk = doc.addChunk()
#				chunk.addPhotos(photos)
#				chunk_name = item_pre + item.text(0) + item_suf
#				chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
#				chunk.label = chunk_name
#				doc.chunk = chunk
#				doc.save(netpath)
#				autoftg_main.readCameraSettings(item_cam)
#				autoftg_main.useCameraSettings()
#				if self.checkBox_2.isChecked() == True:
#					chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)
#					Metashape.app.update()
#
#				if self.checkBox.isChecked() == True:
#					points_file = image_folder + "/" + item.text(0) + ".txt"
#					points_file_exists = os.path.isfile(points_file)
#					if points_file_exists == True:
#						chunk.importReference(points_file, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
#						chunk.updateTransform()
#						ms_pntfile = item.text(0) + ".txt"
#					else:
#						ms_pntfile = "None"
#					
#					Metashape.app.update()
#					doc.save(netpath)
#					updItem.setIcon(item, 3, iconDone)
#
#
#				align_done = ""
#				if self.checkBox_align.isChecked() == True:
#					chunk.matchPhotos(downscale = 0, keypoint_limit = 40000, tiepoint_limit = 10000, generic_preselection = False, reference_preselection = False)
#					doc.save(netpath)
#					chunk.alignCameras(subdivide_task = True)
#					doc.save(netpath)
#					align_done = item.text(0) + "_aligned"
#					updItem.setIcon(item, 4, iconToDo)
#					Metashape.app.update()
#
#
#				mesh_done = ""
#				if self.checkBox_mesh.isChecked() == True:
#					chunk.buildDepthMaps(downscale = 2, filter_mode = Metashape.MildFiltering)
#					doc.save(netpath)
#					chunk.buildModel(source_data = Metashape.DepthMapsData)
#					doc.save(netpath)
#					chunk.buildUV(page_count = 1, texture_size = 4096)
#					doc.save(netpath)
#					chunk.buildTexture(texture_size=4096, fill_holes=True, ghosting_filter=True)
#					doc.save(netpath)
#					mesh_done = item.text(0) + "_mesh"
#					updItem.setIcon(item, 5, iconToDo)
#					Metashape.app.update()
#
#
#				ptcloud_done = ""
#				if self.checkBox_export.isChecked() == True:
#					chunk.buildPointCloud()
#					doc.save(netpath)
#					ptcloud_done = item.text(0) + "_pointcloud"
#					updItem.setIcon(item, 6, iconToDo)
#					Metashape.app.update()
#
#
#				chunk_emodel = ""
#				chunk_eptc = ""
#				export_done = ""
#				if self.checkBox_pcloud.isChecked() == True:
#					if chunk.model:
#						chunk.exportModel(path=output_folder + "/" + chunk_name + ".obj", binary=True, precision=4, texture_format='ImageFormatJPEG', save_texture=True, save_uv=True, save_normals=True, save_colors=True, save_confidence=False, save_cameras=True, save_markers=True, save_udim=False, save_alpha=False, embed_texture=False, strip_extensions=False, colors_rgb_8bit=True, comment=chunk_name, save_comment=True)
#						chunk_emodel = "(M)"
#						Metashape.app.update()
#
#					if chunk.point_cloud:
#						chunk.exportPointCloud(output_folder + "/" + chunk_name + ".laz", source_data = Metashape.PointCloudData, save_point_color=True, save_point_normal=True, save_point_confidence=True)
#						chunk_eptc = "(PC)"
#						Metashape.app.update()
#
#					export_done = chunk_emodel + chunk_eptc + "," + output_folder
#
#
#				now = datetime.now()
#				dt_string = now.strftime("%d.%m.%Y")
#				tm_string = now.strftime("%H:%M")
#				ms_data = list(dt_string, tm_string, chunk_name, str(len(photos)), ms_pntfile, item_cam, image_folder, align_done, mesh_done, ptcloud_done, export_done)
#				self.logWriteArchive(ms_data)
#				
#				self.treeWidget.setItemSelected(item, False)
#				self.progressBar.setValue(i_cnt)
#				Metashape.app.update()
#				doc.save(netpath)
#
#
#			if i_cnt < sel_count:
#				self.pushButton_3.setIcon(iconError)
#				self.pushButton_3.setText(u"Error!")
#				self.label_8.setText(u"<html><head/><body><p><b>Processing error!</b> / Imported " + str(i_cnt) + " of " + str(sel_count) + " / Could not import <b>" + str(item.text(0)) + "</b></p></body></html>")
#			else:
#				self.pushButton_3.setIcon(iconOk)
#				self.pushButton_3.setText(u"Finished")
#				self.label_8.setText(u"<html><head/><body><p><b>Processing Finished!</b> / Imported " + str(i_cnt) + " of " + str(sel_count) + "</p></body></html>")
#
#
#			Metashape.app.update()
#			doc.save(netpath)
				

	def processBatch(self):
		if self.checkBox_3.isChecked() == True:
			self.processBatchAuto()
		else:
			# self.processBatchManual()
			Metashape.app.messageBox("Feature in development. Coming soon.")


	def quitChunkBatch(self):
		self.reject()


	def diaSettingsMesh(self):
		app_inst = QtWidgets.QApplication.instance()
		parent = app_inst.activeWindow()
		setMeshDia = Ui_DialogSettingsMesh(parent)
		self.setCurrentSettings()


