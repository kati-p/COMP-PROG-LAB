# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 14:04:50 2021

@author: DELUX
"""

a, b, c = input('Enter coefficients a, b, c : ').split(',')
a = float(a)
b = float(b)
c = float(c)

n = b**2-4*a*c

print('Can use quadratic formula:', n>=0 and a>0)