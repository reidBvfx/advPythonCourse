# STYLE ***************************************************************************
# content = creates object to hold all of double-sided geos info
#        
# date    = 2025-08-08
# author  = Reid Bryan (reidwarhola@gmail.com)
#**********************************************************************************
import json
import re
import os
from abc import ABC

import maya.cmds as cmds #type: ignore

class DSObject():
    def __init__(self, name):
        self.objName = name
        self.simObjName = name + "_SIM"
        self.simShapeName = name + "_SIMShape" 
        self.outerFaces = []
        self.innerFaces = []
        self.thickness = 0
        #print("DSobj called")

    def setName(self,name):
        self.objName = name
        self.simObjName = name + "_SIM"
        self.simShapeName = name + "_SIMShape" 

    def setThickness(self, v):
        self.thickness = v
    # inner faces commands ###################################
    def setInnerFaceList(self, faces):
        newList = self.correctNameFace(faces)
        newList = self.removeDuplicates(self.innerFaces, newList)
        for each in newList:
            self.innerFaces.append(each) 
        return newList

    def clearInnerFaces(self):
        self.innerFaces = []
        
    def removeInnerFace(self, index):
        self.innerFaces.pop(index)

    # outer faces commands ################################### 
    def setOuterFaceList(self, faces):
        newList = self.correctNameFace(faces)
        newList = self.removeDuplicates(self.outerFaces, newList)
        for each in newList:
            self.outerFaces.append(each) 
        self.removeDuplicates(self.outerFaces)    
        return newList
    
    def removeOuterFace(self, index):
        self.outerFaces.pop(index)

    def clearOuterFaces(self):
        self.outerFaces = []

    # getters
    def getInnerFaces(self):
         return self.innerFaces
    
    
    def getOuterFaces(self):
         return self.outerFaces
    
    def getName(self):
        return self.objName
    
    def getSimName(self):
        return self.simObjName
    
    def getThickness(self):
        return self.thickness
    # helper functs 

    def findVertNumber(self, vert):
        """ take vertex name and return int inside the brackets"""
        try:
            objName, bracket = vert.split('.vtx')
            nPCompile = re.compile(r'(\d+)') 
            number = nPCompile.findall(bracket)[0]
            return number
        except:
            return  
        
    def findNumber(self, vert):
        """ take vertex name and return int inside the brackets"""
        try:
            objName, bracket = vert.split('.f')
            nPCompile = re.compile(r'(\d+)') 
            number = nPCompile.findall(bracket)[0]
            return number
        except:
            return  
        
    def removeDuplicates(self, list, comp = []):
        temp =[]
        for each in comp:
            if each not in list:
                temp.append(each)
        return temp
    
    def correctNameFace(self, facesList):
        """ removed range from bracket [x:y] and inserts value in range into new list"""
        temp_faceList = []
        for face in facesList:
                objName, bracket = face.split('.f')
                if ":" in face:  
                    nPCompile = re.compile(r'(\d+)') 
                    numbers = nPCompile.findall(bracket)
                    for i in range(int(numbers[0]), int(numbers[1])+1):
                        temp_faceList.append(objName + ".f[" +str(i) + ']') 
                        i += 1
                else:
                    temp_faceList.append(face)
        return temp_faceList    
        
    def correctNameVertex(self, vertexList):
        """ removed range from bracket [x:y] and inserts value in range into new list"""
        temp_vertexList = []
        for vertex in vertexList:
                objName, bracket = vertex.split('.vtx')
                # correct naming convention
                if ":" in vertex:  
                    nPCompile = re.compile(r'(\d+)') 
                    numbers = nPCompile.findall(bracket)
                    for i in range(int(numbers[0]), int(numbers[1])+1):
                        temp_vertexList.append(objName + ".vtx[" +str(i) + ']') 
                        i += 1
                else:
                    temp_vertexList.append(vertex)
        return temp_vertexList        
    
    def getVertexNumbers(self, vertexList):
        """ removed range from bracket [x:y] and inserts value in range into new list"""
        temp_vertexList = []
        for vertex in vertexList:
                objName, bracket = vertex.split('.vtx[')
                # correct naming convention
                nPCompile = re.compile(r'(\d+)') 
                numbers = nPCompile.findall(bracket)
                temp_vertexList.append(numbers[0]) 
        return temp_vertexList       
    
    def createSimMesh(self):
        self.simObjName = cmds.duplicate(self.getName(), n = (self.getSimName()))[0]
        

    def deleteFaces(self):
        # select all but inner face mesh
        cmds.select( clear=True )#clear anything selected
        cmds.select(self.simShapeName + ".f[*]")#select all faces
        # deselect all inner faces
        try:
            faceNum = []
            for face in self.innerFaces:
                faceNum.append(str(self.findNumber(face)))
            # faceSelect = []
            for num in faceNum:
                try:    
                    faceSelect =(self.simShapeName + ".f[" + num + "]") 
                    cmds.select(faceSelect, tgl = True)  
                except:
                    print("error")
                    pass
            # cmds.select(faceSelect, d = True)  
            cmds.delete()
        except:
            pass
        
        # cmds.delete(simMesh, constructionHistory = True)
        


