from functions import *

START_YEAR = 1921
UNIT = 'ft'

DU = ['NA']

Rain = zeros_2D(100,12)

rainfall_File = open('rainfall.txt','r')

lines = rainfall_File.readlines()

title =lines[0].split()
DU.append(title[1+1])

n_lines = len(lines[1:])

for line in lines[1:]:
    line=line.strip().split()
    try:
        year = int(line[0])
        month = int(line[1])
        iyr = year - START_YEAR + 1
        #print year, month, iyr
        Rain[iyr][month] = float(line[2])
    except:
        print 'error!'

#i=1
#for iyr in range(1,3):
#    for mon in range(1,13):
#        line = lines[i].split()      
#        if len(line[1]) > 0:
#            Rain_WaterMonth[iyr][mon] = float(line[2])
#        i=i+1  
        
         

#    #print line
#    #line = line.strip()
#    for mon in range(1,13):
#        
#        if len(line[1]) > 0:
#            Rainfall.append(float(line[2]))
#



print Rain[1954-START_YEAR+1][6]