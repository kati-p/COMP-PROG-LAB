# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:31:45 2021

@author: DELUX
"""

a, b, c = input('Enter coefficients a, b, c : ').split(',')
a = float(a)
b = float(b)
c = float(c)

n = b**2-4*a*c
if n<0 or a==0:
    print('No real solution.')
elif n==0:
    x = (-b+(b**2-4*a*c)**0.5)/(2*a)
    print('x =', x)
else:
    xp = (-b+(b**2-4*a*c)**0.5)/(2*a) 
    xm = (-b-(b**2-4*a*c)**0.5)/(2*a)
    print('x =', xp,',', xm)