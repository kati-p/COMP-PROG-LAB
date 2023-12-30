# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:33:57 2021

@author: DELUX
"""

name = input('Enter username : ')
x = 'Hello, ' + name
n = 1
while name != 'Tirawich':
    if n < 3 :
        name = input('Incorrect. Enter again : ')
        n += 1
    else:
        x = 'Not allowed. Incorrect name.'
        break
print(x)