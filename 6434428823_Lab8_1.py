# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:05:45 2021

@author: DELUX
"""


vec_file = open('vector.txt')

line1 = vec_file.readline().strip()
line2 = vec_file.readline().strip()    

vec_file.close()

v1 = []
for i in line1.split():
    v1.append(float(i))
v2 = []
for i in line2.split():
    v2.append(float(i))
print('v1 = ' + str(v1) + '\n' + 'v2 = ' + str(v2))

if len(v1) != len(v2):
    print('Incompatible size')
else:
    v = []
    for i in range(len(v1)):
        v.append(v1[i]*v2[i])
    print('v1*v2 = ' + str(sum(v)))
