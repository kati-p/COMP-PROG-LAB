# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 22:20:34 2021

@author: DELUX
"""

x = int(input('Enter an integer : '))
print(x , 'is divisible by:')
for i in range(1 , x+1):
    if x%i == 0:
        print(i)