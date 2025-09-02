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
        #print("DSJSON called")
        # read json file
        with open(self.json_path) as json_file:
            self.objectData = json.load(json_file) 
        """Used config file because each object has a large amount of data set up in an easily callable way
            having all the data within a py file would make it hard to parse and edit"""
        super().__init__(self.objectData['objectName'])
        #self.objName = objectData['objectName'] 
        self.simObjName = self.objectData['simObjectName']
        self.simShapeName = self.simObjName + "Shape"

        self.outerFaces = self.correctNameFace(self.objectData['outerFaces'])
        self.innerFaces = self.correctNameFace(self.objectData['innerFaces'])

    
    def setMatched(self, jsonFile):
         self.matchedVertPath = jsonFile

    def alreadyMatched(self):
        """ if getVertexInfo has already created a JSON file of matchedVerts it will 
        return the dictionary otherwise a empty dictonary"""
        dict = {}
        #change to check orginal JSON
        #print("testing")
        try:
            with open(self.json_path) as json_file:
                self.objectData = json.load(json_file) 
                testData = self.objectData['matchedVerts'] 
        except:
            return False
        
        
        #print("True")
        if testData:
            return False
        else:
            return True
        # try:
        #     with open(self.matchedVertPath) as json_file:
        #         objectData = json.load(json_file) 
            
        #     self.matchedVertDict = objectData[self.objectName]
        #     return self.matchedVertDict
        # except:
        #      return dict

    def getVertsDict(self):
        return self.objectData['matchedVerts']
    
    
    