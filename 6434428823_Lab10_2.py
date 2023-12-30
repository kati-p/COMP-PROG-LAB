# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 13:28:27 2021

@author: DELUX
"""

f = open('conversation.txt')
conv = {}
for line in f:
    for i in line.split():
        i = i.strip(':?,.')
        if i in conv:
            conv[i] = conv[i] + 1
        else:
            conv[i] = 1            
f.close()

for k in conv:
    print(k,conv[k])