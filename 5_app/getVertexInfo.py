#################################################
#convert selected faces into vertices and get world location of each vertices 

import os
import re

import maya.cmds as cmds

class vertexInfo():
    def __init__(self):
        self.outerFaces = []
        self.innerFaces = []
        #self.verts = []
        
    
    def faceToVert(self, faces):
        verts = []
        for face in faces:
            verts.append(cmds.polyListComponentConversion(face, ff = True, tv = True))
        newVerts = []
        #objNCompile = face.split('[')[0]
        objName = face.split('.f')[0]

        for vert in verts:
            for v in vert:
                #break up into individual verts
                if ":" in v:  
                    nPCompile = re.compile(r'(\d+)') 
                    numbers = nPCompile.findall(v)
                    for i in range(int(numbers[0]), int(numbers[1])+1):
                        newVerts.append(objName + ".vtx[" +str(i) + ']')
                        i += 1
                else:
                    newVerts.append(v)
        return newVerts

    def getMirrorFace(self, face):
        faceLoc = cmds.xform(face, bb = True, q = True)
        smallestDiff = .5
        matchFace = ""
        #find face with the closest matching bounding box on 2 planes
        for oFace in self.outerFaces:
            oFaceLoc = cmds.xform(oFace, bb = True, q = True)
            match = 0
            diff = 0
            for i in range(5):
                diffN = abs(faceLoc[i] - oFaceLoc[i])
                if(diffN < .5):
                    match += 1
                    diff += diffN
                if(match == 4):
                    if(diff < smallestDiff):
                        matchFace = oFace
                        smallestDiff = diff
                elif(i > 3 & match < 2):
                    i = 5
                i+=1
        return matchFace

    def findMirrorVert(self, v, vertsList):
        vLoc = cmds.xform(v, t = True, q = True)
        smallestDiff = .5

        for vert in vertsList:
            vertLoc = cmds.xform(vert, t = True, q = True)
            match = 0
            diff = 0

            for i in range(2):
                diffN = abs(vLoc[i] - vertLoc[i])

                if(diffN < .5):
                    match += 1
                    diff += diffN

                if(match == 2):
                    if(diff < smallestDiff):
                        matchVert = vert
                        smallestDiff = diff
                i+=1
        return matchVert
    
    def moveVert(self, mirroredVerts):
        inner = [mirroredVerts[0], mirroredVerts[1], mirroredVerts[2], mirroredVerts[3]]
        outer = [mirroredVerts[4], mirroredVerts[5], mirroredVerts[6], mirroredVerts[7]]
        for v in inner:
            match = self.findMirrorVert(v, outer)
            newLoc = self.makeGeo(v, match)
            nPCompile = re.compile(r'(\d+)') 
            number = nPCompile.findall(v)[0]
            dupObject = "military_uniform3.vtx[" + number + "]"
            dup = cmds.select(dupObject)
            cmds.xform(t = newLoc)


    def makeGeo(self, innerv, outerv):
        inner =cmds.xform(innerv, t = True, q = True)
        outer = cmds.xform(outerv, t = True, q = True)

        if (outer[0] == inner[0]):
            x = outer[0]
        else:
            x = outer[0] - ((outer[0] - inner[0])/2)
        
        if (outer[1] == inner[1]):
            y = outer[outerv][1]
        else:
            y = (outer[1] - inner[1])/2 
            y = outer[1] - y
        
        if (outer[2] == inner[2]):
            z = outer[2]
        else:
            z = (outer[2] - inner[2])/2
            z = (outer[2] ) - z
        
        return([x, y, z])
                
    def test(self):
        self.outerFaces = ['military_uniform.f[11548]', 'military_uniform.f[11617]', 'military_uniform.f[12530]','military_uniform.f[12146]', 'military_uniform.f[12347]', 'military_uniform.f[12349]', ]

        mirrored = ['military_uniform.f[11218]']
        mirrored.append(self.getMirrorFace('military_uniform.f[11218]'))

        found = self.faceToVert(mirrored)
        self.moveVert(found)
        self.innerFaces = ['pCube1.f[9]', 'pCube1.f[12]', 'pCube1.f[13]', 'pCube1.f[5]']

        #innerVerts = self.faceToVert(innerFaces)

d = vertexInfo()
d.test()