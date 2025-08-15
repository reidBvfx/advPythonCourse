# STYLE ***************************************************************************
# content = convert selected faces into vertices and get world location of each vertices 
#           then find matching faces/vertices and move duplicated mesh to be evenly between the inner and 
#           outerfaces
# date    = 2025-07-25
# needed  = 
#           - simplify nested for loops for finding mirrored faces/verts
#           - make functional if a seam is single sided
#**********************************************************************************

import json
import time
import os 
import sys

import maya.cmds as cmds # type: ignore
sys.path.append(os.path.dirname(__file__))
from DSObject import DSObject as ds

class vertexInfo():
    def __init__(self, cloth):
        self.cloth = cloth
        
        self.unMatchedFaces = cloth.getInnerFaces()
        self.matchedFacesDict = {}
        self.matchedVertsDict = cloth.alreadyMatched()
        #path to export matching verts Dict
        self.json_pathWrite = os.path.join(os.path.dirname(__file__), 'configFiles//jacketMirroredVerts.json')
         
    def faceToVert(self, faces):
        """ Convert list of faces into list of corresponding vertices
            Reformat vertices list to meet standard naming convention
        
        Args: faces = [list of faces names]
        
        Returns:list of vertices
        """
        tempVerts = [] # raw verts list
        verts = [] # all verts with corrected names
        if type(faces) is not list:
            faces = [faces]
        
        for face in faces:
            tempVerts.append(cmds.polyListComponentConversion(face, ff = True, tv = True))
        # break up into individual verts
        for vert in tempVerts:
            tempVerts = self.cloth.correctNameVertex(vert)
            for each in tempVerts:
                verts.append(each)
        return verts

    def getMirrorFace(self, face):
        """ Finds corresponding outer face to the given inner face """
        
        faceLoc = cmds.xform(face, t = True, q = True)
        smallestDiff = 2
        matchFace = ""
        rangeL = len(faceLoc)

        # find face with the closest matching bounding box on 2 planes
        for oFace in self.unMatchedFaces:
            oFaceLoc = cmds.xform(oFace, t = True, q = True)
            #edge faces have 9 others have 6
           
            if(len(oFaceLoc) != rangeL):
                break
            match = 0
            diff = 0
            
            for i in range(rangeL):
                diffN = abs(faceLoc[i] - oFaceLoc[i])
                if(diffN < 3):
                    match += 1
                diff += diffN
                # if 3 elements have been examined and only 1 matches it cannot be mirrored face
                if(i == 2 & match < 2):
                    i = 9        
                i += 1
            
            if(diff < smallestDiff):
                matchFace = oFace
                smallestDiff = diff

        try:
            self.unMatchedFaces.remove(matchFace) 
            self.matchedFacesDict[face] = matchFace  
        except:
            print("Error with " + face + "because " + matchFace + " not in dictionary")    
             
        return matchFace   

    def moveAllVerts(self):
        # get matching verts for every face in dictonary
        for key in self.matchedFacesDict:
            innerVerts = self.faceToVert(key)
            self.outerVerts = []
            self.outerVerts = self.faceToVert(self.matchedFacesDict[key])
            
            for each in innerVerts:
                self.findMirrorVert(each, self.outerVerts)
   
        # all matching verts are in dict so find center
        for keyVert in self.matchedVertsDict:
            center = self.findCenter(keyVert, self.matchedVertsDict[keyVert])
            vNumber = self.cloth.findNumber(keyVert)
            dupV = f"{self.cloth.simShapeName}.vtx[{vNumber}]"
            cmds.xform(dupV, t = center)
    
    def findMirrorVert(self, v, vertsList):
        """Compares location of vert closest to being mirror across 2 axises """
        #only run if matching vert has not already been found
        if v in self.matchedVertsDict:
            return
            
        vLoc = cmds.xform(v, t = True, q = True)
        smallestDiff = 10
        matchVert = ""
        
        for vert in vertsList:
            vertLoc = cmds.xform(vert, t = True, q = True)
            match = 0
            diff = 0
            
            for i in range(3):
                diffN = abs(vLoc[i] - vertLoc[i])
                if(diffN < 3):
                    match += 1
                    diff += diffN
                i+=1
            
            if(diff < smallestDiff):
                        matchVert = vert
                        smallestDiff = diff

        self.matchedVertsDict[v] = matchVert
        self.outerVerts.remove(matchVert)       
        return matchVert

    def findCenter(self, innerv, outerv):
        """ Find point in space equidistant to two given vertices
        Args: - innerv: vertex from an inner face
              - outerv: vertex from outer face
        Returns:
              - list of x, y, and z coordinates
        """
        inner =cmds.xform(innerv, t = True, q = True)
        outer = cmds.xform(outerv, t = True, q = True)
        if (abs(outer[0] - inner[0]) < .2):
            x = inner[0]
 
        else:
            x = outer[0] - ((outer[0] - inner[0])/2)
       
        if (abs(outer[1] - inner[1]) < .1):
            y = inner[1]
        else:
            y = (outer[1] - inner[1])/2 
            y = inner[1] + y
        
        if (abs(outer[2] - inner[2]) < .1):
            z = inner[2]

        else:
            z = (outer[2] - inner[2])/2
            z = (inner[2]) + z
        
        return([x, y, z])
                
    def start(self):
        """Tested on geo from : https://www.turbosquid.com/3d-models/military-uniform-2418050 """
        print(self.matchedVertsDict)
        # #for each in self.innerFaces:
        # #self.getMirrorFace(each)
        
        start = time.time()
        innerFacesList = self.cloth.getInnerFaces()
        
        for i in range(300):
            self.getMirrorFace(innerFacesList [i])
            
        self.moveAllVerts()    
        end = time.time()
        print("time " + str(end-start))
        # print(self.matchedFacesDict)
        # print(self.matchedVertsDict)

        vertDictContainer = {}
        vertDictContainer[self.cloth.objectName] = self.matchedVertsDict

        with open(self.json_pathWrite, 'w') as outfile:
            json.dump(vertDictContainer, outfile, indent=4)

jacket = ds(os.path.join(os.path.dirname(__file__), 'JacketMirroredVerts.json'))
    #r"C:\Users\apoll\Desktop\advPythonCourse\5_app\objectData_militaryJacket.json")
VertexInfo = vertexInfo(jacket)
VertexInfo.start()