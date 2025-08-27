import maya.cmds as cmds

def getNeighbor(face, mirrorFace):
    edges = (cmds.polyListComponentConversion(face, ff = True, te = True))
    mirrorEdges = (cmds.polyListComponentConversion(mirrorFace, ff = True, te = True))
    faces = cmds.polyListComponentConversion(edges[0], tf=True, bo = True)
    
    solved = 0
    attemps = 0
    size = 4
    cmds.select( clear=True )
    print(len(faces))
    for solved in range(len(faces)):
         attemps = 0
         face = faces[solved]
         print(face)
         matched = ""
         if(attemps < size):
            mirroredFaces = cmds.polyListComponentConversion( mirrorEdges[attemps], tf=True, bo = True)
            mirroredFaces = correctNameFace(mirroredFaces)
            matched = getMirrorFace(face, mirroredFaces)
            if matched == "":
                 attemps += 1
            else:
                print(face + " : " + matched)
                cmds.select(face, matched)
                attemps = 5
                solved += 1
                

    # while(solved != len):
    #     cmds.polyListComponentConversion( edges[solved], tf=True, bo = True)
    #     mirrorLen = len(mirrorEdges)
    #     remaining = 0
    #     for remaining in range(mirrorLen):
    #          mFaces = cmds.polyListComponentConversion( mirrorEdges[solved], tf=True, bo = True)
    #          matched = getMirrorFace(edges[solved], mFaces)


def getMirrorFace(face, mirroredFaces):
    """ Finds corresponding outer face to the given inner face """
    faceLoc = cmds.xform(face, t = True, q = True)
    print(face + " : ")
    print(mirroredFaces)    
    smallestDiff = 2
    matchFace = ""
    rangeL = len(faceLoc)
    for mFace in mirroredFaces:
        mFaceLoc = cmds.xform(mFace, t = True, q = True)
        
        if(len(mFaceLoc) != rangeL):
            break
        match = 0
        diff = 0
            
        for i in range(rangeL):
            diffN = abs(faceLoc[i] - mFaceLoc[i])
            if(diffN < 3):
                match += 1
            diff += diffN
            # if 3 elements have been examined and only 1 matches it cannot be mirrored face
            if(i == 2 & match < 2):
                i = 9        
            i += 1
            
        if(diff < smallestDiff):
            matchFace = mFace
            smallestDiff = diff

        return matchFace   

def correctNameFace(facesList):
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
def test():
    face = 'military_uniformShape.f[405]'
    mFace = 'military_uniformShape.f[1140]'
    getNeighbor(face, mFace)
    
test()    