# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiAddNewChunkQuick.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import qtresources_rc

class Ui_DialogAddChunkQuick(object):
    def setupUi(self, DialogAddChunkQuick):
        if not DialogAddChunkQuick.objectName():
            DialogAddChunkQuick.setObjectName(u"DialogAddChunkQuick")
        DialogAddChunkQuick.resize(310, 155)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogAddChunkQuick.sizePolicy().hasHeightForWidth())
        DialogAddChunkQuick.setSizePolicy(sizePolicy)
        DialogAddChunkQuick.setMinimumSize(QSize(310, 155))
        DialogAddChunkQuick.setMaximumSize(QSize(310, 155))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(9)
        DialogAddChunkQuick.setFont(font)
        DialogAddChunkQuick.setWindowTitle(u"Create New Chunk")
        self.verticalLayoutWidget = QWidget(DialogAddChunkQuick)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 295, 141))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelQuickAdd = QLabel(self.verticalLayoutWidget)
        self.labelQuickAdd.setObjectName(u"labelQuickAdd")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelQuickAdd.sizePolicy().hasHeightForWidth())
        self.labelQuickAdd.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.labelQuickAdd.setFont(font1)
        self.labelQuickAdd.setText(u"Create New Chunk")

        self.verticalLayout.addWidget(self.labelQuickAdd)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setText(u"Select chunk creation settings:")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label)

        self.cbChunkSettings = QComboBox(self.verticalLayoutWidget)
        icon = QIcon()
        icon.addFile(u":/icons/icons8-add-tab-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbChunkSettings.addItem(icon, u"New Chunk (Default)")
        icon1 = QIcon()
        icon1.addFile(u":/icons/kalota_m.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbChunkSettings.addItem(icon1, u"KALOTA")
        icon2 = QIcon()
        icon2.addFile(u":/icons/stopnca_o.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbChunkSettings.addItem(icon2, u"STOPNICA - IZKOP")
        icon3 = QIcon()
        icon3.addFile(u":/icons/stopnca_s.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbChunkSettings.addItem(icon3, u"STOPNICA - B.BET.")
        self.cbChunkSettings.setObjectName(u"cbChunkSettings")
        sizePolicy1.setHeightForWidth(self.cbChunkSettings.sizePolicy().hasHeightForWidth())
        self.cbChunkSettings.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(11)
        self.cbChunkSettings.setFont(font2)
        self.cbChunkSettings.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(statustip)
        self.cbChunkSettings.setStatusTip(u"Choose settings used for chunk creation...")
#endif // QT_CONFIG(statustip)
        self.cbChunkSettings.setCurrentText(u"New Chunk (Default)")
        self.cbChunkSettings.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.cbChunkSettings)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCreate = QPushButton(self.verticalLayoutWidget)
        self.btnCreate.setObjectName(u"btnCreate")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnCreate.sizePolicy().hasHeightForWidth())
        self.btnCreate.setSizePolicy(sizePolicy2)
        self.btnCreate.setText(u"Create")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-add-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCreate.setIcon(icon4)
        self.btnCreate.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btnCreate)

        self.checkBoxAutoProc = QCheckBox(self.verticalLayoutWidget)
        self.checkBoxAutoProc.setObjectName(u"checkBoxAutoProc")
        self.checkBoxAutoProc.setText(u"Auto Processing")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons8-in-progress-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBoxAutoProc.setIcon(icon5)
        self.checkBoxAutoProc.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxAutoProc)

        self.btnCancel = QPushButton(self.verticalLayoutWidget)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy2.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy2)
        self.btnCancel.setText(u"Cancel")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons8-cancel-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCancel.setIcon(icon6)
        self.btnCancel.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DialogAddChunkQuick)
        self.btnCancel.clicked.connect(DialogAddChunkQuick.reject)
    # setupUi

    def retranslateUi(self, DialogAddChunkQuick):

        pass
    # retranslateUi

