# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 15:35:29 2021

@author: DELUX
"""

menu = {('Cappuccino','S'): 60, ('Cappuccino','L'): 70,
        ('Espresso','S'): 45, ('Espresso','L'): 50,
        ('Latte','S'): 65, ('Latte','L'): 75}

coff,size,num = input('Enter drink, size and number: ').split()
key = (coff,size)
if coff not in ['Cappuccino', 'Espresso', 'Latte']:
    print('Drink not available.')
if size not in ['S','L']:
    print('Incorrect size.')
if not num.isdigit():
    print('Incorrect number.')
elif key in menu:
    print('Total : ' + str(menu[key]*int(num)))