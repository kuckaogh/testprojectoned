import re
import area

inFile = open('rain_by_WBA.txt','r')

WBA_name=['NA']
WBA_name_short=[]
DU_name_short =[]


lines = inFile.readlines()

line = lines[1]
line = line.strip().split()
line = line[2:]
WBA_name[1:] = line

for name in WBA_name:
    shortname = name.replace('WBA','')
    WBA_name_short.append(shortname)
#print line
for name in area.DU:
    shortname = name.replace 
#print WBA_name_short

str = 'spam_egg_yel'
m = re.search(r'(?<=_)\w+', str)
m = re.findall(r'([a-zA-Z0-9]+)_', str)
print m
#strnew = str.replace('_'+m.group(0),'')
#print strnew



#for line in lines[2:]:
#    line = line.strip().split()
#    print line[2]