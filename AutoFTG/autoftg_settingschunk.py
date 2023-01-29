import os
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

import AutoFTG.autoftg_main as ftgMain
from AutoFTG.qtresources import *


class Ui_DialogChunkSettings(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.setObjectName(u"DialogChunkSettings")
		self.setWindowModality(Qt.WindowModal)
		self.resize(720, 360)
		self.setWindowTitle(u"Chunk Definition Settings")
		sizePolicy0 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		sizePolicy0.setHorizontalStretch(0)
		sizePolicy0.setVerticalStretch(0)
		sizePolicy0.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy0)
		self.setMinimumSize(QSize(720, 480))
		self.setMaximumSize(QSize(720, 480))
		icon = QIcon()
		icon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(icon)
		self.gridLayoutWidget = QWidget(self)
		self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
		self.gridLayoutWidget.setGeometry(QRect(9, 10, 701, 461))
		self.gridLayout = QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setSpacing(5)
		self.gridLayout.setContentsMargins(10, 10, 10, 10)
		self.gridLayout.setObjectName(u"gridLayout")
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.label_menuSet_2 = QLabel(self.gridLayoutWidget)
		self.label_menuSet_2.setObjectName(u"label_menuSet_2")
		sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
		sizePolicy1.setHorizontalStretch(0)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.label_menuSet_2.sizePolicy().hasHeightForWidth())
		self.label_menuSet_2.setSizePolicy(sizePolicy1)
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label_menuSet_2.setFont(font)
		self.label_menuSet_2.setFrameShape(QFrame.StyledPanel)
		self.label_menuSet_2.setText(u"Chunk Definitions List")

		self.gridLayout.addWidget(self.label_menuSet_2, 0, 0, 1, 1)

		self.listWidgetChunkDefs = QListWidget(self.gridLayoutWidget)
		self.listWidgetChunkDefs.setObjectName(u"listWidgetChunkDefs")
		sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
		sizePolicy2.setHorizontalStretch(0)
		sizePolicy2.setVerticalStretch(0)
		sizePolicy2.setHeightForWidth(self.listWidgetChunkDefs.sizePolicy().hasHeightForWidth())
		self.listWidgetChunkDefs.setSizePolicy(sizePolicy2)
		font1 = QFont()
		font1.setFamily(u"Segoe UI")
		font1.setPointSize(11)
		self.listWidgetChunkDefs.setFont(font1)
		self.listWidgetChunkDefs.setAutoScrollMargin(20)
		self.listWidgetChunkDefs.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.listWidgetChunkDefs.setProperty("showDropIndicator", False)
		self.listWidgetChunkDefs.setSelectionBehavior(QAbstractItemView.SelectItems)
		self.listWidgetChunkDefs.setIconSize(QSize(24, 24))
		self.listWidgetChunkDefs.setViewMode(QListView.ListMode)
		self.listWidgetChunkDefs.setUniformItemSizes(True)
		self.listWidgetChunkDefs.setSelectionRectVisible(True)
		self.listWidgetChunkDefs.setSortingEnabled(False)

		self.gridLayout.addWidget(self.listWidgetChunkDefs, 1, 0, 1, 1)

		self.horizontalLayout_6 = QHBoxLayout()
		self.horizontalLayout_6.setSpacing(5)
		self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
		self.pushButton_sremove = QPushButton(self.gridLayoutWidget)
		self.pushButton_sremove.setObjectName(u"pushButton_sremove")
		self.pushButton_sremove.setEnabled(True)
		sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
		sizePolicy3.setHorizontalStretch(0)
		sizePolicy3.setVerticalStretch(0)
		sizePolicy3.setHeightForWidth(self.pushButton_sremove.sizePolicy().hasHeightForWidth())
		self.pushButton_sremove.setSizePolicy(sizePolicy3)
		self.pushButton_sremove.setMinimumSize(QSize(0, 30))
