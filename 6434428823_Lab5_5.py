# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 07:55:22 2021

@author: DELUX
"""

dep = float(50000)
while dep != 0:
    witd = float(input('Witdraw : '))
    if dep - witd < 0 :
        print('Insufficient fund.')
        continue
    dep = dep - witd
print('Balance is 0.')