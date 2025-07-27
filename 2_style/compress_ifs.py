# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# date    = 2025-03-07
# email   = contact@alexanderrichtertd.com
#**********************************************************************************


# COMMENT --------------------------------------------------
# Not optimal

def set_color(ctrlList=None, color=None):

    #dictionary of possible colors and related overRideColor Setting
    colorSettings = { 1 : 4, 2 : 13, 3 : 25, 4 : 17, 5 : 17, 6 : 15, 7 : 6, 8 : 16}
    
    for ctrlName in ctrlList:
        try:
            mc.setAttr(ctrlName + 'Shape.overrideEnabled', 1)
        except:
            pass
        
        try: 
            mc.setAttr(ctrlName + 'Shape.overrideColor', colorSettings[color])        
        except:
            pass
           


# EXAMPLE
# set_color(['circle','circle1'], 8)
