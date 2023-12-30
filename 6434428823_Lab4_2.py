# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:13:41 2021

@author: DELUX
"""

w,uw = input('Weight: ').split()
h,uh = input('Height: ').split()
w = float(w)
h = float(h)

if uw == 'lbs':
    w = w/2.205
if uh == 'cm':
    h = h*1e-2
elif uh == 'ft':
    h = h/3.2808399
    
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