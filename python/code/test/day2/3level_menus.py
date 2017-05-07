#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:freeman

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

exit_flag = False

while not exit_flag:
    for i1 in menu:
        print(i1)
    choice1 = input("选择1》》：")
    if choice1 in menu:
        while not exit_flag:
            for i2 in menu[choice1]:
                print("\t", i2)
            choice2 = input("选择2》》：")
            if choice2 in menu[choice1]:
                while not exit_flag:
                    for i2 in menu[choice1][choice2]:
                        print("\t", i2)
                    choice3 = input("选择3》》：")
                    if choice3 in menu[choice1][choice2]:
                        while not exit_flag:
                            for i3 in menu[choice1][choice2][choice3]:
                                print("\t\t", i3)
                            choice4 = input("选择4》》：")
                            if choice4 in menu[choice1][choice2][choice3]:
                                while not exit_flag:
                                    for i4 in menu[choice1][choice2][choice3][choice4]:
                                        print("\t\t\t", i4)
                                    choice5 = input("The last one ,choose 'b' back or 'q' exit》》：")
                                    if choice5 == "b":
                                        break
                                    elif choice5 == "q":
                                        exit_flag = True
                            if choice4 == "b":
                                break
                            elif choice4 == "q":
                                exit_flag = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True
    elif choice1 == "q":
        exit_flag = True







