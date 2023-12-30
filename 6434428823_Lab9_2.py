# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:17:30 2021

@author: DELUX
"""

def sum_digits(string):
    x = 0
    for i in string:
        if i.isdigit():
            x = x + int(i)
    return x