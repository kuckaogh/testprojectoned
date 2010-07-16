import os #os.getcwd()
import area, lookup, rain    # user input
import DP              # output
#from numpy import *   # bug in ironclad
from functions import *
from constants import *

DP_out = open('DP.out', 'w')

DP.Pond = zeros(12)
DP.NonPond = zeros(12)
DP.Grow = zeros(12)
DP.Burn = zeros_2D(85,12)
DP.Sum = zeros_2D(85,12)



for DU_id in (75,75):
    for mon in range(1, 12+1): # 1 to 12
        DP.Pond[mon] = lookup.Pond[mon] * DP_RATE * area.Pond[DU_id]
        DP.Grow[mon] = lookup.Grow[mon] * DP_RATE * area.Total[DU_id]
        DP.NonPond[mon]  = 0


    for calendar_year in range(1922, 2006):
        iyr = calendar_year-rain.START_YEAR+1
        for mon in range(1, 12+1): # 1 to 12
            DP.Burn[iyr][mon] = lookup.NonGrow[mon] * min(rain.Rain[iyr][mon],DP_RATE)* area.Burn[DU_id]
            DP.Sum[iyr][mon] = DP.Burn[iyr][mon] + ( DP.Pond[mon] + DP.NonPond[mon] + DP.Grow[mon] )

#print area.DU[75]
#print DP.Pond[1:]
#print DP.Grow[1:]
#print DP.Sum

for calendar_year in range(1922, 2006):
    iyr = calendar_year-rain.START_YEAR+1
    for mon in range(1,13):
        DP_out.writelines( str(calendar_year)+'  '+str(mon) +'  '+ str(DP.Sum[iyr][mon])+'\n' )
#print DP.Burn[1:]
#print rain.Rain[1967-rain.START_YEAR+1][4]


#raw_input("Press ENTER to exit")

