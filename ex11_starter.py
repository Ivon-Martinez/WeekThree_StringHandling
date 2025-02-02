#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# Question 1(a)
print(len(Belgium)*'-')
# print(Belgium)
# checking the length of the string & multiplying hyphens by length of the string.

#Question 1(b)
print(Belgium.replace(',',':'))
# replacing the commas in the string by colon.

# Question 1(c)
print(int(Belgium[26:32]) + int(Belgium[8:16]))

# Alternative methods
# Bel = Belgium.split(',')
# Belgium = ":".join(Bel)
# print(Belgium)
# print(int(Bel[1])+int(Bel[3])

# country = int(Belgium[8:16])
# city = int(Belgium[26:32])
# print(city + country)



