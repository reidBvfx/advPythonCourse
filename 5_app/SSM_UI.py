# STYLE ***************************************************************************
# content = UI setup for single sided mesh creation
#
# date    = 2025-07-20
#
# needs   = - all need buttons and elements show on screen but is not intuitive or visually pleasing
#           - buttons for added outer faces and showing list 
#           - buttons are non-functional 
#           - need to collected selected faces/objects to corresponding buttons
#           - need to make collected info global for other modules to use
#           - see if best to use getter/setter functions or use global variables
#**********************************************************************************

import maya.cmds as cmds

class SSM_UI():
    def __init__(self, winName = "SSM", winTitle = 'SSM'):
        self.winName = winName
        self.winTitle = winTitle
        self.object = ""
        self.innerFaces = []
        self.outerFaces = []

    def ui_elem(self, args=None):
        """Creates all UI elements and calls function for button press
        
        args: 
            None
        """
        if cmds.window(self.winName, exists=True):
            cmds.deleteUI(self.winName)
        win = cmds.window(self.winName, title = self.winTitle)
        winFormat = cmds.formLayout()

        # buttons
        self.objNameButton = cmds.textFieldButtonGrp(label='Object Name:', text='', buttonLabel='Load Selected',w = 490, bc = self.getObjName)
        
        self.addInnerFaces = cmds.button(label='Add Selected Object', w = 120, h = 30)
        self.innerFacesList = cmds.cmdScrollFieldExecuter(width=200, height=100)
        
        # window formatting
        cmds.formLayout( winFormat, edit=True, attachForm=[(self.objNameButton, 'top', 120), (self.addInnerFaces, 'top', 220), (self.addInnerFaces, 'left', 220), (self.innerFacesList, 'top', 220),(self.innerFacesList, 'left', 360)])
        cmds.showWindow(self.winName)
        cmds.window(self.winName, edit=True, widthHeight = (1000, 600))

    def getObjName(self):
        """
        Returns:
            name of selected object
        """
        print("obj name")

    def start(self):
        self.ui_elem()

d = SSM_UI()
d.start()