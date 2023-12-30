# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:27:59 2021

@author: DELUX
"""

stocks = {}
for i in range(10):
    ID,size,num = input('Enter product ID, size, number of items : ').split()
    num = int(num)
    if (ID,size) in stocks:
        stocks[(ID,size)] = stocks[(ID,size)] + num
    else:
        stocks[(ID,size)] = num
print('Stocks :')
for k in stocks:
    print(k[0],k[1],stocks[k])