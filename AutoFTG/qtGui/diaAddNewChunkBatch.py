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

import qtresources
from autoftg_main import *

class Ui_DialogBatchChunk(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.sel_items = []
		self.setObjectName(u"DialogBatchChunk")
		self.setWindowTitle(u"Batch Chunk Creator")
		self.resize(800, 570)
		icon = QIcon()
		icon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(icon)
		self.verticalLayoutWidget = QWidget(self)
		self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
		self.verticalLayoutWidget.setGeometry(QRect(10, 0, 786, 561))
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
		sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
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
		sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		sizePolicy1.setHorizontalStretch(0)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
		self.label_3.setSizePolicy(sizePolicy1)
		font = QFont()
		font.setFamily(u"Segoe UI")
		font.setPointSize(16)
		font.setBold(False)
		font.setItalic(False)
		font.setUnderline(False)
		font.setWeight(50)
		self.label_3.setFont(font)
		self.label_3.setText(u"Batch Chunk Creator")

		self.horizontalLayout_9.addWidget(self.label_3)


		self.verticalLayout_2.addLayout(self.horizontalLayout_9)

		self.line_4 = QFrame(self.verticalLayoutWidget)
		self.line_4.setObjectName(u"line_4")
		self.line_4.setFrameShape(QFrame.HLine)
		self.line_4.setFrameShadow(QFrame.Sunken)

		self.verticalLayout_2.addWidget(self.line_4)

		self.gridLayout = QGridLayout()
		self.gridLayout.setSpacing(5)
		self.gridLayout.setObjectName(u"gridLayout")
		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setSpacing(5)
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.label_2 = QLabel(self.verticalLayoutWidget)
		self.label_2.setObjectName(u"label_2")
		sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
		sizePolicy2.setHorizontalStretch(0)
		sizePolicy2.setVerticalStretch(0)
		sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
		self.label_2.setSizePolicy(sizePolicy2)
		font1 = QFont()
		font1.setFamily(u"Segoe UI")
		font1.setPointSize(11)
		font1.setBold(True)
		font1.setWeight(75)
		self.label_2.setFont(font1)
		self.label_2.setText(u"Data location")

		self.horizontalLayout_2.addWidget(self.label_2)

		self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_4.setObjectName(u"checkBox_4")
		sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
		sizePolicy3.setHorizontalStretch(0)
		sizePolicy3.setVerticalStretch(0)
		sizePolicy3.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
		self.checkBox_4.setSizePolicy(sizePolicy3)
#if QT_CONFIG(statustip)
		self.checkBox_4.setStatusTip(u"Disable to set custom location for data. Enable to use project default data location settings.")
#endif // QT_CONFIG(statustip)
		self.checkBox_4.setText(u"Use Project Data Location")
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons8-copy-to-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_4.setIcon(icon1)
		self.checkBox_4.setIconSize(QSize(20, 20))
		self.checkBox_4.setChecked(True)

		self.horizontalLayout_2.addWidget(self.checkBox_4)


		self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

		self.gridLayout_3 = QGridLayout()
		self.gridLayout_3.setSpacing(5)
		self.gridLayout_3.setObjectName(u"gridLayout_3")
		self.horizontalLayout_3 = QHBoxLayout()
		self.horizontalLayout_3.setSpacing(5)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.label_10 = QLabel(self.verticalLayoutWidget)
		self.label_10.setObjectName(u"label_10")
		sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
		sizePolicy4.setHorizontalStretch(0)
		sizePolicy4.setVerticalStretch(0)
		sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
		self.label_10.setSizePolicy(sizePolicy4)
		font2 = QFont()
		font2.setFamily(u"Segoe UI")
		font2.setPointSize(9)
		font2.setBold(True)
		font2.setWeight(75)
		self.label_10.setFont(font2)
		self.label_10.setText(u"Suffix:")

		self.horizontalLayout_3.addWidget(self.label_10)

		self.label_7 = QLabel(self.verticalLayoutWidget)
		self.label_7.setObjectName(u"label_7")
		sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
		self.label_7.setSizePolicy(sizePolicy2)
		self.label_7.setFrameShape(QFrame.StyledPanel)
		self.label_7.setText(u"Suffix...")

		self.horizontalLayout_3.addWidget(self.label_7)


		self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

		self.horizontalLayout_6 = QHBoxLayout()
		self.horizontalLayout_6.setSpacing(5)
		self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
		self.label_9 = QLabel(self.verticalLayoutWidget)
		self.label_9.setObjectName(u"label_9")
		sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
		self.label_9.setSizePolicy(sizePolicy4)
		self.label_9.setFont(font2)
		self.label_9.setFrameShape(QFrame.NoFrame)
		self.label_9.setText(u"Type:	  ")

		self.horizontalLayout_6.addWidget(self.label_9)

		self.label_12 = QLabel(self.verticalLayoutWidget)
		self.label_12.setObjectName(u"label_12")
		sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
		self.label_12.setSizePolicy(sizePolicy2)
		self.label_12.setFrameShape(QFrame.StyledPanel)
		self.label_12.setText(u"TextLabel")

		self.horizontalLayout_6.addWidget(self.label_12)


		self.gridLayout_3.addLayout(self.horizontalLayout_6, 7, 0, 1, 1)

		self.horizontalLayout_5 = QHBoxLayout()
		self.horizontalLayout_5.setSpacing(5)
		self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
		self.label_11 = QLabel(self.verticalLayoutWidget)
		self.label_11.setObjectName(u"label_11")
		sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
		self.label_11.setSizePolicy(sizePolicy4)
		self.label_11.setFont(font2)
		self.label_11.setText(u"Prefix:")

		self.horizontalLayout_5.addWidget(self.label_11)

		self.label_6 = QLabel(self.verticalLayoutWidget)
		self.label_6.setObjectName(u"label_6")
		sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
		self.label_6.setSizePolicy(sizePolicy2)
		self.label_6.setFrameShape(QFrame.StyledPanel)
		self.label_6.setText(u"Prefix...")

		self.horizontalLayout_5.addWidget(self.label_6)


		self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

		self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
		icon = QIcon()
		icon.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons8-panorama-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon2 = QIcon()
		icon2.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon3 = QIcon()
		icon3.addFile(u":/icons/icons8-video-stabilization-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon4 = QIcon()
		icon4.addFile(u":/icons/icons8-touchscreen-48.png", QSize(), QIcon.Normal, QIcon.Off)
		icon5 = QIcon()
		icon5.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon5a = QIcon()
		icon5a.addFile(u":/icons/icons8-ios-application-placeholder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		for cam in cam_list:
			icon_type = camCfg.get(cam, "Type")
			icon_subtype = camCfg.get(cam, "SubType")
			if icon_subtype == "SmartPhone":
				self.comboBox_2.addItem(icon4, cam)
			elif icon_subtype == "Drone":
				self.comboBox_2.addItem(icon5, cam)
			else:
				if icon_type == "Fisheye":
					self.comboBox_2.addItem(icon1, cam)
				elif icon_type == "Spherical":
					self.comboBox_2.addItem(icon3, cam)
				elif icon_type == "Cylindrical":
					self.comboBox_2.addItem(icon2, cam)
				elif icon_type == "RPC":
					self.comboBox_2.addItem(icon5a, cam)
				else:
					self.comboBox_2.addItem(icon, cam)

		self.comboBox_2.setCurrentText(selected_camera)
		self.comboBox_2.setObjectName(u"comboBox_2")
		sizePolicy2.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
		self.comboBox_2.setSizePolicy(sizePolicy2)
		font3 = QFont()
		font3.setFamily(u"Segoe UI")
		font3.setPointSize(11)
		self.comboBox_2.setFont(font3)
		self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.comboBox_2.setStatusTip(u"Choose camera settings to be applied when creating new chunk...")
#endif // QT_CONFIG(statustip)
		self.comboBox_2.setIconSize(QSize(20, 20))

		self.gridLayout_3.addWidget(self.comboBox_2, 6, 0, 1, 1)

		self.checkBox = QCheckBox(self.verticalLayoutWidget)
		self.checkBox.setObjectName(u"checkBox")
		sizePolicy2.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
		self.checkBox.setSizePolicy(sizePolicy2)
		font4 = QFont()
		font4.setFamily(u"Segoe UI")
		font4.setPointSize(9)
		self.checkBox.setFont(font4)
		self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Marker coordinates will be imported after target detection. <span style=\" font-weight:600;\">*</span></p><p><span style=\" font-weight:600;\">Disabled:</span> Coordinates are not imported. User must manually import coordinates.</p><p><span style=\" font-weight:600;\">*</span> Automatic importing of marker coordinates only works if point file name is the same as it's parent folder name, and contains a header with metadata. Point coordinates should start at row #7.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox.setText(u"Import Marker Coordinates")
		icon8 = QIcon()
		icon8.addFile(u":/icons/icons8-map-marker-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox.setIcon(icon8)
		self.checkBox.setIconSize(QSize(20, 20))
		self.checkBox.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox, 12, 0, 1, 1)

		self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_2.setObjectName(u"checkBox_2")
		sizePolicy2.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
		self.checkBox_2.setSizePolicy(sizePolicy2)
		self.checkBox_2.setFont(font4)
		self.checkBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_2.setToolTip(u"<html><head/><body><p>Enable automatic target detection when new chunk is created...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_2.setText(u"Automatic Target Detection")
		icon9 = QIcon()
		icon9.addFile(u":/icons/icons8-my-location-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_2.setIcon(icon9)
		self.checkBox_2.setIconSize(QSize(20, 20))
		self.checkBox_2.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox_2, 11, 0, 1, 1)

		self.cbChunkSettings = QComboBox(self.verticalLayoutWidget)
		for section in chunk_sections:
			menu_icon = menuCfg.get(section, "menu_icon")
			seticon = QIcon()
			seticon.addFile(menu_icon, QSize(), QIcon.Normal, QIcon.Off)
			self.cbChunkSettings.addItem(seticon, section)
		self.cbChunkSettings.setObjectName(u"cbChunkSettings")
		sizePolicy2.setHeightForWidth(self.cbChunkSettings.sizePolicy().hasHeightForWidth())
		self.cbChunkSettings.setSizePolicy(sizePolicy2)
		self.cbChunkSettings.setFont(font3)
		self.cbChunkSettings.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.cbChunkSettings.setStatusTip(u"Choose settings used for chunk creation...")
#endif // QT_CONFIG(statustip)
		self.cbChunkSettings.setIconSize(QSize(20, 20))

		self.gridLayout_3.addWidget(self.cbChunkSettings, 1, 0, 1, 1)

		self.label_4 = QLabel(self.verticalLayoutWidget)
		self.label_4.setObjectName(u"label_4")
		sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
		sizePolicy5.setHorizontalStretch(0)
		sizePolicy5.setVerticalStretch(0)
		sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
		self.label_4.setSizePolicy(sizePolicy5)
		self.label_4.setMinimumSize(QSize(240, 0))
		self.label_4.setMaximumSize(QSize(240, 25))
		self.label_4.setFont(font1)
		self.label_4.setText(u"Camera")
		self.label_4.setAlignment(Qt.AlignCenter)

		self.gridLayout_3.addWidget(self.label_4, 5, 0, 1, 1)

		self.line_6 = QFrame(self.verticalLayoutWidget)
		self.line_6.setObjectName(u"line_6")
		self.line_6.setFrameShape(QFrame.HLine)
		self.line_6.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line_6, 4, 0, 1, 1)

		self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_3.setObjectName(u"checkBox_3")
		font5 = QFont()
		font5.setFamily(u"Segoe UI")
		font5.setPointSize(10)
		self.checkBox_3.setFont(font5)
		self.checkBox_3.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_3.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Automatic chunk creation with predefined settings</p><p><span style=\" font-weight:600;\">Disabled:</span> Manual confirmation of intermediate steps</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_3.setText(u"Automatic Processing")
		icon14 = QIcon()
		icon14.addFile(u":/icons/icons8-in-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_3.setIcon(icon14)
		self.checkBox_3.setIconSize(QSize(20, 20))
		self.checkBox_3.setCheckable(True)
		self.checkBox_3.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox_3, 14, 0, 1, 1)

		self.label_5 = QLabel(self.verticalLayoutWidget)
		self.label_5.setObjectName(u"label_5")
		sizePolicy5.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
		self.label_5.setSizePolicy(sizePolicy5)
		self.label_5.setMinimumSize(QSize(240, 0))
		self.label_5.setMaximumSize(QSize(240, 25))
		self.label_5.setFont(font1)
		self.label_5.setText(u"Markers")
		self.label_5.setAlignment(Qt.AlignCenter)

		self.gridLayout_3.addWidget(self.label_5, 10, 0, 1, 1)

		self.horizontalLayout_7 = QHBoxLayout()
		self.horizontalLayout_7.setSpacing(5)
		self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
		self.label_13 = QLabel(self.verticalLayoutWidget)
		self.label_13.setObjectName(u"label_13")
		sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
		self.label_13.setSizePolicy(sizePolicy4)
		self.label_13.setFont(font2)
		self.label_13.setText(u"SubType:")

		self.horizontalLayout_7.addWidget(self.label_13)

		self.label_14 = QLabel(self.verticalLayoutWidget)
		self.label_14.setObjectName(u"label_14")
		sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
		self.label_14.setSizePolicy(sizePolicy2)
		self.label_14.setFrameShape(QFrame.StyledPanel)
		self.label_14.setText(u"TextLabel")

		self.horizontalLayout_7.addWidget(self.label_14)


		self.gridLayout_3.addLayout(self.horizontalLayout_7, 8, 0, 1, 1)

		self.label = QLabel(self.verticalLayoutWidget)
		self.label.setObjectName(u"label")
		sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy5)
		self.label.setMinimumSize(QSize(240, 0))
		self.label.setMaximumSize(QSize(240, 25))
		self.label.setFont(font1)
		self.label.setText(u"Chunk Creation")
		self.label.setAlignment(Qt.AlignCenter)

		self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

		self.line = QFrame(self.verticalLayoutWidget)
		self.line.setObjectName(u"line")
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line, 9, 0, 1, 1)

		self.line_3 = QFrame(self.verticalLayoutWidget)
		self.line_3.setObjectName(u"line_3")
		self.line_3.setFrameShape(QFrame.HLine)
		self.line_3.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line_3, 13, 0, 1, 1)


		self.gridLayout.addLayout(self.gridLayout_3, 0, 2, 3, 1)

		self.line_5 = QFrame(self.verticalLayoutWidget)
		self.line_5.setObjectName(u"line_5")
		self.line_5.setFrameShape(QFrame.VLine)
		self.line_5.setFrameShadow(QFrame.Sunken)

		self.gridLayout.addWidget(self.line_5, 0, 1, 5, 1)

		self.horizontalLayout_4 = QHBoxLayout()
		self.horizontalLayout_4.setSpacing(5)
		self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
		self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_3.setObjectName(u"pushButton_3")
		self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.pushButton_3.setToolTip(u"Press [Ctrl+P] to start processing")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
		self.pushButton_3.setStatusTip(u"Process selected folders, and create new chunks...")
