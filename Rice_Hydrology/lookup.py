Grow=['NA']
Pond = ['NA'] 
NonGrow=['NA']

lookup_flags_file = open('lookup.txt', 'r')

lines = lookup_flags_file.readlines()
for i,line in enumerate (lines[1:]):  #skip comment 
    line = line.strip().split()
    #print line
    #line = line.strip()
    try:
        Grow.append(float(line[1]))
        NonGrow.append(1.0-float(line[1]))
        Pond.append(float(line[2])) 
    except:
        print "error in lookup.py!"
