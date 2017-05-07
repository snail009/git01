#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:freeman

list_1 = [1,2,5,2,7,9,6]
list_1 = set(list_1)
print(list_1,type(list_1))

list_2 = set([0,2,9,22,10,13])
list_3 = set([1,2,5,2,7,9,6,10])

#交集
print(list_1.intersection(list_2))

#并集
print(list_1.union(list_2))

#差集
print(list_1.difference(list_2))

#子集
print(list_1.issubset(list_2))
print(list_1.issubset(list_3))

#父集
print(list_1.issuperset(list_2))
print(list_3.issuperset(list_1))

#对称差集
print(list_1.symmetric_difference(list_2))
print(list_1^list_2)
print(list_1.symmetric_difference_update(list_2))

#
print(list_1.isdisjoint(list_2))

#添加
list_1.add(999)

#添加多项
list_1.update([12,33,55])
print(list_1)

#删除
list_1.remove(12)
print(list_1)

#长度计算
print(len(list_1))


#判断成员是否在集合里面
if 233 not in list_1:
    print("1")
else:
    print ("0")

#删除任意一个
print(list_1.pop())

#删除
list_1.discard(22)
print(list_1)