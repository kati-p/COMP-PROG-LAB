# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 12:58:42 2021

@author: DELUX
"""

def add_item(x):
    item = input('Enter item: ')
    if item in x:
        print('Item is already in the list')
    else:
        x.append(item)
        print('Item has been added')
    return x
def change_item(x):
    item = input('Enter item you want to change: ')
    if item in x:
        i = x.index(item)
        x[i] = input('Enter new item: ')
        print('Item has been changed')
    else:
        print('Item is not in the list')
    return x
def insert_item(x):
    item = input('Enter item: ')
    location = input('Enter location that you want to insert: ')
    x.insert(int(location),item)
    print('Item has been inserted')
    return x
def remove_item(x):
    item = input('Enter item you want to remove: ')
    if item in x:
        i = x.index(item)
        del x[i]
        print('Item has been removed')
    else:
        print('This item is not in the list')
    return x
def show_items(x):
    if x == []:
        print('The list is currently empty')
    else:
        print(x)

item_list = []
print('What would you like to do?\n' + 
      '1: add item\n' +
      '2: change item\n' +
      '3: insert item\n' +
      '4: remove item\n' +
      '5: show item\n' +
      '6: exit')
ip = input('Enter a number: ')
while ip != '6':
    if ip == '1':
        item_list = add_item(item_list)
    elif ip == '2':
        item_list = change_item(item_list)
    elif ip == '3':
        item_list = insert_item(item_list)
    elif ip == '4':
        item_list = remove_item(item_list)
    elif ip == '5':
        show_items(item_list)
    else:
        print('This option is not available')
    ip = input('Enter a number: ')