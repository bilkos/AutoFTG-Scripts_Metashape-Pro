
class Ui_DialogBatchChunkOld(QtWidgets.QDialog):
	def __init__(self, parent):
		QtWidgets.QDialog.__init__(self, parent)
		self.sel_items = []
		self.itemDef = projCfg.get("PROJECT SETTINGS", "default_chunk_def")
		self.itemDefFolder = menuCfg.get(self.itemDef, "work_folder")
		self.itemDefFolderName = self.itemDefFolder.split(os.sep)[-1]
		self.setObjectName(u"DialogBatchChunk")
		self.setWindowTitle(u"Batch Chunk Creator")
		self.resize(800, 580)
		appIcon = QIcon()
		appIcon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
		self.setWindowIcon(appIcon)
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
		icoTripod = QIcon()
		icoTripod.addFile(u":/icons/icons8-camera-on-tripod-96.png", QSize(), QIcon.Normal, QIcon.Off)
		for cam in cam_list:
			icon_type = camCfg.get(cam, "Type")
			icon_subtype = camCfg.get(cam, "SubType")
			if icon_subtype == "SmartPhone":
				self.comboBox_2.addItem(icon4, cam)
			elif icon_subtype == "Drone":
				self.comboBox_2.addItem(icon5, cam)
			elif icon_subtype == "Special":
				self.comboBox_2.addItem(icoTripod, cam)
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
		self.cbChunkSettings.setObjectName(u"cbChunkSettings")
		sizePolicy2.setHeightForWidth(self.cbChunkSettings.sizePolicy().hasHeightForWidth())
		self.cbChunkSettings.setSizePolicy(sizePolicy2)
		self.cbChunkSettings.setFont(font3)
		self.cbChunkSettings.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
		self.cbChunkSettings.setStatusTip(u"Choose settings used for chunk creation...")
