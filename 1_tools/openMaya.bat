

::script path
set "SCRIPT_PATH=C:\Users\apoll\Desktop\mayaScripts"
set "PYTHONPATH=%SCRIPT_PATH%;%PYTHONPATH%"

::set variable
set "MAYA_VERSION=2024"

::maya path with variable
set "MAYA_PATH=C:\Program Files\Autodesk\Maya%MAYA_VERSION%"



::add to plugin path
set "XBMLANGPATH=%SCRIPT_PATH%\MayaEDUStartupImage.png;%XBMLANGPATH%"

::set splashscreen
set "XBMLANGPATH=%SCRIPT_PATH%img;%XBMLANGPATH%"
::disable report
set "MAYA_DISABLE_CIP=1"
set "MAYA_DISABLE_CER=1"
::start
start "" "%MAYA_PATH%\bin\maya.exe"

