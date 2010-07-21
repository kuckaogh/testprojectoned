# Total Applied Water

import lookup, tableRain
import AWr, RR, SWR
#import AWr              # output
#from numpy import *   # bug in ironclad
from functions import *
from constants import *

#ETr_out = open('AWr.out', 'w')

#def ETr_initialize(85)
Reuse_Water = zeros_2D(85,12)
Total = zeros_2D(85,12)
_AW_Required  = zeros_2D(85,12)
_Reuse_Runoff = zeros_2D(85,12)
_Reuse_Return = zeros_2D(85,12)

DU_id = 75

def find():
#
    for DU_id in (75,75):                    
        for calendar_year in range(1922, 2006):
            iyr = calendar_year-tableRain.START_YEAR+1
            for mon in range(1, 12+1): # 1 to 12
                _AW_Required[iyr][mon] = AWr.Grow[mon] + AWr.NonPond[mon] + AWr.Pond[iyr][mon]
                _Reuse_Runoff[iyr][mon] = lookup.Reuse_Runoff[mon]*(RR.Grow[iyr][mon] + RR.NonPond[iyr][mon] + RR.Pond_Op[iyr][mon] + RR.Pond_NonOp[iyr][mon] + RR.Burn[iyr][mon])
                _Reuse_Return[iyr][mon] = lookup.Reuse_Return[mon]*(SWR.Grow[mon] + SWR.Pond[mon] + SWR.NonPond[iyr][mon]) 
                Reuse_Water[iyr][mon] = min( _AW_Required[iyr][mon], _Reuse_Return[iyr][mon]+ _Reuse_Runoff[iyr][mon] )  
                Total[iyr][mon] = _AW_Required[iyr][mon] - Reuse_Water[iyr][mon]    
                    
def record(outFile):
    
    for calendar_year in range(1922, 2006):
        iyr = calendar_year-tableRain.START_YEAR+1
        for mon in range(1,13):
            outFile.writelines( str(calendar_year)+'  '+str(mon) +'  '+ str(Total[iyr][mon])+'\n' )
            

find()