# Rainfall data by WBA. Total 41 WBAs
# converted to feet/month from inch/month

import re
import lookup, area
from constants import *
from functions import *

_inFile = open('table_rainfall_by_WBA.txt','r')

WBA_name=['NA']
WBA_name_short=[]
#DU_name_short =[]

Rain           = zeros_3D(41,100,12)
Vol_NonPond    = zeros_3D(41,100,12)
Vol_Pond_Op    = zeros_3D(41,100,12)
Vol_Pond_NonOp = zeros_3D(41,100,12)
Vol_Grow       = zeros_3D(41,100,12)
Vol_Burn       = zeros_3D(41,100,12)




_lines = _inFile.readlines()

_line = _lines[1]
_line = _line.strip().split()
WBA_name[1:] = _line[2:]


for _name in WBA_name:
    #shortname = _name.replace('WBA','')
    WBA_name_short.append(_name.replace('WBA',''))
#print WBA_name_short


for _line in _lines[2:]:
    _line=_line.strip().split()
    try:
        year = int(_line[0])
        month = int(_line[1])
        iyr = year - START_YEAR + 1
        #print year, month
        for (id, data) in enumerate(_line[1:]):
            
            if id>0:
                Rain[id][iyr][month] = float(data)/12
            
                Vol_NonPond[id][iyr][month] = lookup.NonGrow[month]*area.NonPond[id]*Rain[id][iyr][month]
            
                Vol_Grow[id][iyr][month]    = lookup.Grow[month]*area.Total[id]*Rain[id][iyr][month]
                Vol_Pond_Op[id][iyr][month]    = lookup.Pond[month]*area.Pond[id]*Rain[id][iyr][month]
                Vol_Pond_NonOp[id][iyr][month] = (1.0-lookup.Pond[month])*area.Pond[id]*Rain[id][iyr][month] - Vol_Grow[id][iyr][month]*area.Pond_Ratio[id]
                Vol_Pond_NonOp[id][iyr][month] =  max(0,Vol_Pond_NonOp[id][iyr][month])
                Vol_Burn[id][iyr][month]    = lookup.NonGrow[month]*area.Burn[id]*Rain[id][iyr][month]           
            #
            
            
            
    except:
        print 'error in tableRainWBA.py '

#for name in area.DU:
#    shortname = name.replace 
#print WBA_name_short



#for _line in _lines[2:]:
#    _line = _line.strip().split()
#    print _line[2]