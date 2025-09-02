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
        #print("DSobj called")

    def setName(self,name):
        self.objName = name
        self.simObjName = name + "_SIM"
        self.simShapeName = name + "_SIMShape" 

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
    # helper functs 
    def findNumber(self, vert):
        """ take vertex name and return int inside the brackets"""
        nPCompile = re.compile(r'(\d+)') 
        number = nPCompile.findall(vert)[0]
        return number
    
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
                objName = face.split('.f')[0]
                if ":" in face:  
                    nPCompile = re.compile(r'(\d+)') 
                    numbers = nPCompile.findall(face)
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
                objName = vertex.split('.vtx')[0]
                # correct naming convention
                if ":" in vertex:  
                    nPCompile = re.compile(r'(\d+)') 
                    numbers = nPCompile.findall(vertex)
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
                objName = vertex.split('.vtx')[0]
                # correct naming convention
                nPCompile = re.compile(r'(\d+)') 
                numbers = nPCompile.findall(vertex)
                temp_vertexList.append(numbers[0]) 
        return temp_vertexList       
    
    def createSimMesh(self):
        self.simObjName = cmds.duplicate(self.getName(), n = (self.getName() + "_SIM"))[0]

    def deleteFaces(self):
        # select all but inner face mesh
        cmds.select( clear=True )#clear anything selected
        cmds.select(self.simShapeName + ".f[*]")#select all faces
        
        # deselect all inner faces
        for face in self.innerFaces:
            faceSelect = (self.simShapeName + ".f[" + str(self.findNumber(face)) + "]")
            cmds.select(faceSelect, d = True)
        cmds.delete()
        # cmds.delete(simMesh, constructionHistory = True)
        


