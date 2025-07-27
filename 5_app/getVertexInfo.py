# STYLE ***************************************************************************
# content = convert selected faces into vertices and get world location of each vertices 
#           then find matching faces/vertices and move duplicated mesh to be evenly between the inner and outer faces
# date    = 2025-07-25
#
#needed changes/additions(delete later):
#   get object name, innerFaces, and outerFaces from SSM_UI
#   create separate function for getting number from vertex name
#       or easier/cleaner way to select corresponding vert of duplicated geo
#   create clearer order of operations
#   simplify nested for loops for finding mirrored faces/verts
#**********************************************************************************



import os
import re

import maya.cmds as cmds

class vertexInfo():
    def __init__(self):
        self.outerFaces = []
        self.innerFaces = []
        #self.verts = []
        
    
    def faceToVert(self, faces):
        """
        Convert list of faces into list of corresponding vertices
            Reformat vertices list to meet standard naming convention

        Arguments:
            faces = [list of faces names]

        Returns:
            [list of [list of 4 connected vertices]]
            [[x1, x2, x3, x4], [y1 , y2, y3, y4]]
        """
        verts = []
        for face in faces:
            verts.append(cmds.polyListComponentConversion(face, ff = True, tv = True))
        newVerts = []
        objName = face.split('.f')[0]

        #break up into individual verts

        for vert in verts:
            for v in vert:
                #correct naming convention
                if ":" in v:  
                    nPCompile = re.compile(r'(\d+)') 
                    numbers = nPCompile.findall(v)
                    for i in range(int(numbers[0]), int(numbers[1])+1):
                        newVerts.append(objName + ".vtx[" +str(i) + ']')
                        i += 1
                else:
                    newVerts.append(v)
        return newVerts

    #takes in a single inner face name and compares against outerFaces
    def getMirrorFace(self, face):
        """
        Finds corresponding outer face to the given inner face. 
        The corresponding outer and inners faces will be nearly equal on 2 planes

        Arguments:
            face: inner face 

        Returns:
            matchFace: name of mirrored face that matches argument
        """
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
                # if 3 elements have been examined and only 1 matches it cannot be mirrored face
                # exit the loop    
                if(i == 3 & match < 2): 
                    i = 5    
                if(match == 4):
                    if(diff < smallestDiff):
                        matchFace = oFace
                        smallestDiff = diff
                
                i+=1
        return matchFace

    #arg1 : 1 vert from an inner face
    #arg2: list of all vert of the corresponding outer face
    def findMirrorVert(self, v, vertsList):
        """
        Compares location of two vertices to find which two are the closest to being mirror across 2 axises 
        
        Arguments: 
            v : 1 vert from an inner face
            vertsList : list of all vert of the corresponding outer face
        
        Returns:
            matchVert : name from matching vert within vertsList
        """
        #similar to findMirrorFace but use tranform instead of bounding box
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
        """
        Within for loop- for each inner vert
          1.find mirrored vert
          2. find {x,y,z} of the spot equidistant between the matching verts
          3. get the number of the inner vertex
          4. select corresponding vertex on duplicated geo  //currently hardcoded will need to be variable
          5. transform duplicated geo vert
        
        Arguments:
            mirredVerts = list of 8 verts. 0-3 belong to innerface and 4-7 belong to outer face
        
        Returns:
            nothing
        """
        inner = [mirroredVerts[0], mirroredVerts[1], mirroredVerts[2], mirroredVerts[3]]
        outer = [mirroredVerts[4], mirroredVerts[5], mirroredVerts[6], mirroredVerts[7]]
        for v in inner:
            match = self.findMirrorVert(v, outer)
            newLoc = self.findCenter(v, match)
            nPCompile = re.compile(r'(\d+)') 
            number = nPCompile.findall(v)[0]
            dupObject = "military_uniform3.vtx[" + number + "]"
            dup = cmds.select(dupObject)
            cmds.xform(t = newLoc)



    def findCenter(self, innerv, outerv):
        """
        Find the point in space equidistant to two given vertices

        Arguments:
            innerv: vertex from an inner face
            outerv: vertex from outer face

        Returns:
            list of x, y, and z coordinates
        """
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
        """
        is currently tested on geo that can be downloaded at https://www.turbosquid.com/3d-models/military-uniform-2418050
        """
        self.outerFaces = ['military_uniform.f[11548]', 'military_uniform.f[11617]', 'military_uniform.f[12530]','military_uniform.f[12146]', 'military_uniform.f[12347]', 'military_uniform.f[12349]', ]

        mirrored = ['military_uniform.f[11218]']
        mirrored.append(self.getMirrorFace('military_uniform.f[11218]'))

        found = self.faceToVert(mirrored)
        self.moveVert(found)
        self.innerFaces = ['pCube1.f[9]', 'pCube1.f[12]', 'pCube1.f[13]', 'pCube1.f[5]']

        #innerVerts = self.faceToVert(innerFaces)

d = vertexInfo()
d.test()