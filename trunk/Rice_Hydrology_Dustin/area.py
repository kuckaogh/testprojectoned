
DU_name= ['NA'] # 75 is 73_XA

Pond_Ratio = ['NA']
Pond = ['NA']
NonPond_Ratio = ['NA']
NonPond = ['NA']
Burn_Ratio = ['NA']
Burn = ['NA']
Total = ['NA']


areaFile = open('table_area.txt', 'r')

lines = areaFile.readlines()
for i,line in enumerate (lines[1:]):  #skip comment 

    line = line.strip().split()
    #print line
    try:
        DU_name.append(line[0])
        
        _total = float(line[1])
        _pr = float(line[2])/100
        _npr = float(line[3])/100
        _br  = 1.0 - _pr - _npr
        
        Total.append(_total)
        
        Pond_Ratio.append(_pr)
        Pond.append( _total * _pr )
        NonPond_Ratio.append(_npr)
        NonPond.append( _total * _npr )
        Burn_Ratio.append( _br )
        Burn.append( _total * _br)
    except:
        print "Error!"
    