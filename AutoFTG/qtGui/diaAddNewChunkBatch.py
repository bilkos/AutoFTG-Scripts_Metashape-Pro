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
import qtresources

class Ui_DialogBatchChunk(object):
    def setupUi(self, DialogBatchChunk):
        if not DialogBatchChunk.objectName():
            DialogBatchChunk.setObjectName(u"DialogBatchChunk")
        DialogBatchChunk.resize(800, 580)
        icon = QIcon()
        icon.addFile(u":/icons/AutoFTG-appicon.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogBatchChunk.setWindowIcon(icon)
        self.verticalLayoutWidget = QWidget(DialogBatchChunk)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 786, 561))
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
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_10.setFont(font1)
        self.label_10.setText(u"Suffix:")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setFrameShape(QFrame.StyledPanel)
        self.label_7.setText(u"Suffix...")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setFont(font1)
        self.label_9.setFrameShape(QFrame.NoFrame)
        self.label_9.setText(u"Type:      ")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setFrameShape(QFrame.StyledPanel)
        self.label_12.setText(u"TextLabel")

        self.horizontalLayout_6.addWidget(self.label_12)


        self.gridLayout_3.addLayout(self.horizontalLayout_6, 7, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setFont(font1)
        self.label_11.setText(u"Prefix:")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setFrameShape(QFrame.StyledPanel)
        self.label_6.setText(u"Prefix...")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon1, u"Cam 1")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-video-wall-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon2, u"Cam 2")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-live-photos-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon3, u"Cam 3")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon4, u"Cam 4")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons8-video-stabilization-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon5, u"Cam 5")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_2.addItem(icon6, u"Cam 6")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy3.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(11)
        self.comboBox_2.setFont(font2)
        self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
        self.comboBox_2.setStatusTip(u"Choose camera settings to be applied when creating new chunk...")
#endif // QT_CONFIG(statustip)
        self.comboBox_2.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.comboBox_2, 6, 0, 1, 1)

        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy3.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(9)
        self.checkBox.setFont(font3)
        self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Marker coordinates will be imported after target detection. <span style=\" font-weight:600;\">*</span></p><p><span style=\" font-weight:600;\">Disabled:</span> Coordinates are not imported. User must manually import coordinates.</p><p><span style=\" font-weight:600;\">*</span> Automatic importing of marker coordinates only works if point file name is the same as it's parent folder name, and contains a header with metadata. Point coordinates should start at row #7.</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(u"Import Marker Coordinates")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons8-map-marker-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox.setIcon(icon7)
        self.checkBox.setIconSize(QSize(20, 20))
        self.checkBox.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox, 12, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy3.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy3)
        self.checkBox_2.setFont(font3)
        self.checkBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.checkBox_2.setToolTip(u"<html><head/><body><p>Enable automatic target detection when new chunk is created...</p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.checkBox_2.setText(u"Automatic Target Detection")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons8-my-location-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox_2.setIcon(icon8)
        self.checkBox_2.setIconSize(QSize(20, 20))
        self.checkBox_2.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_2, 11, 0, 1, 1)

        self.cbChunkSettings = QComboBox(self.verticalLayoutWidget)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons8-add-tab-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbChunkSettings.addItem(icon9, u"Default")
        icon10 = QIcon()
        icon10.addFile(u":/icons/kalota_m.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbChunkSettings.addItem(icon10, u"KALOTA")
        icon11 = QIcon()
        icon11.addFile(u":/icons/stopnca_o.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbChunkSettings.addItem(icon11, u"STOPNICA - IZKOP")
        icon12 = QIcon()
        icon12.addFile(u":/icons/stopnca_s.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbChunkSettings.addItem(icon12, u"STOPNICA - B.BET.")
        self.cbChunkSettings.setObjectName(u"cbChunkSettings")
        sizePolicy3.setHeightForWidth(self.cbChunkSettings.sizePolicy().hasHeightForWidth())
        self.cbChunkSettings.setSizePolicy(sizePolicy3)
        self.cbChunkSettings.setFont(font2)
        self.cbChunkSettings.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
        self.cbChunkSettings.setStatusTip(u"Choose settings used for chunk creation...")
#endif // QT_CONFIG(statustip)
        self.cbChunkSettings.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.cbChunkSettings, 1, 0, 1, 1)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setMinimumSize(QSize(240, 0))
        self.label_4.setMaximumSize(QSize(240, 25))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_4.setFont(font4)
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
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons8-in-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox_3.setIcon(icon13)
        self.checkBox_3.setIconSize(QSize(20, 20))
        self.checkBox_3.setCheckable(True)
        self.checkBox_3.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_3, 14, 0, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setMinimumSize(QSize(240, 0))
        self.label_5.setMaximumSize(QSize(240, 25))
        self.label_5.setFont(font4)
        self.label_5.setText(u"Markers")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 10, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setFont(font1)
        self.label_13.setText(u"SubType:")

        self.horizontalLayout_7.addWidget(self.label_13)

        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setFrameShape(QFrame.StyledPanel)
        self.label_14.setText(u"TextLabel")

        self.horizontalLayout_7.addWidget(self.label_14)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 8, 0, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setMinimumSize(QSize(240, 0))
        self.label.setMaximumSize(QSize(240, 25))
        self.label.setFont(font4)
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


        self.gridLayout.addLayout(self.gridLayout_3, 0, 1, 3, 1)

        self.progressBar = QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy5)
        self.progressBar.setFont(font5)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(10)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 1)

        self.treeWidget = QTreeWidget(self.verticalLayoutWidget)
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons8-folder-tree-50.png", QSize(), QIcon.Normal, QIcon.Off)
        font6 = QFont()
        font6.setBold(True)
        font6.setWeight(75)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(2, u"Images");
        __qtreewidgetitem.setText(1, u"Point File");
        __qtreewidgetitem.setText(0, u"Folders");
        __qtreewidgetitem.setFont(0, font6);
        __qtreewidgetitem.setIcon(0, icon14);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons8-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons8-done-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons8-no-camera-96.png", QSize(), QIcon.Normal, QIcon.Off)
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons8-add-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        __qtreewidgetitem1.setText(2, u"No images");
        __qtreewidgetitem1.setIcon(2, icon17);
        __qtreewidgetitem1.setIcon(1, icon16);
        __qtreewidgetitem1.setText(0, u"20230109-0530");
        __qtreewidgetitem1.setIcon(0, icon15);
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem2.setFlags(Qt.NoItemFlags);
        __qtreewidgetitem2.setText(2, u"20");
        __qtreewidgetitem2.setIcon(2, icon19);
        __qtreewidgetitem2.setIcon(1, icon18);
        __qtreewidgetitem2.setText(0, u"20230109-0030");
        __qtreewidgetitem2.setFont(0, font7);
        __qtreewidgetitem2.setIcon(0, icon15);
        __qtreewidgetitem3 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        __qtreewidgetitem3.setText(2, u"27");
        __qtreewidgetitem3.setIcon(2, icon19);
        __qtreewidgetitem3.setIcon(1, icon16);
        __qtreewidgetitem3.setText(0, u"20230109-0010");
        __qtreewidgetitem3.setFont(0, font3);
        __qtreewidgetitem3.setIcon(0, icon15);
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
        self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
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
        sizePolicy5.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy5)
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
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy7)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
        self.pushButton.setStatusTip(u"Data location (root folder with sub-folders containing data)")
