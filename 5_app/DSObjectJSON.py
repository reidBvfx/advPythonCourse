# STYLE ***************************************************************************
# content = child of DSObject reads from JSON file and passed to getVertexInfo
# date    = 2025-08-08
# author  = Reid Bryan (reidwarhola@gmail.com)
#**********************************************************************************
import json
from abc import ABC

from DSObject import DSObject 

class DSObjectJSON(DSObject, ABC):
    def __init__(self, path):
        # path to get object info
        self.json_path = path
        # read json file
        with open(self.json_path) as json_file:
            self.objectData = json.load(json_file) 
        # create DSObject with info
        super().__init__(self.objectData['objectName'])
        
        self.simObjName = self.objectData['simObjectName']
        self.simShapeName = self.simObjName + "Shape"
        self.outerFaces = self.correctNameFace(self.objectData['outerFaces'])
        self.innerFaces = self.correctNameFace(self.objectData['innerFaces'])
        self.thickness = self.objectData['thickness']

    def setMatched(self, jsonFile):
         self.matchedVertPath = jsonFile

    def setPath(self, newPath):
        self.json_path = newPath

    def alreadyMatched(self):
        """ if getVertexInfo has already created a JSON file of matchedVerts it will 
        return the dictionary otherwise a empty dictonary"""
        dict = {}
        #change to check orginal JSON
        try:
            with open(self.json_path) as json_file:
                self.objectData = json.load(json_file) 
                testData = self.objectData['matchedVerts'] 
        except:
            return False
        
        # check if dictonary has any data inside it
        if testData:
            return True
        else:
            return False

    def getVertsDict(self):
        return self.objectData['matchedVerts']
    
    
    