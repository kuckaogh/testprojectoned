import area, lookup
from functions import *
from constants import *

UNIT = 'ft'

DU = ['NA']

Rain = zeros_2D(100,12)
Vol_NonPond = zeros_2D(100,12)
Vol_Pond_Op = zeros_2D(100,12)
Vol_Pond_NonOp = zeros_2D(100,12)
Vol_Grow = zeros_2D(100,12)
Vol_Burn = zeros_2D(100,12)

rainfall_File = open('rainfall.txt','r')

_lines = rainfall_File.readlines()

title =_lines[1].split()
DU.append(title[1+1])

n_lines = len(_lines[2:])

for line in _lines[2:]:
    line=line.strip().split()
    try:
        year = int(line[0])
        month = int(line[1])
        iyr = year - START_YEAR + 1
        #print year, month, iyr
        Rain[iyr][month] = float(line[2])
        
        for DU_id in (75,75):
            Vol_NonPond[iyr][month] = lookup.NonGrow[month]*area.NonPond[DU_id]*Rain[iyr][month]

            Vol_Grow[iyr][month]    = lookup.Grow[month]*area.Total[DU_id]*Rain[iyr][month]
            Vol_Pond_Op[iyr][month]    = lookup.Pond[month]*area.Pond[DU_id]*Rain[iyr][month]
            Vol_Pond_NonOp[iyr][month] = (1.0-lookup.Pond[month])*area.Pond[DU_id]*Rain[iyr][month] - Vol_Grow[iyr][month]*area.Pond_Ratio[DU_id]
            Vol_Pond_NonOp[iyr][month] =  max(0,Vol_Pond_NonOp[iyr][month])
            Vol_Burn[iyr][month]    = lookup.NonGrow[month]*area.Burn[DU_id]*Rain[iyr][month]
    except:
        print 'error!'

