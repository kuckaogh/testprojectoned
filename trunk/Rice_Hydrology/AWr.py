# Applied water required without re-use water calculation

import area, lookup, tableRain, tableAW   # user input
import DP, LP, ETr

#from numpy import *   # bug in ironclad
from functions import *
from constants import *


Pond = zeros_2D(85,12)
NonPond = zeros(12)
Grow = zeros(12)

def find(DU_id):
#
        for mon in range(1, 12+1): # 1 to 12
            
            NonPond[mon] = tableAW.NonPond[mon]*area.NonPond[DU_id] 
            
            
            if (mon != 9): 
                Grow[mon] = ETr.Grow[mon] + (tableAW.Grow_FlowT[mon] + tableAW.Grow[mon])*area.Total[DU_id] + DP.Grow[mon] + LP.Grow[mon]
            else:
                Grow[mon] = ETr.Grow[mon] + tableAW.Grow_FlowT[mon]*area.Total[DU_id] 
                
                    
        for calendar_year in range(1922, 2006):
            iyr = calendar_year-START_YEAR+1
            for mon in range(1, 12+1): # 1 to 12
                if (mon != 2):
                    Pond[iyr][mon] = ETr.Pond_Op[mon] + (tableAW.Decomp_FlowT[mon] + tableAW.Pond[mon]- lookup.Pond[mon]*tableRain.Rain[iyr][mon]*0.1)*area.Pond[DU_id] + DP.Pond[mon] + LP.Pond[mon] 
                    Pond[iyr][mon] = max(0,Pond[iyr][mon])
                else:
                    Pond[iyr][mon] = ETr.Pond_Op[mon] + (tableAW.Decomp_FlowT[mon] + tableAW.Pond[mon]- lookup.Pond[mon]*tableRain.Rain[iyr][mon]*0.1)*area.Pond[DU_id]
                    Pond[iyr][mon] = max(0,Pond[iyr][mon])
                    
     
