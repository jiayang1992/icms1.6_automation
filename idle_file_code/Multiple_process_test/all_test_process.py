#--------------------------多进程执行文件并发送邮件报告-----------------------------
#coding=utf-8
import unittest, time, os, multiprocessing
import commands
from email.mime.text import MIMEText
import HTMLTestRunner
import threading
import sys
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
sys.path.append("D:\Python\pycharm_code\idle_file_code\Multiple_process_test")
listaa = "D:\Python\pycharm_code\idle_file_code\Multiple_process_test"
def creatsuite():
    casedir = []
    folder_list = os.listdir("D:\Python\pycharm_code\idle_file_code\Multiple_process_test")
    for xx in folder_list:
        if "thread" in xx:
            casedir.append(xx)
    print(casedir)
    suite = []
    for n in casedir:
        testunit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(listaa,pattern='start_*.py',top_level_dir=None)
        for test_suit in discover:
            for test_case in test_suit:
                testunit.addTests(test_case)
        suite.append(testunit)
    return suite,casedir
def multiRunCase(suite,casedir):
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    filename = 'D:\\Python\\pycharm_code\\idle_file_code\\Multiple_process_test\\report\\' +now+ 'result.html'
    fp = open(filename,'wb')
    proclist = []
    s=0
    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
             title=str(casedir[s])+u'测试报告',
            description=u'用例执行情况:'
        )
        proc = threading.Thread(target=runner.run,args=[i,])
        proclist.append(proc)
        s = s+1
    for proc in proclist:
            proc.start()
    for proc in proclist:
            proc.join()
    fp.close()
def sendmail(file_new):
    #发件箱
    mailfrom = '344810409@qq.com'
    mailserver = 'smtp.qq.com'
    mailto = '15709277263@163.com'
    username = '344810409@qq.com'
    password = 'tlkejbebcdhxbiba'
    #正文
    f = open(file_new,'rb')
    #f = open(file_new,'rb')
    mailbody = f.read()
    f.close()
    msg = MIMEText(mailbody, _subtype='html', _charset='utf-8')
    msg['subject'] = u'测试报告'
    msg['date']=time.strftime('%a,%d %b %Y %H:%M:%S %z')
    #创建smtp对象
    try:
        smtp = smtplib.SMTP()
        #建立连接
        smtp.connect('smtp.qq.com',25)
        smtp.starttls()
        #登录
        smtp.login(username,password)
        smtp.sendmail(mailfrom,mailto,msg.as_string())
        print("邮件发送成功")
        smtp.quit()
    except smtplib.SMTPException:
        print("邮件发送失败")
def sendreportmail():
    result_dir = "D:\Python\pycharm_code\idle_file_code\Multiple_process_test"
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn:os.path.getmtime(result_dir + "\\"+ fn) if not os.path.isdir(result_dir + "\\" + fn) else 0)
    print(u'最新测试报告'+ lists[-2])
    file_new = os.path.join(result_dir,lists[-2])
    print(file_new)
    sendmail(filename)


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = 'D:\Python\pycharm_code\idle_file_code\cron_job\report' + now + '\result.html'
    runtmp=creatsuite()
    multiRunCase(runtmp[0],runtmp[1])
    sendreportmail()
#----------------------------------------多线程并发执行文件---------------------------------------
# #coding=utf-8
# import unittest, time, os, multiprocessing
# import commands
# from email.mime.text import MIMEText
# import HTMLTestRunner
# import threading
# import sys
# sys.path.append(r'D:\\Phyon\\pycharm_code\\idle_file_code\\Multiple_process_test')
# listaa = "D:\\Phyon\\pycharm_code\\idle_file_code\\Multiple_process_test"
# def creatsuite():
#     casedir = []
#     folder_list = os.listdir('D:\\Phyon\\pycharm_code\\idle_file_code\\Multiple_process_test')
#     for xx in folder_list:
#         if "thread" in xx:
#             casedir.append(xx)
#     print(casedir)
#     suite = []
#     for n in casedir:
#         testunit = unittest.TestSuite()
#         discover = unittest.defaultTestLoader.discover(listaa,pattern='start_*.py',top_level_dir=None)
#         for test_suit in discover:
#             for test_case in test_suit:
#                 testunit.addTests(test_case)
#         suite.append(testunit)
#     return suite,casedir
# def multiRunCase(suite,casedir):
#     now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
#     filename = 'D:\\Phyon\\pycharm_code\\idle_file_code\\Multiple_process_test\\report\\'+now+'result.html'
#     fp = open(filename,'wb')
#     proclist = []
#     s=0
#     for i in suite:
#         runner = HTMLTestRunner.HTMLTestRunner(
#             stream=fp,
#              title=str(casedir[s])+u'测试报告',
#             description=u'用例执行情况:'
#         )
#         proc = threading.Thread(target=runner.run,args=(i,))
#         proclist.append(proc)
#         s = s+1
#     for proc in proclist:
#             proc.start()
#     for proc in proclist:
#             proc.join()
#     fp.close()
# if __name__ == "__main__":
#     runtmp=creatsuite()
#     multiRunCase(runtmp[0],runtmp[1])
# ------------------------------------------------------------------------------



