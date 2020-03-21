#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 7:43 上午
# @Author  : yym(阿墨与白猫)
# @Site    : 
# @File    : ModifiedTime.py
# @Software: PyCharm
import os
import datetime
print(f"当前时间:{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
for root,dirs,files in os.walk(r"/Users/yangyumo/Downloads"):         #定义需要查看文件时间的目录
    for file in files:
        Path_file = os.path.join(root,file)             #获取文件的绝对路径
        ModifedTime = datetime.datetime.fromtimestamp(os.path.getmtime(Path_file))      #获取修改时间，转化成datatime类型
        Now = datetime.datetime.now()
        diff_time = Now - ModifedTime           #获取时间差
        #print(f"{Path_file}".ljust(25),f"{diff_time.seconds%3600//60}分")
        # print(
        #     f"{Path_file:<27s}修改时间[{ModifedTime.strftime('%Y-%m-%d %H:%M:%S')}]距今[{diff_time.days:3d}天{diff_time.seconds//3600:2d}时{(diff_time.seconds%3600)//60:2d}分]"
        # )
        if diff_time.days > 90 :        #如果修改时间大于90天就删除
            # print(f"{Path_file}修改时间大于60天，为[{diff_time.days}]天")
            os.remove(Path_file)
