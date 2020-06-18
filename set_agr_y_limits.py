import sys
import re

try:
    agrname = sys.argv[1]
    ymin = str(float(sys.argv[2]))
    ymax = str(float(sys.argv[3]))
except:
    sys.exit('usage: set_agr_y_limits filename ymin ymax')

f = open(agrname)
lines = f.read()
f.close()
newlines = re.sub(r'world (-?\d+\.\d+), -?\d+\.\d+, (-?\d+\.\d+), -?\d+\.\d+', r'world \1, '+ymin+r', \2, '+ymax,lines)
f = open(agrname,'w')
f.write(newlines)
f.close()