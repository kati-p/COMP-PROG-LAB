# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:47:56 2021

@author: DELUX
"""

ID = (input('Enter student ID: '))
ID_len = len(ID)
ID = int(ID)
ID_3 = ID//1e7%10
ID_2f = ID//1e8
ID_2b = ID%1e2
x = False

if ID_len!=10:
    print('Invalid ID')
elif ID_2f<=49:
    print('Invalid ID')
elif ID_3!=3 and ID_3!=4 and ID_3!=7:
    print('Invalid ID')
elif ID_2b<21 or ID_2b>28:
    print('Invalid ID')
else:
    sem = int(input('Enter semester: '))
    if sem!=1 and sem!=2 and sem!=3:
        print('Invalid semester')
    elif ID_2b==21 or ID_2b==23 or ID_2b==25 or ID_2b==28:
        if ID_3==3 or ID_3==4:
            if 50<=ID_2f<=55 and (sem==1 or sem==2):
                x='18,000'
            elif ID_2f>=56 and (sem==1 or sem==2):
                x='21,000'
            elif 50<=ID_2f<=55 and sem==3:
                x='4,500'
            elif ID_2f>=56 and sem==3:
                x='5,250'
        elif ID_3==7:
            if 50<=ID_2f<=55 and (sem==1 or sem==2):
                x='26,000'
            elif ID_2f>=56 and (sem==1 or sem==2):
                x='31,000'
            elif 50<=ID_2f<=55 and sem==3:
                x='7,000'
            elif ID_2f>=56 and sem==3:
                x='7,750'
    elif ID_2b==22 or ID_2b==24 or ID_2b==26 or ID_2b==27:
        if ID_3==3 or ID_3==4:
            if 50<=ID_2f<=55 and (sem==1 or sem==2):
                x='14,500'
            elif ID_2f>=56 and (sem==1 or sem==2):
                x='17,000'
            elif 50<=ID_2f<=55 and sem==3:
                x='4,500'
            elif ID_2f>=56 and sem==3:
                x='5,250'
        elif ID_3==7:
            if 50<=ID_2f<=55 and (sem==1 or sem==2):
                x='19,000'
            elif ID_2f>=56 and (sem==1 or sem==2):
                x='23,000'
            elif 50<=ID_2f<=55 and sem==3:
                x='7,000'
            elif ID_2f>=56 and sem==3:
                x='7,750'

if x!=False:
    print('Registration fee :',x)

