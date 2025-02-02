#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print(len(Belgium)*'-')
#print(Belgium)
# checking the length of the string

Bel = Belgium.replace(',',':')
print(Bel)

# Bel = Belgium.split(',')
# Belgium = ":".join(Bel)
# print(Belgium)
# print(int(Bel[1])+int(Bel[3])

# country = int(Belgium[8:16])
# city = int(Belgium[26:32])
# print(city + country)

print(int(Belgium[26:32]) + int(Belgium[8:16]))





