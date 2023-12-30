# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:41:27 2021

@author: DELUX
"""

def f(x):
    fac = 1
    for i in range(1,x+1):
        fac = fac*i
    rfac = 1/fac
    return rfac
def summation(a,b):
    s = 0
    while a <= b:
        s = s + f(a)
        a = a + 1
    return s

m = int(input('Enter m: '))
n = int(input('Enter n: '))
if m < n:
    print(summation(m,n))
else:
    print(summation(n,m))