# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diaAddNewChunkBatch.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import qtresources_rc

class Ui_DialogBatchChunk(object):
	def setupUi(self, DialogBatchChunk):
		if not DialogBatchChunk.objectName():
			DialogBatchChunk.setObjectName(u"DialogBatchChunk")
		DialogBatchChunk.resize(870, 750)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(DialogBatchChunk.sizePolicy().hasHeightForWidth())
		DialogBatchChunk.setSizePolicy(sizePolicy)
		DialogBatchChunk.setMinimumSize(QSize(870, 750))
		DialogBatchChunk.setMaximumSize(QSize(900, 800))
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(9)
		DialogBatchChunk.setFont(font)
		DialogBatchChunk.setWindowTitle(u"Batch Chunk Creator")
		icon = QIcon()
		icon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		DialogBatchChunk.setWindowIcon(icon)
		self.verticalLayoutWidget = QWidget(DialogBatchChunk)
		self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
		self.verticalLayoutWidget.setGeometry(QRect(10, 10, 851, 732))
		self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setSpacing(5)
		self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_2.setObjectName(u"verticalLayout_2")
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_9 = QHBoxLayout()
		self.horizontalLayout_9.setSpacing(5)
		self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
		self.label_15 = QLabel(self.verticalLayoutWidget)
		self.label_15.setObjectName(u"label_15")
		sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
		sizePolicy1.setHorizontalStretch(0)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
		self.label_15.setSizePolicy(sizePolicy1)
		self.label_15.setMaximumSize(QSize(32, 32))
		self.label_15.setPixmap(QPixmap(u":/icons/icons8-apps-tab-50.png"))
		self.label_15.setScaledContents(True)

		self.horizontalLayout_9.addWidget(self.label_15)

		self.label_3 = QLabel(self.verticalLayoutWidget)
		self.label_3.setObjectName(u"label_3")
		sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		sizePolicy2.setHorizontalStretch(0)
		sizePolicy2.setVerticalStretch(0)
		sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
		self.label_3.setSizePolicy(sizePolicy2)
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
		self.line_4.setFrameShadow(QFrame.Plain)
		self.line_4.setFrameShape(QFrame.HLine)

		self.verticalLayout_2.addWidget(self.line_4)

		self.gridLayout = QGridLayout()
		self.gridLayout.setSpacing(5)
		self.gridLayout.setObjectName(u"gridLayout")
		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setSpacing(5)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.lineEdit = QLineEdit(self.verticalLayoutWidget)
		self.lineEdit.setObjectName(u"lineEdit")
		self.lineEdit.setEnabled(False)
		sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		sizePolicy3.setHorizontalStretch(0)
		sizePolicy3.setVerticalStretch(0)
		sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
		self.lineEdit.setSizePolicy(sizePolicy3)
		font2 = QFont()
		font2.setFamily(u"Segoe UI")
		font2.setPointSize(10)
		self.lineEdit.setFont(font2)
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
		sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
		sizePolicy4.setHorizontalStretch(0)
		sizePolicy4.setVerticalStretch(0)
		sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
		self.pushButton.setSizePolicy(sizePolicy4)
		self.pushButton.setMinimumSize(QSize(0, 30))
		self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.pushButton.setStatusTip(u"Data location (root folder with sub-folders containing data)")
