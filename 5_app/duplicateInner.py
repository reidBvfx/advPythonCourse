# STYLE ***************************************************************************
#
# content = create a duplicate mesh's "inner faces"
#
# date    = 2025-07-20
#
# needed  = -list of inner faces - SSM_UI
#           -list of outer faces - SSM_UI
#           -name of selected mesh -SSM_UI
#           -split duplication and deletion
#           -need to duplicate geo move verts and then delete so that vertex names correspond to original geo
#**********************************************************************************

import maya.cmds as cmds

class duplicateInner():

    def dupAndDel(self,obj, innerFaces, outerFaces):
        """
        Creates a duplicated mesh of selected object and deletes faces to create a single sided mesh
        
        Arguments: 
            innerFaces = [names of all inner faces]
            outerFaces = [names of all outer faces]
        Returns:
            name of duplicated mesh
        """
        simMesh =cmds.duplicate(obj, n = (obj + "_SIM"))[0]
        
        # select all but inner face mesh
        cmds.select( clear=True )#clear anything selected
        cmds.select(obj + "_SIM" + ".f[*]")#select all faces
        
        # deselect all inner faces
        for face in innerFaces:
            faceSelect = (simMesh + ".f[" + str(face) + "]")
            cmds.select(faceSelect, deselect = True)
        cmds.delete()
        # cmds.delete(simMesh, constructionHistory = True)

        return simMesh

    def test(self):
        outerFaces = [4, 7, 15, 10]
        objectName = "pCube1"
        innerFaces = [9, 12, 13,5]
        self.dupAndDel(objectName, innerFaces, outerFaces)

d = duplicateInner()
d.test()
        