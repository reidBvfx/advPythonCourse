#################################################
#create a duplicate of inner layer of mesh 

import os
import re

import maya.cmds as cmds

class duplicateInner():
    def __init__(self, ):
        pass

    def dupAndDel(self,obj, innerFaces, outerFaces):
        simMesh =cmds.duplicate(obj, n = (obj + "_SIM"))[0]
        
        #select all but inner face mesh
        
        cmds.select( clear=True )#clear anything selected
        cmds.select(obj + "_SIM" + ".f[*]")#select all faces
        #deselect all inner faces
        for face in innerFaces:
            faceSelect = (simMesh + ".f[" + str(face) + "]")
            cmds.select(faceSelect, deselect = True)
        cmds.delete()
        #cmds.delete(simMesh, constructionHistory = True)

    def test(self):
        outerFaces = [4, 7, 15, 10]
        objectName = "pCube1"
        innerFaces = [9, 12, 13,5]
        self.dupAndDel(objectName, innerFaces, outerFaces)

d = duplicateInner()
d.test()
        