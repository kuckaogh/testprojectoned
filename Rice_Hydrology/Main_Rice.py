import os #os.getcwd()
import tableRain
import ETr, LP, DP, AWr, RR
#import ETr            # output
#from numpy import *   # bug in ironclad
#from functions import *
from constants import *

ETr_File = open('ETr_out.out','w') 
AWr_File = open('AWr_out.out','w') 
LP_File = open('LP_out.out','w') 
DP_File = open('DP_out.out','w') 

calendar_year=1934
iyr=calendar_year-tableRain.START_YEAR+1

LP.find()
DP.find()

ETr.find()
#print ETr.Burn
AWr.find()

#print AWr.Pond[calendar_year-tableRain.START_YEAR+1]
#print AWr.NonPond

#print LP.Grow

RR.find()
#print RR.NonPond[iyr]
print tableRain.VolNonPond[iyr]

LP.record(LP_File)
DP.record(DP_File)
ETr.record(ETr_File)
AWr.record(AWr_File)