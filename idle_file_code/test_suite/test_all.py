#coding=utf-8
import unittest
import os
#这里需要导入测试文件
#import baidu1,youdao1
import HTMLTestRunner
import time
import allcase_list
# import sys
# sys.path.append("\test_suite")#为了标识目录是可以引用的包
# from test_suite import baidu1
# from test_suite import youdao1

#在__init__中import baidu,youdao后，就可以在文件中直接调用
#from test_suite import baidu
#将所有测试用例装数组
# alltestcasenames={baidu1.Baidu,youdao1.Youdao}
alltestcasenames = allcase_list.caselist()
#创建测试套件
testunit = unittest.TestSuite()

#循环读取测试用例
for test in alltestcasenames:
    testunit.addTest(unittest.makeSuite(test))
#将测试用例加入测试容器中
# testunit.addTest(unittest.makeSuite(baidu1.Baidu))
# testunit.addTest(unittest.makeSuite(youdao1.Youdao))

#执行测试套件
# runner=unittest.TextTestRunner()
# runner.run(testunit)
#获取当前时间
u"""获取当前时间"""
now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))
#定义报告存放路径，支持相对路径
filename = "D:\\Phyon\\pycharm_code\\idle_file_code\\test_suite\\reportforemail\\"+ now+'result.html'
fp = open(filename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'百度测试报告',description=u'用例执行情况：')

#执行测试用例
runner.run(testunit)
fp.close()