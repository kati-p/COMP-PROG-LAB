# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 22:37:24 2021

@author: DELUX
"""

x = int(input('Enter an integer : '))
cnt = 0
for i in range(1 , x+1):
    if x%i == 0:
        cnt += 1
if cnt == 2:
    print(x , 'is a prime number.')
else:
    print(x , 'is not a prime number.')