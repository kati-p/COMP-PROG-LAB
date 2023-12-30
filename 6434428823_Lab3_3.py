# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:07:06 2021

@author: DELUX
"""

x,y = input('Enter x,y : ').split(',')
x = float(x)
y = float(y)

Ax = 0<x<40
Ay = 0<y<40
Bx = -40<x<10
By = -20<y<20

if Ax==Bx and Ay==By:
    print('(',x,',',y,')','is in C')
elif Ax and Ay:
    print('(',x,',',y,')','is in A')
elif Bx and By:
    print('(',x,',',y,')','is in B')
else:
    print('(',x,',',y,')','is in D')