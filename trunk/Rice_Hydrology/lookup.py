#lookup table for operations and re-use water ratio

Grow=['NA']
Pond = ['NA'] 
NonGrow=['NA']
Reuse_Runoff =['NA']
Reuse_Return =['NA']

lookup_flags_file = open('lookup.txt', 'r')

lines = lookup_flags_file.readlines()
for i,line in enumerate (lines[2:]):  #skip title and comment 
    line = line.strip().split()
    #print line
    #line = line.strip()
    try:
        Grow.append(float(line[1]))
        NonGrow.append(1.0-float(line[1]))
        Pond.append(float(line[2])) 
        Reuse_Runoff.append(float(line[3])) 
        Reuse_Return.append(float(line[4])) 
        
    except:
        print "error in lookup.py!"
