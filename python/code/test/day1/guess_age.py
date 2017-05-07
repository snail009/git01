#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:freeman


'''
#猜字谜
#if  else 的应用
age_of_freeman = 56
guess_age = int(input("pls input age:"))            #默认input输入的都是字符串string，所以需要转换一下

if guess_age == age_of_freeman:
    print("yes,you are right!")
elif guess_age > age_of_freeman:
    print("omg,think bigger!")
else:
    print("no,think smaller!")
'''



#while的使用
age_of_freeman = 56
count = 0
'''
while True:                      #while count <3:
    if count ==3:
        break
    guess_age = int(input("pls input age:"))
    if guess_age == age_of_freeman:
        print("yes,you are right!")
        break
    elif guess_age > age_of_freeman:
        print("omg,think bigger!")
    else:
        print("no,think smaller!")
    count +=1
else:
    print("you have tried too many times...")
'''

#方式二

while count < 3:
    guess_age = int(input("pls input age:"))
 #   if guess_age.isdigit() == True:
    if guess_age == age_of_freeman:
            print("yes,you are right!")
            break
    elif guess_age > age_of_freeman:
            print("omg,think bigger!")
    else:
            print("no,think smaller!")
            count += 1
    if count ==3:
        continue_cofirm = input("do you want to keeping?[y/n]:")
        if continue_cofirm != 'n':
                    count =0
else:
    print("you have tried too many times...")



