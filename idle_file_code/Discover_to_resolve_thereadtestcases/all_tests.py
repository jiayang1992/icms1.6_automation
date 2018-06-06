#coding = uft-8
import unittest
import HTMLTestRunner
import os,time


caselist = 'D:\\Phyon\pycharm_code\\idle_file_code\\Discover_to_resolve_thereadtestcases'
#定义测试用力集
def createsuite():
    testunite =   unittest.TestSuite()
    #定义discover
    discover = unittest.defaultTestLoader.discover(caselist,pattern = 'start_*.py',top_level_dir=None)
    #将discovr方法筛选的用例循环添加到测试套件中
    for test_suit in discover:
        for test_case in test_suit:
            testunite.addTest(test_case)
            print(testunite)
            return testunite
        alltestnames = createsuite()
        now = time.strftime("%Y-%y-%d_%H_%M_%S",time.localtime(time.time()))
        filename = 'D:\\Phyon\\pycharm_code\\idle_file_code\\Discover_to_resolve_thereadtestcases\\reportforemail'+now+'result.html'
        fp = open(filename,'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况')
        runner.run(alltestnames)