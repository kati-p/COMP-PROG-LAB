# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:53:24 2021

@author: DELUX
"""

w = input('Enter you weight(kg.): ')
h = input('Enter you height(m.): ')
w = float(w)
h = float(h)

bmi = w/h**2

if bmi<18.5:
    print('ผอม')
elif 18.5<=bmi<23.0:
    print('รูปร่างปกติ')
elif 23.0<=bmi<25.0:
    print('รูปร่างอ้วน')
elif 25.0<=bmi<30:
    print('อ้วนระดับ 1')
elif bmi>=30:
    print('อ้วนระดับ 2')