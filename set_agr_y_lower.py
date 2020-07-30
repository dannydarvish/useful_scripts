import sys
import re

try:
    agrname = sys.argv[1]
    ymin = str(float(sys.argv[2]))
except:
    sys.exit('usage: set_agr_y_lower filename ymin')

f = open(agrname)
lines = f.read()
f.close()
newlines = re.sub(r'world (-?\d+\.\d+), -?\d+\.\d+, (-?\d+\.\d+), (-?\d+\.\d+)', r'world \1, '+ymin+r', \2, \3',lines)
f = open(agrname,'w')
f.write(newlines)
f.close()