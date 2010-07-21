# Rainfall-Runoff

import os #os.getcwd()
import area, lookup, tableRain, tableAW    # user input
import ETr, OW, LP, DP, ETmet
#import DP              # output
#from numpy import *   # bug in ironclad
from functions import *
from constants import *

#outFile = open('DP_out', 'w')

Pond_Op = zeros_2D(85,12)
Pond_NonOp = zeros_2D(85,12)
NonPond = zeros_2D(85,12)
Grow = zeros_2D(85,12)
Burn = zeros_2D(85,12)
Sum = zeros_2D(85,12)


Demand_Pond = zeros(12)
Eff_Rain_Pond = zeros_2D(85,12)
Eff_Rain_Burn = zeros_2D(85,12)

def find():

    for DU_id in (75,75):
        for mon in range(1, 12+1): # 1 to 12
            #Pond[mon] = lookup.Pond[mon] * DP_RATE * area.Pond[DU_id]
            #Grow[mon] = lookup.Grow[mon] * tableRain.Rain[mon] * area.Total[DU_id]
            #NonPond[mon]  = 0
            k=3
    
        for calendar_year in range(1922, 2006):
            iyr = calendar_year - START_YEAR + 1
            for mon in range(1, 12+1): # 1 to 12
                Grow[iyr][mon] = lookup.Grow[mon] * tableRain.Rain[iyr][mon] * area.Total[DU_id]
                
                # NonPond
                NonPond[iyr][mon] = OW.NonPond[mon] + tableRain.Vol_NonPond[iyr][mon] - ETmet.NonPond[iyr][mon]-LP.NonPond[iyr][mon]
                NonPond[iyr][mon] = max(0, NonPond[iyr][mon])
                
                # Pond
                Demand_Pond[mon] = DP.Pond[mon]+LP.Pond[mon] + tableAW.Decomp_FlowT[mon]*area.Pond[DU_id]+ETr.Pond_Op[mon] + OW.Pond[mon]
                Eff_Rain_Pond[iyr][mon] = min( Demand_Pond[mon], 0.1*tableRain.Vol_Pond_Op[iyr][mon] )
                Pond_Op[iyr][mon] = tableRain.Vol_Pond_Op[iyr][mon] - Eff_Rain_Pond[iyr][mon]
                
                Pond_NonOp[iyr][mon]=max(0, tableRain.Vol_Pond_NonOp[iyr][mon] -ETr.Pond_NonOp[mon])
                
                
                # Burn
                Eff_Rain_Burn[iyr][mon] = min( DP.Burn[iyr][mon]+ETr.Burn[iyr][mon], tableRain.Vol_Burn[iyr][mon] )
                Burn[iyr][mon] = tableRain.Vol_Burn[iyr][mon] - Eff_Rain_Burn[iyr][mon]
                
                # Sum
                Sum[iyr][mon] = Grow[iyr][mon] + Pond_Op[iyr][mon] + Pond_NonOp[iyr][mon] + NonPond[iyr][mon] + Burn[iyr][mon]
                Sum[iyr][mon] = (1-lookup.Reuse_Runoff[mon])* Sum[iyr][mon]

def record(outFile):
    
    for calendar_year in range(1922, 2006):
        iyr = calendar_year-START_YEAR+1
        for mon in range(1,13):
            outFile.writelines( str(calendar_year)+'  '+str(mon) +'  '+ str(Sum[iyr][mon])+'\n' )


find()

#iyr = 1944-START_YEAR+1
#print DP.Pond[12], LP.Pond[12], tableAW.Decomp_FlowT[12]*area.Pond[75], ETr.Pond_Op[12]

#print Sum[iyr]
