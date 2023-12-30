# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:32:15 2021

@author: DELUX
"""

ip = input('Enter a number between [0,9]: ')
data = [x for x in range(1,101) if ip in str(x)]
print(data)