# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 14:25:59 2021

@author: DELUX
"""

a, b, c = input('Enter Length of 3 sides : ').split(',')
a = float(a)
b = float(b)
c = float(c)

ca = a**2 == b**2 + c**2
cb = b**2 == a**2 + c**2
cc = c**2 == a**2 + b**2

print('Right triangle:', ca or cb or cc)