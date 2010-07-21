#Surface water return

import tableAW, tableRain, area, lookup    # user input
import LP, DP, ETr, OW, AWr

from functions import *
from constants import *

#outFile = open('LP_out', 'w')

Pond = zeros(12)
NonPond = zeros_2D(85,12)
Grow = zeros(12)
WaterPonded_Grow = zeros(12)
WaterPonded_Pond = zeros(12)
Sum = zeros_2D(85,12)

#Burn = zeros_2D(85,12)
#Sum = zeros_2D(85,12)

def find():

    for DU_id in (75,75):
       # for Grow
        for mon in range(1, 12+1): # 1 to 12                      
            if (mon>4 and mon<9):
                WaterPonded_Grow[mon] = WaterPonded_Grow[mon-1] + AWr.Grow[mon] - DP.Grow[mon] -LP.Grow[mon]- tableAW.Grow_FlowT[mon]*area.Total[DU_id] - ETr.Grow[mon]
            else:
                WaterPonded_Grow[mon] = 0         
        for mon in range(1, 12+1): # 1 to 12
            if (mon == 9 ):
                Grow[mon] = WaterPonded_Grow[mon-1] + tableAW.Grow_FlowT[mon]*area.Total[DU_id] - DP.Grow[mon]
                Grow[mon] = max( 0, Grow[mon] )
            else:
                Grow[mon] = LP.Grow[mon] +tableAW.Grow_FlowT[mon]*area.Total[DU_id]
 
       # for Ponded
        for mon in range(1, 12+1): # 1 to 12                      
            if (mon == 1):
                WaterPonded_Pond[mon] = WaterPonded_Pond[12] + OW.Pond[mon]            
            elif (mon<4 or mon>9):
                WaterPonded_Pond[mon] = WaterPonded_Pond[mon-1] + OW.Pond[mon]
            else:
                WaterPonded_Pond[mon] = 0    
        for mon in range(1, 12+1): # 1 to 12
            if (mon != 2 ):               
                Pond[mon] = LP.Pond[mon] + tableAW.Decomp_FlowT[mon]*area.Pond[DU_id]
            else:
                Pond[mon] = WaterPonded_Pond[mon-1] + tableAW.Decomp_FlowT[mon]*area.Pond[DU_id] - DP.Pond[mon]
                Pond[mon] = max( 0, Pond[mon] ) 
                
       # for NonPonded and Sum    
        for calendar_year in range(1922, 2006):
            iyr = calendar_year - START_YEAR + 1
            for mon in range(1, 12+1): # 1 to 12

                NonPond[iyr][mon] = LP.NonPond[iyr][mon]
                Sum[iyr][mon]     = (1.0 - lookup.Reuse_Return[mon] ) *( Grow[mon]+Pond[mon]+NonPond[iyr][mon] )
                #Burn[iyr][mon] = lookup.NonGrow[mon] * min(tableRain.Rain[iyr][mon],LP_RATE)* area.Burn[DU_id]
                #Sum[iyr][mon] = Pond[mon] + NonPond[iyr][mon] + Grow[mon]
                #Sum[iyr][mon] = (1.0-lookup.Reuse_Return[mon])*Sum[iyr][mon]
                
def record(outFile):
    
    for calendar_year in range(1922, 2006):
        iyr = calendar_year-START_YEAR+1
        for mon in range(1,13):
            outFile.writelines( str(calendar_year)+'  '+str(mon) +'  '+ str(Sum[iyr][mon])+'\n' )


find()


