# STYLE ***************************************************************************
# content = creates object to hold all of double-sided geos info
#           reads from JSON file and passed to getVertexInfo
# date    = 2025-08-08
# author  = Reid Bryan (reidwarhola@gmail.com)
#**********************************************************************************
""" Made double sided object(DSO) into a class because every DSO will have the same attributes and 
    needs the same modification before being sent to getVertexInfo
    Also makes getVertexInfo.py less clutter and more concentrated """
import json
import re
import os
__file__ = 'C:\\Users\\apoll\\Desktop\\advPythonCourse\\5_app\\'
#import maya.cmds as cmds #type: ignore

class DSObject():
    def __init__(self, path):
        # path to get object info
        self.json_path = path
        
        # read json file
        with open(self.json_path) as json_file:
            objectData = json.load(json_file) 
        """Used config file because each object has a large amount of data set up in an easily callable way
            having all the data within a py file would make it hard to parse and edit"""
        
        self.objName = objectData['objectName'] 
        self.simObjName = objectData['simObjectName']
        self.simShapeName = self.simObjName + "Shape"

        self.outerFaces = self.correctNameFace(objectData['outerFaces'])
        self.innerFaces = self.correctNameFace(objectData['innerFaces'])

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
    
    def findNumber(self, vert):
        """ take vertex name and return int inside the brackets"""
        nPCompile = re.compile(r'(\d+)') 
        number = nPCompile.findall(vert)[0]
        return number
    
    def getInnerFaces(self):
         return self.innerFaces
    
    
    def getOuterFaces(self):
         return self.outerFaces
    
    def setMatched(self, jsonFile):
         self.matchedVertPath = jsonFile

    def alreadyMatched(self):
        """ if getVertexInfo has already created a JSON file of matchedVerts it will 
        return the dictionary otherwise a empty dictonary"""
        dict = {}
        try:
            with open(self.matchedVertPath) as json_file:
                objectData = json.load(json_file) 
            
            self.matchedVertDict = objectData[self.objectName]
            return self.matchedVertDict
        except:
             return dict


    def dupAndDel(self, obj, innerFaces):
        """
        Creates a duplicated mesh of selected object and deletes faces to create a single sided mesh
        
        Arguments: 
            innerFaces = [names of all inner faces]
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


militaryJacket = DSObject(os.path.join(os.path.dirname(__file__), 'configFiles//jacketData.json'))


