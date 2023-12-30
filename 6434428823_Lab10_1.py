# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:54:18 2021

@author: DELUX
"""

courses = {'2301117' : 'Calculus I 4',
           '2301118' : 'Calculus II 4',
           '2301286' : 'Probability and Statistics 3',
           '2301399' : 'Project Proposal 1',
           '2301499' : 'Senior Project 2',
           '2302113' : 'General Chemistry Lab I 1',
           '2302161' : 'General Chemistry 3',
           }

ip = input('Course ID: ')
while ip != '0':
    if ip in courses:
        print(courses[ip])
    else:
        print('Unknown')
    ip = input('Course ID: ')