#-*-coding=utf-8 -*-
import os
import BatchExecuteCase1
import unittest

#定位文件位置
caselist = os.listdir("D:\\Phyon\pycharm_code\\idle_file_code\\BatchExecuteCase")

for a in caselist:
    s=a.split('.')[1]
    if len(a.split('.'))<3:break
    #选取后缀名为.py的文件
    if s=='py':
           #执行dos命令并把日志保存到log.txt文件中
           # 2>&1是什么意思？0 stdin，1 stdout，2 stderr,2>&1应该分成两个部分来看，一个是2>以及另一个是&1，,其中2>就是将标准出错重定向到某个特定的地方；&1是指无论标准输出在哪里。
           # 所以2>&1的意思就是说无论标准出错在哪里(哪怕是没有?)，都将标准出错重定向到标准输出中
        os.system('D:\\Phyon\\pycharm_code\\idle_file_code\\BatchExecuteCase\\%s 1>>log.txt 2>&1'% a)


