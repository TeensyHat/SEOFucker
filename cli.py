#! /bin/python3
from sys import argv
from os.path import isfile
from helpers import *

help = '''Usage:
seofucker [words,splitted,by,comma] [output file]
'''

if 'help' in ''.join(argv).lower():
    print(help)
    exit()

if len(argv) != 3:
    print('Error: Not enough arguments.')
    print(help)
    exit()

words = argv[1].replace(' ', '').replace('.', '').split(',')
opfile = argv[2]
if isfile(opfile):
    print('Warning: The file exists, wanna overwrite it?')
    yesno = input('(Y/n) ').lower()
    if yesno.startswith('y'):
        print('Ok.')
    else:
        print('Exitting...')
        exit()

non_dup = []
for i in words:
    if not i in non_dup:
        non_dup.append(i)

del words

combos = get_combos(non_dup)
html = get_html(combos)
print('Html:\n'+html)
try:
    open(opfile, 'w').write(html)
except:
    print('Can\'t write to the output file.')
