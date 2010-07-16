
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
        
        total = float(line[1])
        pr = float(line[2])/100
        npr = float(line[3])/100
        br  = 1.0 - pr - npr
        
        Total.append(total)
        
        Pond_Ratio.append(pr)
        Pond.append( total * pr )
        NonPond_Ratio.append(npr)
        NonPond.append( total * npr )
        Burn_Ratio.append( br )
        Burn.append( total * br)
    except:
        print "Error!"
    