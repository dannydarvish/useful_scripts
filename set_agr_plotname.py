import sys
import re

try:
    agrname = sys.argv[1]
    name = sys.argv[2]
except:
    sys.exit('usage: set_agr_plotname.py filename plotname')

f = open(agrname)
lines = f.read()
f.close()
newlines = re.sub(r'\\f\{0\}Re\\f\{\} \\f\{1\}C\\sAA\\N\(t\),   \\m\{3\}.*"', f'{name}"', lines)
f = open(agrname,'w')
f.write(newlines)
f.close()