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
        DialogBatchChunk.resize(870, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogBatchChunk.sizePolicy().hasHeightForWidth())
        DialogBatchChunk.setSizePolicy(sizePolicy)
        DialogBatchChunk.setMinimumSize(QSize(870, 650))
        DialogBatchChunk.setMaximumSize(QSize(870, 650))
        DialogBatchChunk.setWindowTitle(u"Batch Chunk Creator")
        icon = QIcon()
        icon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogBatchChunk.setWindowIcon(icon)
        self.verticalLayoutWidget = QWidget(DialogBatchChunk)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 851, 641))
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
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.lineEdit.setFont(font1)
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
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setText(u"Camera")
        self.label_4.setIndent(10)

        self.gridLayout_3.addWidget(self.label_4, 7, 0, 1, 1)

        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy5)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(9)
        self.checkBox.setFont(font3)
        self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Marker coordinates will be imported after target detection. <span style=\" font-weight:600;\">*</span></p><p><span style=\" font-weight:600;\">Disabled:</span> Coordinates are not imported. User must manually import coordinates.</p><p><span style=\" font-weight:600;\">*</span> Automatic importing of marker coordinates only works if point file name is the same as it's parent folder name, and contains a header with metadata. Point coordinates should start at row #7.</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(u"Import Marker Coordinates")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-map-marker-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox.setIcon(icon3)
        self.checkBox.setIconSize(QSize(24, 24))
        self.checkBox.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox, 14, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 19, 0, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setFont(font2)
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setText(u"Markers")
        self.label_5.setIndent(10)

        self.gridLayout_3.addWidget(self.label_5, 12, 0, 1, 1)

        self.line_3 = QFrame(self.verticalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 11, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon4, u"Cam 1")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons8-video-wall-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon5, u"Cam 2")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons8-live-photos-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon6, u"Cam 3")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon7, u"Cam 4")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons8-video-stabilization-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon8, u"Cam 5")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon9, u"Cam 6")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy6)
        self.comboBox_2.setMinimumSize(QSize(200, 0))
        self.comboBox_2.setFont(font1)
        self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
        self.comboBox_2.setStatusTip(u"Choose camera settings to be applied when creating new chunk...")
#endif // QT_CONFIG(statustip)
        self.comboBox_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.comboBox_2)

        self.btnDefCam = QPushButton(self.verticalLayoutWidget)
        self.btnDefCam.setObjectName(u"btnDefCam")
#if QT_CONFIG(tooltip)
        self.btnDefCam.setToolTip(u"Set as default")