#endif // QT_CONFIG(statustip)
        self.pushButton.setText(u"Browse")
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons8-loading-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon20)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy7.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy7)
        self.pushButton_4.setText(u"Reload")
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons8-reset-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon21)
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
        self.label_8.setFrameShape(QFrame.StyledPanel)
        self.label_8.setText(u"Selected: -")
        self.label_8.setIndent(10)

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

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
        self.pushButton_3.setIcon(icon13)
        self.pushButton_3.setIconSize(QSize(24, 24))
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(u"P")
#endif // QT_CONFIG(shortcut)
        self.pushButton_3.setChecked(False)

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy7.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy7)
#if QT_CONFIG(statustip)
        self.pushButton_2.setStatusTip(u"Exit chunk creator...")
#endif // QT_CONFIG(statustip)
        self.pushButton_2.setText(u"Close")
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons8-close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon22)
        self.pushButton_2.setIconSize(QSize(24, 24))
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(u"X")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setFont(font4)
        self.label_2.setText(u"Data location")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy7.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy7)
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


        self.verticalLayout_2.addLayout(self.gridLayout)

#if QT_CONFIG(shortcut)
        self.label_7.setBuddy(self.cbChunkSettings)
        self.label_6.setBuddy(self.cbChunkSettings)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(DialogBatchChunk)
        self.checkBox_4.toggled.connect(self.pushButton.setDisabled)
        self.checkBox_4.toggled.connect(self.lineEdit.setDisabled)
        self.checkBox_2.toggled.connect(self.checkBox.toggle)
        self.cbChunkSettings.currentTextChanged.connect(self.lineEdit.setText)
        self.lineEdit.textChanged.connect(self.treeWidget.doItemsLayout)
        self.treeWidget.itemSelectionChanged.connect(self.label_8.clear)
        self.pushButton_2.clicked.connect(DialogBatchChunk.reject)
        self.pushButton_3.clicked.connect(self.progressBar.reset)

        self.pushButton_3.setDefault(False)

    # setupUi

    def retranslateUi(self, DialogBatchChunk):
        DialogBatchChunk.setWindowTitle(QCoreApplication.translate("DialogBatchChunk", u"Batch Chunk Creator", None))



        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

