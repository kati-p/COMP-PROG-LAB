# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:47:16 2021

@author: DELUX
"""

order = input('Enter ice cream or cake: ')
if order == 'ice cream':
    topping = input('Enter topping or not: ')
    if topping == 'topping':
        print('your cost: 15 baht')
    else:
        print('your cost: 10 baht')
elif order == 'cake':
    cake = input('Enter butter or sponge or chiffon: ')
    if cake == 'butter':
        print('your cost: 25 baht')
    elif cake == 'sponge':
        print('your cost: 29 baht')
    elif cake == 'chiffon':
        print('your cost: 19 baht')
    else:
        print('you ordered wrong')
else:
    print('you ordered wrong')
    