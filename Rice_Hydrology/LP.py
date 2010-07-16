import os #os.getcwd()
import area, lookup, tableRain    # user input
#import DP              # output
#from numpy import *   # bug in ironclad
from functions import *
from constants import *

#outFile = open('LP_out', 'w')

Pond = zeros(12)
NonPond = zeros(12)
Grow = zeros(12)
Burn = zeros_2D(85,12)
Sum = zeros_2D(85,12)

def find():

    for DU_id in (75,75):
        for mon in range(1, 12+1): # 1 to 12
            Pond[mon] = lookup.Pond[mon] * LP_RATE * area.Pond[DU_id]
            Grow[mon] = lookup.Grow[mon] * LP_RATE * area.Total[DU_id]
            NonPond[mon]  = 0
    
    
        for calendar_year in range(1922, 2006):
            iyr = calendar_year - tableRain.START_YEAR + 1
            for mon in range(1, 12+1): # 1 to 12
                Burn[iyr][mon] = lookup.NonGrow[mon] * min(tableRain.Rain[iyr][mon],LP_RATE)* area.Burn[DU_id]
                Sum[iyr][mon] = Burn[iyr][mon] + ( Pond[mon] + NonPond[mon] + Grow[mon] )

def write_LP(outFile):
    
    for calendar_year in range(1922, 2006):
        iyr = calendar_year-tableRain.START_YEAR+1
        for mon in range(1,13):
            outFile.writelines( str(calendar_year)+'  '+str(mon) +'  '+ str(Sum[iyr][mon])+'\n' )


