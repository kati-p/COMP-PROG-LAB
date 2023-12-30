# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:31:36 2021

@author: DELUX
"""

ID = input("Enter student ID: ")
ID_len = len(ID)
ID = float(ID)
ID_2 = ID//1e8
ID_3 = (ID//1e7)%10
ID_2f = ID%1e2

if ID_len!=10:
    print('Invalid ID')
elif 49<ID_2<64 == False:
    print('Invalid ID')
elif ID_3!=3 and ID_3!=4 and ID_3!=7:
    print('Invalid ID')
elif 20<ID_2f<29 == False:
    print('Invalid ID')
else:
    print('Valid ID')