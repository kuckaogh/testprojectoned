# Rainfall data by DU
import area, lookup
#import tableRainWBA
from functions import *
from constants import *

UNIT = 'ft'

DU_name = ['NA']

Rain           = zeros_2D(100,12)
Vol_NonPond    = zeros_3D(75,100,12)
Vol_Pond_Op    = zeros_3D(75,100,12)
Vol_Pond_NonOp = zeros_3D(75,100,12)
Vol_Grow       = zeros_3D(75,100,12)
Vol_Burn       = zeros_3D(75,100,12)

rainfall_File = open('rainfall.txt','r')

_lines = rainfall_File.readlines()

_title =_lines[1].split()
DU_name[1:]=_title[1+1:]

n_lines = len(_lines[2:])

for line in _lines[2:]:
    line=line.strip().split()
    try:
        year = int(line[0])
        month = int(line[1])
        iyr = year - START_YEAR + 1
        #print year, month, iyr
        
        
        for DU_id in (75,75):
            Rain[iyr][month] = float(line[2])    
            
            Vol_NonPond[DU_id][iyr][month] = lookup.NonGrow[month]*area.NonPond[DU_id]*Rain[iyr][month]

            Vol_Grow[DU_id][iyr][month]    = lookup.Grow[month]*area.Total[DU_id]*Rain[iyr][month]
            Vol_Pond_Op[DU_id][iyr][month]    = lookup.Pond[month]*area.Pond[DU_id]*Rain[iyr][month]
            Vol_Pond_NonOp[DU_id][iyr][month] = (1.0-lookup.Pond[month])*area.Pond[DU_id]*Rain[iyr][month] - Vol_Grow[DU_id][iyr][month]*area.Pond_Ratio[DU_id]
            Vol_Pond_NonOp[DU_id][iyr][month] =  max(0,Vol_Pond_NonOp[DU_id][iyr][month])
            Vol_Burn[DU_id][iyr][month]    = lookup.NonGrow[month]*area.Burn[DU_id]*Rain[iyr][month]
    except:
        print 'tableRain error!'

