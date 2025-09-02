# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'singleSidedGeoUI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(670, 479)
        Form.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(90, 90, 90);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	\n"
"	text-align: left;\n"
"	ToolButtonPopupMode: 2;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(110, 110, 110);\n"
"	border: none;\n"
"	margin: 1px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QFrame{\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 255, 255);\n"
"	margin: 0;\n"
"}\n"
"QLabel{\n"
"	border:none;\n"
"}\n"
"QLineEdit{\n"
"	border: none;\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QListView{\n"
"	background-color: rgb(65, 65, 65);\n"
"	border: none;\n"
"}\n"
"\n"
"QSlider::groove{\n"
" 	height: 4px;\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"QSlider::handle{\n"
"	background: rgb(223, 223, 223);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 9px;\n"
"    margin: -8px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius:"
                        " 3px;\n"
"}\n"
"QToolButton::menu-button {\n"
"    border: 2px solid gray;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"}\n"
"QToolButton::menu-indicator { \n"
"image: none;\n"
" }\n"
"")
        self.actionShowHelp = QAction(Form)
        self.actionShowHelp.setObjectName(u"actionShowHelp")
        self.actionShowHelp.setCheckable(True)
        self.actionShowHelp.setMenuRole(QAction.NoRole)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.hl_ToolBar = QHBoxLayout()
        self.hl_ToolBar.setObjectName(u"hl_ToolBar")
        self.hl_ToolBar.setContentsMargins(-1, 0, -1, -1)
        self.btnSave = QPushButton(Form)
        self.btnSave.setObjectName(u"btnSave")

        self.hl_ToolBar.addWidget(self.btnSave)

        self.btnLoad = QPushButton(Form)
        self.btnLoad.setObjectName(u"btnLoad")
        self.btnLoad.setStyleSheet(u"text-align: left;")

        self.hl_ToolBar.addWidget(self.btnLoad)

        self.toolBtnHelp = QPushButton(Form)
        self.toolBtnHelp.setObjectName(u"toolBtnHelp")
        self.toolBtnHelp.setStyleSheet(u"text-align: left;")

        self.hl_ToolBar.addWidget(self.toolBtnHelp)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl_ToolBar.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.hl_ToolBar)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.labelObject = QLabel(Form)
        self.labelObject.setObjectName(u"labelObject")
        self.labelObject.setFrameShape(QFrame.HLine)
        self.labelObject.setFrameShadow(QFrame.Raised)
        self.labelObject.setLineWidth(0)

        self.horizontalLayout_3.addWidget(self.labelObject)

        self.lineObject = QLineEdit(Form)
        self.lineObject.setObjectName(u"lineObject")
        self.lineObject.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_3.addWidget(self.lineObject)

        self.btnAddSelectedObject = QPushButton(Form)
        self.btnAddSelectedObject.setObjectName(u"btnAddSelectedObject")

        self.horizontalLayout_3.addWidget(self.btnAddSelectedObject)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.btnInnerFaces = QPushButton(Form)
        self.btnInnerFaces.setObjectName(u"btnInnerFaces")
        self.btnInnerFaces.setStyleSheet(u"background-color: rgb(136, 105, 105);")

        self.verticalLayout_2.addWidget(self.btnInnerFaces)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.listInner = QListWidget(self.frame)
        self.listInner.setObjectName(u"listInner")

        self.horizontalLayout_2.addWidget(self.listInner)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnAddSelectedInner = QPushButton(self.frame)
        self.btnAddSelectedInner.setObjectName(u"btnAddSelectedInner")

        self.verticalLayout_3.addWidget(self.btnAddSelectedInner)

        self.btnRemoveInner = QPushButton(self.frame)
        self.btnRemoveInner.setObjectName(u"btnRemoveInner")

        self.verticalLayout_3.addWidget(self.btnRemoveInner)

        self.btnClearAllInner = QPushButton(self.frame)
        self.btnClearAllInner.setObjectName(u"btnClearAllInner")

        self.verticalLayout_3.addWidget(self.btnClearAllInner)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.btnOuterFaces = QPushButton(Form)
        self.btnOuterFaces.setObjectName(u"btnOuterFaces")
        self.btnOuterFaces.setStyleSheet(u"background-color: rgb(136, 105, 105);")

        self.verticalLayout_6.addWidget(self.btnOuterFaces)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.listOuter = QListWidget(self.frame_2)
        self.listOuter.setObjectName(u"listOuter")

        self.horizontalLayout.addWidget(self.listOuter)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btnAddSelectedOuter = QPushButton(self.frame_2)
        self.btnAddSelectedOuter.setObjectName(u"btnAddSelectedOuter")

        self.verticalLayout_8.addWidget(self.btnAddSelectedOuter)

        self.btnRemoveOuter = QPushButton(self.frame_2)
        self.btnRemoveOuter.setObjectName(u"btnRemoveOuter")

        self.verticalLayout_8.addWidget(self.btnRemoveOuter)

        self.btnClearAllOuter = QPushButton(self.frame_2)
        self.btnClearAllOuter.setObjectName(u"btnClearAllOuter")

        self.verticalLayout_8.addWidget(self.btnClearAllOuter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.vl_Ghosting = QVBoxLayout()
        self.vl_Ghosting.setObjectName(u"vl_Ghosting")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.btnCreate = QPushButton(Form)
        self.btnCreate.setObjectName(u"btnCreate")
        self.btnCreate.setMinimumSize(QSize(0, 40))

        self.verticalLayout_5.addWidget(self.btnCreate)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_5.addWidget(self.progressBar)

        self.verticalLayout_5.setStretch(0, 1)

        self.vl_Ghosting.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.vl_Ghosting)

        self.verticalLayout.setStretch(3, 4)
        self.verticalLayout.setStretch(4, 4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"SingleSidedMesh Creation", None))
        self.actionShowHelp.setText(QCoreApplication.translate("Form", u"ShowHelp", None))
        self.btnSave.setText(QCoreApplication.translate("Form", u"Save", None))
        self.btnLoad.setText(QCoreApplication.translate("Form", u"Load", None))
        self.toolBtnHelp.setText(QCoreApplication.translate("Form", u"Help", None))
        self.labelObject.setText(QCoreApplication.translate("Form", u"Object:", None))
        self.btnAddSelectedObject.setText(QCoreApplication.translate("Form", u"Add Selected", None))
        self.btnInnerFaces.setText(QCoreApplication.translate("Form", u"Inner Faces", None))
        self.btnAddSelectedInner.setText(QCoreApplication.translate("Form", u"Add Selected Meshes", None))
        self.btnRemoveInner.setText(QCoreApplication.translate("Form", u"Remove Highlighted", None))
        self.btnClearAllInner.setText(QCoreApplication.translate("Form", u"Clear All", None))
        self.btnOuterFaces.setText(QCoreApplication.translate("Form", u"Outer Faces", None))
        self.btnAddSelectedOuter.setText(QCoreApplication.translate("Form", u"Add Selected Meshes", None))
        self.btnRemoveOuter.setText(QCoreApplication.translate("Form", u"Remove Highlighted", None))
        self.btnClearAllOuter.setText(QCoreApplication.translate("Form", u"Clear All", None))
        self.btnCreate.setText(QCoreApplication.translate("Form", u"CREATE", None))
    # retranslateUi

