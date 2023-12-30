# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 14:04:13 2021

@author: DELUX
"""

Name = input('Enter your name: ')
age = input('Enter your age: ')
bd = 2564-int(age)
x,bm = str(float(bd)/100).split('.')

print(Name+str(int(float(bm)))+'@chula.ac.th')

