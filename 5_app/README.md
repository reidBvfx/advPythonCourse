Better single sided geometry
Clothing geo is usually 2 sided geometry, but must be simmed with a single plane of geometry. The standard to get the single sided geo is delete all the faces except the innermost faces of the meat. This can often lead to IPs that can’t be seen until viewing the render geo. I would create a tool that will recreate the geo equidistant between the two vertices and calculate the thickness of the render geo to give a more accurate simulation with less IP fixes being needed. 


Changes:

getVertexInfo:
    - now takes DSObject as an argument
    - cleaner moveAllVerts
    - outputs matching verts to JSON file
    
    

DSObect:
    - reads from JSON file
    - fixing naming conventions now 2 functions [correctNameFace & correctNameVertex]
    - finding number in poly name is own function
    - getter and setter functions for path and lists