#endif // QT_CONFIG(tooltip)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons8-christmas-star-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDefCam.setIcon(icon10)
        self.btnDefCam.setIconSize(QSize(21, 21))
        self.btnDefCam.setAutoDefault(False)
        self.btnDefCam.setFlat(True)

        self.horizontalLayout_12.addWidget(self.btnDefCam)


        self.gridLayout_3.addLayout(self.horizontalLayout_12, 8, 0, 1, 1)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 15, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy7)
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(9)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_10.setFont(font4)
        self.label_10.setText(u"Suffix")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy8)
        self.label_7.setMinimumSize(QSize(180, 0))
        self.label_7.setMaximumSize(QSize(180, 16777215))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(8)
        self.label_7.setFont(font5)
        self.label_7.setFrameShape(QFrame.StyledPanel)
        self.label_7.setText(u"")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.checkBox_align = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_align.setObjectName(u"checkBox_align")
        self.checkBox_align.setEnabled(False)
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.checkBox_align.sizePolicy().hasHeightForWidth())
        self.checkBox_align.setSizePolicy(sizePolicy9)
        self.checkBox_align.setFont(font1)
        self.checkBox_align.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.checkBox_align.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Automatic chunk creation with predefined settings</p><p><span style=\" font-weight:600;\">Disabled:</span> Manual confirmation of intermediate steps</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.checkBox_align.setText(u"Align Cameras at Creation")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons8-cameras-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox_align.setIcon(icon11)
        self.checkBox_align.setIconSize(QSize(24, 24))
        self.checkBox_align.setCheckable(True)
        self.checkBox_align.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_align, 18, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy7.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy7)
        self.label_11.setFont(font4)
        self.label_11.setText(u"Prefix")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy8.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy8)
        self.label_6.setMinimumSize(QSize(180, 0))
        self.label_6.setMaximumSize(QSize(180, 16777215))
        self.label_6.setFont(font5)
        self.label_6.setFrameShape(QFrame.StyledPanel)
        self.label_6.setText(u"")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy5.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy5)
        self.checkBox_2.setFont(font3)
        self.checkBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.checkBox_2.setToolTip(u"<html><head/><body><p>Enable automatic target detection when new chunk is created...</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.checkBox_2.setText(u"Automatic Target Detection")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons8-my-location-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox_2.setIcon(icon12)
        self.checkBox_2.setIconSize(QSize(24, 24))
        self.checkBox_2.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_2, 13, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cbChunkSettings = QComboBox(self.verticalLayoutWidget)
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons8-add-tab-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbChunkSettings.addItem(icon13, u"Default")
        icon14 = QIcon()
        icon14.addFile(u":/icons/kalota_m.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbChunkSettings.addItem(icon14, u"KALOTA")
        icon15 = QIcon()
        icon15.addFile(u":/icons/stopnca_o.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbChunkSettings.addItem(icon15, u"STOPNICA - IZKOP")
        icon16 = QIcon()
        icon16.addFile(u":/icons/stopnca_s.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbChunkSettings.addItem(icon16, u"STOPNICA - B.BET.")
        self.cbChunkSettings.setObjectName(u"cbChunkSettings")
        sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.cbChunkSettings.sizePolicy().hasHeightForWidth())
        self.cbChunkSettings.setSizePolicy(sizePolicy10)
        self.cbChunkSettings.setMinimumSize(QSize(200, 0))
        self.cbChunkSettings.setFont(font1)
        self.cbChunkSettings.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
        self.cbChunkSettings.setStatusTip(u"Choose settings used for chunk creation...")
#endif // QT_CONFIG(statustip)
        self.cbChunkSettings.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.cbChunkSettings)

        self.btnDefChunk = QPushButton(self.verticalLayoutWidget)
        self.btnDefChunk.setObjectName(u"btnDefChunk")
#if QT_CONFIG(tooltip)
        self.btnDefChunk.setToolTip(u"Set as default")
#endif // QT_CONFIG(tooltip)
        self.btnDefChunk.setIcon(icon10)
        self.btnDefChunk.setIconSize(QSize(21, 21))
        self.btnDefChunk.setAutoDefault(False)
        self.btnDefChunk.setFlat(True)

        self.horizontalLayout_8.addWidget(self.btnDefChunk)


        self.gridLayout_3.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.label_17 = QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 30))
        self.label_17.setFont(font2)
        self.label_17.setFrameShape(QFrame.NoFrame)
        self.label_17.setText(u"Processing")
        self.label_17.setIndent(10)

        self.gridLayout_3.addWidget(self.label_17, 16, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy9.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy9)
        self.checkBox_3.setFont(font1)
        self.checkBox_3.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.checkBox_3.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Automatic chunk creation with predefined settings</p><p><span style=\" font-weight:600;\">Disabled:</span> Manual confirmation of intermediate steps</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.checkBox_3.setText(u"Auto Processing")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons8-in-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox_3.setIcon(icon17)
        self.checkBox_3.setIconSize(QSize(24, 24))
        self.checkBox_3.setCheckable(True)
        self.checkBox_3.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_3, 17, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setFont(font4)
        self.label_13.setText(u"SubType")

        self.horizontalLayout_7.addWidget(self.label_13)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy8.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy8)
        self.label_14.setMinimumSize(QSize(180, 0))
        self.label_14.setMaximumSize(QSize(180, 16777215))
        self.label_14.setFont(font5)
        self.label_14.setFrameShape(QFrame.StyledPanel)
        self.label_14.setText(u"")

        self.horizontalLayout_7.addWidget(self.label_14)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 10, 0, 1, 1)

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
        sizePolicy8.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy8)
        self.label_12.setMinimumSize(QSize(180, 0))
        self.label_12.setMaximumSize(QSize(180, 16777215))
        self.label_12.setFont(font5)
        self.label_12.setFrameShape(QFrame.StyledPanel)
        self.label_12.setText(u"")

        self.horizontalLayout_6.addWidget(self.label_12)


        self.gridLayout_3.addLayout(self.horizontalLayout_6, 9, 0, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setFont(font2)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setText(u"Chunk Creation")
        self.label.setIndent(10)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_18 = QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        sizePolicy7.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy7)
        self.label_18.setFont(font4)
        self.label_18.setText(u"Name Format")

        self.horizontalLayout_10.addWidget(self.label_18)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.label_19 = QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        sizePolicy8.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy8)
        self.label_19.setMinimumSize(QSize(180, 0))
        self.label_19.setMaximumSize(QSize(180, 16777215))
        self.label_19.setFont(font5)
        self.label_19.setFrameShape(QFrame.StyledPanel)
        self.label_19.setText(u"")

        self.horizontalLayout_10.addWidget(self.label_19)


        self.gridLayout_3.addLayout(self.horizontalLayout_10, 5, 0, 1, 1)

        self.line_5 = QFrame(self.verticalLayoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 6, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 0, 2, 3, 1)

        self.label_16 = QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
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
        self.label_2.setFont(font2)
        self.label_2.setText(u"Data location")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy4.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy4)
