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

def find(DU_id):

        DP.find(DU_id)
       # for Grow
        for mon in(5,6,7,8):                   
            WaterPonded_Grow[mon] = WaterPonded_Grow[mon-1] + AWr.Grow[mon] - DP.Grow[mon] -LP.Grow[mon]- tableAW.Grow_FlowT[mon]*area.Total[DU_id] - ETr.Grow[mon]
       
        for mon in range(1, 12+1): # 1 to 12
            Grow[mon] = LP.Grow[mon] +tableAW.Grow_FlowT[mon]*area.Total[DU_id]

        mon=9
        Grow[mon] = WaterPonded_Grow[mon-1] + tableAW.Grow_FlowT[mon]*area.Total[DU_id] - DP.Grow[mon]
        Grow[mon] = max(0,Grow[mon])
                
 
        # for Ponded
        for mon in (10,11,12): 
            WaterPonded_Pond[mon] = WaterPonded_Pond[mon-1] + OW.Pond[mon]
            
        WaterPonded_Pond[1] = WaterPonded_Pond[12] + OW.Pond[1]      
        for mon in (2,3): 
            WaterPonded_Pond[mon] = WaterPonded_Pond[mon-1] + OW.Pond[mon]    
  
        for mon in range(1, 12+1): # 1 to               
            Pond[mon] = LP.Pond[mon] + tableAW.Decomp_FlowT[mon]*area.Pond[DU_id]
            if ( mon == 2 ):
                Pond[mon] = WaterPonded_Pond[mon-1] + tableAW.Decomp_FlowT[mon]*area.Pond[DU_id] - DP.Pond[mon]
                Pond[mon] = max( 0, Pond[mon] ) 
                
       # for NonPonded and Sum    
        for calendar_year in range(1922, 2006):
            iyr = calendar_year - START_YEAR + 1
            for mon in range(1, 12+1): # 1 to 12

                NonPond[iyr][mon] = LP.NonPond[iyr][mon]
                Sum[iyr][mon]     = (1.0 - lookup.Reuse_Return[mon] ) *( Grow[mon]+Pond[mon]+NonPond[iyr][mon] )




find(75)


