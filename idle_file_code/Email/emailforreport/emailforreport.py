#coding = utf-8
import os,datetime,time
import unittest
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
import allcase_list


def sendmail(file_new):
    # 发件箱
    mailfrom = '344810409@qq.com'
    # 收件箱
    mailreceive = '15709277263@163.com'
    smtpserver = 'smtp.qq.com'
    username = '344810409@qq.com'
    password = 'tlkejbebcdhxbiba'
    # 定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    # 定义标题
    msg['subject'] = u'邮件发送测试报告'
    # 定义发送时间
    msg['date'] = time.strftime('%a,%d %b %Y %H:%M:%S %z')
    # 创建smtp对象
    try:
        smtp = smtplib.SMTP()
        # 建立连接诶
        smtp.connect('smtp.qq.com', 25)
        smtp.starttls()
        # 登录
        smtp.login(username, password)
        # 发送邮件邮箱账号和密码
        smtp.sendmail(mailfrom, mailreceive, msg.as_string())
        print("邮件发送成功！")
        smtp.quit()
    except smtplib.SMTPException:
        print("邮件发送失败！")

def sendreportemail():
    result_dir = 'D:\\Phyon\\pycharm_code\\idle_file_code\\Email\\emailforreport'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" +fn) if not os.path.isdir(result_dir + "\\" +fn) else 0)
    print(u'最新测试报告：'+ lists[-2])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-2])
    print(file_new)
    sendmail(filename)

if __name__=="__main__":
    alltestcasenames = allcase_list.caselist()
    # 创建测试套件
    testunit = unittest.TestSuite()
     # 循环读取测试用例
    for test in alltestcasenames:
        testunit.addTest(unittest.makeSuite(test))
    # 获取当前时间
    u"""获取当前时间"""
    now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    # 定义报告存放路径，支持相对路径
    filename = "D:\\Phyon\pycharm_code\\idle_file_code\\Email\\emailforreport\\reportforemail\\" + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'百度测试报告', description=u'用例执行情况：')
    runner.run(testunit)
    sendreportemail()

