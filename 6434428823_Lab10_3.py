# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 14:01:52 2021

@author: DELUX
"""

f = open('studentScore.txt')
ss = {}
for line in f:
    name,score = line.split()
    ss[name] = int(score)
f.close()

name_sort = []
score_sort = list(ss.values())
score_sort.sort(reverse=True)
for sc in score_sort:
    for nm in ss:
        if sc == ss[nm] and nm not in name_sort:
            name_sort.append(nm)
for i in name_sort:
    print(i)