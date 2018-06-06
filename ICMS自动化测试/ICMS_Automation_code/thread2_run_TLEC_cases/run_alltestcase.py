#coding = utf-8
import unittest, time, os,sys, multiprocessing
# from unittest.test import test_case
#import commands   pycharm3中commands用subprocess代替了
import subprocess
from email.mime.text import MIMEText
import HTMLTestRunner
import threading
import sys
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart

listaa = "E:\\WS自动化测试\\ICMS自动化测试\\ICMS_Automation_code"
sys.path.append("E:\\WS自动化测试\\ICMS自动化测试\\ICMS_Automation_code")
def createsuit():
    casedir =[]
    folder_list=os.listdir("E:\\WS自动化测试\\ICMS自动化测试\\ICMS_Automation_code")
    for xx in folder_list:
        if "thread" in xx:
            casedir.append(xx)
    print(casedir)
    suit = []
    testsuit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa,pattern='case_*.py',top_level_dir=None)
    for test_suit in discover:
        for test_case in test_suit:
            testsuit.addTests(test_case)
    suit.append(testsuit)
    return casedir,suit
def MutiRunCase(suit,casedir):
    now = time.strftime("%Y-%y-%d_%H-%M-%S",time.localtime(time.time()))
    filename = 'E:\\WS自动化测试\\ICMS自动化测试\\ICMS_Automation_code\\report\\' + now + '_result.html'
    f = open(filename,'wb')
    prolist = []
    s = 0
    for i in suit:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title=u'测试报告',
            description=u'用例执行情况'
        )
        proc = threading.Thread(target=runner.run,args=[i,])
        prolist.append(proc)
        s = s+1
    for proc in prolist:
        proc.start()
    for proc in prolist:
        proc.join()
    f.close()
def sendrmail(file_new):
    #发件箱
    mailfrom = '344810409@qq.com'
    mailserver = 'smtp.qq.com'
    mailto = '15709277263@163.com'
    username = '344810409@qq.com'
    password = 'tlkejbebcdhxbiba'

    #正文
    f =open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['subject'] = u'测试报告'
    msg['date'] = time.strftime('%a,%d %b %Y %H：%M:%S %z')

    #创建smtp对象
    try:
        smtp = smtplib.SMTP()
        #建立连接
        smtp.connect('smtp.qq.com',25)
        smtp.starttls()
        #登录
        smtp.login(username,password)
        smtp.sendmail(mailfrom,mailto,msg.as_string())
        print('邮件发送成功')
        smtp.quit()
    except smtplib.SMTPException:
        print('邮件发送失败')
def sendreportemail():
    results_dir = "E:\\WS自动化测试\\ICMS自动化测试\\ICMS_Automation_code"
    lists = os.listdir(results_dir)
    lists.sort(key=lambda fn:os.path.getmtime(results_dir + "\\" +fn) if not os.path.isdir(results_dir + "\\" + fn) else 0 )
    print(u'最新测试报告' + lists[-2])
    file_new = os.path.join(results_dir,lists[-2])
    print(file_new)
    sendrmail(filename)

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename ='E:\\WS自动化测试\\ICMS自动化测试\\ICMS_Automation_code\\report\\' + now + '_result.html'
    runtmp=createsuit()
    MutiRunCase(runtmp[0],runtmp[1])
    sendreportemail()

    








