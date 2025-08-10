import json
json_path = r"C:\Users\apoll\Desktop\advPythonCourse\5_app\objectData_militaryJacket.json"

object_data =   {'objectName'   : "military_uniform" ,
                'simObjectName' : "military_uniform_SIM",
                'innerFaces'    : ['military_uniformShape.f[735:1469]', 'military_uniformShape.f[1655:1743]', 
                                  'military_uniformShape.f[2097:2185]', 'military_uniformShape.f[3185:3919]', 
                                  'military_uniformShape.f[4853:5689]', 'military_uniformShape.f[5764:5837]', 
                                  'military_uniformShape.f[6902:7797]', 'military_uniformShape.f[7872:7945]', 
                                  'military_uniformShape.f[8677:8891]', 'military_uniformShape.f[12368:13679]']
                ,
                'outerFaces'    : ['military_uniformShape.f[0:734]', 'military_uniformShape.f[1566:1654]', 
                                  'military_uniformShape.f[2008:2096]', 'military_uniformShape.f[2450:3184]', 
                                  'military_uniformShape.f[4016:4852]', 'military_uniformShape.f[5690:5763]', 
                                  'military_uniformShape.f[6006:6901]', 'military_uniformShape.f[7798:7871]', 
                                  'military_uniformShape.f[8462:8676]', 'military_uniformShape.f[11056:12367]']
}
  
# write json file
with open(json_path, 'w') as outfile:
    json.dump(object_data, outfile, indent=4)