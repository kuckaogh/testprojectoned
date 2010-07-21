#Operation Water

import area, tableAW, tableRain, lookup    # user input
#import DP              # output
#from numpy import *   # bug in ironclad
from functions import *
from constants import *

NonPond = zeros(12)
Pond = zeros(12)
Grow = zeros(12)


def find(DU_id):

    for mon in range(1, 12+1): # 1 to 12
        NonPond[mon]  = tableAW.NonPond[mon] * area.NonPond[DU_id]
        Pond[mon]     = tableAW.Pond[mon] * area.Pond[DU_id]
        Grow[mon]     = lookup.Grow[mon]* tableAW.Grow[mon] * area.Total[DU_id]
    
