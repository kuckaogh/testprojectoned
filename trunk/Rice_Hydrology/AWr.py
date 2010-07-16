import os #os.getcwd()
import area, lookup, tableRain, tableAW   # user input
import DP, LP, ETr
#import AWr              # output
#from numpy import *   # bug in ironclad
from functions import *
from constants import *

#ETr_out = open('AWr.out', 'w')

#def ETr_initialize(85)
Pond = zeros_2D(85,12)
NonPond = zeros(12)
Grow = zeros(12)
Burn = zeros_2D(85,12)
Sum = zeros_2D(85,12)

ETr.find()
DP.find()
LP.find()
# non-Sept
mon=6
DU_id = 75
#Grow = tableAW.Grow + tableAW.Grow_FlowT + DP.Grow
Grow[mon] = ETr.Grow[mon] + tableAW.Grow_FlowT[mon]*area.Total[DU_id] + tableAW.Grow[mon]*area.Total[DU_id] + DP.Grow[mon] + LP.Grow[mon]

def find():
#
    for DU_id in (75,75):
        for mon in range(1, 12+1): # 1 to 12
            
            NonPond[mon] = tableAW.NonPond[mon]*area.NonPond[DU_id] 
            
            
            if (mon != 9): 
                Grow[mon] = ETr.Grow[mon] + (tableAW.Grow_FlowT[mon] + tableAW.Grow[mon])*area.Total[DU_id] + DP.Grow[mon] + LP.Grow[mon]
            else:
                Grow[mon] = ETr.Grow[mon] + tableAW.Grow_FlowT[mon]*area.Total[DU_id] 
                
                    
        for calendar_year in range(1922, 2006):
            iyr = calendar_year-tableRain.START_YEAR+1
            for mon in range(1, 12+1): # 1 to 12
                if (mon!=2):
                    Pond[iyr][mon] = ETr.Pond[mon] + (tableAW.Decomp_FlowT[mon] + tableAW.Pond[mon]- tableRain.Rain[iyr][mon]*0.1)*area.Pond[DU_id] + DP.Pond[mon] + LP.Pond[mon] 
                    Pond[iyr][mon]
                else:
                    Pond[iyr][mon] = ETr.Pond[mon] + (tableAW.Decomp_FlowT[mon] + tableAW.Pond[mon]- tableRain.Rain[iyr][mon]*0.1)*area.Pond[DU_id]
##
#