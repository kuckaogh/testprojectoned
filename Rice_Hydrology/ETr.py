import os #os.getcwd()
import area, lookup, tableRain, tableET   # user input
#import ETr              # output
#from numpy import *   # bug in ironclad
from functions import *
from constants import *

#ETr_out = open('out', 'w')

#def ETr_initialize(85)
Pond = zeros(12)
NonPond = zeros(12)
Grow = zeros(12)
Burn = zeros_2D(85,12)
#Sum = zeros_2D(85,12)

#print tableET.Burn[1:12]
#print lookup.NonGrow[1:12]
#print area.Burn[75]


def find():

    for DU_id in (75,75):
        for mon in range(1, 12+1): # 1 to 12
    
            Grow[mon] = lookup.Grow[mon] * tableET.Grow[mon] * area.Total[DU_id]
            
            Pond[mon] = lookup.Pond[mon] * tableET.Pond[mon] * area.Pond[DU_id] - Grow[mon]*area.Pond_Ratio[mon]
            Pond[mon] = max(0,Pond[mon])
            
            NonPond[mon] = tableET.NonPond[mon] * area.NonPond[DU_id] - Grow[mon]*area.NonPond_Ratio[mon]
            NonPond[mon] = max(0,NonPond[mon])
    
    
        for calendar_year in range(1922, 2006):
            iyr = calendar_year-tableRain.START_YEAR+1
            for mon in range(1, 12+1): # 1 to 12
                Burn[iyr][mon] = lookup.NonGrow[mon] * tableET.Burn[mon] * area.Burn[DU_id]

def record(outFile):
    
    for calendar_year in range(1922, 2006):
        iyr = calendar_year-tableRain.START_YEAR+1
        for mon in range(1,13):
            outFile.writelines( str(calendar_year)+'  '+str(mon) +'  '+ str(Grow[mon])+'  '+ str(Pond[mon])+'  '+ str(NonPond[mon])+'  '+ str(Burn[iyr][mon])+'\n' )
            
