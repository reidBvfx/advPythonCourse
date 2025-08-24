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

import os
import sys
import webbrowser

from Qt import QtWidgets, QtGui, QtCore, QtCompat

#*******************************************************************
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]

#*******************************************************************
# CLASS
class singleSidedGeoUI():
    def __init__(self):
        # BUILD local ui path
        path_ui = "/".join([os.path.dirname(__file__), "ui", TITLE + ".ui"])

        # LOAD ui with absolute path
        self.wgUtil = QtCompat.loadUi(path_ui)

        # BUTTONS***********************************************************************
        self.wgUtil.btnAddSelectedObject.clicked.connect(self.addSel_obj)
        
        # for inner faces
        self.wgUtil.btnAddSelectedInner.clicked.connect(self.addSel_inner)
        self.wgUtil.btnRemoveInner.clicked.connect(self.removeSel_inner)
        self.wgUtil.btnClearAllInner.clicked.connect(self.clear_inner)

        # for outer faces
        self.wgUtil.btnAddSelectedOuter.clicked.connect(self.addSel_outer)
        self.wgUtil.btnRemoveOuter.clicked.connect(self.removeSel_outer)
        self.wgUtil.btnClearAllOuter.clicked.connect(self.clear_outer)
        
        # SHOW the UI
        self.wgUtil.show()

    #************************************************************
    # PRESS
    def addSel_obj(self):
        self.wgUtil.lineObject.setText(cmds.ls(sl=1,sn=True)[0])

    def addSel_inner(self):
        for face in cmds.ls(sl=1,sn=True):
            self.wgUtil.listInner.addItem(face)

    def removeSel_inner(self):
        items = self.wgUtil.listInner.selectedItems()
        for item in items:
            row = self.wgUtil.listInner.row(item)
            self.wgUtil.listInner.takeItem(row)

    def clear_inner(self):
        self.wgUtil.listInner.clear()

    def addSel_outer(self):
        for face in cmds.ls(sl=1,sn=True):
            self.wgUtil.listOuter.addItem(face)
    
    def removeSel_outer(self):
        items = self.wgUtil.listOuter.selectedItems()
        for item in items:
            row = self.wgUtil.listOuter.row(item)
            self.wgUtil.listOuter.takeItem(row)

    def clear_outer(self):
        self.wgUtil.listOuter.clear()
        
#*******************************************************************
# START
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    classVar = singleSidedGeoUI()
    app.exec_()
