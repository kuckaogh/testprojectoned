# find DU rainfall (ft/month) from WBA rainfall data (in/month)
import re
import area, lookup
import tableRainWBA
from functions import *
from constants import *

Rain           = zeros_3D(75,100,12)
Vol_NonPond    = zeros_3D(75,100,12)
Vol_Pond_Op    = zeros_3D(75,100,12)
Vol_Pond_NonOp = zeros_3D(75,100,12)
Vol_Grow       = zeros_3D(75,100,12)
Vol_Burn       = zeros_3D(75,100,12)

DU_name_short = ['NA']

for (id, _name) in enumerate(area.DU_name[1:]):
    #print _name
    m = re.findall(r'([a-zA-Z0-9]+)_', _name)
    DU_name_short.append( m[0])

#print DU_name_short
#print area.DU_name


for (DU_id, _DU_name) in enumerate(DU_name_short):
    
    for (_WBA_id, _WBA_name) in enumerate(tableRainWBA.WBA_name_short):
        if DU_id > 0: 
                if cmp(_DU_name.upper(), _WBA_name.upper()) == 0:
                #print _DU_id+1, _WBA_id+1, _DU_name, _WBA_name,area.DU_name[_DU_id+1],tableRainWBA.WBA_name[_WBA_id+1]  
                    Rain[DU_id] = tableRainWBA.Rain[_WBA_id]
                    #Rain[DU_id] = Rain[DU_id]/12
                    

                    for calendar_year in range (START_YEAR, END_YEAR+1):
                        iyr = calendar_year - START_YEAR + 1
                        for month in range (1,12+1):
                            Vol_NonPond[DU_id][iyr][month] = lookup.NonGrow[month]*area.NonPond[DU_id]*Rain[DU_id][iyr][month]
            
                            Vol_Grow[DU_id][iyr][month]    = lookup.Grow[month]*area.Total[DU_id]*Rain[DU_id][iyr][month]
                            Vol_Pond_Op[DU_id][iyr][month]    = lookup.Pond[month]*area.Pond[DU_id]*Rain[DU_id][iyr][month]
                            Vol_Pond_NonOp[DU_id][iyr][month] = (1.0-lookup.Pond[month])*area.Pond[DU_id]*Rain[DU_id][iyr][month] - Vol_Grow[DU_id][iyr][month]*area.Pond_Ratio[DU_id]
                            Vol_Pond_NonOp[DU_id][iyr][month] =  max(0,Vol_Pond_NonOp[DU_id][iyr][month])
                            Vol_Burn[DU_id][iyr][month]    = lookup.NonGrow[month]*area.Burn[DU_id]*Rain[DU_id][iyr][month]   
                    #
                    #Vol_NonPond[DU_id]    = Vol_NonPond[_WBA_id]   
                    #Vol_Grow[DU_id]       = Vol_Grow[_WBA_id]      
                    #Vol_Pond_Op[DU_id]    = Vol_Pond_Op[_WBA_id]   
                    #
                    #Vol_Pond_NonOp[DU_id] = Vol_Pond_NonOp[_WBA_id]
                    #Vol_Pond_NonOp[DU_id] = Vol_Pond_NonOp[_WBA_id]
                    #Vol_Burn[DU_id]       = Vol_Burn[_WBA_id]      
                
                              
                
#print Rain[75][25][3]


                