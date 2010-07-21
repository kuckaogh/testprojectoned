# main function
import tableRain
import DP, RR, SWR, AWT
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
AWT_File = open('AWT_out.out','w') 

DP_Sum = zeros_3D(75,85,12)
RR_Sum = zeros_3D(75,85,12)
SWR_Sum = zeros_3D(75,85,12)
AWT_Total = zeros_3D(75,85,12)
DP_Sum[75] = DP.Sum
RR_Sum[75] = RR.Sum
SWR_Sum[75] = SWR.Sum
AWT_Total[75] = AWT.Total

#print AWr.Pond[calendar_year-START_YEAR+1]
#print AWr.NonPond

#print LP.Grow


#print RR.NonPond[iyr]


#DP.record(DP_File)
output(DP_File,DP_Sum[75],75,75)
#RR.record(RR_File)
output(RR_File,RR_Sum[75],75,75)
#SWR.record(SWR_File)
output(SWR_File,SWR_Sum[75],75,75)
output(AWT_File,AWT_Total[75],75,75)
#LP.record(LP_File)
#ETr.record(ETr_File)
#AWr.record(AWr_File)