#if QT_CONFIG(tooltip)
		self.pushButton_sremove.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Remove<br/></span>Remove selected definition</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.pushButton_sremove.setText(u"Remove")
		icon7 = QIcon()
		icon7.addFile(u":/icons/icons8-full-recycle-bin-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_sremove.setIcon(icon7)
		self.pushButton_sremove.setIconSize(QSize(20, 20))
#if QT_CONFIG(shortcut)
		self.pushButton_sremove.setShortcut(u"R")
#endif // QT_CONFIG(shortcut)
		self.pushButton_sremove.setAutoDefault(False)

		self.horizontalLayout_6.addWidget(self.pushButton_sremove)

		self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

		self.pushButton_sedit = QPushButton(self.gridLayoutWidget)
		self.pushButton_sedit.setObjectName(u"pushButton_sedit")
		self.pushButton_sedit.setEnabled(True)
		sizePolicy3.setHeightForWidth(self.pushButton_sedit.sizePolicy().hasHeightForWidth())
		self.pushButton_sedit.setSizePolicy(sizePolicy3)
		self.pushButton_sedit.setMinimumSize(QSize(0, 30))
#if QT_CONFIG(tooltip)
		self.pushButton_sedit.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Edit</span><br/>Edit selected chunk definition</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.pushButton_sedit.setLayoutDirection(Qt.RightToLeft)
		self.pushButton_sedit.setText(u"Edit")
		icon8 = QIcon()
		icon8.addFile(u":/icons/icons8-design-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_sedit.setIcon(icon8)
		self.pushButton_sedit.setIconSize(QSize(20, 20))
#if QT_CONFIG(shortcut)
		self.pushButton_sedit.setShortcut(u"E")
#endif // QT_CONFIG(shortcut)
		self.pushButton_sedit.setAutoDefault(False)

		self.horizontalLayout_6.addWidget(self.pushButton_sedit)


		self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

		self.line = QFrame(self.gridLayoutWidget)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.gridLayout.addWidget(self.line, 3, 0, 1, 2)

		self.formLayout = QFormLayout()
		self.formLayout.setSpacing(5)
		self.formLayout.setObjectName(u"formLayout")
		self.formLayout.setHorizontalSpacing(5)
		self.formLayout.setVerticalSpacing(5)
		self.label_menuSet = QLabel(self.gridLayoutWidget)
		self.label_menuSet.setObjectName(u"label_menuSet")
		sizePolicy1.setHeightForWidth(self.label_menuSet.sizePolicy().hasHeightForWidth())
		self.label_menuSet.setSizePolicy(sizePolicy1)
		self.label_menuSet.setFont(font)
		self.label_menuSet.setFrameShape(QFrame.StyledPanel)
		self.label_menuSet.setText(u"Menu Settings")

		self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_menuSet)

		self.label_nameicon = QLabel(self.gridLayoutWidget)
		self.label_nameicon.setObjectName(u"label_nameicon")
		self.label_nameicon.setMinimumSize(QSize(80, 0))
		self.label_nameicon.setMaximumSize(QSize(80, 16777215))
		self.label_nameicon.setText(u"Name")
		self.label_nameicon.setIndent(5)

		self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_nameicon)

		self.horizontalLayout_4 = QHBoxLayout()
		self.horizontalLayout_4.setSpacing(5)
		self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
		self.lineEdit_name = QLineEdit(self.gridLayoutWidget)
		self.lineEdit_name.setObjectName(u"lineEdit_name")
		sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
		sizePolicy4.setHorizontalStretch(0)
		sizePolicy4.setVerticalStretch(0)
		sizePolicy4.setHeightForWidth(self.lineEdit_name.sizePolicy().hasHeightForWidth())
		self.lineEdit_name.setSizePolicy(sizePolicy4)
		font2 = QFont()
		font2.setFamily(u"Segoe UI")
		font2.setPointSize(12)
		self.lineEdit_name.setFont(font2)
		self.lineEdit_name.setPlaceholderText(u"Name shown in list...")

		self.horizontalLayout_4.addWidget(self.lineEdit_name)


		self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_4)

		self.label_nameicon_2 = QLabel(self.gridLayoutWidget)
		self.label_nameicon_2.setObjectName(u"label_nameicon_2")
		sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		sizePolicy5.setHorizontalStretch(0)
		sizePolicy5.setVerticalStretch(0)
		sizePolicy5.setHeightForWidth(self.label_nameicon_2.sizePolicy().hasHeightForWidth())
		self.label_nameicon_2.setSizePolicy(sizePolicy5)
		font3 = QFont()
		font3.setFamily(u"Segoe UI")
		font3.setPointSize(9)
		self.label_nameicon_2.setFont(font3)
		self.label_nameicon_2.setText(u"Icon")
		self.label_nameicon_2.setIndent(5)

		self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_nameicon_2)

		self.comboBox_icon = QComboBox(self.gridLayoutWidget)
		self.comboBox_icon.setObjectName(u"comboBox_icon")
		sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
		sizePolicy6.setHorizontalStretch(0)
		sizePolicy6.setVerticalStretch(0)
		sizePolicy6.setHeightForWidth(self.comboBox_icon.sizePolicy().hasHeightForWidth())
		self.comboBox_icon.setSizePolicy(sizePolicy6)
		self.comboBox_icon.setMaximumSize(QSize(100, 16777215))
#if QT_CONFIG(tooltip)
		self.comboBox_icon.setToolTip(u"Choose icon to be used in list...")
