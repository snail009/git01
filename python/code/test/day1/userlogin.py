#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:freeman

import getpass

#用户登陆
'''
name = input("Pls input your name:")
password = input("Pls input your password:")
print("the user info is: ",name,password)
'''

#输出用户信息
name = input("name:")
age = int(input("age:"))       #强制将str转换为int
print(type (age),type(str(age)))                     #打印数据类型,同时将int转会string
print(type (age))
job = input("job:")
salary = input("salary:")

#格式化拼接
info = '''
#########the %s info#########
name:%s
age:%d
job:%s
salary:%s
'''%(name,name,age,job,salary)




#第二中格式化拼接输出
info2 = '''
#########the {_name} info#########
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
''' .format(_name=name,
            _age=age,
            _job=job,
            _salary=salary)

#第三种格式化拼接输出
info3 = '''
#########the {0} info#########
name:{0}
age:{1}
job:{2}
salary:{3}
''' .format(name,age,job,salary)

print(info3)                           #%s---%string,%d---%date,