#endif // QT_CONFIG(statustip)
		self.pushButton_3.setText(u"Process")
		icon15 = QIcon()
		icon15.addFile(u":/icons/icons8-synchronize-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_3.setIcon(icon15)
		self.pushButton_3.setIconSize(QSize(24, 24))
#if QT_CONFIG(shortcut)
		self.pushButton_3.setShortcut(u"P")
#endif // QT_CONFIG(shortcut)
		self.pushButton_3.setChecked(False)

		self.horizontalLayout_4.addWidget(self.pushButton_3)

		self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_2.setObjectName(u"pushButton_2")
#if QT_CONFIG(statustip)
		self.pushButton_2.setStatusTip(u"Exit chunk creator...")
#endif // QT_CONFIG(statustip)
		self.pushButton_2.setText(u"Exit")
		icon16 = QIcon()
		icon16.addFile(u":/icons/icons8-enter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_2.setIcon(icon16)
		self.pushButton_2.setIconSize(QSize(24, 24))
#if QT_CONFIG(shortcut)
		self.pushButton_2.setShortcut(u"X")
#endif // QT_CONFIG(shortcut)

		self.horizontalLayout_4.addWidget(self.pushButton_2)


		self.gridLayout.addLayout(self.horizontalLayout_4, 4, 2, 1, 1)

		self.treeWidget = QTreeWidget(self.verticalLayoutWidget)
		icon17 = QIcon()
		icon17.addFile(u":/icons/icons8-folder-tree-50.png", QSize(), QIcon.Normal, QIcon.Off)
		font6 = QFont()
		font6.setBold(True)
		font6.setWeight(75)
		__qtreewidgetitem = QTreeWidgetItem()
		__qtreewidgetitem.setText(2, u"Images");
		__qtreewidgetitem.setText(1, u"Point File");
		__qtreewidgetitem.setText(0, u"Folders");
		__qtreewidgetitem.setFont(0, font6);
		__qtreewidgetitem.setIcon(0, icon17);
		self.treeWidget.setHeaderItem(__qtreewidgetitem)
		icon18 = QIcon()
		icon18.addFile(u":/icons/icons8-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon19 = QIcon()
		icon19.addFile(u":/icons/icons8-done-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon20 = QIcon()
		icon20.addFile(u":/icons/icons8-no-camera-96.png", QSize(), QIcon.Normal, QIcon.Off)
		font7 = QFont()
		font7.setFamily(u"Segoe UI")
		icon21 = QIcon()
		icon21.addFile(u":/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
		icon22 = QIcon()
		icon22.addFile(u":/icons/icons8-add-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.treeWidget.setObjectName(u"treeWidget")
		sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
		sizePolicy6.setHorizontalStretch(0)
		sizePolicy6.setVerticalStretch(0)
		sizePolicy6.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
		self.treeWidget.setSizePolicy(sizePolicy6)
		self.treeWidget.setMinimumSize(QSize(525, 0))
		self.treeWidget.setMaximumSize(QSize(525, 16777215))
		self.treeWidget.setAutoScrollMargin(20)
		self.treeWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
		self.treeWidget.setTabKeyNavigation(True)
		self.treeWidget.setProperty("showDropIndicator", False)
		self.treeWidget.setAlternatingRowColors(True)
		self.treeWidget.setSelectionMode(QAbstractItemView.MultiSelection)
		self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
		self.treeWidget.setIconSize(QSize(20, 20))
		self.treeWidget.setUniformRowHeights(True)
		self.treeWidget.setSortingEnabled(True)
		self.treeWidget.setAllColumnsShowFocus(True)
		self.treeWidget.header().setVisible(True)
		self.treeWidget.header().setDefaultSectionSize(170)

		self.gridLayout.addWidget(self.treeWidget, 2, 0, 1, 1)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setSpacing(5)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.lineEdit = QLineEdit(self.verticalLayoutWidget)
		self.lineEdit.setObjectName(u"lineEdit")
		self.lineEdit.setEnabled(False)
		sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy7.setHorizontalStretch(0)
		sizePolicy7.setVerticalStretch(0)
		sizePolicy7.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
		self.lineEdit.setSizePolicy(sizePolicy7)
		self.lineEdit.setFont(font5)
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
		sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
		self.pushButton.setSizePolicy(sizePolicy3)
		self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.pushButton.setStatusTip(u"Data location (root folder with sub-folders containing data)")
#endif // QT_CONFIG(statustip)
		self.pushButton.setText(u"Browse")
		icon23 = QIcon()
		icon23.addFile(u":/icons/icons8-loading-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton.setIcon(icon23)
		self.pushButton.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton)

		self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
		self.pushButton_4.setObjectName(u"pushButton_4")
		sizePolicy3.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
		self.pushButton_4.setSizePolicy(sizePolicy3)
		self.pushButton_4.setText(u"Reload")
		icon24 = QIcon()
		icon24.addFile(u":/icons/icons8-reset-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_4.setIcon(icon24)
		self.pushButton_4.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton_4)


		self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

		self.label_8 = QLabel(self.verticalLayoutWidget)
		self.label_8.setObjectName(u"label_8")
		font8 = QFont()
		font8.setFamily(u"Segoe UI")
		font8.setPointSize(10)
		font8.setBold(True)
		font8.setWeight(75)
		self.label_8.setFont(font8)
		self.label_8.setFrameShape(QFrame.NoFrame)
		self.label_8.setText(u"Selected: 2")
		self.label_8.setIndent(10)

		self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

		self.progressBar = QProgressBar(self.verticalLayoutWidget)
		self.progressBar.setObjectName(u"progressBar")
		self.progressBar.setEnabled(False)
		sizePolicy7.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
		self.progressBar.setSizePolicy(sizePolicy7)
		self.progressBar.setFont(font5)
		self.progressBar.setMinimum(0)
		self.progressBar.setMaximum(10)
		self.progressBar.setValue(0)
		self.progressBar.setFormat(u"Processing chunk: %v/%m")

		self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 1)


		self.verticalLayout_2.addLayout(self.gridLayout)

#if QT_CONFIG(shortcut)
		self.label_7.setBuddy(self.cbChunkSettings)
		self.label_6.setBuddy(self.cbChunkSettings)
#endif // QT_CONFIG(shortcut)

		self.checkBox_4.toggled.connect(self.pushButton.setDisabled)
		self.checkBox_4.toggled.connect(self.lineEdit.setDisabled)
		self.checkBox_2.toggled.connect(self.checkBox.toggle)
		self.cbChunkSettings.currentTextChanged.connect(self.lineEdit.setText)
		self.lineEdit.textChanged.connect(self.treeWidget.doItemsLayout)
		self.treeWidget.itemSelectionChanged.connect(self.label_8.clear)
		self.pushButton_2.clicked.connect(self.reject)
		self.pushButton_3.clicked.connect(self.progressBar.reset)

		self.pushButton_3.setDefault(False)

		
		__sortingEnabled = self.treeWidget.isSortingEnabled()
		self.treeWidget.setSortingEnabled(False)
		self.treeWidget.setSortingEnabled(__sortingEnabled)

