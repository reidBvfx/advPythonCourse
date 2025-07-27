import os
import re

import maya.cmds as cmds

class SSM_UI():
    def __init__(self, winName = "SSM", winTitle = 'SSM'):
        self.winName = winName
        self.winTitle = winTitle
        self.object = ""
        self.innerFaces = []
        self.outerFaces = []

    def ui_elem(self, args = None):
        if cmds.window(self.winName, exists=True):
            cmds.deleteUI(self.winName)
        win = cmds.window(self.winName, title = self.winTitle)
        winFormat = cmds.formLayout()


        #buttons
        self.objNameButton = cmds.textFieldButtonGrp(label='Object Name:', text='', buttonLabel='Load Selected',w = 490, bc = self.getObjName)
        
        self.addInnerFaces = cmds.button(label='Add Selected Object', w = 120, h = 30)
        
        
        #self.addInnerFaces = cmds.button(label='Add Selected Faces', w = 120, h = 30)
        self.innerFacesList = cmds.cmdScrollFieldExecuter(width=200, height=100)
        
        
        #window formatting
        cmds.formLayout( winFormat, edit=True, attachForm=[(self.objNameButton, 'top', 120), (self.addInnerFaces, 'top', 220), (self.addInnerFaces, 'left', 220), (self.innerFacesList, 'top', 220),(self.innerFacesList, 'left', 360)])
        cmds.showWindow(self.winName)
        cmds.window(self.winName, edit=True, widthHeight = (1000, 600))

    def getObjName(self):
        print("obj name")
d = SSM_UI()
d.ui_elem()