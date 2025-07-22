import os
import re

import maya.cmds as cmds

def getMirrorFace(self, face):
        faceLoc = cmds.xform(face, bb = True, q = True)
        smallestDiff = .5
        matchFace = ""
        #find face with the closest matching bounding box on 2 planes
        for oFace in self.outerFaces: # an array of face names
            oFaceLoc = cmds.xform(oFace, bb = True, q = True) # returns [x1, y1, z1, x2, y2, z2]
            match = 0
            diff = 0
            for i in range(5):
                diffN = abs(faceLoc[i] - oFaceLoc[i])
                if(diffN < .5):
                    print(oFace + " : " + str(abs(faceLoc[i] - oFaceLoc[i])))
                    match += 1
                    diff += diffN
                if(match == 4):
                    print(oFace + " : " + str(diff))
                    if(diff < smallestDiff):
                        matchFace = oFace
                        smallestDiff = diff
                i+=1
                
        print(matchFace)
        return oFaceLoc