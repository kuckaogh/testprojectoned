# ET met


import area, lookup, tableRain, tableET   # user input
import ETr, OW             
#from numpy import *   # bug in ironclad
from functions import *
from constants import *

#ETr_out = open('out', 'w')

#def ETr_initialize(85)
#Pond = zeros(12)
NonPond = zeros_2D(85,12)
#Grow = zeros(12)
#Burn = zeros_2D(85,12)
#Sum = zeros_2D(85,12)

#print tableET.Burn[1:12]
#print lookup.NonGrow[1:12]
#print area.Burn[75]





for DU_id in (75,75):
    for mon in range(1, 12+1): # 1 to 12

        
        k=3


    for calendar_year in range(1922, 2006):
        iyr = calendar_year-tableRain.START_YEAR+1
        for mon in range(1, 12+1): # 1 to 12
            NonPond[iyr][mon] = min( (tableRain.Vol_NonPond[iyr][mon] + OW.NonPond[mon]), ETr.NonPond[mon] )

def record(outFile):
    
    for calendar_year in range(1922, 2006):
        iyr = calendar_year-tableRain.START_YEAR+1
        for mon in range(1,13):
            outFile.writelines( str(calendar_year)+'  '+str(mon) +'  '+ str(NonPond[iyr][mon])+' '+str(OW.NonPond[mon]) +'\n' )
            