#endif // QT_CONFIG(tooltip)
		self.comboBox_icon.setIconSize(QSize(24, 24))

		self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_icon)

		self.label_chunkSet = QLabel(self.gridLayoutWidget)
		self.label_chunkSet.setObjectName(u"label_chunkSet")
		sizePolicy1.setHeightForWidth(self.label_chunkSet.sizePolicy().hasHeightForWidth())
		self.label_chunkSet.setSizePolicy(sizePolicy1)
		self.label_chunkSet.setFont(font)
		self.label_chunkSet.setFrameShape(QFrame.StyledPanel)
		self.label_chunkSet.setText(u"Chunk Settings")

		self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.label_chunkSet)

		self.horizontalLayout_7 = QHBoxLayout()
		self.horizontalLayout_7.setSpacing(5)
		self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
		self.groupBoxChunkName = QGroupBox(self.gridLayoutWidget)
		self.groupBoxChunkName.setObjectName(u"groupBoxChunkName")
		sizePolicy7 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
		sizePolicy7.setHorizontalStretch(0)
		sizePolicy7.setVerticalStretch(0)
		sizePolicy7.setHeightForWidth(self.groupBoxChunkName.sizePolicy().hasHeightForWidth())
		self.groupBoxChunkName.setSizePolicy(sizePolicy7)
		self.groupBoxChunkName.setMinimumSize(QSize(0, 130))
		font4 = QFont()
		font4.setFamily(u"Segoe UI")
		font4.setPointSize(9)
		font4.setBold(True)
		font4.setWeight(75)
		self.groupBoxChunkName.setFont(font4)
		self.groupBoxChunkName.setTitle(u"Chunk Name Format")
		self.gridLayoutWidget_2 = QWidget(self.groupBoxChunkName)
		self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
		self.gridLayoutWidget_2.setGeometry(QRect(12, 25, 411, 100))
		self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
		self.gridLayout_2.setSpacing(5)
		self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
		self.gridLayout_2.setObjectName(u"gridLayout_2")
		self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
		self.radioButton_5 = QRadioButton(self.gridLayoutWidget_2)
		self.radioButton_5.setObjectName(u"radioButton_5")
		sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		sizePolicy8.setHorizontalStretch(0)
		sizePolicy8.setVerticalStretch(0)
		sizePolicy8.setHeightForWidth(self.radioButton_5.sizePolicy().hasHeightForWidth())
		self.radioButton_5.setSizePolicy(sizePolicy8)
		font5 = QFont()
		font5.setFamily(u"Segoe UI")
		font5.setPointSize(9)
		font5.setBold(False)
		font5.setWeight(50)
		self.radioButton_5.setFont(font5)
		self.radioButton_5.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.radioButton_5.setToolTip(u"<html><head/><body><p>Use date and time found in first image file that is imported from work folder.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.radioButton_5.setText(u"Image date-time")

		self.gridLayout_2.addWidget(self.radioButton_5, 1, 1, 1, 1)

		self.radioButton_3 = QRadioButton(self.gridLayoutWidget_2)
		self.radioButton_3.setObjectName(u"radioButton_3")
		sizePolicy8.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
		self.radioButton_3.setSizePolicy(sizePolicy8)
		self.radioButton_3.setFont(font5)
		self.radioButton_3.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.radioButton_3.setToolTip(u"<html><head/><body><p>Use metadata string from point file that must be located in imported data folder, and must also have the same name as data folder..</p><p><span style=\" font-weight:600;\">Info:</span> String must be in metadata format at the beginnig of point file, as described in help.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.radioButton_3.setText(u"Point File Metadata")

		self.gridLayout_2.addWidget(self.radioButton_3, 2, 0, 1, 1)

		self.radioButton_6 = QRadioButton(self.gridLayoutWidget_2)
		self.radioButton_6.setObjectName(u"radioButton_6")
		sizePolicy8.setHeightForWidth(self.radioButton_6.sizePolicy().hasHeightForWidth())
		self.radioButton_6.setSizePolicy(sizePolicy8)
		self.radioButton_6.setFont(font5)
		self.radioButton_6.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.radioButton_6.setToolTip(u"<html><head/><body><p>Use date and time at which chunk is created in custom provided format.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.radioButton_6.setText(u"Custom date-time")

		self.gridLayout_2.addWidget(self.radioButton_6, 2, 1, 1, 1)

		self.radioButton_2 = QRadioButton(self.gridLayoutWidget_2)
		self.radioButton_2.setObjectName(u"radioButton_2")
		sizePolicy8.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
		self.radioButton_2.setSizePolicy(sizePolicy8)
		self.radioButton_2.setFont(font5)
		self.radioButton_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.radioButton_2.setToolTip(u"<html><head/><body><p>Uses the name of folder from which data is beeing imported from.</p><p>* Recommended naming format.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.radioButton_2.setText(u"Data Folder Name")

		self.gridLayout_2.addWidget(self.radioButton_2, 1, 0, 1, 1)

		self.radioButton_1 = QRadioButton(self.gridLayoutWidget_2)
		self.radioButton_1.setObjectName(u"radioButton_1")
		sizePolicy8.setHeightForWidth(self.radioButton_1.sizePolicy().hasHeightForWidth())
		self.radioButton_1.setSizePolicy(sizePolicy8)
		self.radioButton_1.setFont(font5)
		self.radioButton_1.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.radioButton_1.setToolTip(u"<html><head/><body><p>Use default naming format provided by Metashape.</p><p>Example: Chunk 1, Chunk 2,...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.radioButton_1.setText(u"Metashape Default")

		self.gridLayout_2.addWidget(self.radioButton_1, 0, 0, 1, 1)

		self.radioButton_4 = QRadioButton(self.gridLayoutWidget_2)
		self.radioButton_4.setObjectName(u"radioButton_4")
		sizePolicy8.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
		self.radioButton_4.setSizePolicy(sizePolicy8)
		self.radioButton_4.setFont(font5)
		self.radioButton_4.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.radioButton_4.setToolTip(u"<html><head/><body><p>Use date and time at which chunk is created.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.radioButton_4.setText(u"Creation date-time")

		self.gridLayout_2.addWidget(self.radioButton_4, 0, 1, 1, 1)

		self.horizontalLayout_8 = QHBoxLayout()
		self.horizontalLayout_8.setSpacing(5)
		self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
		self.horizontalSpacer_4 = QSpacerItem(225, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

		self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

		self.lineEdit = QLineEdit(self.gridLayoutWidget_2)
		self.lineEdit.setObjectName(u"lineEdit")
		self.lineEdit.setEnabled(False)
		sizePolicy8.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
		self.lineEdit.setSizePolicy(sizePolicy8)
		self.lineEdit.setMinimumSize(QSize(140, 0))
		self.lineEdit.setFont(font5)
#if QT_CONFIG(tooltip)
		self.lineEdit.setToolTip(u"<html><head/><body><p>Enter format string in python format.</p><p>*For details please check help first.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.lineEdit.setPlaceholderText(u"%Y%m%d-%H%M%S")

		self.horizontalLayout_8.addWidget(self.lineEdit)

		self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


		self.gridLayout_2.addLayout(self.horizontalLayout_8, 3, 0, 1, 2)


		self.horizontalLayout_7.addWidget(self.groupBoxChunkName)


		self.formLayout.setLayout(4, QFormLayout.SpanningRole, self.horizontalLayout_7)

		self.label_wfolder_2 = QLabel(self.gridLayoutWidget)
		self.label_wfolder_2.setObjectName(u"label_wfolder_2")
		self.label_wfolder_2.setFont(font3)
		self.label_wfolder_2.setText(u"Prefix/Suffix")
		self.label_wfolder_2.setIndent(5)

		self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_wfolder_2)

		self.horizontalLayout_5 = QHBoxLayout()
		self.horizontalLayout_5.setSpacing(5)
		self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
		self.lineEdit_pre = QLineEdit(self.gridLayoutWidget)
		self.lineEdit_pre.setObjectName(u"lineEdit_pre")
		self.lineEdit_pre.setEnabled(False)
		sizePolicy4.setHeightForWidth(self.lineEdit_pre.sizePolicy().hasHeightForWidth())
		self.lineEdit_pre.setSizePolicy(sizePolicy4)
#if QT_CONFIG(tooltip)
		self.lineEdit_pre.setToolTip(u"Leave empty to disable prefix.")
#endif // QT_CONFIG(tooltip)
		self.lineEdit_pre.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
		self.lineEdit_pre.setPlaceholderText(u"PREFIX_")

		self.horizontalLayout_5.addWidget(self.lineEdit_pre)

		self.label = QLabel(self.gridLayoutWidget)
		self.label.setObjectName(u"label")
		self.label.setStyleSheet(u"color: rgb(157, 158, 149);")
		self.label.setText(u"<chunk name>")
		self.label.setAlignment(Qt.AlignCenter)

		self.horizontalLayout_5.addWidget(self.label)

		self.lineEdit_suf = QLineEdit(self.gridLayoutWidget)
		self.lineEdit_suf.setObjectName(u"lineEdit_suf")
		self.lineEdit_suf.setEnabled(False)
		sizePolicy4.setHeightForWidth(self.lineEdit_suf.sizePolicy().hasHeightForWidth())
		self.lineEdit_suf.setSizePolicy(sizePolicy4)
#if QT_CONFIG(tooltip)
		self.lineEdit_suf.setToolTip(u"Leave empty to disable suffix.")
#endif // QT_CONFIG(tooltip)
		self.lineEdit_suf.setPlaceholderText(u"_SUFFIX")

		self.horizontalLayout_5.addWidget(self.lineEdit_suf)


		self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_5)

		self.label_wfolder = QLabel(self.gridLayoutWidget)
		self.label_wfolder.setObjectName(u"label_wfolder")
		self.label_wfolder.setFont(font3)
		self.label_wfolder.setText(u"Data Folder")
		self.label_wfolder.setIndent(5)

		self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_wfolder)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setSpacing(5)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.lineEdit_wfolder = QLineEdit(self.gridLayoutWidget)
		self.lineEdit_wfolder.setObjectName(u"lineEdit_wfolder")
		self.lineEdit_wfolder.setPlaceholderText(u"Path to folder with data...")

		self.horizontalLayout.addWidget(self.lineEdit_wfolder)

		self.pushButton_browsewf = QPushButton(self.gridLayoutWidget)
		self.pushButton_browsewf.setObjectName(u"pushButton_browsewf")
		sizePolicy3.setHeightForWidth(self.pushButton_browsewf.sizePolicy().hasHeightForWidth())
		self.pushButton_browsewf.setSizePolicy(sizePolicy3)
#if QT_CONFIG(tooltip)
		self.pushButton_browsewf.setToolTip(u"<html><head/><body><p>Select location with working data for this definition.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.pushButton_browsewf.setText(u"")
		icon9 = QIcon()
		icon9.addFile(u":/icons/icons8-opened-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_browsewf.setIcon(icon9)
		self.pushButton_browsewf.setIconSize(QSize(20, 20))
		self.pushButton_browsewf.setAutoDefault(False)

		self.horizontalLayout.addWidget(self.pushButton_browsewf)


		self.formLayout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout)

		self.label_efolder = QLabel(self.gridLayoutWidget)
		self.label_efolder.setObjectName(u"label_efolder")
		self.label_efolder.setFont(font3)
		self.label_efolder.setText(u"Export Folder")
		self.label_efolder.setIndent(5)

		self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_efolder)

		self.horizontalLayout_10 = QHBoxLayout()
		self.horizontalLayout_10.setSpacing(5)
		self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
		self.lineEdit_efolder = QLineEdit(self.gridLayoutWidget)
		self.lineEdit_efolder.setObjectName(u"lineEdit_efolder")
		self.lineEdit_efolder.setPlaceholderText(u"Path to folder for exporting...")

		self.horizontalLayout_10.addWidget(self.lineEdit_efolder)

		self.pushButton_browseef = QPushButton(self.gridLayoutWidget)
		self.pushButton_browseef.setObjectName(u"pushButton_browseef")
		sizePolicy3.setHeightForWidth(self.pushButton_browseef.sizePolicy().hasHeightForWidth())
		self.pushButton_browseef.setSizePolicy(sizePolicy3)
#if QT_CONFIG(tooltip)
		self.pushButton_browseef.setToolTip(u"<html><head/><body><p>Select location with working data for this definition.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.pushButton_browseef.setText(u"")
		self.pushButton_browseef.setIcon(icon9)
		self.pushButton_browseef.setIconSize(QSize(20, 20))
		self.pushButton_browseef.setAutoDefault(False)

		self.horizontalLayout_10.addWidget(self.pushButton_browseef)


		self.formLayout.setLayout(7, QFormLayout.FieldRole, self.horizontalLayout_10)

		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setSpacing(5)
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

		self.pushButton_save = QPushButton(self.gridLayoutWidget)
		self.pushButton_save.setObjectName(u"pushButton_save")
		self.pushButton_save.setEnabled(False)
		sizePolicy3.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
		self.pushButton_save.setSizePolicy(sizePolicy3)
		self.pushButton_save.setMinimumSize(QSize(0, 30))
#if QT_CONFIG(tooltip)
		self.pushButton_save.setToolTip(u"<html><head/><body><p>Save currently selected chunk definition</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.pushButton_save.setText(u"Save")
		icon10 = QIcon()
		icon10.addFile(u":/icons/icons8-save-as-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_save.setIcon(icon10)
		self.pushButton_save.setIconSize(QSize(20, 20))
#if QT_CONFIG(shortcut)
		self.pushButton_save.setShortcut(u"S")
#endif // QT_CONFIG(shortcut)
		self.pushButton_save.setAutoDefault(False)

		self.horizontalLayout_2.addWidget(self.pushButton_save)

		self.pushButton_add = QPushButton(self.gridLayoutWidget)
		self.pushButton_add.setObjectName(u"pushButton_add")
		sizePolicy3.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
		self.pushButton_add.setSizePolicy(sizePolicy3)
		self.pushButton_add.setMinimumSize(QSize(0, 30))
#if QT_CONFIG(tooltip)
		self.pushButton_add.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Add new</span><br/>Add new chunk settings definition</p><p>*Crates new chunk definition with current options.<br/>**Definition Name must be unique.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.pushButton_add.setText(u"Add New")
		icon11 = QIcon()
		icon11.addFile(u":/icons/icons8-add-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_add.setIcon(icon11)
		self.pushButton_add.setIconSize(QSize(20, 20))
#if QT_CONFIG(shortcut)
		self.pushButton_add.setShortcut(u"A")
#endif // QT_CONFIG(shortcut)
		self.pushButton_add.setAutoDefault(True)

		self.horizontalLayout_2.addWidget(self.pushButton_add)


		self.formLayout.setLayout(9, QFormLayout.FieldRole, self.horizontalLayout_2)

		self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

		self.formLayout.setItem(10, QFormLayout.LabelRole, self.verticalSpacer)

		self.line_2 = QFrame(self.gridLayoutWidget)
		self.line_2.setObjectName(u"line_2")
		self.line_2.setFrameShape(QFrame.HLine)
		self.line_2.setFrameShadow(QFrame.Sunken)

		self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.line_2)


		self.gridLayout.addLayout(self.formLayout, 0, 1, 3, 1)

		self.horizontalLayout_3 = QHBoxLayout()
		self.horizontalLayout_3.setSpacing(5)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.label_2 = QLabel(self.gridLayoutWidget)
		self.label_2.setObjectName(u"label_2")
		font6 = QFont()
		font6.setFamily(u"Segoe UI")
		font6.setPointSize(8)
		self.label_2.setFont(font6)
		self.label_2.setText(u"<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Shortcuts</span>: [A] Add New / [E] Edit / [R] Remove / [S] Save / [C] Close</p></body></html>")

		self.horizontalLayout_3.addWidget(self.label_2)

		self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout_3.addItem(self.horizontalSpacer)

		self.pushButton_close = QPushButton(self.gridLayoutWidget)
		self.pushButton_close.setObjectName(u"pushButton_close")
		sizePolicy3.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
		self.pushButton_close.setSizePolicy(sizePolicy3)
		self.pushButton_close.setMinimumSize(QSize(0, 30))
#if QT_CONFIG(tooltip)
		self.pushButton_close.setToolTip(u"Close Chunk Settings Editor")
#endif // QT_CONFIG(tooltip)
		self.pushButton_close.setText(u"Close")
		icon12 = QIcon()
		icon12.addFile(u":/icons/icons8-close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_close.setIcon(icon12)
		self.pushButton_close.setIconSize(QSize(20, 20))
#if QT_CONFIG(shortcut)
		self.pushButton_close.setShortcut(u"C")
#endif // QT_CONFIG(shortcut)

		self.horizontalLayout_3.addWidget(self.pushButton_close)


		self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 2)

		QWidget.setTabOrder(self.listWidgetChunkDefs, self.pushButton_sremove)
		QWidget.setTabOrder(self.pushButton_sremove, self.pushButton_sedit)
		QWidget.setTabOrder(self.pushButton_sedit, self.lineEdit_name)
		QWidget.setTabOrder(self.lineEdit_name, self.comboBox_icon)
		QWidget.setTabOrder(self.comboBox_icon, self.radioButton_1)
		QWidget.setTabOrder(self.radioButton_1, self.radioButton_2)
		QWidget.setTabOrder(self.radioButton_2, self.radioButton_3)
		QWidget.setTabOrder(self.radioButton_3, self.radioButton_4)
		QWidget.setTabOrder(self.radioButton_4, self.radioButton_5)
		QWidget.setTabOrder(self.radioButton_5, self.radioButton_6)
		QWidget.setTabOrder(self.radioButton_6, self.lineEdit)
		QWidget.setTabOrder(self.lineEdit, self.lineEdit_pre)
		QWidget.setTabOrder(self.lineEdit_pre, self.lineEdit_suf)
		QWidget.setTabOrder(self.lineEdit_suf, self.lineEdit_wfolder)
		QWidget.setTabOrder(self.lineEdit_wfolder, self.pushButton_browsewf)
		QWidget.setTabOrder(self.pushButton_browsewf, self.lineEdit_efolder)
		QWidget.setTabOrder(self.lineEdit_efolder, self.pushButton_browseef)
		QWidget.setTabOrder(self.pushButton_browseef, self.pushButton_save)
		QWidget.setTabOrder(self.pushButton_save, self.pushButton_add)
		QWidget.setTabOrder(self.pushButton_add, self.pushButton_close)

		self.btnAction = True
		self.selFormat = str("metashape")

		self.pushButton_sremove.clicked.connect(self.removeSelectedItem)
		self.pushButton_add.clicked.connect(self.addBtnAction)
		self.pushButton_close.clicked.connect(self.reject)
		self.listWidgetChunkDefs.currentItemChanged.connect(self.pushButton_sedit.setEnabled(True))
		self.listWidgetChunkDefs.currentItemChanged.connect(self.pushButton_sremove.setEnabled(True))
		self.pushButton_sedit.clicked.connect(self.editSelectedItem)
		self.pushButton_browsewf.clicked.connect(self.selectWorkFolder)
		self.pushButton_browseef.clicked.connect(self.selectExportFolder)
		self.pushButton_save.clicked.connect(self.saveSelectedItem)
		self.radioButton_1.toggled.connect(self.lineEdit_pre.setDisabled)
		self.radioButton_1.toggled.connect(self.lineEdit_suf.setDisabled)
		self.radioButton_2.toggled.connect(self.lineEdit_pre.setEnabled)
		self.radioButton_2.toggled.connect(self.lineEdit_suf.setEnabled)
		self.radioButton_3.toggled.connect(self.lineEdit_pre.setEnabled)
		self.radioButton_3.toggled.connect(self.lineEdit_suf.setEnabled)
		self.radioButton_4.toggled.connect(self.lineEdit_pre.setEnabled)
		self.radioButton_4.toggled.connect(self.lineEdit_suf.setEnabled)
		self.radioButton_5.toggled.connect(self.lineEdit_pre.setEnabled)
		self.radioButton_5.toggled.connect(self.lineEdit_suf.setEnabled)
		self.radioButton_6.toggled.connect(self.lineEdit_pre.setEnabled)
		self.radioButton_6.toggled.connect(self.lineEdit_suf.setEnabled)
		self.radioButton_6.toggled.connect(self.lineEdit.setEnabled)
		self.radioButton_1.toggled.connect(self.updateChunkFormat)
		self.radioButton_2.toggled.connect(self.updateChunkFormat)
		self.radioButton_3.toggled.connect(self.updateChunkFormat)
		self.radioButton_4.toggled.connect(self.updateChunkFormat)
		self.radioButton_5.toggled.connect(self.updateChunkFormat)
		self.radioButton_6.toggled.connect(self.updateChunkFormat)
		
		self.pushButton_close.setDefault(True)

		self.listChunkDefs()
		self.readIconsIni()
		self.selectChunkFormat()


		self.exec()

		# Dialog setup end

	def updateChunkFormat(self):
		selected_format = self.sender()
		
		if selected_format.isChecked():
			sel_name = selected_format.text()
			self.selFormat = str(sel_name).split(" ")[0].lower()
			self.selectChunkFormat()
		


	def selectChunkFormat(self):
		if self.selFormat == "metashape":
			self.radioButton_1.setChecked(True)
		elif self.selFormat == "data":
			self.radioButton_2.setChecked(True)
		elif self.selFormat == "point":
			self.radioButton_3.setChecked(True)
		elif self.selFormat == "creation":
			self.radioButton_4.setChecked(True)
		elif self.selFormat == "image":
			self.radioButton_5.setChecked(True)
		elif self.selFormat == "custom":
			self.radioButton_6.setChecked(True)
		

	def listChunkDefs(self):
		self.lineEdit_wfolder.setText(ftgMain.selected_data_folder)
		self.pushButton_save.setDisabled(True)
		self.pushButton_sremove.setEnabled(True)
		self.listWidgetChunkDefs.clear()
		for section in ftgMain.chunk_sections:
			menu_icon = ftgMain.menuCfg.get(section, "menu_icon")
			menu_icon_path = u":/icons/" + ftgMain.icoCfg.get("ICONS", menu_icon)
			seticon = QIcon()
			seticon.addFile(menu_icon_path, QSize(), QIcon.Normal, QIcon.Off)
			self.qlistwidgetitem = QListWidgetItem(self.listWidgetChunkDefs)
			self.qlistwidgetitem.setText(section)
			self.qlistwidgetitem.setIcon(seticon)


	def readIconsIni(self):
		ico_count = 0
		for iconitem in ftgMain.icons_list:
			aicon_name = "ico-" + str(ico_count)
			aicon_path = u":/icons/" + ftgMain.icoCfg.get("ICONS", iconitem)
			aicon = QIcon()
			aicon.addFile(aicon_path, QSize(), QIcon.Normal, QIcon.Off)
			self.comboBox_icon.addItem(aicon, aicon_name)
			ico_count += 1


	def editSelectedItem(self):
		selected_item = self.listWidgetChunkDefs.currentItem().text()
		self.lineEdit_name.setText(selected_item)
		self.comboBox_icon.setCurrentText(str(ftgMain.menuCfg.get(selected_item, "menu_icon")))
		self.selFormat = str(ftgMain.menuCfg.get(selected_item, "chunk_name_format"))
		self.selectChunkFormat()
		self.lineEdit_wfolder.setText(str(ftgMain.menuCfg.get(selected_item, "work_folder")))
		self.lineEdit_efolder.setText(str(ftgMain.menuCfg.get(selected_item, "export_folder")))
		self.lineEdit_pre.setText(str(ftgMain.menuCfg.get(selected_item, "chunk_name_prefix")))
		self.lineEdit_suf.setText(str(ftgMain.menuCfg.get(selected_item, "chunk_name_suffix")))
		self.lineEdit_name.setDisabled(True)
		self.listWidgetChunkDefs.setDisabled(True)
		self.pushButton_sedit.setDisabled(True)
		self.pushButton_sremove.setDisabled(True)
		self.pushButton_save.setEnabled(True)
		self.pushButton_add.setText(u"Cancel")
		abanicon = QIcon()
		abanicon.addFile(u":/icons/icons8-unavailable-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_add.setIcon(abanicon)
		self.btnAction = False
		
	
	def removeSelectedItem(self):
		selected_item = self.listWidgetChunkDefs.currentItem().text()
		confirm_remove = Metashape.app.getBool("Remove (" + selected_item + ")?")
		
		if confirm_remove == True:
			self.backupSettings()
			ftgMain.menuCfg.remove_section(selected_item)
			
			with open(ftgMain.menuCfgFilePath, 'w') as menuconfig:
				ftgMain.menuCfg.write(menuconfig)

			self.lineEdit_name.clear
			self.comboBox_icon.setCurrentIndex(0)
			self.lineEdit_wfolder.clear
			self.lineEdit_efolder.clear
			self.lineEdit_pre.clear
			self.lineEdit_suf.clear
			self.pushButton_sedit.setEnabled(True)
			self.pushButton_save.setDisabled(True)
			self.pushButton_add.setEnabled(True)
			self.lineEdit_name.setEnabled(True)
			self.listWidgetChunkDefs.takeItem(self.listWidgetChunkDefs.currentRow())
			print("Chunk definition removed from settings...\nRemoved: " + str(selected_item) + "\n")


	def saveSelectedItem(self):
		edit_section = self.lineEdit_name.text()
		ftgMain.menuCfg.set(edit_section, "menu_icon", self.comboBox_icon.currentText())
		ftgMain.menuCfg.set(edit_section, "chunk_name_format", self.selFormat)
		ftgMain.menuCfg.set(edit_section, "chunk_name_prefix", self.lineEdit_pre.text())
		ftgMain.menuCfg.set(edit_section, "chunk_name_suffix", self.lineEdit_suf.text())
		ftgMain.menuCfg.set(edit_section, "work_folder", self.lineEdit_wfolder.text())
		ftgMain.menuCfg.set(edit_section, "export_folder", self.lineEdit_efolder.text())
		
		with open(ftgMain.menuCfgFilePath, 'w') as menuconfig:
			ftgMain.menuCfg.write(menuconfig)
		
		ftgMain.chunksCfgLoad()
		
		self.listWidgetChunkDefs.setEnabled(True)
		self.lineEdit_name.setEnabled(True)
		self.lineEdit_name.clear()
		self.lineEdit_wfolder.clear()
		self.lineEdit_efolder.clear()
		self.lineEdit_pre.clear()
		self.lineEdit_suf.clear()
		self.comboBox_icon.setCurrentIndex(0)
		self.pushButton_save.setDisabled(True)
		self.pushButton_sedit.setEnabled(True)
		self.pushButton_add.setEnabled(True)
		self.pushButton_add.setText(u"Add New")
		addicon = QIcon()
		addicon.addFile(u":/icons/icons8-add-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_add.setIcon(addicon)
		self.pushButton_add_action = False
		self.btnAction = True
		print("Chunk definition updated...\nUpdated: " + str(edit_section) + "\n")
		self.selFormat = str("metashape")
		self.selectChunkFormat()
		self.listChunkDefs()


	def addBtnAction(self):
		if self.btnAction == True:
			self.backupSettings()
			new_section = self.lineEdit_name.text()
			ftgMain.menuCfg.add_section(new_section)
			ftgMain.menuCfg.set(new_section, "menu_icon", self.comboBox_icon.currentText())
			ftgMain.menuCfg.set(new_section, "chunk_name_format", self.selFormat)
			ftgMain.menuCfg.set(new_section, "chunk_name_prefix", self.lineEdit_pre.text())
			ftgMain.menuCfg.set(new_section, "chunk_name_suffix", self.lineEdit_suf.text())
			ftgMain.menuCfg.set(new_section, "work_folder", self.lineEdit_wfolder.text())
			ftgMain.menuCfg.set(new_section, "export_folder", self.lineEdit_efolder.text())
			
			with open(ftgMain.menuCfgFilePath, 'w') as menuconfig:
				ftgMain.menuCfg.write(menuconfig)
			
			ftgMain.chunksCfgLoad()
			
			self.listWidgetChunkDefs.setEnabled(True)
			self.lineEdit_name.clear()
			self.lineEdit_wfolder.clear()
			self.lineEdit_efolder.clear()
			self.lineEdit_pre.clear()
			self.lineEdit_suf.clear()
			self.comboBox_icon.setCurrentIndex(0)
			self.pushButton_save.setDisabled(True)
			print("New chunk definition added...\nAdded: " + str(new_section) + "\n")
			self.btnAction = True
			self.selFormat = str("metashape")
			self.selectChunkFormat()
			self.listChunkDefs()

		else:
			self.listWidgetChunkDefs.setEnabled(True)
			self.pushButton_sedit.setEnabled(True)
			self.lineEdit_name.setEnabled(True)
			self.pushButton_save.setEnabled(True)
			self.pushButton_add.setText(u"Add New")
			addicon = QIcon()
			addicon.addFile(u":/icons/icons8-add-50.png", QSize(), QIcon.Normal, QIcon.Off)
			self.pushButton_add.setIcon(addicon)
			self.pushButton_add_action = False
			self.lineEdit_name.clear()
			self.lineEdit_wfolder.clear()
			self.lineEdit_efolder.clear()
			self.lineEdit_pre.clear()
			self.lineEdit_suf.clear()
			self.comboBox_icon.setCurrentIndex(0)
			print("Aborted editing chunk definition...")
			self.btnAction = True
			self.selFormat = str("metashape")
			self.selectChunkFormat()
			self.listChunkDefs()


	def backupSettings(self):
		menuCfgFileBackup = "settings_newchunk.old"
		menuCfgFileBackupPath =  ftgMain.menuCfgPath + "/" + menuCfgFileBackup
		shutil.copy2(ftgMain.menuCfgFilePath, menuCfgFileBackupPath)
		print("Creating backup of chunk definitions...\nBackup file: " + str(menuCfgFileBackup) + "\n")


	def selectWorkFolder(self):
		if self.lineEdit_wfolder.text() == "" or self.lineEdit_wfolder.text() ==  None:
			sel_folder = Metashape.app.getExistingDirectory("Choose Work Folder", ftgMain.selected_data_folder)
		else:
			cur_folder = self.lineEdit_wfolder.text()
			sel_folder = Metashape.app.getExistingDirectory("Choose Work Folder", cur_folder)
		
		if sel_folder == "":
			self.lineEdit_wfolder.setText(str(cur_folder))
			print("Work folder not changed!")
		else:
			self.lineEdit_wfolder.setText(str(sel_folder))
			print("Work folder location selected!")


	def selectExportFolder(self):
		if self.lineEdit_efolder.text() == "" or self.lineEdit_efolder.text() ==  None:
			sel_folder = Metashape.app.getExistingDirectory("Choose Export Folder", ftgMain.selected_data_folder)
		else:
			cur_folder = self.lineEdit_efolder.text()
			sel_folder = Metashape.app.getExistingDirectory("Choose Export Folder", cur_folder)
		
		if sel_folder == "":
			self.lineEdit_efolder.setText(str(cur_folder))
			print("Export folder not changed!")
		else:
			self.lineEdit_efolder.setText(str(sel_folder))
			print("Export folder location selected!")

