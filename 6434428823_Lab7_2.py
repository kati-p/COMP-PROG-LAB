# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:00:25 2021

@author: DELUX
"""

pos = input('Initial position : ')
x , y = pos.split()
x = int(x)
y = int(y)
Invalid = False

fm = open('move.txt')

for line in fm:
    if line.strip() == 'L':
        if x - 1 != -10:
            x = x - 1
    elif line.strip() == 'R':
        if x + 1 != 10:
            x = x + 1
    elif line.strip() == 'U':
        if y + 1 != 10:
            y = y + 1
    elif line.strip() == 'D':
        if y - 1 != -10:
            y = y - 1
    else:
        Invalid = True
        break        
               
fm.close()

if Invalid == True:
    print('Invalid command')
else:
    print('Robot stops at' , str(x) + ',' + str(y))