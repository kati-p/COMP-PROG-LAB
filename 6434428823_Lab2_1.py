# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:05:42 2021

@author: DELUX
"""

a, b, c = input('Enter coefficients a, b, c : ').split(',')
a = float(a)
b = float(b)
c = float(c)

xp = (-b+(b**2-4*a*c)**0.5)/(2*a) 
xm = (-b-(b**2-4*a*c)**0.5)/(2*a)

print('x =', xp,',', xm)

