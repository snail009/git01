#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:freeman

import copy

'''
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
#list.append("110")
#list.insert(1,"higk")
print(list)
del list
print(list)
'''
names = ['Alex','Tenglan',["jack","sunny"],'Eric','Rain','Tom','Amy']
'''
names2 = copy.deepcopy(names)
print(names)
print(names2)
names[1] = "自由人"
names[2][0] = "JACK"
print(names)
print(names2)
'''
print(names[0:-1:2])
print(names[::2])

for i in names:
    print(i)
