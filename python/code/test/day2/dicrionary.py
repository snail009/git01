#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:freeman



#key-value

info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}



dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'};

print("dict['Name:]",dict.get('Name'))
print("dict['Alice']: ", dict.get('Alice'))

print('Alice' in dict)

print(dict.values())
print(dict.keys())

print(dict.setdefault("Name",'123'))
print(dict.setdefault("freeman","123"))

dict2 = {'Name': '123', 'freeman': 7, 'Alex': 'First'};
dict.update(dict2)
print(dict.items())

B = dict.fromkeys([1,2,3],[1,{'name':'freeman'},'snail01'])
print(B)

B[2][1]['name'] = 'alex'
print(B)

for i in dict:
    print(i,dict[i])


for i,v in dict.items():
    print(i,v)





