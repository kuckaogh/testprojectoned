Grow=['NA']
NonPond = ['NA'] 
Pond=['NA']
Burn = ['NA']

TableET_file = open('table_ET.txt', 'r')

lines = TableET_file.readlines()
for i,line in enumerate (lines[2:]):  #skip title and comment 
    line = line.strip().split()
    #print line
    #line = line.strip()
    try:
        Grow.append(float(line[1])/12)
        NonPond.append(float(line[2])/12)
        Pond.append(float(line[3])/12)
        Burn.append(float(line[4])/12)

    except:
        print "error in TableET.py!"
