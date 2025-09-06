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
# try:
#     test = __file__
# except NameError:
#     MY_SCRIPT_PATH = "C:\\Users\\apoll\\Desktop\\advPythonCourse\\5_app"
#     if MY_SCRIPT_PATH not in sys.path:
#         sys.path.append(MY_SCRIPT_PATH)

from DSObject import DSObject
from DSObjectJSON import DSObjectJSON
from getVertexInfo import getVertexInfo
import singleSidedGeoUI as script

#*******************************************************************
# VARIABLE
TITLE = os.path.splitext(os.path.basename(script.__file__))[0]

#*******************************************************************
# CLASS
class singleSidedGeoUI(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(singleSidedGeoUI, self).__init__(*args, **kwargs)
        # BUILD local ui path
        
        
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

        #load
        self.btnLoad.clicked.connect(self.load)

        #save
        self.btnSave.clicked.connect(self.saveFileDialog)
        self.progressBar.setValue(0)
        self.VI = ""
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
        try:
            self.doubleObj
        except:
            name = self.getName(faces[0])
            name = name.replace("Shape", "")
            self.doubleObj = DSObject(name)
            self.lineObject.setText(name)
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
        try:
            self.doubleObj
        except:
            name = self.getName(faces[0])
            name = name.replace("Shape", "")
            self.doubleObj = DSObject(name)
            self.lineObject.setText(name)
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
    
    def incrementProgress(self, v):
        self.progressBar.setValue(v)
    
    # create
    def create(self):
        self.VI = getVertexInfo(self.doubleObj, self)
        self.VI.start()

    def load(self):
        if self.btnLoad.text() == "Unload":
            self.unload()
        else:
            options = QtWidgets.QFileDialog.Options()
            self.fileReadName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Load JSON", "","All Files (*)", options=options)
            if self.fileReadName:
                print("Loading " + self.fileReadName)
                self.doubleObj = DSObjectJSON(self.fileReadName)
                self.lineObject.setText(self.doubleObj.getName())
                for face in self.doubleObj.getInnerFaces():
                    self.listInner.addItem(face)
                for face in self.doubleObj.getOuterFaces():
                    self.listOuter.addItem(face)

                self.btnLoad.setStyleSheet('background-color: Red;')
                self.btnLoad.setText("Unload")

    def unload(self):
        self.doubleObj.setPath(" ")
        self.doubleObj.setMatched(" ")
        self.btnLoad.setStyleSheet('background-color:  rgb(110, 110, 110);')
        self.btnLoad.setText("Load")

    def saveFileDialog(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setWindowTitle("Save JSON")
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptSave)
        file_dialog.setViewMode(QtWidgets.QFileDialog.ViewMode.Detail)

        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            if ".json" not in selected_file:
                selected_file = selected_file + ".json"
            self.VI.writeJSON(selected_file)
            print("Saved at: ", selected_file)
                
    def getName(self, face):
        objName = face.split('.f')[0]
        return objName

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

