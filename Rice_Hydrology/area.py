
DU= ['NA'] # 75 is 73_XA

Pond_Ratio = ['NA']
Pond = ['NA']
NonPond_Ratio = ['NA']
NonPond = ['NA']
Burn_Ratio = ['NA']
Burn = ['NA']
Total = ['NA']


areaFile = open('area_table.txt', 'r')

lines = areaFile.readlines()
for i,line in enumerate (lines[1:]):  #skip comment 

    line = line.strip().split()
    #print line
    try:
        DU.append(line[0])
        
        _total = float(line[1])
        pr = float(line[2])/100
        npr = float(line[3])/100
        br  = 1.0 - pr - npr
        
        Total.append(_total)
        
        Pond_Ratio.append(pr)
        Pond.append( _total * pr )
        NonPond_Ratio.append(npr)
        NonPond.append( _total * npr )
        Burn_Ratio.append( br )
        Burn.append( _total * br)
    except:
        print "Error!"
    