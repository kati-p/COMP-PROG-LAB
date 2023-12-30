# -*- coding: utf-8 -*-
"""

6434428823 Tirawich Kasemchaiyanan

"""

training = {'Mike':{'MO':1, 'TU':2, 'FR':3}, 'Got':{'MO':1, 'WE':2, 'FR':1},
'Jane':{'MO':1, 'TH':2, 'FR':3}}
tra_class = {}
ip = input('Enter name and day to get number of training class : ')
while ip != '0':
    name,day = ip.split()
    if name in training.keys():
        if day in training[name].keys():
            print('Number of training class :',training[name][day])
            if name not in tra_class:
                tra_class[name] = training[name][day]
            else:
                tra_class[name] = tra_class[name] + training[name][day]
        else:
            print('Not found')
    else:
        print('Not found')
    ip = input('Enter name and day to get number of training class : ')
print('Dictionary of total number of classes :',tra_class)