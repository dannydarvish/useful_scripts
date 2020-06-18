import sys
import re

try:
    agrname = sys.argv[1]
    axis = sys.argv[2]
except:
    sys.exit('usage: turn_off_agr_labels.py filename axis (x or y) keep_tick_labels (optional)')

f = open(agrname)
lines = f.read()
f.close()
newlines = re.sub(rf'@    {axis}axis  label.*\n', '', lines)
keep_tick_lables = False
try:
    argv3 = sys.argv[3]
    if argv3 == 'keep_tick_labels':
        keep_tick_lables = True
except:
    pass
if not keep_tick_lables:
    newlines = re.sub(rf'@    {axis}axis  ticklabel on', rf'@    {axis}axis  ticklabel off', newlines)
f = open(agrname,'w')
f.write(newlines)
f.close()