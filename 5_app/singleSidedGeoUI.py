# STYLE ***************************************************************************
# content = UI setup for single sided mesh creation
#
# date    = 2025-07-20
#
# needs   =   - need to make collected info global for other modules to use
#           - see if best to use getter/setter functions or use global variables
# author  = Reid Bryan (reidwarhola@gmail.com)
#**********************************************************************************

import maya.cmds as cmds #type: ignore
import maya.OpenMayaUI as omui#type: ignore

import os
import sys


from Qt import QtWidgets, QtGui, QtCore, QtCompat
from shiboken2 import *



# don't delete!!!!doesn't work otherwise ----------------------------------
mw_ptr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(int(mw_ptr), QtWidgets.QMainWindow)
#--------------------------------------------------------------------------
try:
    test = __file__
except NameError:
    MY_SCRIPT_PATH = "C:\\Users\\apoll\\Desktop\\advPythonCourse\\5_app"
    if MY_SCRIPT_PATH not in sys.path:
        sys.path.append(MY_SCRIPT_PATH)

from DSObject import DSObject
from getVertexInfo import getVertexInfo
import singleSidedGeoUI as script

#*******************************************************************
# VARIABLE
try:
    TITLE = os.path.splitext(os.path.basename(__file__))[0]
    if(TITLE == ""):
        raise NameError
except NameError:
    TITLE = os.path.splitext(os.path.basename(script.__file__))[0]

TITLE = os.path.splitext(os.path.basename(script.__file__))[0]

#*******************************************************************
# CLASS
class singleSidedGeoUI(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(singleSidedGeoUI, self).__init__(*args, **kwargs)
        # BUILD local ui path
        
        try:
            path_ui = "/".join([os.path.dirname(__file__), "ui", TITLE + ".ui"])
        except:
             path_ui = "/".join([os.path.dirname(script.__file__), "ui", TITLE + ".ui"])
 
        # LOAD ui with absolute path
        QtCompat.loadUi(path_ui, self)

        # BUTTONS***********************************************************************
        self.btnAddSelectedObject.clicked.connect(self.addSel_obj)
        
        # for inner faces
        self.btnAddSelectedInner.clicked.connect(self.addSel_inner)
        self.btnRemoveInner.clicked.connect(self.removeSel_inner)
        self.btnClearAllInner.clicked.connect(self.clear_inner)

        # for outer faces
        self.btnAddSelectedOuter.clicked.connect(self.addSel_outer)
        self.btnRemoveOuter.clicked.connect(self.removeSel_outer)
        self.btnClearAllOuter.clicked.connect(self.clear_outer)
        
        # create
        self.btnCreate.clicked.connect(self.create)

        # SHOW the UI
        self.show()
        self.resize(500, 500)

    #************************************************************
    # PRESS
    def addSel_obj(self):
        name = cmds.ls(sl=1,sn=True)[0]
        self.lineObject.setText(name)
        try:
            self.doubleObj.setName(name)
        except AttributeError:
            self.doubleObj = DSObject(name)

    def addSel_inner(self):
        faces = cmds.ls(sl=1,sn=True)
        faces = self.doubleObj.setInnerFaceList(faces)
        for face in faces:
            self.listInner.addItem(face)

    def removeSel_inner(self):
        items = self.listInner.selectedItems()
        for item in items:
            row = self.listInner.row(item)
            self.listInner.takeItem(row)
            self.doubleObj.removeInnerFace(row)

    def clear_inner(self):
        self.listInner.clear()
        self.doubleObj.clearInnerFaces()

    def addSel_outer(self):
        faces = cmds.ls(sl=1,sn=True)
        faces = self.doubleObj.setOuterFaceList(faces)
        for face in faces:
            self.listOuter.addItem(face)
    
    def removeSel_outer(self):
        items = self.listOuter.selectedItems()
        for item in items:
            row = self.listOuter.row(item)
            self.doubleObj.removeOuterFace(row)
            self.listOuter.takeItem(row)

    def clear_outer(self):
        self.listOuter.clear()
        self.doubleObj.clearOuterFaces()
    # create
    def create(self):
        #print("length Inner : " + str((len(self.doubleObj.getInnerFaces()))))
        VI = getVertexInfo(self.doubleObj)
        VI.start()
        #print("pressed start")

def getMainWindow():
    mw_ptr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mw_ptr), QtWidgets.QMainWindow)
    return mayaMainWindow

def show():
    win = singleSidedGeoUI(parent = getMainWindow())
    win.setWindowFlags(QtCore.Qt.Window)
    win.show()  
    win = None


show()

