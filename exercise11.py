#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print(len(Belgium)*'-') # printing a line of hyphens with the same length.
print(Belgium) #checking that the strings are the same line with the hyphen
#exercise 1b
Bel= Belgium.split(',')
print(Bel)
Belgium = ":".join(Bel)
print(Belgium)
#exercise
Bel2 = Belgium.replace(',',':')
print(Bel2)
#another way
print(Belgium.replace(',',':'))
#exerciseC
#we are looking to add the first field and the fourth field. However python starts with 0 so we would be looking to do the first and third field.
print(int(Bel[1])+int(Bel[3]))