#endif // QT_CONFIG(statustip)
		self.pushButton.setText(u"Browse")
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons8-browse-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton.setIcon(icon1)
		self.pushButton.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton)

		self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_4.setObjectName(u"pushButton_4")
		sizePolicy4.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
		self.pushButton_4.setSizePolicy(sizePolicy4)
		self.pushButton_4.setMinimumSize(QSize(0, 30))
		self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_4.setText(u"Refresh")
		icon2 = QIcon()
		icon2.addFile(u":/icons/icons8-available-updates-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_4.setIcon(icon2)
		self.pushButton_4.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton_4)


		self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

		self.gridLayout_3 = QGridLayout()
		self.gridLayout_3.setSpacing(5)
		self.gridLayout_3.setObjectName(u"gridLayout_3")
		self.horizontalLayout_13 = QHBoxLayout()
		self.horizontalLayout_13.setSpacing(5)
		self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
		self.checkBox_align_2 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_align_2.setObjectName(u"checkBox_align_2")
		self.checkBox_align_2.setEnabled(True)
		sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy5.setHorizontalStretch(0)
		sizePolicy5.setVerticalStretch(0)
		sizePolicy5.setHeightForWidth(self.checkBox_align_2.sizePolicy().hasHeightForWidth())
		self.checkBox_align_2.setSizePolicy(sizePolicy5)
		self.checkBox_align_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_align_2.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Build Mesh and Textures</p><p><span style=\" font-weight:600;\">Disabled:</span> Skip...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_align_2.setText(u"Build Mesh && Textures")
		icon3 = QIcon()
		icon3.addFile(u":/icons/icons8-national-park-48.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_align_2.setIcon(icon3)
		self.checkBox_align_2.setIconSize(QSize(21, 21))
		self.checkBox_align_2.setCheckable(True)
		self.checkBox_align_2.setChecked(False)
		self.checkBox_align_2.setTristate(False)

		self.horizontalLayout_13.addWidget(self.checkBox_align_2)

		self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_6.setObjectName(u"pushButton_6")
		self.pushButton_6.setEnabled(False)
		sizePolicy4.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
		self.pushButton_6.setSizePolicy(sizePolicy4)
		self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
		icon4 = QIcon()
		icon4.addFile(u":/icons/icons8-adjust-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_6.setIcon(icon4)
		self.pushButton_6.setFlat(True)

		self.horizontalLayout_13.addWidget(self.pushButton_6)


		self.gridLayout_3.addLayout(self.horizontalLayout_13, 20, 0, 1, 1)

		self.horizontalLayout_15 = QHBoxLayout()
		self.horizontalLayout_15.setSpacing(5)
		self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
		self.checkBox_align_3 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_align_3.setObjectName(u"checkBox_align_3")
		self.checkBox_align_3.setEnabled(True)
		sizePolicy5.setHeightForWidth(self.checkBox_align_3.sizePolicy().hasHeightForWidth())
		self.checkBox_align_3.setSizePolicy(sizePolicy5)
		self.checkBox_align_3.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_align_3.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Export selected data after build is complete.</p><p><span style=\" font-weight:600;\">Disabled:</span> Skip...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_align_3.setText(u"Data Export")
		icon5 = QIcon()
		icon5.addFile(u":/icons/icons8-share-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_align_3.setIcon(icon5)
		self.checkBox_align_3.setIconSize(QSize(21, 21))
		self.checkBox_align_3.setCheckable(True)
		self.checkBox_align_3.setChecked(False)
		self.checkBox_align_3.setTristate(False)

		self.horizontalLayout_15.addWidget(self.checkBox_align_3)

		self.pushButton_8 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_8.setObjectName(u"pushButton_8")
		self.pushButton_8.setEnabled(False)
		sizePolicy4.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
		self.pushButton_8.setSizePolicy(sizePolicy4)
		self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
		icon6 = QIcon()
		icon6.addFile(u":/icons/icons8-true-false-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_8.setIcon(icon6)
		self.pushButton_8.setFlat(True)

		self.horizontalLayout_15.addWidget(self.pushButton_8)


		self.gridLayout_3.addLayout(self.horizontalLayout_15, 23, 0, 1, 1)

		self.horizontalLayout_16 = QHBoxLayout()
		self.horizontalLayout_16.setSpacing(5)
		self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
		self.checkBox_align_4 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_align_4.setObjectName(u"checkBox_align_4")
		self.checkBox_align_4.setEnabled(True)
		sizePolicy5.setHeightForWidth(self.checkBox_align_4.sizePolicy().hasHeightForWidth())
		self.checkBox_align_4.setSizePolicy(sizePolicy5)
		self.checkBox_align_4.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_align_4.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Build Point Cloud</p><p><span style=\" font-weight:600;\">Disabled:</span> Skip...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_align_4.setText(u"Build Point Cloud")
		icon7 = QIcon()
		icon7.addFile(u":/icons/icons8-live-photos-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_align_4.setIcon(icon7)
		self.checkBox_align_4.setIconSize(QSize(21, 21))
		self.checkBox_align_4.setCheckable(True)
		self.checkBox_align_4.setChecked(False)
		self.checkBox_align_4.setTristate(False)

		self.horizontalLayout_16.addWidget(self.checkBox_align_4)

		self.pushButton_9 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_9.setObjectName(u"pushButton_9")
		self.pushButton_9.setEnabled(False)
		sizePolicy4.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
		self.pushButton_9.setSizePolicy(sizePolicy4)
		self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_9.setIcon(icon4)
		self.pushButton_9.setFlat(True)

		self.horizontalLayout_16.addWidget(self.pushButton_9)


		self.gridLayout_3.addLayout(self.horizontalLayout_16, 21, 0, 1, 1)

		self.line_3 = QFrame(self.verticalLayoutWidget)
		self.line_3.setObjectName(u"line_3")
		self.line_3.setFrameShadow(QFrame.Plain)
		self.line_3.setFrameShape(QFrame.HLine)

		self.gridLayout_3.addWidget(self.line_3, 11, 0, 1, 1)

		self.label_17 = QLabel(self.verticalLayoutWidget)
		self.label_17.setObjectName(u"label_17")
		sizePolicy5.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
		self.label_17.setSizePolicy(sizePolicy5)
		self.label_17.setMaximumSize(QSize(16777215, 24))
		font3 = QFont()
		font3.setFamily(u"Segoe UI")
		font3.setPointSize(11)
		font3.setBold(True)
		font3.setWeight(75)
		self.label_17.setFont(font3)
		self.label_17.setFrameShape(QFrame.NoFrame)
		self.label_17.setText(u"Processing")
		self.label_17.setIndent(10)

		self.gridLayout_3.addWidget(self.label_17, 16, 0, 1, 1)

		self.line_5 = QFrame(self.verticalLayoutWidget)
		self.line_5.setObjectName(u"line_5")
		self.line_5.setFrameShadow(QFrame.Plain)
		self.line_5.setFrameShape(QFrame.HLine)

		self.gridLayout_3.addWidget(self.line_5, 6, 0, 1, 1)

		self.label_4 = QLabel(self.verticalLayoutWidget)
		self.label_4.setObjectName(u"label_4")
		sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
		self.label_4.setSizePolicy(sizePolicy5)
		self.label_4.setMaximumSize(QSize(16777215, 24))
		self.label_4.setFont(font3)
		self.label_4.setFrameShape(QFrame.NoFrame)
		self.label_4.setText(u"Camera")
		self.label_4.setIndent(10)

		self.gridLayout_3.addWidget(self.label_4, 7, 0, 1, 1)

		self.label = QLabel(self.verticalLayoutWidget)
		self.label.setObjectName(u"label")
		sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy5)
		self.label.setMaximumSize(QSize(16777215, 24))
		self.label.setFont(font3)
		self.label.setFrameShape(QFrame.NoFrame)
		self.label.setText(u"Chunk Creation")
		self.label.setIndent(10)

		self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

		self.horizontalLayout_14 = QHBoxLayout()
		self.horizontalLayout_14.setSpacing(5)
		self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
		self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_3.setObjectName(u"checkBox_3")
		sizePolicy5.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
		self.checkBox_3.setSizePolicy(sizePolicy5)
		self.checkBox_3.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_3.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Automatic chunk creation with predefined settings</p><p><span style=\" font-weight:600;\">Disabled:</span> Manual confirmation of intermediate steps</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_3.setText(u"Auto Import Processing")
		icon8 = QIcon()
		icon8.addFile(u":/icons/icons8-in-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_3.setIcon(icon8)
		self.checkBox_3.setIconSize(QSize(21, 21))
		self.checkBox_3.setCheckable(True)
		self.checkBox_3.setChecked(True)

		self.horizontalLayout_14.addWidget(self.checkBox_3)

		self.pushButton_7 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_7.setObjectName(u"pushButton_7")
		sizePolicy4.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
		self.pushButton_7.setSizePolicy(sizePolicy4)
		self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
		icon9 = QIcon()
		icon9.addFile(u":/icons/icons8-support-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_7.setIcon(icon9)
		self.pushButton_7.setFlat(True)

		self.horizontalLayout_14.addWidget(self.pushButton_7)


		self.gridLayout_3.addLayout(self.horizontalLayout_14, 17, 0, 1, 1)

		self.line_2 = QFrame(self.verticalLayoutWidget)
		self.line_2.setObjectName(u"line_2")
		self.line_2.setFrameShadow(QFrame.Plain)
		self.line_2.setFrameShape(QFrame.HLine)

		self.gridLayout_3.addWidget(self.line_2, 15, 0, 1, 1)

		self.checkBox = QCheckBox(self.verticalLayoutWidget)
		self.checkBox.setObjectName(u"checkBox")
		sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
		sizePolicy6.setHorizontalStretch(0)
		sizePolicy6.setVerticalStretch(0)
		sizePolicy6.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
		self.checkBox.setSizePolicy(sizePolicy6)
		self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Marker coordinates will be imported after target detection. <span style=\" font-weight:600;\">*</span></p><p><span style=\" font-weight:600;\">Disabled:</span> Coordinates are not imported. User must manually import coordinates.</p><p><span style=\" font-weight:600;\">*</span> Automatic importing of marker coordinates only works if point file name is the same as it's parent folder name, and contains a header with metadata. Point coordinates should start at row #7.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox.setText(u"Import Marker Coordinates")
		icon10 = QIcon()
		icon10.addFile(u":/icons/icons8-map-marker-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox.setIcon(icon10)
		self.checkBox.setIconSize(QSize(21, 21))
		self.checkBox.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox, 14, 0, 1, 1)

		self.horizontalLayout_7 = QHBoxLayout()
		self.horizontalLayout_7.setSpacing(5)
		self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
		self.label_13 = QLabel(self.verticalLayoutWidget)
		self.label_13.setObjectName(u"label_13")
		sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
		self.label_13.setSizePolicy(sizePolicy1)
		font4 = QFont()
		font4.setFamily(u"Segoe UI")
		font4.setPointSize(9)
		font4.setBold(False)
		font4.setWeight(50)
		self.label_13.setFont(font4)
		self.label_13.setText(u"SubType")

		self.horizontalLayout_7.addWidget(self.label_13)

		self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

		self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

		self.label_14 = QLabel(self.verticalLayoutWidget)
		self.label_14.setObjectName(u"label_14")
		sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
		sizePolicy7.setHorizontalStretch(0)
		sizePolicy7.setVerticalStretch(0)
		sizePolicy7.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
		self.label_14.setSizePolicy(sizePolicy7)
		self.label_14.setMinimumSize(QSize(180, 0))
		self.label_14.setMaximumSize(QSize(180, 16777215))
		font5 = QFont()
		font5.setFamily(u"Segoe UI")
		font5.setPointSize(8)
		self.label_14.setFont(font5)
		self.label_14.setFrameShape(QFrame.StyledPanel)
		self.label_14.setText(u"")

		self.horizontalLayout_7.addWidget(self.label_14)


		self.gridLayout_3.addLayout(self.horizontalLayout_7, 10, 0, 1, 1)

		self.horizontalLayout_3 = QHBoxLayout()
		self.horizontalLayout_3.setSpacing(5)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.label_10 = QLabel(self.verticalLayoutWidget)
		self.label_10.setObjectName(u"label_10")
		sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
		sizePolicy8.setHorizontalStretch(0)
		sizePolicy8.setVerticalStretch(0)
		sizePolicy8.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
		self.label_10.setSizePolicy(sizePolicy8)
		self.label_10.setFont(font4)
		self.label_10.setText(u"Suffix")

		self.horizontalLayout_3.addWidget(self.label_10)

		self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

		self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

		self.label_7 = QLabel(self.verticalLayoutWidget)
		self.label_7.setObjectName(u"label_7")
		sizePolicy7.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
		self.label_7.setSizePolicy(sizePolicy7)
		self.label_7.setMinimumSize(QSize(180, 0))
		self.label_7.setMaximumSize(QSize(180, 16777215))
		self.label_7.setFont(font5)
		self.label_7.setFrameShape(QFrame.StyledPanel)
		self.label_7.setText(u"")

		self.horizontalLayout_3.addWidget(self.label_7)


		self.gridLayout_3.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

		self.horizontalLayout_12 = QHBoxLayout()
		self.horizontalLayout_12.setSpacing(5)
		self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
		self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
		icon11 = QIcon()
		icon11.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon11, u"Cam 1")
		icon12 = QIcon()
		icon12.addFile(u":/icons/icons8-video-wall-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon12, u"Cam 2")
		self.comboBox_2.addItem(icon7, u"Cam 3")
		icon13 = QIcon()
		icon13.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon13, u"Cam 4")
		icon14 = QIcon()
		icon14.addFile(u":/icons/icons8-video-stabilization-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon14, u"Cam 5")
		icon15 = QIcon()
		icon15.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon15, u"Cam 6")
		self.comboBox_2.setObjectName(u"comboBox_2")
		sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
		sizePolicy9.setHorizontalStretch(0)
		sizePolicy9.setVerticalStretch(0)
		sizePolicy9.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
		self.comboBox_2.setSizePolicy(sizePolicy9)
		self.comboBox_2.setMinimumSize(QSize(200, 0))
		self.comboBox_2.setFont(font2)
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
		icon16 = QIcon()
		icon16.addFile(u":/icons/icons8-christmas-star-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.btnDefCam.setIcon(icon16)
		self.btnDefCam.setIconSize(QSize(20, 20))
		self.btnDefCam.setAutoDefault(False)
		self.btnDefCam.setFlat(True)

		self.horizontalLayout_12.addWidget(self.btnDefCam)


		self.gridLayout_3.addLayout(self.horizontalLayout_12, 8, 0, 1, 1)

		self.line_6 = QFrame(self.verticalLayoutWidget)
		self.line_6.setObjectName(u"line_6")
		self.line_6.setFrameShape(QFrame.HLine)
		self.line_6.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line_6, 18, 0, 1, 1)

		self.label_5 = QLabel(self.verticalLayoutWidget)
		self.label_5.setObjectName(u"label_5")
		sizePolicy5.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
		self.label_5.setSizePolicy(sizePolicy5)
		self.label_5.setMaximumSize(QSize(16777215, 24))
		self.label_5.setFont(font3)
		self.label_5.setFrameShape(QFrame.NoFrame)
		self.label_5.setText(u"Markers")
		self.label_5.setIndent(10)

		self.gridLayout_3.addWidget(self.label_5, 12, 0, 1, 1)

		self.horizontalLayout_10 = QHBoxLayout()
		self.horizontalLayout_10.setSpacing(5)
		self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
		self.label_18 = QLabel(self.verticalLayoutWidget)
		self.label_18.setObjectName(u"label_18")
		sizePolicy8.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
		self.label_18.setSizePolicy(sizePolicy8)
		self.label_18.setFont(font4)
		self.label_18.setText(u"Name Format")

		self.horizontalLayout_10.addWidget(self.label_18)

		self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

		self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

		self.label_19 = QLabel(self.verticalLayoutWidget)
		self.label_19.setObjectName(u"label_19")
		sizePolicy7.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
		self.label_19.setSizePolicy(sizePolicy7)
		self.label_19.setMinimumSize(QSize(180, 0))
		self.label_19.setMaximumSize(QSize(180, 16777215))
		self.label_19.setFont(font5)
		self.label_19.setFrameShape(QFrame.StyledPanel)
		self.label_19.setText(u"")

		self.horizontalLayout_10.addWidget(self.label_19)


		self.gridLayout_3.addLayout(self.horizontalLayout_10, 5, 0, 1, 1)

		self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

		self.gridLayout_3.addItem(self.verticalSpacer, 24, 0, 1, 1)

		self.horizontalLayout_11 = QHBoxLayout()
		self.horizontalLayout_11.setSpacing(5)
		self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
		self.checkBox_align = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_align.setObjectName(u"checkBox_align")
		self.checkBox_align.setEnabled(True)
		sizePolicy5.setHeightForWidth(self.checkBox_align.sizePolicy().hasHeightForWidth())
		self.checkBox_align.setSizePolicy(sizePolicy5)
		self.checkBox_align.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_align.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Align Photos after import.</p><p><span style=\" font-weight:600;\">Disabled:</span> Skip...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_align.setText(u"Align Photos")
		icon17 = QIcon()
		icon17.addFile(u":/icons/icons8-bursts-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_align.setIcon(icon17)
		self.checkBox_align.setIconSize(QSize(21, 21))
		self.checkBox_align.setCheckable(True)
		self.checkBox_align.setChecked(False)
		self.checkBox_align.setTristate(False)

		self.horizontalLayout_11.addWidget(self.checkBox_align)

		self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_5.setObjectName(u"pushButton_5")
		self.pushButton_5.setEnabled(False)
		sizePolicy4.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
		self.pushButton_5.setSizePolicy(sizePolicy4)
		self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_5.setIcon(icon4)
		self.pushButton_5.setFlat(True)

		self.horizontalLayout_11.addWidget(self.pushButton_5)


		self.gridLayout_3.addLayout(self.horizontalLayout_11, 19, 0, 1, 1)

		self.horizontalLayout_5 = QHBoxLayout()
		self.horizontalLayout_5.setSpacing(5)
		self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
		self.label_11 = QLabel(self.verticalLayoutWidget)
		self.label_11.setObjectName(u"label_11")
		sizePolicy8.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
		self.label_11.setSizePolicy(sizePolicy8)
		self.label_11.setFont(font4)
		self.label_11.setText(u"Prefix")

		self.horizontalLayout_5.addWidget(self.label_11)

		self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

		self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

		self.label_6 = QLabel(self.verticalLayoutWidget)
		self.label_6.setObjectName(u"label_6")
		sizePolicy7.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
		self.label_6.setSizePolicy(sizePolicy7)
		self.label_6.setMinimumSize(QSize(180, 0))
		self.label_6.setMaximumSize(QSize(180, 16777215))
		self.label_6.setFont(font5)
		self.label_6.setFrameShape(QFrame.StyledPanel)
		self.label_6.setText(u"")

		self.horizontalLayout_5.addWidget(self.label_6)


		self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)

		self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_2.setObjectName(u"checkBox_2")
		sizePolicy6.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
		self.checkBox_2.setSizePolicy(sizePolicy6)
		self.checkBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_2.setToolTip(u"<html><head/><body><p>Enable automatic target detection when new chunk is created...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_2.setText(u"Automatic Target Detection")
		icon18 = QIcon()
		icon18.addFile(u":/icons/icons8-my-location-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_2.setIcon(icon18)
		self.checkBox_2.setIconSize(QSize(21, 21))
		self.checkBox_2.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox_2, 13, 0, 1, 1)

		self.horizontalLayout_8 = QHBoxLayout()
		self.horizontalLayout_8.setSpacing(5)
		self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
		self.cbChunkSettings = QComboBox(self.verticalLayoutWidget)
		icon19 = QIcon()
		icon19.addFile(u":/icons/icons8-add-tab-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbChunkSettings.addItem(icon19, u"Default")
		icon20 = QIcon()
		icon20.addFile(u":/icons/kalota_m.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbChunkSettings.addItem(icon20, u"KALOTA")
		icon21 = QIcon()
		icon21.addFile(u":/icons/stopnca_o.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbChunkSettings.addItem(icon21, u"STOPNICA - IZKOP")
		icon22 = QIcon()
		icon22.addFile(u":/icons/stopnca_s.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbChunkSettings.addItem(icon22, u"STOPNICA - B.BET.")
		self.cbChunkSettings.setObjectName(u"cbChunkSettings")
		sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
		sizePolicy10.setHorizontalStretch(0)
		sizePolicy10.setVerticalStretch(0)
		sizePolicy10.setHeightForWidth(self.cbChunkSettings.sizePolicy().hasHeightForWidth())
		self.cbChunkSettings.setSizePolicy(sizePolicy10)
		self.cbChunkSettings.setMinimumSize(QSize(200, 0))
		self.cbChunkSettings.setFont(font2)
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
		self.btnDefChunk.setIcon(icon16)
		self.btnDefChunk.setIconSize(QSize(20, 20))
		self.btnDefChunk.setAutoDefault(False)
		self.btnDefChunk.setFlat(True)

		self.horizontalLayout_8.addWidget(self.btnDefChunk)


		self.gridLayout_3.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

		self.horizontalLayout_6 = QHBoxLayout()
		self.horizontalLayout_6.setSpacing(5)
		self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
		self.label_9 = QLabel(self.verticalLayoutWidget)
		self.label_9.setObjectName(u"label_9")
		sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
		self.label_9.setSizePolicy(sizePolicy1)
		self.label_9.setFont(font4)
		self.label_9.setFrameShape(QFrame.NoFrame)
		self.label_9.setText(u"Type")

		self.horizontalLayout_6.addWidget(self.label_9)

		self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

		self.horizontalLayout_6.addItem(self.horizontalSpacer)

		self.label_12 = QLabel(self.verticalLayoutWidget)
		self.label_12.setObjectName(u"label_12")
		sizePolicy7.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
		self.label_12.setSizePolicy(sizePolicy7)
		self.label_12.setMinimumSize(QSize(180, 0))
		self.label_12.setMaximumSize(QSize(180, 16777215))
		self.label_12.setFont(font5)
		self.label_12.setFrameShape(QFrame.StyledPanel)
		self.label_12.setText(u"")

		self.horizontalLayout_6.addWidget(self.label_12)


		self.gridLayout_3.addLayout(self.horizontalLayout_6, 9, 0, 1, 1)

		self.line_7 = QFrame(self.verticalLayoutWidget)
		self.line_7.setObjectName(u"line_7")
		self.line_7.setFrameShape(QFrame.HLine)
		self.line_7.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line_7, 22, 0, 1, 1)


		self.gridLayout.addLayout(self.gridLayout_3, 0, 2, 3, 1)

		self.label_16 = QLabel(self.verticalLayoutWidget)
		self.label_16.setObjectName(u"label_16")
		self.label_16.setFont(font2)
		self.label_16.setFrameShape(QFrame.NoFrame)
		self.label_16.setText(u"<html><head/><body><p>Selected: <span style=\" font-weight:600;\">0</span></p></body></html>")

		self.gridLayout.addWidget(self.label_16, 3, 2, 1, 1)

		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setSpacing(5)
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.label_2 = QLabel(self.verticalLayoutWidget)
		self.label_2.setObjectName(u"label_2")
		sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
		sizePolicy11.setHorizontalStretch(0)
		sizePolicy11.setVerticalStretch(0)
		sizePolicy11.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
		self.label_2.setSizePolicy(sizePolicy11)
		self.label_2.setFont(font3)
		self.label_2.setText(u"Data Location")

		self.horizontalLayout_2.addWidget(self.label_2)

		self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_4.setObjectName(u"checkBox_4")
		sizePolicy4.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
		self.checkBox_4.setSizePolicy(sizePolicy4)
		self.checkBox_4.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.checkBox_4.setStatusTip(u"Disable to set custom location for data. Enable to use project default data location settings.")
#endif // QT_CONFIG(statustip)
		self.checkBox_4.setText(u"Use Project Data Location")
		icon23 = QIcon()
		icon23.addFile(u":/icons/icons8-copy-to-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_4.setIcon(icon23)
		self.checkBox_4.setIconSize(QSize(20, 20))
		self.checkBox_4.setChecked(True)

		self.horizontalLayout_2.addWidget(self.checkBox_4)


		self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

		self.label_8 = QLabel(self.verticalLayoutWidget)
		self.label_8.setObjectName(u"label_8")
		sizePolicy7.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
		self.label_8.setSizePolicy(sizePolicy7)
		font6 = QFont()
		font6.setFamily(u"Segoe UI")
		font6.setPointSize(10)
		font6.setBold(False)
		font6.setWeight(50)
		self.label_8.setFont(font6)
		self.label_8.setFrameShape(QFrame.NoFrame)
		self.label_8.setText(u"<html><head/><body><p><span style=\" font-weight:600;\">Ready... </span>Select folder(s) to process.</p></body></html>")
		self.label_8.setIndent(10)

		self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

		self.treeWidget = QTreeWidget(self.verticalLayoutWidget)
		font7 = QFont()
		font7.setBold(True)
		font7.setWeight(75)
		icon24 = QIcon()
		icon24.addFile(u":/icons/icons8-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon25 = QIcon()
		icon25.addFile(u":/icons/icons8-map-pin-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon26 = QIcon()
		icon26.addFile(u":/icons/icons8-sd-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.treeWidget.headerItem().setText(3, "")
		self.treeWidget.headerItem().setText(4, "")
		icon27 = QIcon()
		icon27.addFile(u":/icons/icons8-country-48.png", QSize(), QIcon.Normal, QIcon.Off)
		self.treeWidget.headerItem().setText(5, "")
		self.treeWidget.headerItem().setText(6, "")
		self.treeWidget.headerItem().setText(7, "")
		__qtreewidgetitem = QTreeWidgetItem()
		__qtreewidgetitem.setIcon(7, icon7);
		__qtreewidgetitem.setIcon(6, icon12);
		__qtreewidgetitem.setIcon(5, icon27);
		__qtreewidgetitem.setIcon(4, icon17);
		__qtreewidgetitem.setTextAlignment(3, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem.setIcon(3, icon26);
		__qtreewidgetitem.setText(2, u"Points");
		__qtreewidgetitem.setTextAlignment(2, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem.setIcon(2, icon25);
		__qtreewidgetitem.setText(1, u"Images");
		__qtreewidgetitem.setTextAlignment(1, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem.setIcon(1, icon24);
		__qtreewidgetitem.setText(0, u"Folders");
		__qtreewidgetitem.setTextAlignment(0, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem.setFont(0, font7);
#if QT_CONFIG(tooltip)
		__qtreewidgetitem.setToolTip(7, u"Point Cloud");
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
		__qtreewidgetitem.setToolTip(5, u"Mesh Model");
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
		__qtreewidgetitem.setToolTip(3, u"Import Status");
#endif // QT_CONFIG(tooltip)
		self.treeWidget.setHeaderItem(__qtreewidgetitem)
		icon28 = QIcon()
		icon28.addFile(u":/icons/icons8-folder-tree-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon29 = QIcon()
		icon29.addFile(u":/icons/icons8-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon30 = QIcon()
		icon30.addFile(u":/icons/icons8-add-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon31 = QIcon()
		icon31.addFile(u":/icons/icons8-location-off-48.png", QSize(), QIcon.Normal, QIcon.Off)
		icon32 = QIcon()
		icon32.addFile(u":/icons/icons8-done-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon33 = QIcon()
		icon33.addFile(u":/icons/icons8-no-camera-96.png", QSize(), QIcon.Normal, QIcon.Off)
		icon34 = QIcon()
		icon34.addFile(u":/icons/icons8-error-48.png", QSize(), QIcon.Normal, QIcon.Off)
		font8 = QFont()
		font8.setFamily(u"Segoe UI")
		icon35 = QIcon()
		icon35.addFile(u":/icons/icons8-check-file-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon36 = QIcon()
		icon36.addFile(u":/icons/icons8-ok-50.png", QSize(), QIcon.Normal, QIcon.Off)
		__qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
		__qtreewidgetitem1.setText(0, u"root");
		__qtreewidgetitem1.setFont(0, font7);
		__qtreewidgetitem1.setIcon(0, icon28);
		__qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
		__qtreewidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
		__qtreewidgetitem2.setIcon(4, icon32);
		__qtreewidgetitem2.setIcon(3, icon32);
		__qtreewidgetitem2.setIcon(2, icon31);
		__qtreewidgetitem2.setIcon(1, icon30);
		__qtreewidgetitem2.setText(0, u"20230125-1010");
		__qtreewidgetitem2.setIcon(0, icon29);
		__qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem1)
		__qtreewidgetitem3.setFlags(Qt.NoItemFlags);
		__qtreewidgetitem3.setTextAlignment(3, Qt.AlignTrailing|Qt.AlignVCenter);
		__qtreewidgetitem3.setTextAlignment(2, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem3.setIcon(2, icon34);
		__qtreewidgetitem3.setTextAlignment(1, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem3.setIcon(1, icon33);
		__qtreewidgetitem3.setText(0, u"20230109-0530");
		__qtreewidgetitem3.setIcon(0, icon29);
		__qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem1)
		__qtreewidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
		__qtreewidgetitem4.setText(2, u"Found");
		__qtreewidgetitem4.setIcon(2, icon35);
		__qtreewidgetitem4.setText(1, u"20");
		__qtreewidgetitem4.setIcon(1, icon24);
		__qtreewidgetitem4.setText(0, u"20230109-0030");
		__qtreewidgetitem4.setFont(0, font8);
		__qtreewidgetitem4.setIcon(0, icon29);
		__qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem1)
		__qtreewidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
		__qtreewidgetitem5.setIcon(7, icon36);
		__qtreewidgetitem5.setIcon(6, icon36);
		__qtreewidgetitem5.setIcon(5, icon36);
		__qtreewidgetitem5.setIcon(4, icon32);
		__qtreewidgetitem5.setTextAlignment(3, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem5.setIcon(3, icon32);
		__qtreewidgetitem5.setText(2, u"3D: 0.0021");
		__qtreewidgetitem5.setIcon(2, icon18);
		__qtreewidgetitem5.setText(1, u"27");
		__qtreewidgetitem5.setIcon(1, icon30);
		__qtreewidgetitem5.setText(0, u"20230109-0010");
		__qtreewidgetitem5.setIcon(0, icon29);
		self.treeWidget.setObjectName(u"treeWidget")
		sizePolicy12 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
		sizePolicy12.setHorizontalStretch(0)
		sizePolicy12.setVerticalStretch(0)
		sizePolicy12.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
		self.treeWidget.setSizePolicy(sizePolicy12)
		self.treeWidget.setMinimumSize(QSize(550, 0))
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

		self.progressBar = QProgressBar(self.verticalLayoutWidget)
		self.progressBar.setObjectName(u"progressBar")
		self.progressBar.setEnabled(False)
		sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
		self.progressBar.setSizePolicy(sizePolicy3)
		self.progressBar.setMinimum(0)
		self.progressBar.setMaximum(10)
		self.progressBar.setValue(0)
		self.progressBar.setTextVisible(False)
		self.progressBar.setOrientation(Qt.Horizontal)
		self.progressBar.setTextDirection(QProgressBar.TopToBottom)

		self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 1)

		self.horizontalLayout_4 = QHBoxLayout()
		self.horizontalLayout_4.setSpacing(5)
		self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
		self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_3.setObjectName(u"pushButton_3")
		self.pushButton_3.setEnabled(False)
		sizePolicy5.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
		self.pushButton_3.setSizePolicy(sizePolicy5)
		self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.pushButton_3.setToolTip(u"Press [Ctrl+P] to start processing")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
		self.pushButton_3.setStatusTip(u"Process selected folders, and create new chunks...")
#endif // QT_CONFIG(statustip)
		self.pushButton_3.setText(u"Ready")
		icon37 = QIcon()
		icon37.addFile(u":/icons/icons8-submit-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
		icon37.addFile(u":/icons/icons8-ok-50.png", QSize(), QIcon.Disabled, QIcon.Off)
		self.pushButton_3.setIcon(icon37)
		self.pushButton_3.setIconSize(QSize(24, 24))
#if QT_CONFIG(shortcut)
		self.pushButton_3.setShortcut(u"P")
#endif // QT_CONFIG(shortcut)
		self.pushButton_3.setChecked(False)

		self.horizontalLayout_4.addWidget(self.pushButton_3)

		self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_2.setObjectName(u"pushButton_2")
		sizePolicy4.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
		self.pushButton_2.setSizePolicy(sizePolicy4)
		self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.pushButton_2.setStatusTip(u"Exit chunk creator...")
#endif // QT_CONFIG(statustip)
		self.pushButton_2.setText(u"Close")
		icon38 = QIcon()
		icon38.addFile(u":/icons/icons8-close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_2.setIcon(icon38)
		self.pushButton_2.setIconSize(QSize(24, 24))
#if QT_CONFIG(shortcut)
		self.pushButton_2.setShortcut(u"X")
#endif // QT_CONFIG(shortcut)

		self.horizontalLayout_4.addWidget(self.pushButton_2)


		self.gridLayout.addLayout(self.horizontalLayout_4, 4, 2, 1, 1)

		self.line = QFrame(self.verticalLayoutWidget)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.VLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.gridLayout.addWidget(self.line, 0, 1, 5, 1)


		self.verticalLayout_2.addLayout(self.gridLayout)


		self.retranslateUi(DialogBatchChunk)
		self.checkBox_4.toggled.connect(self.pushButton.setDisabled)
		self.checkBox_4.toggled.connect(self.lineEdit.setDisabled)
		self.checkBox_2.toggled.connect(self.checkBox.toggle)
		self.cbChunkSettings.currentTextChanged.connect(self.lineEdit.setText)
		self.lineEdit.textChanged.connect(self.treeWidget.doItemsLayout)
		self.treeWidget.itemSelectionChanged.connect(self.label_8.clear)
		self.pushButton_2.clicked.connect(DialogBatchChunk.reject)
		self.pushButton_3.clicked.connect(self.progressBar.reset)
		self.progressBar.valueChanged.connect(self.treeWidget.doItemsLayout)
		self.treeWidget.customContextMenuRequested.connect(self.pushButton_7.showMenu)
		self.checkBox_align.toggled.connect(self.pushButton_5.toggle)

		self.pushButton_3.setDefault(False)


		QMetaObject.connectSlotsByName(DialogBatchChunk)
	# setupUi

	def retranslateUi(self, DialogBatchChunk):
		self.pushButton_6.setText("")
		self.pushButton_8.setText("")
		self.pushButton_9.setText("")
		self.pushButton_7.setText("")

		self.pushButton_5.setText("")

#if QT_CONFIG(tooltip)
		___qtreewidgetitem = self.treeWidget.headerItem()
#endif
#if QT_CONFIG(tooltip)
		___qtreewidgetitem.setToolTip(6, QCoreApplication.translate("DialogBatchChunk", u"Textures", None));
#endif // QT_CONFIG(tooltip)

		__sortingEnabled = self.treeWidget.isSortingEnabled()
		self.treeWidget.setSortingEnabled(False)
		___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
		___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
		___qtreewidgetitem2.setText(2, QCoreApplication.translate("DialogBatchChunk", u"3D: -", None));
		___qtreewidgetitem2.setText(1, QCoreApplication.translate("DialogBatchChunk", u"21", None));
		___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
		___qtreewidgetitem3.setText(2, QCoreApplication.translate("DialogBatchChunk", u"Missing", None));
		self.treeWidget.setSortingEnabled(__sortingEnabled)

		pass
	# retranslateUi

	def rightClick(self, pos):
		rmenu = QMenu("", self.treeWidget)
		rmenuOpenFe = rmenu.addAction("Open in File Explorer", rmenu)
		action = rmenu.exec_(self.mapToGlobal(pos))

		if action ==rmenuOpenFe:
			self.openAction()
			

	def openAction(self):
		if self._slideShowWin:
			self._slideShowWin.showImageByPath(self._twoDLst[row][column])
			self._animateUpOpen()

