
import area, lookup, tableRain    # user input
#from numpy import *   # bug in ironclad
from functions import *
from constants import *


Pond = zeros(12)
NonPond = zeros(12)
Grow = zeros(12)
Burn = zeros_2D(100,12)
Sum = zeros_2D(100,12)

def find(DU_id,year_begin, year_end):

        for mon in range(1, 12+1): # 1 to 12
            Pond[mon] = lookup.Pond[mon] * DP_RATE * area.Pond[DU_id]
            Grow[mon] = lookup.Grow[mon] * DP_RATE * area.Total[DU_id]
            NonPond[mon]  = 0
    
    
        for calendar_year in range(year_begin, year_end+1):
            iyr = calendar_year - START_YEAR + 1
            for mon in range(1, 12+1): # 1 to 12
                Burn[iyr][mon] = lookup.NonGrow[mon] * min(tableRain.Rain[DU_id][iyr][mon],DP_RATE)* area.Burn[DU_id]
                Sum[iyr][mon] = Burn[iyr][mon] + ( Pond[mon] + NonPond[mon] + Grow[mon] )


            
