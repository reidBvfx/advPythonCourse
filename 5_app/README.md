Better single sided geometry <br />
Clothing geo is usually 2 sided geometry, but must be simmed with a single plane of geometry. The standard to get the single sided geo is delete all the faces except the innermost faces of the meat. This can often lead to IPs that can’t be seen until viewing the render geo. I would create a tool that will recreate the geo equidistant between the two vertices and calculate the thickness of the render geo to give a more accurate simulation with less IP fixes being needed. <br />


Changes:<br />

getVertexInfo:<br />
    - now takes DSObject as an argument<br />
    - cleaner moveAllVerts<br />
    - outputs matching verts to JSON file<br />

DSObect:<br />
    - reads from JSON file<br />
    - fixing naming conventions now 2 functions [correctNameFace & correctNameVertex]<br />
    - finding number in poly name is own function<br />
    - getter and setter functions for path and lists<br />
    - dupandDelete.py merged into this file<br />

Renaming:

SSM_UI.py -> singleSidedGeoUI.py<br />
militaryJacketDataJSONCREATION.py -> jacketDataconfig.py<br />
objectData_militaryJacket.json -> jacketData.json
objectData_militaryJacket_mirroredVerts.json -> jacketMirroredVerts.json

Folder creation: <br />
images:
    - moved innerOuterGeo.jpg and NullDistance.jpg

configFiles:
    - moved jacketDataconfig.py, jacketMirroredVerts.json, jacketDataconfig.py

