# main function
import tableRain
import DP, RR, SWR, AW_Sum
#import ETr            # output
#from numpy import *   # bug in ironclad
from functions import *
from constants import *

#ETr_File = open('ETr_out.out','w') 
#AWr_File = open('AWr_out.out','w') 
#LP_File = open('LP_out.out','w') 
DP_File = open('DP_out.out','w') 
RR_File = open('RR_out.out','w') 
SWR_File = open('SWR_out.out','w') 
AW_Sum_File = open('AW_Sum_out.out','w') 

calendar_year=1934
iyr=calendar_year-START_YEAR+1


#print AWr.Pond[calendar_year-START_YEAR+1]
#print AWr.NonPond

#print LP.Grow


#print RR.NonPond[iyr]


#DP.record(DP_File)
output(DP_File,DP.Sum,75,75)
#RR.record(RR_File)
output(RR_File,RR.Sum,75,75)
#SWR.record(SWR_File)
output(SWR_File,SWR.Sum,75,75)
AW_Sum.record(AW_Sum_File)
#LP.record(LP_File)
#ETr.record(ETr_File)
#AWr.record(AWr_File)
