from constants import *

def zeros(size):
    output = [['NA']]
    for i in range(0,size):
        output.append(0)
    return output   

def zeros_2D(sizeX, sizeY):
    output = [['NA']]
    for i in range(0,sizeX):
        output.append(zeros(sizeY))
    return output    

def zeros_3D(sizeX, sizeY, sizeZ):
    output = [['NA']]
    for i in range(0,sizeX):
        output.append(zeros_2D(sizeY, sizeZ))
    return output    


def output(outFile,var,DU_id,year_begin, month_begin,year_end,month_end):
    
    for calendar_year in range(year_begin, year_end+1):
        iyr = calendar_year-START_YEAR+1
        _mon_b = 1
        _mon_e = 12
        if calendar_year == year_begin: 
            _mon_b = month_begin
        elif calendar_year == year_end:
            _mon_e = month_end    
        
        for mon in range(_mon_b, _mon_e+1):
            #outFile.writelines( str(calendar_year)+'  '+str(mon) +'  '+ str(Sum[iyr][mon])+'\n' )
            #outFile.writelines( str(calendar_year)+'\t'+str(mon) +'\t'+ str(Sum[iyr][mon])+'\n' )
            #outFile.write( ("%4d\t%0.5f\n" %(calendar_year,Sum[iyr][mon])).rjust(9) )
            outFile.write( ("%d\t" %calendar_year).rjust(4)+("%d\t" %mon).rjust(4) )
            #for DU_id in range(ibegin,iend+1):
            outFile.write( ("%.2f\t" %var[DU_id][iyr][mon]).rjust(10)  )
            outFile.write( '\n' )
            #outFile.write( "ser %s \n" %(repr(Sum[iyr][mon]).rjust(2) ) )
            #for i in range(1,5):
            #    outFile.write( '%s\t' %str(area.DU[i]) )
            #    outFile.write( '\n' )    

def output_4digit(outFile,var,DU_id,year_begin,month_begin,year_end,month_end):
    
    for calendar_year in range(year_begin, year_end+1):
        iyr = calendar_year-START_YEAR+1
        
        _mon_b = 1
        _mon_e = 12
        if calendar_year == year_begin: 
            _mon_b = month_begin
        elif calendar_year == year_end:
            _mon_e = month_end    
        
        for mon in range(_mon_b, _mon_e+1):
            #outFile.writelines( str(calendar_year)+'  '+str(mon) +'  '+ str(Sum[iyr][mon])+'\n' )
            #outFile.writelines( str(calendar_year)+'\t'+str(mon) +'\t'+ str(Sum[iyr][mon])+'\n' )
            #outFile.write( ("%4d\t%0.5f\n" %(calendar_year,Sum[iyr][mon])).rjust(9) )
            outFile.write( ("%d\t" %calendar_year).rjust(4)+("%d\t" %mon).rjust(4) )
            #for DU_id in range(ibegin,iend+1):
            outFile.write( ("%.4f\t" %var[DU_id][iyr][mon]).rjust(10)  )
            outFile.write( '\n' )
            #outFile.write( "ser %s \n" %(repr(Sum[iyr][mon]).rjust(2) ) )
            #for i in range(1,5):
            #    outFile.write( '%s\t' %str(area.DU[i]) )
            #    outFile.write( '\n' )    
        
def output_2D(outFile,var):
    
        for mon in range(1,13):
            #outFile.writelines( str(calendar_year)+'  '+str(mon) +'  '+ str(Sum[iyr][mon])+'\n' )
            #outFile.writelines( str(calendar_year)+'\t'+str(mon) +'\t'+ str(Sum[iyr][mon])+'\n' )
            #outFile.write( ("%4d\t%0.5f\n" %(calendar_year,Sum[iyr][mon])).rjust(9) )
            outFile.write( ("%d\t" %mon).rjust(4) )

            outFile.write( ("%.2f\t" %var[mon]).rjust(10)  )
            outFile.write( '\n' )
            #outFile.write( "ser %s \n" %(repr(Sum[iyr][mon]).rjust(2) ) )
            #for i in range(1,5):
            #    outFile.write( '%s\t' %str(area.DU[i]) )
            #    outFile.write( '\n' )      