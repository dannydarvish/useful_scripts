import sys
import re

try:
    agrname = sys.argv[1]
    spacing = sys.argv[2]
except:
    sys.exit('usage: set_agr_major_x_tick_spacing filename spacing')

f = open(agrname)
lines = f.read()
f.close()
newlines = re.sub(r'xaxis  tick major (\d+.\d+)|xaxis  tick major \d',r'xaxis  tick major ' + spacing,lines)
f = open(agrname,'w')
f.write(newlines)
f.close()