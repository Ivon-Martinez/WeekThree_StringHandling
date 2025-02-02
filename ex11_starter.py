#!/usr/bin/python
from os.path import split

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium)

print('-' * len(Belgium), end='')
BelSep = Belgium.split(',')

Belgium = ':'.join(BelSep)

print(Belgium, end=':')
print(int(BelSep[1]) + int(BelSep[3]))