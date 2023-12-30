# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:54:50 2021

@author: DELUX
"""

import random
n,m = input('Enter number of gacha and cost of 1 gacha: ').split()
n = int(n)
m = int(n)
x = 1
profit = 0
pt = 'You have got'
while x<=n:
    rate = random.randint(1,100)
    if 1 <= rate <= 5:
        pt = pt + ' SSR'
        profit = profit + 200 - m
    elif 6 <= rate <= 25:
        pt = pt + ' SR'
        profit = profit + 100 - m
    else:
        pt = pt + ' R'
        profit = profit + 10 - m
    x+=1
print(pt + '.' + ' and your profit is ' + str(profit) + ' baht.')