#endif // QT_CONFIG(statustip)
		self.cbChunkSettings.setIconSize(QSize(20, 20))
		for section in chunk_sections:
			menu_icon = menuCfg.get(section, "menu_icon")
			setticon = QIcon()
			setticon.addFile(menu_icon, QSize(), QIcon.Normal, QIcon.Off)
			self.cbChunkSettings.addItem(setticon, section)
		self.cbChunkSettings.setCurrentText(self.itemDef)

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
		iconInProgress = QIcon()
		iconInProgress.addFile(u":/icons/icons8-in-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_3.setIcon(iconInProgress)
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
		iconStartProc = QIcon()
		iconStartProc.addFile(u":/icons/icons8-synchronize-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconStartProc.addFile(u":/icons/icons8-synchronize-50.png", QSize(), QIcon.Disabled, QIcon.Off)
		self.pushButton_3.setDisabled(1)

		self.pushButton_3.setIcon(iconStartProc)
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


		self.gridLayout.addLayout(self.horizontalLayout_4, 4, 1, 1, 1)

		
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
		self.lineEdit.setStatusTip(u"Path to main folder with data in sub-folders...")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
		self.lineEdit.setWhatsThis(u"Path to main folder with data in sub-folders...")
#endif // QT_CONFIG(whatsthis)
		self.lineEdit.setPlaceholderText(u"Data location...")

		self.lineEdit.setText(self.itemDefFolder)

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
		iconMoveToFolder = QIcon()
		iconMoveToFolder.addFile(u":/icons/icons8-move-to-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton.setIcon(iconMoveToFolder)
		self.pushButton.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton)

		self.pushButton_reload = QPushButton(self.verticalLayoutWidget)
		self.pushButton_reload.setObjectName(u"pushButton_reload")
		sizePolicy3.setHeightForWidth(self.pushButton_reload.sizePolicy().hasHeightForWidth())
		self.pushButton_reload.setSizePolicy(sizePolicy3)
		self.pushButton_reload.setText(u"Reload")
		iconReload = QIcon()
		iconReload.addFile(u":/icons/icons8-rotate-48.png", QSize(), QIcon.Normal, QIcon.Off)
		iconLoading = QIcon()
		iconLoading.addFile(u":/icons/icons8-loading-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_reload.setIcon(iconReload)
		self.pushButton_reload.setIconSize(QSize(20, 20))

		self.horizontalLayout.addWidget(self.pushButton_reload)

		self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
		
		self.treeWidget = QTreeWidget(self.verticalLayoutWidget)
		self.treeWidget.setObjectName(u"treeWidget")
		font6 = QFont()
		font6.setBold(True)
		font6.setWeight(75)
		
		iconFolderTree = QIcon()
		iconFolderTree.addFile(u":/icons/icons8-folder-tree-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconFolder = QIcon()
		iconFolder.addFile(u":/icons/icons8-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconDone = QIcon()
		iconDone.addFile(u":/icons/icons8-done-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconNoCam = QIcon()
		iconNoCam.addFile(u":/icons/icons8-no-camera-96.png", QSize(), QIcon.Normal, QIcon.Off)
		font7 = QFont()
		font7.setFamily(u"Segoe UI")
		iconClose = QIcon()
		iconClose.addFile(u":/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
		iconAddCam = QIcon()
		iconAddCam.addFile(u":/icons/icons8-add-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
		sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
		sizePolicy6.setHorizontalStretch(0)
		sizePolicy6.setVerticalStretch(0)
		sizePolicy6.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
		__qtreewidgetitem = QTreeWidgetItem()
		__qtreewidgetitem.setText(3, u"Imported");
		__qtreewidgetitem.setText(2, u"Images");
		__qtreewidgetitem.setText(1, u"Point File");
		__qtreewidgetitem.setText(0, u"Folders");
		self.treeWidget.setHeaderItem(__qtreewidgetitem)

		self.treeWidget.setSizePolicy(sizePolicy6)
		self.treeWidget.setMinimumSize(QSize(490, 0))
		self.treeWidget.setMaximumSize(QSize(490, 16777215))
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
		self.treeWidget.resizeColumnToContents(0)
		# self.treeWidget.header().setDefaultSectionSize(165)
		# self.treeWidget.header().setMinimumWidth(120)
		
		self.gridLayout.addWidget(self.treeWidget, 2, 0, 1, 1)

		self.label_8 = QLabel(self.verticalLayoutWidget)
		self.label_8.setObjectName(u"label_8")
		sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
		sizePolicy8.setHorizontalStretch(0)
		sizePolicy8.setVerticalStretch(0)
		sizePolicy8.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
		self.label_8.setSizePolicy(sizePolicy8)
		font8 = QFont()
		font8.setFamily(u"Segoe UI")
		font8.setPointSize(9)
		self.label_8.setFont(font8)
		self.label_8.setFrameShape(QFrame.StyledPanel)
		self.label_8.setText(u"Select folders to process...")
		self.label_8.setIndent(10)

		self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

		#self.label_selnr = QLabel(self.verticalLayoutWidget)
		#self.label_selnr.setObjectName(u"label_selnr")
		#sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
		#self.label_selnr.setSizePolicy(sizePolicy8)
		#self.label_selnr.setFont(font2)
		#self.label_selnr.setText(u"<html><head/><body><p>Select items to process</p></body></html>")
		#self.label_selnr.setIndent(5)
		#
#
		#self.gridLayout.addWidget(self.label_selnr, 3, 1, 1, 1)
		
		self.progressBar = QProgressBar(self.verticalLayoutWidget)
		self.progressBar.setObjectName(u"progressBar")
		sizePolicy7.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
		sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
		self.progressBar.setSizePolicy(sizePolicy7)
		self.progressBar.setFont(font5)
		self.progressBar.setMinimum(1)
		self.progressBar.setMaximum(1)
		self.progressBar.setValue(0)
		self.progressBar.setDisabled(True)
		self.progressBar.setTextVisible(False)
		self.progressBar.setAlignment(Qt.AlignCenter)
		self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 1)


		self.verticalLayout_2.addLayout(self.gridLayout)

#if QT_CONFIG(shortcut)
		self.label_7.setBuddy(self.cbChunkSettings)
		self.label_6.setBuddy(self.cbChunkSettings)
#endif // QT_CONFIG(shortcut)

		__sortingEnabled = self.treeWidget.isSortingEnabled()
		self.treeWidget.setSortingEnabled(True)
		self.treeWidget.setSortingEnabled(__sortingEnabled)

		defChk = self.cbChunkSettings.currentText()
		self.label_6.setText(menuCfg.get(defChk, "chunk_name_prefix"))
		self.label_7.setText(menuCfg.get(defChk, "chunk_name_suffix"))

		defCam = self.comboBox_2.currentText()
		self.label_12.setText(camCfg.get(defCam, "type"))
		self.label_14.setText(camCfg.get(defCam, "subtype"))
		
		self.checkBox_4.toggled.connect(self.pushButton.setDisabled)
		self.checkBox_4.toggled.connect(self.lineEdit.setDisabled)
		self.checkBox_2.toggled.connect(self.checkBox.toggle)
		self.cbChunkSettings.currentTextChanged.connect(self.setCurrentSettings)
		self.cbChunkSettings.currentTextChanged.connect(self.updateFolders)
		#self.lineEdit.textChanged.connect(self.updateFolders)
		self.comboBox_2.currentTextChanged.connect(self.setCurrentCamera)
		self.pushButton_2.clicked.connect(self.quitChunkBatch)
		self.pushButton_3.clicked.connect(self.progressBar.reset)
		self.pushButton_3.clicked.connect(self.processBatch)
		self.pushButton_reload.clicked.connect(self.updateFolders)
		self.pushButton.clicked.connect(self.browseFolder)
		self.treeWidget.itemSelectionChanged.connect(self.updateSelected)

		self.projDoc = Metashape.app.document
		self.projDocFile = str(projDoc).replace("<Document '", "").replace("'>", "")
		self.logFilenamePath = self.projDocFile.replace(".psx", "_log.csv")	# Datoteka z nastavitvami projekta
		
		self.updateFolders()
		
		self.exec()


	def setCurrentSettings(self):
		chunkSet = self.cbChunkSettings.currentText()
		if chunkSet == "Default":
			self.lineEdit.clear()
			self.pushButton.setEnabled(True)
			self.lineEdit.setEnabled(True)
			self.checkBox_4.setChecked(False)
			self.lineEdit.setText(str(menuCfg.get(chunkSet, "work_folder")))
			self.label_6.setText(menuCfg.get(chunkSet, "chunk_name_prefix"))
			self.label_7.setText(menuCfg.get(chunkSet, "chunk_name_suffix"))
		else:
			self.lineEdit.setText(str(menuCfg.get(chunkSet, "work_folder")))
			self.pushButton.setDisabled(True)
			self.lineEdit.setDisabled(True)
			self.checkBox_4.setChecked(True)
			self.label_6.setText(menuCfg.get(chunkSet, "chunk_name_prefix"))
			self.label_7.setText(menuCfg.get(chunkSet, "chunk_name_suffix"))


	def setCurrentCamera(self):
		chunkCam = self.comboBox_2.currentText()
		self.label_12.setText(camCfg.get(chunkCam, "type"))
		self.label_14.setText(camCfg.get(chunkCam, "subtype"))
		

	def updateFolders(self):
		global logArchive
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
		
		self.pushButton_reload.setIcon(iconLoading)
		
		self.treeWidget.clear()
		
		itemCurFolder = str(self.lineEdit.text()).split(os.sep)[-1]

		open_folder = self.lineEdit.text() + "\\"
		
		qtreewidgetitem_top = QTreeWidgetItem(self.treeWidget)
		qtreewidgetitem_top.setText(0, itemCurFolder)
		qtreewidgetitem_top.setFont(0, font6)
		qtreewidgetitem_top.setIcon(0, iconFolderTree)
		qtreewidgetitem_top.setExpanded(True)

		folder_list = []
		folder_list = next(os.walk(open_folder))[1];
		
		for folder in folder_list:
			__qtreewidgetitem1 = QTreeWidgetItem(qtreewidgetitem_top);
			image_folder = str(open_folder).replace("\\", "/") + "/" + folder
			photos_count = len(find_files(image_folder, [".jpg", ".jpeg", ".png", ".tif", ".tiff"]));
			if folder in logArchive:
				__qtreewidgetitem1.setIcon(3, iconDone);
			if photos_count > 0:
				__qtreewidgetitem1.setText(2, str(photos_count) + " image(s)");
				__qtreewidgetitem1.setIcon(2, iconAddCam);
				__qtreewidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
				
			else:
				__qtreewidgetitem1.setText(2, "No images");
				__qtreewidgetitem1.setIcon(2, iconNoCam);
				__qtreewidgetitem1.setFlags(Qt.ItemIsEnabled);
								
			points_file = image_folder + "/" + folder + ".txt"
			points_file_exists = os.path.isfile(points_file);
			if points_file_exists == True:
				__qtreewidgetitem1.setIcon(1, iconDoneFile);
				__qtreewidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
				__qtreewidgetitem1.setText(1, u"Found");
			else:
				__qtreewidgetitem1.setIcon(1, iconClose);
				__qtreewidgetitem1.setText(1, u"Not Found");
				__qtreewidgetitem1.setFlags(Qt.ItemIsEnabled);

			__qtreewidgetitem1.setText(0, folder);
			__qtreewidgetitem1.setIcon(0, iconFolder);
			__qtreewidgetitem1.setSizeHint(0, QSize(165, 0))


		self.pushButton_3.setIcon(iconStart)
		self.pushButton_3.setDisabled(True)
		self.label_8.setText(u"<html><head/><body><p>Folder contents reloaded...</p></body></html>")
		self.progressBar.setMinimum(1)
		self.progressBar.setMaximum(1)
		self.progressBar.setValue(0)
		self.progressBar.setTextVisible(False)
		self.progressBar.setDisabled(True)
		self.treeWidget.resizeColumnToContents(0)
		self.treeWidget.sortItems(0, Qt.AscendingOrder)
		self.treeWidget.scrollToBottom()
		self.pushButton_reload.setIcon(iconReload)
		

	def browseFolder(self):
		defFolder = Metashape.app.getExistingDirectory("Data folder")
		self.lineEdit.setText(defFolder)
		self.updateFolders()


	def logReadArchive(self):
		global logArchive
		logFilenameExists = os.path.isfile(self.logFilenamePath)	# Preveri, če datoteka z projektom obstaja
		if logFilenameExists == False:
			ms_header = "Date, Time, Chunk Name, Photos, Point File, Path, Camera\n"
			print(str(ms_header))
			with open(self.logFilenamePath, "w") as f:
				f.write(ms_header)
				f.close()

		readlog = open(self.logFilenamePath, "r")
		logArchive = readlog.read()
		readlog.close()


	def logWriteBatch(self, data):
		logFilenameExists = os.path.isfile(self.logFilenamePath)	# Preveri, če datoteka z projektom obstaja

		if logFilenameExists == False:
			ms_header = "Date, Time, Chunk Name, Photos, Point File, Path, Camera\n" + data
			print(str(ms_header))
			with open(self.logFilenamePath, "w") as f:
				f.write(ms_header)
		else:
			print(str(data))
			with open(self.logFilenamePath, "a") as f:
				f.write(data)


	def updateSelected(self):
		iconStart = QIcon()
		iconStart.addFile(u":/icons/icons8-synchronize-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_3.setIcon(iconStart)
		self.pushButton_3.setEnabled(True)
		sel_items = self.treeWidget.selectedItems()
		sel_count = len(sel_items)
		if sel_count > 0:
			self.pushButton_3.setEnabled(True)
		else:
			self.pushButton_3.setDisabled(True)
			self.label_8.setText(u"<html><head/><body><p>Select items to process</p></body></html>")
		
		# self.label_8.setText(u"Selected: " + str(sel_count))
		

	# Process selected folders automatically (no user interaction)
	def processBatchAuto(self):
		self.sel_items = self.treeWidget.selectedItems()
		sel_count = len(self.sel_items)
		item_menu = self.cbChunkSettings.currentText()
		item_pre = menuCfg.get(item_menu, "chunk_name_prefix")
		item_suf = menuCfg.get(item_menu, "chunk_name_suffix")
		item_cam = self.comboBox_2.currentText()
		
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
		
		if sel_count > 0:
			i_cnt = 0
			self.progressBar.setEnabled(True)
			self.progressBar.setMinimum(i_cnt)
			self.progressBar.setMaximum(sel_count)
			self.progressBar.setValue(i_cnt)
			self.progressBar.setTextVisible(True)
			self.pushButton_3.setDisabled(True)
			self.pushButton_3.setIcon(iconProcess)
			self.pushButton_3.setText(u"Processing...")
			
			for item in self.sel_items:
				i_cnt = i_cnt + 1
				self.progressBar.setFormat(u"Completed %v/%m")
				self.label_8.setText(u"Processing folder " + str(i_cnt) + " of " + str(sel_count) + " | Current: <b>" + str(item.text(0)) + "</b>")
				doc = Metashape.app.document
				netpath = Metashape.app.document.path
				netroot = self.lineEdit.text()
				image_folder = str(netroot).replace("\\", "/") + "/" + item.text(0)
				photos = find_files(image_folder, [".jpg", ".jpeg", ".png", ".tif", ".tiff"])
				chunk = doc.addChunk()
				chunk.addPhotos(photos)
				chunk_name = item_pre + item.text(0) + item_suf
				chunk.label = chunk_name
				doc.chunk = chunk
				doc.save(netpath)
				Metashape.app.update()
				time.sleep(3)
				readCameraSettings(item_cam)
				useCameraSettings()
				if self.checkBox_2.isChecked() == True:
					chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=98)

				if self.checkBox.isChecked() == True:
					points_file = image_folder + "/" + item.text(0) + ".txt"
					points_file_exists = os.path.isfile(points_file)
					if points_file_exists == True:
						chunk.importReference(points_file, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
						chunk.updateTransform()
						ms_pntfile = item.text(0) + ".txt"
					else:
						ms_pntfile = "None"
				
				now = datetime.now()
				dt_string = now.strftime("%d.%m.%Y")
				tm_string = now.strftime("%H:%M")
				ms_data = dt_string + ", " + tm_string + ", " + chunk_name + ", " + str(len(photos)) + ", " + ms_pntfile + ", " + image_folder + ", " + item_cam + "\n"
				self.logWriteBatch(ms_data)
				
				self.treeWidget.setItemSelected(item, False)
				self.progressBar.setValue(i_cnt)

			if i_cnt < sel_count:
				self.pushButton_3.setIcon(iconError)
				self.pushButton_3.setText(u"Error!")
				self.label_8.setText(u"<html><head/><body><p><b>Processing error!</b> / Imported " + str(i_cnt) + " of " + str(sel_count) + " / Could not import <b>" + str(item.text(0)) + "</b></p></body></html>")
			else:
				self.pushButton_3.setIcon(iconOk)
				self.pushButton_3.setText(u"Done")
				self.label_8.setText(u"<html><head/><body><p><b>Processing done!</b> / Imported " + str(i_cnt) + " of " + str(sel_count) + "</p></body></html>")

			Metashape.app.update()
			doc.save(netpath)
			

	# Process selected folders manually (user must confirm chunk name, camera settings, marker detection, and show point file)
	def processBatchManual(self):
		self.sel_items = self.treeWidget.selectedItems()
		sel_count = len(self.sel_items)
		item_menu = self.cbChunkSettings.currentText()
		item_pre = menuCfg.get(item_menu, "chunk_name_prefix")
		item_suf = menuCfg.get(item_menu, "chunk_name_suffix")
		item_cam = self.comboBox_2.currentText()
		
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
		
		if sel_count > 0:
			i_cnt = 0
			self.progressBar.setEnabled(True)
			self.progressBar.setMinimum(i_cnt)
			self.progressBar.setMaximum(sel_count)
			self.progressBar.setValue(i_cnt)
			self.pushButton_3.setDisabled(True)
			self.pushButton_3.setIcon(iconProcess)
			self.pushButton_3.setText(u"Processing...")
			
			for item in self.sel_items:
				i_cnt = i_cnt + 1
				self.progressBar.setFormat(u"Completed %v/%m")
				self.label_8.setText(u"Processing folder " + str(i_cnt) + " of " + str(sel_count) + " | Current: <b>" + str(item.text(0)) + "</b>")
				doc = Metashape.app.document
				netpath = Metashape.app.document.path
				netroot = self.lineEdit.text()
				image_folder = str(netroot).replace("\\", "/") + "/" + item.text(0)
				photos = find_files(image_folder, [".jpg", ".jpeg", ".png", ".tif", ".tiff"])
				chunk = doc.addChunk()
				chunk.addPhotos(photos)
				chunk_name = item_pre + item.text(0) + item_suf
				chunk.label = Metashape.app.getString("Chunk Name", chunk_name)
				chunk.label = chunk_name
				doc.chunk = chunk
				doc.save(netpath)
				readCameraSettings(item_cam)
				useCameraSettings()
				if self.checkBox_2.isChecked() == True:
					chunk.detectMarkers(target_type=Metashape.CircularTarget12bit, tolerance=97)
				
				if self.checkBox.isChecked() == True:
					points_file = image_folder + "/" + item.text(0) + ".txt"
					points_file_exists = os.path.isfile(points_file)
					if points_file_exists == True:
						chunk.importReference(points_file, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
						chunk.updateTransform()
				else:
					points_file = Metashape.app.getOpenFileName("Import marker coordinates", image_folder, "Text file (*.txt)")
					chunk.importReference(points_file, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=',', skip_rows=6, create_markers=True)
					chunk.updateTransform()
				
				now = datetime.now()
				dt_string = now.strftime("%d.%m.%Y")
				tm_string = now.strftime("%H:%M")
				ms_data = dt_string + ", " + tm_string + ", " + chunk_name + ", " + str(len(photos)) + ", " + os.path.basename(points_file) + ", " + image_folder + ", " + item_cam + "\n"
				self.logWriteBatch(ms_data)
				
				self.treeWidget.setItemSelected(item, False)
				self.progressBar.setValue(i_cnt)
				
			if i_cnt < sel_count:
				self.pushButton_3.setIcon(iconError)
				self.pushButton_3.setText(u"Error!")
				self.label_8.setText(u"<html><head/><body><p><b>Processing error!</b> / Imported " + str(i_cnt) + " of " + str(sel_count) + " / Could not import <b>" + str(item.text(0)) + "</b></p></body></html>")
			else:
				self.pushButton_3.setIcon(iconOk)
				self.pushButton_3.setText(u"Done")
				self.label_8.setText(u"<html><head/><body><p><b>Processing done!</b> / Imported " + str(i_cnt) + " of " + str(sel_count) + "</p></body></html>")
			
			Metashape.app.update()
			doc.save(netpath)
				

	def processBatch(self):
		if self.checkBox_3.isChecked() == True:
			self.processBatchAuto()
		else:
			self.processBatchManual()


	def quitChunkBatch(self):
		self.reject()
