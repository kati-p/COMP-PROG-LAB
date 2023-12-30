# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:56:08 2021

@author: DELUX
"""

y1 = ['48','49']
y2 = ['50','51','52','53','54','55']
y3 = [str(i) for i in range(56,100)]
y = y1 + y2 + y3
g1 = ['21','23','25','28','30','31','32','33','35','36','37','38','39','53']
g2 = ['22','24','26','27','29','34','40','51']
g = g1 + g2
fee = {'48-49': {('g1','bach','s1/2'): '16000', ('g1','grad','s1/2'): '22500',
                 ('g2','bach','s1/2'): '12000', ('g2','grad','s1/2'): '16500',
                 ('bach','s3'): '4000', ('grad','s3'): '6000'}, 
       '50-55': {('g1','bach','s1/2'): '18000', ('g1','grad','s1/2'): '26000',
                 ('g2','bach','s1/2'): '14500', ('g2','grad','s1/2'): '19000',
                 ('bach','s3'): '4500', ('grad','s3'): '7000'}, 
       '56+'  : {('g1','bach','s1/2'): '21000', ('g1','grad','s1/2'): '31000',
                 ('g2','bach','s1/2'): '17000', ('g2','grad','s1/2'): '23000',
                 ('bach','s3'): '5250', ('grad','s3'): '7750'}
       }
ID = input('Enter student ID : ')
if len(ID) != 10 or ID[8:10] not in g or ID[:2] not in y:
    print('Invalid ID')
else:
    if ID[2] == '7':
        degree = 'grad'
    else:
        degree = 'bach'
    if ID[8:10] in g1:
        group = 'g1'
    else:
        group = 'g2'
    if ID[:2] in y1:
        year = '48-49'
    elif ID[:2] in y2:
        year = '50-55'
    else:
        year = '56+'
    sem = input('Enter semester : ')
    if sem not in ['1','2','3']:
        print('Invalid semester')
    else:
        if sem == '1' or sem == '2':
            sem = 's1/2'
            print('Registration fee :',fee[year][(group,degree,sem)])
        else:
            sem = 's3'
            print('Registration fee :',fee[year][(degree,sem)])