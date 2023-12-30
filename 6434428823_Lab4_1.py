# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 13:12:52 2021

@author: DELUX
"""

ip = input('Choose circle, square or rectangle: ')
if ip == 'circle' or ip == 'square' or ip == 'rectangle':
    if ip == 'circle':
        r = float(input('Length of the radius of the circle: '))
        x = 22/7*r**2
        print('Area is',x)
    if ip == 'square':
        l = float(input('Length of the side of the square: '))
        x = l**2
        print('Area is',x)
    if ip == 'rectangle':
        L,l = input('Length of two sides of the rectangle: ').split(',')
        L = float(L)
        l = float(l)
        x = L*l
        print('Area is',x)
else:
    print('Invalid choice.')


    