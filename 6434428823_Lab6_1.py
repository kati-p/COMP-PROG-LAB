# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 22:04:52 2021

@author: DELUX
"""
word = input('Next word : ')
snt = ''
while word != '.':
    snt = snt + word + ' '
    word = input('Next word : ')
print('Sentence:' , snt)