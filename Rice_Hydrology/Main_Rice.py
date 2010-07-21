# main function
import tableRain
import ETr, OW, ETmet, LP, DP, AWr, RR, SWR, AWT
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
SWR_NonPond = zeros_3D(75,85,12)
AWT_Total = zeros_3D(75,85,12)

ETr.find(75)
OW.find(75)
ETmet.find(75)
LP.find(75)
DP.find(75)
AWr.find(75)
RR.find(75)
SWR.find(75)
AWT.find(75)

DP_Sum[75] = DP.Sum
RR_Sum[75] = RR.Sum
SWR_Sum[75] = SWR.Sum
SWR_NonPond[75] = SWR.NonPond
AWT_Total[75] = AWT.Total

#print AWr.Pond[calendar_year-START_YEAR+1]
#print AWr.NonPond

#print LP.Grow


#print RR.NonPond[iyr]


#DP.record(DP_File)
output(DP_File,DP_Sum,75,75)
#RR.record(RR_File)
output(RR_File,RR_Sum,75,75)
#SWR.record(SWR_File)
output(SWR_File,SWR_Sum,75,75)

SWRGrow_File = open('SWRGrow_out.out','w') 
output_2D(SWRGrow_File,SWR.Grow)

SWRPond_File = open('SWRPond_out.out','w') 
output_2D(SWRPond_File,SWR.Pond)

SWRWaterPond_File = open('SWRWaterPond_out.out','w') 
output_2D(SWRWaterPond_File,SWR.WaterPonded_Pond)

SWRNonPond_File = open('SWRNonPond_out.out','w') 
output(SWRNonPond_File,SWR_NonPond,75,75)

output(AWT_File,AWT_Total,75,75)
#LP.record(LP_File)
#ETr.record(ETr_File)
#AWr.record(AWr_File)
