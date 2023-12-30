# -*- coding: utf-8 -*-
"""

6434428823 Tirawich Kasemchaiyanan

"""

f = open('inc_exp.txt')
ip = input('Enter month number to get income and expense : ')
inc_exp = {}
for line in f:
    y,inc,exp = line.split()
    bac = int(inc)-int(exp)
    if ip == y:
        print('Month',y,'income =',inc,'expense =',exp,'balance =',str(bac))
    inc_exp[y] = bac
f.close()

income = list(inc_exp.values())
for i in income:
    for j in inc_exp:
        if i == max(income):
            if inc_exp[j] == i: 
                print('Max balance =',i,'is in month',j)