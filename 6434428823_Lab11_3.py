# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 17:34:57 2021

@author: DELUX
"""

score = {}
fs = open('score.txt')
for line in fs:
    nam,s1,s2,s3,s4 = line.split()
    score[nam] = [int(s1),int(s2),int(s3),int(s4)]
fs.close()
score_sum = {i:sum(score[i])for i in score}
score_sort = list(score_sum.values())
score_sort.sort(reverse=True)
name_sort = []
for s in score_sort:
    for k in score_sum:
        if s == score_sum[k] and k not in name_sort:
            name_sort.append(k)
for i in range(3):
    print(str(i+1),':',name_sort[i],score_sum[name_sort[i]])