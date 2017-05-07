#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:freeman

import getpass
#输入密码时，如果想要不可见，需要利用getpass 模块中的 getpass方法，即：

username = input("pls input name:")
password = getpass.getpass("password:")

#print(username,password)




#流程逻辑判断
if username == "freeman" and password == "123456":
    print("Welcom user {name} login...".format(name=username))
else:
    print("Invalid username or password!")