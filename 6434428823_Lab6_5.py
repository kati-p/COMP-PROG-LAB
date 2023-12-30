# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 00:02:20 2021

@author: DELUX
"""

import random
while True:
    x = random.randint(1, 9)
    y = int(input('Your guess : '))
    if x == y:
        print('Correct.')
        break