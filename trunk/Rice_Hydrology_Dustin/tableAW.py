Grow=['NA']
Grow_FlowT=['NA']
NonPond = ['NA'] 
Pond=['NA']
Decomp_FlowT = ['NA']

TableAW_file = open('table_AW.txt', 'r')

lines = TableAW_file.readlines()
for i,line in enumerate (lines[2:]):  #skip title and comment 
    line = line.strip().split()

    try:
        Grow.append(float(line[1])/12)
        Grow_FlowT.append(float(line[2])/12)
        Pond.append(float(line[3])/12)
        NonPond.append(float(line[4])/12)
        Decomp_FlowT.append(float(line[5])/12)
    
    except:
        print "error in TableAW.py!"