#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:freeman

product_list = [
    ('xiaomi',2000),
    ('huawei',1500),
    ('apple',4500),
    ('bike',200),
    ('coffee',23),
    ('water',2),
    ('fruit',15)
]
shopping_list = []
salary = input("pls input you salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
      #  for item in product_list:
      #      print(product_list.index(item)+1,item)
         for index,item in enumerate(product_list):      #enumerate函数把下标打印出来
             print(index+1,item)
         user_choice = input("which do you want?:")
         if user_choice.isdigit():                       #判断输入是否正确
             user_choice = int(user_choice)
             if user_choice <= len(product_list)+1 and user_choice >=0:      #判断是否输入在所选范围
                 p_item = product_list[user_choice-1]
                 if p_item[1] <= salary:                                     #判断余额是否足够
                     shopping_list.append(p_item)
                     salary -=p_item[1]
                     print("add %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item[0],salary))
                 else:
                     print("\033[41;1myour balance have [%s],pls charge again!\033[0m" %(salary))
             else:
                 print("product code %s is no exit,pls try again!" %user_choice)
         elif user_choice == 'q':                          #退出打印shopping list和balance
             print("----------shopping list----------")
             for list in shopping_list:
                 print(list)
             print("your current balance have:",salary)
             exit()
         else:
             print("invalid option")

