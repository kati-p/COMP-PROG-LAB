# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 14:13:03 2021

@author: DELUX
"""

a, b, c = input('Enter Length of 3 sides : ').split(',')
a = float(a)
b = float(b)
c = float(c)

ca = b+c > c
cb = a+c > b
cc = a+b > c

print('Triangle:', ca and cb and cc)