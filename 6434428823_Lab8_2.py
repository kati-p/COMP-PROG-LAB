# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 14:24:05 2021

@author: DELUX
"""


sol_file = open('sol.txt')
sol = sol_file.readline().split()
sol_file.close()

exam_file = open('exam.txt')
exam = []
for line in exam_file:
    exam.append(line.strip())
for i in range(len(exam)):
    exam[i] = [] + exam[i].split()
exam_file.close()

list_score = []
for i in range(len(exam)):
    score = 0
    for j in range(len(sol)):
        if exam[i][j] == sol[j]:
            score += 1
    list_score.append(score)

list_qust = []
for i in range(len(sol)):
    score = 0
    for j in range(len(exam)):
        if sol[i] == exam[j][i]:
            score += 1
    list_qust.append(score/len(exam))

hard_qust = ''
easy_qust = ''
print('Student score: ' + str(list_score) + '\n')
for i in range(len(list_qust)):
    print('Question ' + str(i+1) + ' :' + str(list_qust[i]))
    if list_qust[i] == min(list_qust):
        hard_qust += str(i+1) + ' '
    if list_qust[i] == max(list_qust):
        easy_qust += str(i+1) + ' '
print('\n' + hard_qust + 'is the hardest question.' + '\n'
      + easy_qust + 'is the easiest question.')