#if QT_CONFIG(statustip)
        self.checkBox_4.setStatusTip(u"Disable to set custom location for data. Enable to use project default data location settings.")
#endif // QT_CONFIG(statustip)
        self.checkBox_4.setText(u"Use Project Data Location")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons8-copy-to-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox_4.setIcon(icon18)
        self.checkBox_4.setIconSize(QSize(20, 20))
        self.checkBox_4.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBox_4)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy8.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy8)
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
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(4, u"Aligned");
        __qtreewidgetitem.setText(3, u"Imported");
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setText(2, u"Images");
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setText(1, u"Point File");
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setText(0, u"Folders");
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setFont(0, font7);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons8-folder-tree-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons8-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons8-check-file-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons8-no-camera-96.png", QSize(), QIcon.Normal, QIcon.Off)
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        icon23 = QIcon()
        icon23.addFile(u":/icons/icons8-error-48.png", QSize(), QIcon.Normal, QIcon.Off)
        icon24 = QIcon()
        icon24.addFile(u":/icons/icons8-add-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon25 = QIcon()
        icon25.addFile(u":/icons/icons8-done-50.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1.setText(0, u"root");
        __qtreewidgetitem1.setFont(0, font7);
        __qtreewidgetitem1.setIcon(0, icon19);
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        __qtreewidgetitem2.setTextAlignment(3, Qt.AlignTrailing|Qt.AlignVCenter);
        __qtreewidgetitem2.setText(2, u"No images");
        __qtreewidgetitem2.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem2.setIcon(2, icon22);
        __qtreewidgetitem2.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem2.setIcon(1, icon21);
        __qtreewidgetitem2.setText(0, u"20230109-0530");
        __qtreewidgetitem2.setIcon(0, icon20);
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem3.setFlags(Qt.ItemIsEnabled);
        __qtreewidgetitem3.setText(2, u"20");
        __qtreewidgetitem3.setIcon(2, icon24);
        __qtreewidgetitem3.setIcon(1, icon23);
        __qtreewidgetitem3.setText(0, u"20230109-0030");
        __qtreewidgetitem3.setFont(0, font8);
        __qtreewidgetitem3.setIcon(0, icon20);
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        __qtreewidgetitem4.setIcon(4, icon25);
        __qtreewidgetitem4.setTextAlignment(3, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem4.setIcon(3, icon25);
        __qtreewidgetitem4.setText(2, u"27");
        __qtreewidgetitem4.setIcon(2, icon24);
        __qtreewidgetitem4.setIcon(1, icon21);
        __qtreewidgetitem4.setText(0, u"20230109-0010");
        __qtreewidgetitem4.setFont(0, font3);
        __qtreewidgetitem4.setIcon(0, icon20);
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
        self.treeWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
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
        sizePolicy9.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy9)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(u"Press [Ctrl+P] to start processing")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_3.setStatusTip(u"Process selected folders, and create new chunks...")
#endif // QT_CONFIG(statustip)
        self.pushButton_3.setText(u"Ready")
        icon26 = QIcon()
        icon26.addFile(u":/icons/icons8-submit-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
        icon26.addFile(u":/icons/icons8-ok-50.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.pushButton_3.setIcon(icon26)
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
#if QT_CONFIG(statustip)
        self.pushButton_2.setStatusTip(u"Exit chunk creator...")
#endif // QT_CONFIG(statustip)
        self.pushButton_2.setText(u"Close")
        icon27 = QIcon()
        icon27.addFile(u":/icons/icons8-close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon27)
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

        self.pushButton_3.setDefault(False)


        QMetaObject.connectSlotsByName(DialogBatchChunk)
    # setupUi

    def retranslateUi(self, DialogBatchChunk):



        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        pass
    # retranslateUi

