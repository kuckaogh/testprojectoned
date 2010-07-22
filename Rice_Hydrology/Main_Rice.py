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

def parallel(DU_id):
    
    ETr.find(DU_id)
    OW.find(DU_id)
    ETmet.find(DU_id)
    LP.find(DU_id)
    DP.find(DU_id)
    AWr.find(DU_id)
    RR.find(DU_id)
    SWR.find(DU_id)
    AWT.find(DU_id)

    DP_Sum[DU_id] = DP.Sum
    RR_Sum[DU_id] = RR.Sum
    SWR_Sum[DU_id] = SWR.Sum
    #SWR_NonPond[DU_id] = SWR.NonPond
    AWT_Total[DU_id] = AWT.Total
    
    #DP.record(DP_File)
    output(DP_File,DP_Sum,DU_id)
    #RR.record(RR_File)
    output(RR_File,RR_Sum,DU_id)
    #SWR.record(SWR_File)
    output(SWR_File,SWR_Sum,DU_id)
    output(AWT_File,AWT_Total,DU_id)

#print AWr.Pond[calendar_year-START_YEAR+1]
#print AWr.NonPond

#print LP.Grow
parallel(75)

#print RR.NonPond[iyr]


rainfall_File = open('rainfall_75.out','w') 
output_4digit(rainfall_File,tableRain.Rain,75)

rain_Vol_Grow_File = open('rain_vol_grow_75.out','w') 
output_4digit(rain_Vol_Grow_File,tableRain.Vol_Grow,75)

rain_Vol_NonPond_File = open('rain_vol_nonpond_75.out','w') 
output_4digit(rain_Vol_NonPond_File,tableRain.Vol_NonPond,75)

rain_Vol_Pond_Op_File = open('rain_vol_pond_op_75.out','w') 
output_4digit(rain_Vol_Pond_Op_File,tableRain.Vol_Pond_Op,75)

rain_Vol_Pond_NonOp_File = open('rain_vol_pond_nonop_75.out','w') 
output_4digit(rain_Vol_Pond_NonOp_File,tableRain.Vol_Pond_NonOp,75)

rain_Vol_Burn_File = open('rain_vol_burn_75.out','w') 
output_4digit(rain_Vol_Burn_File,tableRain.Vol_Burn,75)


SWRGrow_File = open('SWRGrow_out.out','w') 
output_2D(SWRGrow_File,SWR.Grow)

SWRPond_File = open('SWRPond_out.out','w') 
output_2D(SWRPond_File,SWR.Pond)

SWRWaterPond_File = open('SWRWaterPond_out.out','w') 
output_2D(SWRWaterPond_File,SWR.WaterPonded_Pond)

#SWRNonPond_File = open('SWRNonPond_out.out','w') 
#output(SWRNonPond_File,SWR_NonPond,75,75)


#LP.record(LP_File)
#ETr.record(ETr_File)
#AWr.record(AWr_File)
