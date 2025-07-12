import os
import re
import maya.cmds as cmds
import array

print("hello world")
cmds.polySphere()



class vertexLocation():
    def __init__(self):
        pass
    def getOuterLoc(self):
        objName = cmds.ls(sl = True, fl =1)[0]
        objName = re.sub(r'\.f\[\d+\]', '', objName) #gets name of selected object
        print(objName)
        verts = self.getVerts() #returns list of all vert from selected faces
        vertLoc = {} #dictionary of all verts and their coordinates
        for each in verts:
            objVertN = objName + ".vtx[" + str(each) + ']' #name for specific vertex of selected obj
            loc = cmds.xform(objVertN, t = True, q = True)
            vertLoc[each] = loc #add each vert and location to dictionary
        print(vertLoc)
    
    def getVerts(self):
        #convert faces into verts
        vertsList = cmds.polyInfo( fe = True) 
        verts = []
        for each in vertsList:
            #separate out vertex from list that is "face #: v1 v2 v3 v4 \n"
            numbers = re.findall(r':\s+(.*)', each)
            #get list of non duplicated verts
            if numbers:
                vertsTemp = [int(num) for num in numbers[0].split()]
                for v in vertsTemp:   
                    if v not in verts:
                        verts.append(v)
        return verts
    def test(self):
        cmds.select('military_uniform.f[2450:3184]')
        self.getOuterLoc()


d = vertexLocation()
d.test()