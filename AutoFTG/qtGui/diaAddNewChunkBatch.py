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
		DialogBatchChunk.resize(900, 830)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(DialogBatchChunk.sizePolicy().hasHeightForWidth())
		DialogBatchChunk.setSizePolicy(sizePolicy)
		DialogBatchChunk.setMinimumSize(QSize(900, 830))
		DialogBatchChunk.setMaximumSize(QSize(900, 830))
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
		self.verticalLayoutWidget.setGeometry(QRect(0, 0, 901, 831))
		self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setSpacing(5)
		self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_2.setObjectName(u"verticalLayout_2")
		self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
		self.verticalLayout_2.setContentsMargins(5, 0, 5, 5)
		self.horizontalLayout_9 = QHBoxLayout()
		self.horizontalLayout_9.setSpacing(5)
		self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
		self.horizontalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
		self.label_15 = QLabel(self.verticalLayoutWidget)
		self.label_15.setObjectName(u"label_15")
		sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
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
		sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
		sizePolicy2.setHorizontalStretch(0)
		sizePolicy2.setVerticalStretch(0)
		sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
		self.label_3.setSizePolicy(sizePolicy2)
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
		sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
		sizePolicy3.setHorizontalStretch(0)
		sizePolicy3.setVerticalStretch(0)
		sizePolicy3.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
		self.line_4.setSizePolicy(sizePolicy3)
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
		__qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
		__qtreewidgetitem1.setText(0, u"root");
		__qtreewidgetitem1.setFont(0, font2);
		__qtreewidgetitem1.setIcon(0, icon7);
		__qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
		__qtreewidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
		__qtreewidgetitem2.setIcon(4, icon11);
		__qtreewidgetitem2.setIcon(3, icon11);
		__qtreewidgetitem2.setText(2, u"3D: -");
		__qtreewidgetitem2.setIcon(2, icon10);
		__qtreewidgetitem2.setText(1, u"21");
		__qtreewidgetitem2.setIcon(1, icon9);
		__qtreewidgetitem2.setText(0, u"20230125-1010");
		__qtreewidgetitem2.setIcon(0, icon8);
		__qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem1)
		__qtreewidgetitem3.setFlags(Qt.NoItemFlags);
		__qtreewidgetitem3.setTextAlignment(3, Qt.AlignTrailing|Qt.AlignVCenter);
		__qtreewidgetitem3.setText(2, u"Missing");
		__qtreewidgetitem3.setTextAlignment(2, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem3.setIcon(2, icon13);
		__qtreewidgetitem3.setTextAlignment(1, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem3.setIcon(1, icon12);
		__qtreewidgetitem3.setText(0, u"20230109-0530");
		__qtreewidgetitem3.setIcon(0, icon8);
		__qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem1)
		__qtreewidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
		__qtreewidgetitem4.setText(2, u"Found");
		__qtreewidgetitem4.setIcon(2, icon14);
		__qtreewidgetitem4.setText(1, u"20");
		__qtreewidgetitem4.setIcon(1, icon1);
		__qtreewidgetitem4.setText(0, u"20230109-0030");
		__qtreewidgetitem4.setFont(0, font3);
		__qtreewidgetitem4.setIcon(0, icon8);
		__qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem1)
		__qtreewidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
		__qtreewidgetitem5.setBackground(6, brush);
		__qtreewidgetitem5.setIcon(6, icon16);
		__qtreewidgetitem5.setBackground(5, brush);
		__qtreewidgetitem5.setIcon(5, icon16);
		__qtreewidgetitem5.setBackground(4, brush);
		__qtreewidgetitem5.setIcon(4, icon16);
		__qtreewidgetitem5.setTextAlignment(3, Qt.AlignLeading|Qt.AlignVCenter);
		__qtreewidgetitem5.setBackground(3, brush);
		__qtreewidgetitem5.setIcon(3, icon11);
		__qtreewidgetitem5.setText(2, u"3D: 0.0021");
		__qtreewidgetitem5.setBackground(2, brush);
		__qtreewidgetitem5.setIcon(2, icon15);
		__qtreewidgetitem5.setText(1, u"27");
		__qtreewidgetitem5.setBackground(1, brush);
		__qtreewidgetitem5.setIcon(1, icon9);
		__qtreewidgetitem5.setText(0, u"20230109-0010");
		__qtreewidgetitem5.setBackground(0, brush);
		__qtreewidgetitem5.setIcon(0, icon8);
		self.treeWidget.setObjectName(u"treeWidget")
		sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
		sizePolicy4.setHorizontalStretch(0)
		sizePolicy4.setVerticalStretch(0)
		sizePolicy4.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
		self.treeWidget.setSizePolicy(sizePolicy4)
		self.treeWidget.setMinimumSize(QSize(580, 500))
		self.treeWidget.setMaximumSize(QSize(16777215, 600))
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
		sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
		sizePolicy5.setHorizontalStretch(0)
		sizePolicy5.setVerticalStretch(0)
		sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
		self.label_2.setSizePolicy(sizePolicy5)
		self.label_2.setMaximumSize(QSize(16777215, 30))
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
		sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
		sizePolicy6.setHorizontalStretch(0)
		sizePolicy6.setVerticalStretch(0)
		sizePolicy6.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
		self.checkBox_4.setSizePolicy(sizePolicy6)
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
		sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy7.setHorizontalStretch(0)
		sizePolicy7.setVerticalStretch(0)
		sizePolicy7.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
		self.pushButton_3.setSizePolicy(sizePolicy7)
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
		sizePolicy6.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
		self.pushButton_2.setSizePolicy(sizePolicy6)
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
		sizePolicy5.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
		self.label_8.setSizePolicy(sizePolicy5)
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
		sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		sizePolicy8.setHorizontalStretch(0)
		sizePolicy8.setVerticalStretch(0)
		sizePolicy8.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
		self.progressBar.setSizePolicy(sizePolicy8)
		self.progressBar.setMinimum(0)
		self.progressBar.setMaximum(10)
		self.progressBar.setValue(0)
		self.progressBar.setTextVisible(False)
		self.progressBar.setOrientation(Qt.Horizontal)
		self.progressBar.setTextDirection(QProgressBar.TopToBottom)

		self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 1)

		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setSpacing(5)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.lineEdit = QLineEdit(self.verticalLayoutWidget)
		self.lineEdit.setObjectName(u"lineEdit")
		self.lineEdit.setEnabled(False)
		sizePolicy8.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
		self.lineEdit.setSizePolicy(sizePolicy8)
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
		sizePolicy6.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
		self.pushButton.setSizePolicy(sizePolicy6)
		self.pushButton.setMinimumSize(QSize(0, 30))
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
		sizePolicy6.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
		self.pushButton_4.setSizePolicy(sizePolicy6)
		self.pushButton_4.setMinimumSize(QSize(0, 30))
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
		self.horizontalLayout_16 = QHBoxLayout()
		self.horizontalLayout_16.setSpacing(5)
		self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
		self.checkBox_pcloud = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_pcloud.setObjectName(u"checkBox_pcloud")
		self.checkBox_pcloud.setEnabled(True)
		sizePolicy7.setHeightForWidth(self.checkBox_pcloud.sizePolicy().hasHeightForWidth())
		self.checkBox_pcloud.setSizePolicy(sizePolicy7)
		self.checkBox_pcloud.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_pcloud.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Build Point Cloud</p><p><span style=\" font-weight:600;\">Disabled:</span> Skip...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_pcloud.setText(u"Build Point Cloud")
		icon23 = QIcon()
		icon23.addFile(u":/icons/icons8-live-photos-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_pcloud.setIcon(icon23)
		self.checkBox_pcloud.setIconSize(QSize(21, 21))
		self.checkBox_pcloud.setCheckable(True)
		self.checkBox_pcloud.setChecked(False)
		self.checkBox_pcloud.setTristate(False)

		self.horizontalLayout_16.addWidget(self.checkBox_pcloud)

		self.pushButton_setPCloud = QPushButton(self.verticalLayoutWidget)
		self.pushButton_setPCloud.setObjectName(u"pushButton_setPCloud")
		self.pushButton_setPCloud.setEnabled(False)
		sizePolicy6.setHeightForWidth(self.pushButton_setPCloud.sizePolicy().hasHeightForWidth())
		self.pushButton_setPCloud.setSizePolicy(sizePolicy6)
		self.pushButton_setPCloud.setCursor(QCursor(Qt.PointingHandCursor))
		icon24 = QIcon()
		icon24.addFile(u":/icons/icons8-adjust-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_setPCloud.setIcon(icon24)
		self.pushButton_setPCloud.setFlat(True)

		self.horizontalLayout_16.addWidget(self.pushButton_setPCloud)


		self.gridLayout_3.addLayout(self.horizontalLayout_16, 29, 0, 1, 1)

		self.horizontalLayout_15 = QHBoxLayout()
		self.horizontalLayout_15.setSpacing(5)
		self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
		self.checkBox_export = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_export.setObjectName(u"checkBox_export")
		self.checkBox_export.setEnabled(True)
		sizePolicy7.setHeightForWidth(self.checkBox_export.sizePolicy().hasHeightForWidth())
		self.checkBox_export.setSizePolicy(sizePolicy7)
		self.checkBox_export.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_export.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Export selected data after build is complete.</p><p><span style=\" font-weight:600;\">Disabled:</span> Skip...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_export.setText(u"Data Export")
		icon25 = QIcon()
		icon25.addFile(u":/icons/icons8-share-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_export.setIcon(icon25)
		self.checkBox_export.setIconSize(QSize(21, 21))
		self.checkBox_export.setCheckable(True)
		self.checkBox_export.setChecked(False)
		self.checkBox_export.setTristate(False)

		self.horizontalLayout_15.addWidget(self.checkBox_export)

		self.pushButton_setExport = QPushButton(self.verticalLayoutWidget)
		self.pushButton_setExport.setObjectName(u"pushButton_setExport")
		self.pushButton_setExport.setEnabled(False)
		sizePolicy6.setHeightForWidth(self.pushButton_setExport.sizePolicy().hasHeightForWidth())
		self.pushButton_setExport.setSizePolicy(sizePolicy6)
		self.pushButton_setExport.setCursor(QCursor(Qt.PointingHandCursor))
		icon26 = QIcon()
		icon26.addFile(u":/icons/icons8-true-false-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_setExport.setIcon(icon26)
		self.pushButton_setExport.setFlat(True)

		self.horizontalLayout_15.addWidget(self.pushButton_setExport)


		self.gridLayout_3.addLayout(self.horizontalLayout_15, 31, 0, 1, 1)

		self.label_17 = QLabel(self.verticalLayoutWidget)
		self.label_17.setObjectName(u"label_17")
		sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
		self.label_17.setSizePolicy(sizePolicy2)
		self.label_17.setMaximumSize(QSize(16777215, 30))
		font7 = QFont()
		font7.setFamily(u"Segoe UI")
		font7.setPointSize(11)
		font7.setBold(True)
		font7.setWeight(75)
		self.label_17.setFont(font7)
		self.label_17.setFrameShape(QFrame.NoFrame)
		self.label_17.setText(u"Processing")
		self.label_17.setIndent(5)

		self.gridLayout_3.addWidget(self.label_17, 23, 0, 1, 1)

		self.line_3 = QFrame(self.verticalLayoutWidget)
		self.line_3.setObjectName(u"line_3")
		self.line_3.setFrameShadow(QFrame.Plain)
		self.line_3.setFrameShape(QFrame.HLine)

		self.gridLayout_3.addWidget(self.line_3, 13, 0, 1, 1)

		self.label_4 = QLabel(self.verticalLayoutWidget)
		self.label_4.setObjectName(u"label_4")
		sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
		self.label_4.setSizePolicy(sizePolicy2)
		self.label_4.setMaximumSize(QSize(16777215, 30))
		self.label_4.setFont(font7)
		self.label_4.setFrameShape(QFrame.NoFrame)
		self.label_4.setText(u"Camera")
		self.label_4.setIndent(5)

		self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

		self.horizontalLayout_14 = QHBoxLayout()
		self.horizontalLayout_14.setSpacing(5)
		self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
		self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_3.setObjectName(u"checkBox_3")
		sizePolicy7.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
		self.checkBox_3.setSizePolicy(sizePolicy7)
		self.checkBox_3.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_3.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Automatic chunk creation with predefined settings</p><p><span style=\" font-weight:600;\">Disabled:</span> Manual confirmation of intermediate steps</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_3.setText(u"Auto Import Processing")
		icon27 = QIcon()
		icon27.addFile(u":/icons/icons8-in-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_3.setIcon(icon27)
		self.checkBox_3.setIconSize(QSize(21, 21))
		self.checkBox_3.setCheckable(True)
		self.checkBox_3.setChecked(True)

		self.horizontalLayout_14.addWidget(self.checkBox_3)


		self.gridLayout_3.addLayout(self.horizontalLayout_14, 25, 0, 1, 1)

		self.horizontalLayout_18 = QHBoxLayout()
		self.horizontalLayout_18.setSpacing(5)
		self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
		self.checkBox_5 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_5.setObjectName(u"checkBox_5")
		self.checkBox_5.setEnabled(False)
		sizePolicy7.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
		self.checkBox_5.setSizePolicy(sizePolicy7)
		self.checkBox_5.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_5.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Automatic chunk creation with predefined settings</p><p><span style=\" font-weight:600;\">Disabled:</span> Manual confirmation of intermediate steps</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_5.setText(u"Import New Data")
		icon28 = QIcon()
		icon28.addFile(u":/icons/icons8-move-to-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_5.setIcon(icon28)
		self.checkBox_5.setIconSize(QSize(21, 21))
		self.checkBox_5.setCheckable(True)
		self.checkBox_5.setChecked(False)

		self.horizontalLayout_18.addWidget(self.checkBox_5)


		self.gridLayout_3.addLayout(self.horizontalLayout_18, 24, 0, 1, 1)

		self.horizontalLayout_8 = QHBoxLayout()
		self.horizontalLayout_8.setSpacing(5)
		self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
		self.cbChunkSettings = QComboBox(self.verticalLayoutWidget)
		icon29 = QIcon()
		icon29.addFile(u":/icons/icons8-add-tab-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbChunkSettings.addItem(icon29, u"Default")
		icon30 = QIcon()
		icon30.addFile(u":/icons/kalota_m.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbChunkSettings.addItem(icon30, u"KALOTA")
		icon31 = QIcon()
		icon31.addFile(u":/icons/stopnca_o.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbChunkSettings.addItem(icon31, u"STOPNICA - IZKOP")
		icon32 = QIcon()
		icon32.addFile(u":/icons/stopnca_s.png", QSize(), QIcon.Normal, QIcon.Off)
		self.cbChunkSettings.addItem(icon32, u"STOPNICA - B.BET.")
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
		icon33 = QIcon()
		icon33.addFile(u":/icons/icons8-christmas-star-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.btnDefChunk.setIcon(icon33)
		self.btnDefChunk.setIconSize(QSize(20, 20))
		self.btnDefChunk.setAutoDefault(False)
		self.btnDefChunk.setFlat(False)

		self.horizontalLayout_8.addWidget(self.btnDefChunk)


		self.gridLayout_3.addLayout(self.horizontalLayout_8, 8, 0, 1, 1)

		self.line_2 = QFrame(self.verticalLayoutWidget)
		self.line_2.setObjectName(u"line_2")
		self.line_2.setFrameShadow(QFrame.Plain)
		self.line_2.setFrameShape(QFrame.HLine)

		self.gridLayout_3.addWidget(self.line_2, 22, 0, 1, 1)

		self.line_6 = QFrame(self.verticalLayoutWidget)
		self.line_6.setObjectName(u"line_6")
		self.line_6.setFrameShape(QFrame.HLine)
		self.line_6.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line_6, 26, 0, 1, 1)

		self.horizontalLayout_13 = QHBoxLayout()
		self.horizontalLayout_13.setSpacing(5)
		self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
		self.checkBox_mesh = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_mesh.setObjectName(u"checkBox_mesh")
		self.checkBox_mesh.setEnabled(True)
		sizePolicy7.setHeightForWidth(self.checkBox_mesh.sizePolicy().hasHeightForWidth())
		self.checkBox_mesh.setSizePolicy(sizePolicy7)
		self.checkBox_mesh.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_mesh.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Build Mesh and Textures</p><p><span style=\" font-weight:600;\">Disabled:</span> Skip...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_mesh.setText(u"Build Mesh && Textures")
		icon34 = QIcon()
		icon34.addFile(u":/icons/icons8-national-park-48.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox_mesh.setIcon(icon34)
		self.checkBox_mesh.setIconSize(QSize(21, 21))
		self.checkBox_mesh.setCheckable(True)
		self.checkBox_mesh.setChecked(False)
		self.checkBox_mesh.setTristate(False)

		self.horizontalLayout_13.addWidget(self.checkBox_mesh)

		self.pushButton_setMesh = QPushButton(self.verticalLayoutWidget)
		self.pushButton_setMesh.setObjectName(u"pushButton_setMesh")
		self.pushButton_setMesh.setEnabled(False)
		sizePolicy6.setHeightForWidth(self.pushButton_setMesh.sizePolicy().hasHeightForWidth())
		self.pushButton_setMesh.setSizePolicy(sizePolicy6)
		self.pushButton_setMesh.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_setMesh.setIcon(icon24)
		self.pushButton_setMesh.setFlat(True)

		self.horizontalLayout_13.addWidget(self.pushButton_setMesh)


		self.gridLayout_3.addLayout(self.horizontalLayout_13, 28, 0, 1, 1)

		self.horizontalLayout_7 = QHBoxLayout()
		self.horizontalLayout_7.setSpacing(5)
		self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
		self.label_13 = QLabel(self.verticalLayoutWidget)
		self.label_13.setObjectName(u"label_13")
		font8 = QFont()
		font8.setFamily(u"Segoe UI")
		font8.setPointSize(9)
		font8.setBold(False)
		font8.setWeight(50)
		self.label_13.setFont(font8)
		self.label_13.setText(u"SubType:")
		self.label_13.setIndent(10)

		self.horizontalLayout_7.addWidget(self.label_13)

		self.label_14 = QLabel(self.verticalLayoutWidget)
		self.label_14.setObjectName(u"label_14")
		sizePolicy5.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
		self.label_14.setSizePolicy(sizePolicy5)
		self.label_14.setMinimumSize(QSize(0, 20))
		self.label_14.setMaximumSize(QSize(16777215, 20))
		font9 = QFont()
		font9.setFamily(u"Segoe UI")
		font9.setPointSize(8)
		self.label_14.setFont(font9)
		self.label_14.setFrameShape(QFrame.NoFrame)
		self.label_14.setText(u"")

		self.horizontalLayout_7.addWidget(self.label_14)


		self.gridLayout_3.addLayout(self.horizontalLayout_7, 5, 0, 1, 1)

		self.line_5 = QFrame(self.verticalLayoutWidget)
		self.line_5.setObjectName(u"line_5")
		self.line_5.setFrameShadow(QFrame.Plain)
		self.line_5.setFrameShape(QFrame.HLine)

		self.gridLayout_3.addWidget(self.line_5, 6, 0, 1, 1)

		self.horizontalLayout_19 = QHBoxLayout()
		self.horizontalLayout_19.setSpacing(5)
		self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
		self.label_20 = QLabel(self.verticalLayoutWidget)
		self.label_20.setObjectName(u"label_20")
		self.label_20.setFont(font8)
		self.label_20.setText(u"Data Export:")
		self.label_20.setIndent(10)

		self.horizontalLayout_19.addWidget(self.label_20)

		self.label_expFolder = QLabel(self.verticalLayoutWidget)
		self.label_expFolder.setObjectName(u"label_expFolder")
		sizePolicy1.setHeightForWidth(self.label_expFolder.sizePolicy().hasHeightForWidth())
		self.label_expFolder.setSizePolicy(sizePolicy1)
		self.label_expFolder.setMinimumSize(QSize(200, 15))
		self.label_expFolder.setMaximumSize(QSize(200, 45))
		self.label_expFolder.setFont(font9)
		self.label_expFolder.setFrameShape(QFrame.NoFrame)
		self.label_expFolder.setText(u"")
		self.label_expFolder.setWordWrap(True)

		self.horizontalLayout_19.addWidget(self.label_expFolder)


		self.gridLayout_3.addLayout(self.horizontalLayout_19, 12, 0, 1, 1)

		self.horizontalLayout_12 = QHBoxLayout()
		self.horizontalLayout_12.setSpacing(5)
		self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
		self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
		icon35 = QIcon()
		icon35.addFile(u":/icons/icons8-full-page-view-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon35, u"Cam 1")
		icon36 = QIcon()
		icon36.addFile(u":/icons/icons8-video-wall-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon36, u"Cam 2")
		self.comboBox_2.addItem(icon23, u"Cam 3")
		icon37 = QIcon()
		icon37.addFile(u":/icons/icons8-aperture-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon37, u"Cam 4")
		icon38 = QIcon()
		icon38.addFile(u":/icons/icons8-video-stabilization-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon38, u"Cam 5")
		icon39 = QIcon()
		icon39.addFile(u":/icons/icons8-quadcopter-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.comboBox_2.addItem(icon39, u"Cam 6")
		self.comboBox_2.setObjectName(u"comboBox_2")
		sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
		sizePolicy10.setHorizontalStretch(0)
		sizePolicy10.setVerticalStretch(0)
		sizePolicy10.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
		self.comboBox_2.setSizePolicy(sizePolicy10)
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
		self.btnDefCam.setIcon(icon33)
		self.btnDefCam.setIconSize(QSize(20, 20))
		self.btnDefCam.setAutoDefault(False)
		self.btnDefCam.setFlat(False)

		self.horizontalLayout_12.addWidget(self.btnDefCam)


		self.gridLayout_3.addLayout(self.horizontalLayout_12, 3, 0, 1, 1)

		self.label_5 = QLabel(self.verticalLayoutWidget)
		self.label_5.setObjectName(u"label_5")
		sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
		self.label_5.setSizePolicy(sizePolicy2)
		self.label_5.setMaximumSize(QSize(16777215, 30))
		self.label_5.setFont(font7)
		self.label_5.setFrameShape(QFrame.NoFrame)
		self.label_5.setText(u"Markers")
		self.label_5.setIndent(5)

		self.gridLayout_3.addWidget(self.label_5, 19, 0, 1, 1)

		self.checkBox = QCheckBox(self.verticalLayoutWidget)
		self.checkBox.setObjectName(u"checkBox")
		sizePolicy2.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
		self.checkBox.setSizePolicy(sizePolicy2)
		self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Marker coordinates will be imported after target detection. <span style=\" font-weight:600;\">*</span></p><p><span style=\" font-weight:600;\">Disabled:</span> Coordinates are not imported. User must manually import coordinates.</p><p><span style=\" font-weight:600;\">*</span> Automatic importing of marker coordinates only works if point file name is the same as it's parent folder name, and contains a header with metadata. Point coordinates should start at row #7.</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox.setText(u"Import Marker Coordinates")
		icon40 = QIcon()
		icon40.addFile(u":/icons/icons8-map-marker-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.checkBox.setIcon(icon40)
		self.checkBox.setIconSize(QSize(21, 21))
		self.checkBox.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox, 21, 0, 1, 1)

		self.horizontalLayout_11 = QHBoxLayout()
		self.horizontalLayout_11.setSpacing(5)
		self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
		self.checkBox_align = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_align.setObjectName(u"checkBox_align")
		self.checkBox_align.setEnabled(True)
		sizePolicy7.setHeightForWidth(self.checkBox_align.sizePolicy().hasHeightForWidth())
		self.checkBox_align.setSizePolicy(sizePolicy7)
		self.checkBox_align.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_align.setToolTip(u"<html><head/><body><p><span style=\" font-weight:600;\">Enabled:</span> Align Photos after import.</p><p><span style=\" font-weight:600;\">Disabled:</span> Skip...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_align.setText(u"Align Photos")
		self.checkBox_align.setIcon(icon4)
		self.checkBox_align.setIconSize(QSize(21, 21))
		self.checkBox_align.setCheckable(True)
		self.checkBox_align.setChecked(False)
		self.checkBox_align.setTristate(False)

		self.horizontalLayout_11.addWidget(self.checkBox_align)

		self.pushButton_setAlign = QPushButton(self.verticalLayoutWidget)
		self.pushButton_setAlign.setObjectName(u"pushButton_setAlign")
		self.pushButton_setAlign.setEnabled(False)
		sizePolicy6.setHeightForWidth(self.pushButton_setAlign.sizePolicy().hasHeightForWidth())
		self.pushButton_setAlign.setSizePolicy(sizePolicy6)
		self.pushButton_setAlign.setCursor(QCursor(Qt.PointingHandCursor))
		self.pushButton_setAlign.setIcon(icon24)
		self.pushButton_setAlign.setFlat(True)

		self.horizontalLayout_11.addWidget(self.pushButton_setAlign)


		self.gridLayout_3.addLayout(self.horizontalLayout_11, 27, 0, 1, 1)

		self.line_7 = QFrame(self.verticalLayoutWidget)
		self.line_7.setObjectName(u"line_7")
		self.line_7.setFrameShape(QFrame.HLine)
		self.line_7.setFrameShadow(QFrame.Sunken)

		self.gridLayout_3.addWidget(self.line_7, 30, 0, 1, 1)

		self.horizontalLayout_5 = QHBoxLayout()
		self.horizontalLayout_5.setSpacing(5)
		self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
		self.label_11 = QLabel(self.verticalLayoutWidget)
		self.label_11.setObjectName(u"label_11")
		self.label_11.setFont(font8)
		self.label_11.setText(u"Prefix:")
		self.label_11.setIndent(10)

		self.horizontalLayout_5.addWidget(self.label_11)

		self.label_6 = QLabel(self.verticalLayoutWidget)
		self.label_6.setObjectName(u"label_6")
		sizePolicy5.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
		self.label_6.setSizePolicy(sizePolicy5)
		self.label_6.setMinimumSize(QSize(0, 20))
		self.label_6.setMaximumSize(QSize(16777215, 20))
		self.label_6.setFont(font9)
		self.label_6.setFrameShape(QFrame.NoFrame)
		self.label_6.setText(u"")

		self.horizontalLayout_5.addWidget(self.label_6)


		self.gridLayout_3.addLayout(self.horizontalLayout_5, 9, 0, 1, 1)

		self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
		self.checkBox_2.setObjectName(u"checkBox_2")
		sizePolicy2.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
		self.checkBox_2.setSizePolicy(sizePolicy2)
		self.checkBox_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
		self.checkBox_2.setToolTip(u"<html><head/><body><p>Enable automatic target detection when new chunk is created...</p></body></html>")
#endif // QT_CONFIG(tooltip)
		self.checkBox_2.setText(u"Automatic Target Detection")
		self.checkBox_2.setIcon(icon15)
		self.checkBox_2.setIconSize(QSize(21, 21))
		self.checkBox_2.setChecked(True)

		self.gridLayout_3.addWidget(self.checkBox_2, 20, 0, 1, 1)

		self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

		self.gridLayout_3.addItem(self.verticalSpacer, 34, 0, 1, 1)

		self.horizontalLayout_6 = QHBoxLayout()
		self.horizontalLayout_6.setSpacing(5)
		self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
		self.label_9 = QLabel(self.verticalLayoutWidget)
		self.label_9.setObjectName(u"label_9")
		self.label_9.setFont(font8)
		self.label_9.setFrameShape(QFrame.NoFrame)
		self.label_9.setText(u"Type:")
		self.label_9.setIndent(10)

		self.horizontalLayout_6.addWidget(self.label_9)

		self.label_12 = QLabel(self.verticalLayoutWidget)
		self.label_12.setObjectName(u"label_12")
		sizePolicy5.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
		self.label_12.setSizePolicy(sizePolicy5)
		self.label_12.setMinimumSize(QSize(0, 20))
		self.label_12.setMaximumSize(QSize(16777215, 20))
		self.label_12.setFont(font9)
		self.label_12.setFrameShape(QFrame.NoFrame)
		self.label_12.setText(u"")

		self.horizontalLayout_6.addWidget(self.label_12)


		self.gridLayout_3.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)

		self.horizontalLayout_3 = QHBoxLayout()
		self.horizontalLayout_3.setSpacing(5)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.label_10 = QLabel(self.verticalLayoutWidget)
		self.label_10.setObjectName(u"label_10")
		self.label_10.setFont(font8)
		self.label_10.setText(u"Suffix:")
		self.label_10.setIndent(10)

		self.horizontalLayout_3.addWidget(self.label_10)

		self.label_7 = QLabel(self.verticalLayoutWidget)
		self.label_7.setObjectName(u"label_7")
		sizePolicy5.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
		self.label_7.setSizePolicy(sizePolicy5)
		self.label_7.setMinimumSize(QSize(0, 20))
		self.label_7.setMaximumSize(QSize(16777215, 20))
		self.label_7.setFont(font9)
		self.label_7.setFrameShape(QFrame.NoFrame)
		self.label_7.setText(u"")

		self.horizontalLayout_3.addWidget(self.label_7)


		self.gridLayout_3.addLayout(self.horizontalLayout_3, 10, 0, 1, 1)

		self.label = QLabel(self.verticalLayoutWidget)
		self.label.setObjectName(u"label")
		sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy2)
		self.label.setMaximumSize(QSize(16777215, 30))
		self.label.setFont(font7)
		self.label.setFrameShape(QFrame.NoFrame)
		self.label.setText(u"Chunk Creation Settings")
		self.label.setIndent(5)

		self.gridLayout_3.addWidget(self.label, 7, 0, 1, 1)

		self.horizontalLayout_10 = QHBoxLayout()
		self.horizontalLayout_10.setSpacing(5)
		self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
		self.label_18 = QLabel(self.verticalLayoutWidget)
		self.label_18.setObjectName(u"label_18")
		self.label_18.setFont(font8)
		self.label_18.setText(u"Name Format:")
		self.label_18.setIndent(10)

		self.horizontalLayout_10.addWidget(self.label_18)

		self.label_19 = QLabel(self.verticalLayoutWidget)
		self.label_19.setObjectName(u"label_19")
		sizePolicy5.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
		self.label_19.setSizePolicy(sizePolicy5)
		self.label_19.setMinimumSize(QSize(0, 20))
		self.label_19.setMaximumSize(QSize(16777215, 20))
		self.label_19.setFont(font9)
		self.label_19.setFrameShape(QFrame.NoFrame)
		self.label_19.setText(u"")

		self.horizontalLayout_10.addWidget(self.label_19)


		self.gridLayout_3.addLayout(self.horizontalLayout_10, 11, 0, 1, 1)

		self.horizontalLayout_20 = QHBoxLayout()
		self.horizontalLayout_20.setSpacing(5)
		self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
		self.pushButton_resetSet = QPushButton(self.verticalLayoutWidget)
		self.pushButton_resetSet.setObjectName(u"pushButton_resetSet")
		sizePolicy6.setHeightForWidth(self.pushButton_resetSet.sizePolicy().hasHeightForWidth())
		self.pushButton_resetSet.setSizePolicy(sizePolicy6)
		self.pushButton_resetSet.setText(u"Reset")
		icon41 = QIcon()
		icon41.addFile(u":/icons/icons8-rotate-48.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_resetSet.setIcon(icon41)
		self.pushButton_resetSet.setIconSize(QSize(20, 20))

		self.horizontalLayout_20.addWidget(self.pushButton_resetSet)

		self.pushButton_saveSet = QPushButton(self.verticalLayoutWidget)
		self.pushButton_saveSet.setObjectName(u"pushButton_saveSet")
		sizePolicy6.setHeightForWidth(self.pushButton_saveSet.sizePolicy().hasHeightForWidth())
		self.pushButton_saveSet.setSizePolicy(sizePolicy6)
		self.pushButton_saveSet.setText(u"Save")
		icon42 = QIcon()
		icon42.addFile(u":/icons/icons8-save-all-50.png", QSize(), QIcon.Normal, QIcon.Off)
		self.pushButton_saveSet.setIcon(icon42)
		self.pushButton_saveSet.setIconSize(QSize(20, 20))
		self.pushButton_saveSet.setAutoDefault(False)
		self.pushButton_saveSet.setFlat(False)

		self.horizontalLayout_20.addWidget(self.pushButton_saveSet)


		self.gridLayout_3.addLayout(self.horizontalLayout_20, 32, 0, 1, 1)


		self.gridLayout.addLayout(self.gridLayout_3, 0, 2, 3, 1)

		self.label_16 = QLabel(self.verticalLayoutWidget)
		self.label_16.setObjectName(u"label_16")
		sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
		self.label_16.setSizePolicy(sizePolicy2)
		self.label_16.setFont(font6)
		self.label_16.setFrameShape(QFrame.NoFrame)
		self.label_16.setText(u"<html><head/><body><p>Selected: <span style=\" font-weight:600;\">0</span></p></body></html>")

		self.gridLayout.addWidget(self.label_16, 3, 2, 1, 1)


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
		self.checkBox_align.toggled.connect(self.pushButton_setAlign.toggle)

		self.pushButton_3.setDefault(False)


		QMetaObject.connectSlotsByName(DialogBatchChunk)
	# setupUi

	def retranslateUi(self, DialogBatchChunk):

		__sortingEnabled = self.treeWidget.isSortingEnabled()
		self.treeWidget.setSortingEnabled(False)
		self.treeWidget.setSortingEnabled(__sortingEnabled)

		self.pushButton_setPCloud.setText("")
		self.pushButton_setExport.setText("")

		self.pushButton_setMesh.setText("")

		self.pushButton_setAlign.setText("")
		pass
	# retranslateUi

