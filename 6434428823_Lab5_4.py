# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 07:28:43 2021

@author: DELUX
"""

n_std = int(input('Number of students : '))
n = 1
total_sc = 0
pass_sc = 0
n_pass = 0
fail_sc = 0
n_fail = 0
high_sc = 0

while n <= n_std:
    std_sc = float(input('student ' + str(n) + ' : '))
    total_sc += std_sc
    if std_sc >= 5:
        pass_sc += std_sc
        n_pass += 1
    if std_sc < 5:
        fail_sc += std_sc
        n_fail += 1      
    if std_sc > high_sc:
        high_sc = std_sc
    n += 1

if n_pass > 0:
    ave_pass = pass_sc / n_pass
else:
    ave_pass = 0
if n_fail > 0:
    ave_fail = fail_sc / n_fail
else:
    ave_fail = 0
if n_std > 0:
    ave_total = total_sc / n_std
else:
    ave_total = 'none'
    ave_pass = 'none'
    ave_fail = 'none'
    high_sc = 'none'

print('Average score : ' + str(ave_total))
print('Average passing score : ' + str(ave_pass))
print('Average failing score : ' + str(ave_fail))
print('Highest score : ' + str(high_sc))


