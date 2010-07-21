import os #os.getcwd()
import area, lookup, tableRain, tableET   # user input
#import ETr              # output
#from numpy import *   # bug in ironclad
from functions import *
from constants import *

#ETr_out = open('out', 'w')

#def ETr_initialize(85)
Pond_Op = zeros(12)
Pond_NonOp = zeros(12)
NonPond = zeros(12)
Grow = zeros(12)
Burn = zeros_2D(85,12)
#Sum = zeros_2D(85,12)

#print tableET.Burn[1:12]
#print lookup.NonGrow[1:12]
#print area.Burn[75]


def find(DU_id):

        for mon in range(1, 12+1): # 1 to 12
    
            Grow[mon] = lookup.Grow[mon] * tableET.Grow[mon] * area.Total[DU_id]
            
            Pond_Op[mon] = lookup.Pond[mon] * tableET.Pond[mon] * area.Pond[DU_id] - Grow[mon]*area.Pond_Ratio[DU_id]
            Pond_Op[mon] = max(0,Pond_Op[mon])

            Pond_NonOp[mon] = (1.0-lookup.Pond[mon]) * tableET.Pond[mon] * area.Pond[DU_id] - Grow[mon]*area.Pond_Ratio[DU_id]
            Pond_NonOp[mon] = max(0,Pond_NonOp[mon])
            
            NonPond[mon] = tableET.NonPond[mon] * area.NonPond[DU_id] - Grow[mon]*area.NonPond_Ratio[mon]
            NonPond[mon] = max(0,NonPond[mon])
    
    
        for calendar_year in range(1922, 2006):
            iyr = calendar_year-START_YEAR+1
            for mon in range(1, 12+1): # 1 to 12
                Burn[iyr][mon] = lookup.NonGrow[mon] * tableET.Burn[mon] * area.Burn[DU_id]

