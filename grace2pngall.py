import os

files = os.popen('ls').read().split()

for file in files:
    if file[-3:] == 'agr':
        os.system('grace2png %s' % file)

