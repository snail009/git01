#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:freeman

import  os

#os.system("dir")
#cmd_res = os.system("dir")     #os.system()是直接输出到屏幕的，不保存结果
cmd_res = os.popen("dir").read()
print("-->",cmd_res)     #输入“0”或“1”只是代表命令成功与否

#创建目录
os.mkdir("new_test_dir")

