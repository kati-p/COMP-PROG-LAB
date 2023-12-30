# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:04:30 2021

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
        x = x - 1
    elif line.strip() == 'R':
        x = x + 1
    elif line.strip() == 'U':
        y = y + 1
    elif line.strip() == 'D':
        y = y - 1
    else:
        Invalid = True
        break
        
fm.close()

if Invalid == True:
    print('Invalid command')
else:
    print('Robot stops at' , str(x) + ',' + str(y))