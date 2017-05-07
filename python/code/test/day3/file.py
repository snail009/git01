#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:freeman

#读操作
#data = open("yesterday",encoding="utf-8").read()     #由于windows平台模式编码格式是gbk，所以需要指定字符集
f = open("yesterday",encoding="utf-8")    #文件句柄，内存对象
data = f.read()
print(data)