#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:freeman

'''
age_of_freeman = 56
for i in range(3):
    guess_age = int(input("pls input age:"))
    if guess_age == age_of_freeman:
        print("yes,you are right!")
        break                                 #如果执行了break，则不执行else模块
    elif guess_age > age_of_freeman:
        print("omg,think bigger!")
    else:
        print("no,think smaller!")
else:
    print("you have tried too many times...")
'''

#打印偶数
#方法1
for i in range(20):
    if i%2 > 0:
        continue
    print (i)

#方法2
for i in range(0,10,2):
    print(i)

