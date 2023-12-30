# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 22:46:22 2021

@author: DELUX
"""

ct = 0
for i in range(1,8):
    T = float(input('Day '+str(i)+' : '))
    ct = T - ct
    if ct < 0:
        print('Temperature dropped on day '+str(i))
    ct = T