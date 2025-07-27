# STYLE ***************************************************************************
# content  = Find the stack frame of the caller so that we can note the source
#            file name, line number and function name.
# original = logging.init.py
# warnings = On some versions of IronPython, currentframe() returns None
#            if IronPython isn't run with -X:Frames.
# date     = 2025-03-07
# email    = contact@alexanderrichtertd.com
#************************************************************************************


def findCaller(self): 
    cFrame = currentframe() 
    if cFrame is not None:
        cFrame = cFrame.f_back
    
    callerInfo = "(unknown file)", 0, "(unknown function)"
    while hasattr(cFrame, "f_code"):
        currentOpen = cFrame.f_code
        filename = os.path.normcase(currentOpen.co_filename)

        if filename == _srcfile:
            cFrame = cFrame.f_back
            continue

        callerInfo = (currentOpen.co_filename, cFrame.f_lineno, currentOpen.co_name)
        break
    
    return callerInfo

