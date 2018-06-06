#coding = utf-8
import HTMLTestRunner
import unittest
import os,time

listaa = "D:\Python\pycharm_code\idle_file_code\cron_job"
def createsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa,pattern='start_*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit
allcasenames =createsuite()
now = time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))
filename = 'D:\\Python\\pycharm_code\\idle_file_code\\cron_job\\report\\' + now +'result.html'
fp = open(filename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试用例报告',description=u'用例执行情况')
k = 1
while k <2:
    timing = time.strftime('%H_%M',time.localtime(time.time()))
    if timing == '11_04':
        print(u"开始运行程序")
        runner.run(allcasenames)
        print(u"用例执行完毕")
        break
    else:
        time.sleep(5)
        print(timing)
fp.close()




