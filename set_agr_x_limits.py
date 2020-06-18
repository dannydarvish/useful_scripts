import sys
import re

try:
    agrname = sys.argv[1]
    xmin = str(float(sys.argv[2]))
    xmax = str(float(sys.argv[3]))
except:
    sys.exit('usage: set_agr_x_limits filename xmin xmax')

f = open(agrname)
lines = f.read()
f.close()
newlines = re.sub(r'world -?\d+\.\d+, (-?\d+\.\d+), -?\d+\.\d+, (-?\d+\.\d+)', r'world '+xmin+r', \1, '+xmax+r', \2',lines)
f = open(agrname,'w')
f.write(newlines)
f.close()