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


DP_Sum = zeros_3D(75,100,12)
RR_Sum = zeros_3D(75,100,12)
SWR_Sum = zeros_3D(75,100,12)
SWR_NonPond = zeros_3D(75,100,12)
AWT_Total = zeros_3D(75,100,12)

def parallel(DU_id,year_begin, month_begin, year_end, month_end):
    
    DP_File =       open('DP_'+str(DU_id)+'.out','w') 
    RR_File =       open('RR_'+str(DU_id)+'.out','w') 
    SWR_File =      open('SWR_'+str(DU_id)+'.out','w') 
    AWT_File =      open('AWT_'+str(DU_id)+'.out','w')
    rainfall_File = open('rainfall_'+str(DU_id)+'.out','w') 
    
    ETr.find(DU_id,year_begin, year_end)
    OW.find(DU_id)
    ETmet.find(DU_id,year_begin, year_end)
    LP.find(DU_id,year_begin, year_end)
    DP.find(DU_id,year_begin, year_end)
    AWr.find(DU_id,year_begin, year_end)
    RR.find(DU_id,year_begin, year_end)
    SWR.find(DU_id,year_begin, year_end)
    AWT.find(DU_id,year_begin, year_end)

    DP_Sum[DU_id] = DP.Sum
    RR_Sum[DU_id] = RR.Sum
    SWR_Sum[DU_id] = SWR.Sum
    #SWR_NonPond[DU_id] = SWR.NonPond
    AWT_Total[DU_id] = AWT.Total
    
    #DP.record(DP_File)
    output(DP_File,DP_Sum,DU_id,year_begin, month_begin, year_end, month_end)
    #RR.record(RR_File)
    output(RR_File,RR_Sum,DU_id,year_begin, month_begin, year_end, month_end)
    #SWR.record(SWR_File)
    output(SWR_File,SWR_Sum,DU_id,year_begin, month_begin, year_end, month_end)
    output(AWT_File,AWT_Total,DU_id,year_begin, month_begin, year_end, month_end)
    
    
    output_4digit(rainfall_File,tableRain.Rain,DU_id,year_begin, month_begin, year_end, month_end)

#print AWr.Pond[calendar_year-START_YEAR+1]
#print AWr.NonPond

#print LP.Grow
parallel(75,1921,10,2006,9)

#print RR.NonPond[iyr]



#
#rain_Vol_Grow_File = open('rain_vol_grow_75.out','w') 
#output_4digit(rain_Vol_Grow_File,tableRain.Vol_Grow,75)
#
#rain_Vol_NonPond_File = open('rain_vol_nonpond_75.out','w') 
#output_4digit(rain_Vol_NonPond_File,tableRain.Vol_NonPond,75)
#
#rain_Vol_Pond_Op_File = open('rain_vol_pond_op_75.out','w') 
#output_4digit(rain_Vol_Pond_Op_File,tableRain.Vol_Pond_Op,75)
#
#rain_Vol_Pond_NonOp_File = open('rain_vol_pond_nonop_75.out','w') 
#output_4digit(rain_Vol_Pond_NonOp_File,tableRain.Vol_Pond_NonOp,75)
#
#rain_Vol_Burn_File = open('rain_vol_burn_75.out','w') 
#output_4digit(rain_Vol_Burn_File,tableRain.Vol_Burn,75)


#SWRGrow_File = open('SWRGrow_out.out','w') 
#output_2D(SWRGrow_File,SWR.Grow)
#
#SWRPond_File = open('SWRPond_out.out','w') 
#output_2D(SWRPond_File,SWR.Pond)
#
#SWRWaterPond_File = open('SWRWaterPond_out.out','w') 
#output_2D(SWRWaterPond_File,SWR.WaterPonded_Pond)
#



#LP.record(LP_File)
#ETr.record(ETr_File)
#AWr.record(AWr_File)
