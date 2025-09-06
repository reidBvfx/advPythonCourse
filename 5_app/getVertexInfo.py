# STYLE ***************************************************************************
# content = convert selected faces into vertices and get world location of each vertices 
#           then find matching faces/vertices and move duplicated mesh to be evenly between the inner and 
#           outerfaces
# date    = 2025-07-25
# needed  = 
#           - simplify nested for loops for finding mirrored faces/verts
#           - make functional if a seam is single sided
# author  = Reid Bryan (reidwarhola@gmail.com)
#**********************************************************************************

import json
import time
import os 
import sys
from copy import copy 
import pprint 
import maya.cmds as cmds # type: ignore
__file__ = 'C:\\Users\\apoll\\Desktop\\advPythonCourse\\5_app\\'

sys.path.append(os.path.dirname(__file__))
from DSObjectJSON import DSObjectJSON as ds
#import singleSidedGeoUI 

class getVertexInfo():
    def __init__(self, cloth, ssg):
        self.cloth = cloth
        self.ssg = ssg
        self.unMatchedFaces = copy(self.cloth.getOuterFaces())
        self.matchedFacesDict = {}
        try:
            if self.cloth.alreadyMatched():
                self.matchedVertsDict = self.cloth.getVertsDict()
            else:
                raise AttributeError
        except (AttributeError, KeyError):
            self.matchedVertsDict = {}

        writePath = 'configFiles//' + cloth.getName() + '.json'
        #path to export matching verts Dict
        self.json_pathWrite = os.path.join(os.path.dirname(__file__), writePath)
        self.locationFaceD = {}
        self.avgDistance = 0
         
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
        try:
            faceLoc = self.locationFaceD[face]
        except: 
            faceLoc = cmds.xform(face, t = True, q = True)
        smallestDiff = 2
        matchFace = ""
        rangeL = len(faceLoc)
        # find face with the closest matching bounding box on 2 planes
        for oFace in self.unMatchedFaces:
            try:
                oFaceLoc = self.locationFaceD[oFace]
            except: 
                oFaceLoc = cmds.xform(oFace, t = True, q = True)
            #oFaceLoc = cmds.xform(oFace, t = True, q = True)
            #edge faces have 9 others have 6
            if(len(oFaceLoc) != rangeL):
                break
            match = 0
            diff = 0.0
            
            for i in range(rangeL):
                diffN = abs(float((faceLoc[i] - oFaceLoc[i])))
                #print(face + " : " + oFace)
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
                if smallestDiff < .85 :
                    self.unMatchedFaces.remove(matchFace) 
                    self.matchedFacesDict[face] = matchFace  
                    self.avgDistance += smallestDiff
                    return matchFace   

        try:
            self.unMatchedFaces.remove(matchFace) 
            self.matchedFacesDict[face] = matchFace  
            self.avgDistance += smallestDiff
        except:
            print("No match for " + face)    
            
        return matchFace   

    def moveAllVerts(self):
        # get matching verts for every face in dictonary
        i = 0
        x = len(self.matchedFacesDict)
        for key in self.matchedFacesDict:
            innerVerts = self.faceToVert(key)
            self.outerVerts = []
            self.outerVerts = self.faceToVert(self.matchedFacesDict[key])
            for each in innerVerts:
                self.findMirrorVert(each, self.outerVerts)
            self.ssg.incrementProgress(25 + int((25*i)/x))
            i += 1
        # all matching verts are in dict so find center
        i = 0
        x = len(self.matchedVertsDict)

        for keyVert in self.matchedVertsDict:
            center = self.findCenter(keyVert, self.matchedVertsDict[keyVert])
            vNumber = self.cloth.findVertNumber(keyVert)
            dupV = f"{self.cloth.simShapeName}.vtx[{vNumber}]"
            cmds.xform(dupV, t = center)
            self.ssg.incrementProgress(50 + int((25*i)/x))
            i += 1
    
    def moveLoadedVerts(self):
        i = 0
        x = len(self.matchedVertsDict)
        
        for keyVert in self.matchedVertsDict:
            center = self.findCenter(keyVert, self.matchedVertsDict[keyVert])
            vNumber = self.cloth.findVertNumber(keyVert)
            dupV = f'{self.cloth.simShapeName}.vtx[{vNumber}]'
            cmds.xform(dupV, t = (center))
            self.ssg.incrementProgress(50 + int((50*i)/x))
            i += 1
    
    def findMirrorVert(self, v, vertsList):
        """Compares location of vert closest to being mirror across 2 axises """
        # only run if matching vert has not already been found
        try:
            if v in self.matchedVertsDict:
                return
        except:
            pass
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
        if(matchVert != ""):
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
        inner = cmds.xform(innerv, t = True, q = True)
        outer = cmds.xform(outerv, t = True, q = True)
        x = outer[0] - ((outer[0] - inner[0])/2)
        y = inner[1] + ((outer[1] - inner[1])/2 )
        z = (inner[2]) + ((outer[2] - inner[2])/2)
     
        return([x, y, z])

    def writeJSON(self, fileName):
        objectData = {}
        objectData['objectName'] = self.cloth.getName()
        objectData['simObjectName'] = self.cloth.getName() + "_SIM"
        objectData['thickness'] = self.cloth.getThickness()
        objectData['innerFaces'] = self.cloth.getInnerFaces()
        objectData['outerFaces'] = self.cloth.getOuterFaces()
        objectData['matchedVerts'] = self.matchedVertsDict

        with open(fileName, 'w') as outfile:
            json.dump(objectData, outfile, indent=4) 
  
    def start(self):
        """Tested on geo from : https://www.turbosquid.com/3d-models/military-uniform-2418050 """   
        
        start = time.time()
        try:
            cmds.select(self.cloth.getSimName())
            
        except:
            self.cloth.createSimMesh()
        self.unMatchedFaces = copy(self.cloth.getOuterFaces())
        try:
            ready = self.cloth.alreadyMatched()
        except:
            ready = False
        # if ready mean file is loaded with matchedVerts already found
        self.innerFacesList = self.cloth.getInnerFaces()
        x = len(self.cloth.getInnerFaces()) 
        if ready:
            self.matchedVertsDict = self.cloth.getVertsDict()
            self.ssg.incrementProgress(50)
            self.moveLoadedVerts()
            
        else:
            for i in range(x):
                try:
                    # x = self.innerFacesList[i]
                    self.getMirrorFace(self.innerFacesList[i])
                    self.ssg.incrementProgress(int((25*i)/x))
                except IndexError:
                    print("error: " + str(i))
                finally:
                    i += 1
            self.moveAllVerts() 
            self.cloth.setThickness(self.avgDistance/x)
        
        print('Thickness: {0:.10f}'.format(self.cloth.getThickness()))
        
        self.ssg.incrementProgress(90)
        self.cloth.deleteFaces()
        self.ssg.incrementProgress(100)
        end = time.time()
        print("time " + str(end-start))

def test():
    jacket = ds(os.path.join(os.path.dirname(__file__), 'configFiles\jacketData.json'))
    VertexInfo = getVertexInfo(jacket)
    #VertexInfo.start()

#test()