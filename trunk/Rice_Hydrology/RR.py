# Rainfall-Runoff

import os #os.getcwd()
import area, lookup, tableRain, tableAW    # user input
import ETr, AWr, LP, DP
#import DP              # output
#from numpy import *   # bug in ironclad
from functions import *
from constants import *

#outFile = open('DP_out', 'w')

Pond = zeros(12)
NonPond = zeros_2D(85,12)
Grow = zeros_2D(85,12)
Burn = zeros_2D(85,12)
Sum = zeros_2D(85,12)
RainVol_NonPond = zeros_2D(85,12)

def find():

    for DU_id in (75,75):
        for mon in range(1, 12+1): # 1 to 12
            #Pond[mon] = lookup.Pond[mon] * DP_RATE * area.Pond[DU_id]
            #Grow[mon] = lookup.Grow[mon] * tableRain.Rain[mon] * area.Total[DU_id]
            #NonPond[mon]  = 0
            k=3
    
        for calendar_year in range(1922, 2006):
            iyr = calendar_year - tableRain.START_YEAR + 1
            for mon in range(1, 12+1): # 1 to 12
                Grow[iyr][mon] = lookup.Grow[mon] * tableRain.Rain[iyr][mon] * area.Total[DU_id]
                
                # NonPond
                #RainVol_NonPond[iyr][mon] = lookup.NonGrow[mon]*tableRain.Rain[iyr][mon]*area.NonPond[DU_id]
                OW = tableAW.NonPond[mon]*area.NonPond[DU_id]
                ET_met = min( tableRain.VolNonPond[iyr][mon], ETr.NonPond[mon])
                NonPond[iyr][mon] = OW + RainVol_NonPond[iyr][mon] - ET_met-LP.NonPond[mon] - DP.NonPond[mon]
                NonPond[iyr][mon] = max(0, NonPond[iyr][mon])
                

def record(outFile):
    
    for calendar_year in range(1922, 2006):
        iyr = calendar_year-tableRain.START_YEAR+1
        for mon in range(1,13):
            outFile.writelines( str(calendar_year)+'  '+str(mon) +'  '+ str(Sum[iyr][mon])+'\n' )


