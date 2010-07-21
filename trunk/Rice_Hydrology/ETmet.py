# ET met


import area, lookup, tableRain, tableET   # user input
import ETr, OW             
#from numpy import *   # bug in ironclad
from functions import *
from constants import *


NonPond = zeros_2D(85,12)


def find(DU_id):

    for calendar_year in range(1922, 2006):
        iyr = calendar_year-START_YEAR+1
        for mon in range(1, 12+1): # 1 to 12
            NonPond[iyr][mon] = min( (tableRain.Vol_NonPond[DU_id][iyr][mon] + OW.NonPond[mon]), ETr.NonPond[mon] )
