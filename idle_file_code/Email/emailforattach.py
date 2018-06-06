#coding = utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import HTMLTestRunner
import os,time,datetime
import unittest

#发送邮箱
sender = '344810409@qq.com'
#接收邮箱
receive = '15709277263@163.com'
#发送邮箱服务器
smtpserver = 'smtp.qq.com'
#发送邮件主题
subject = 'test the case'
#邮箱账号和密码
username = '344810409@qq.com'
password = 'tlkejbebcdhxbiba'
#定义发送多附件
msgRoot = MIMEMultipart('Related')
msgRoot['subject']='test the case for html'
#构造附件
attach = MIMEText(open('D:\\Phyon\\pycharm_code\\idle_file_code\Email\\attach.png','rb').read(),'base64','utf-8')
attach1 = MIMEText(open('D:\\Phyon\\pycharm_code\\idle_file_code\Email\\attach1.png','rb').read(),'base64','utf-8')
#application/octet-stream只能提交二进制，而且只能提交一个二进制，如果提交文件的话，只能提交一个文件,后台接收参数只能有一个，而且只能是流（或者字节数组）
attach['Content-type']='application/octet-stream'
attach1['Conten-type']='application/octet-stream'
# 服务端向客户端游览器发送文件时，如果是浏览器支持的文件类型，一般会默认使用浏览器打开，比如txt、jpg等，会直接在浏览器中显示，
# 如果需要提示用户保存，就要利用Content-Disposition进行一下处理，关键在于一定要加上attachment,这样浏览器会提示保存还是打开，即使选择打开，也会使用相关联的程序比如记事本打开，而不是IE直接打开了
# Content-Disposition就是当用户想把请求所得的内容存为一个文件的时候提供一个默认的文件名
attach['Content-Disposition'] = 'attachment;filename = "attach.png"'
attach1['Content-Disposition']= 'attachment;filename = "attach1.png"'
#添加附件
msgRoot.attach(attach)
msgRoot.attach(attach1)
try:
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com',25)
    smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(sender,receive,msgRoot.as_string())
    print("发送邮件成功")
    smtp.quit()
except smtplib.SMTPException:
    print("发送邮件失败")
file_path = "D:\\Phyon\pycharm_code\\idle_file_code\\Email"
#用于获取目录下的所有文件列表
list = os.listdir(file_path)
#Python 列表有一个内置的列表。sort()方法用于改变列表中元素的位置。还有一个 sorted()内置函数，建立了一种新的迭代排序列表。
#key 是带一个参数的函数，用来为每个元素提取比较值. 默认为 None, 即直接比较每个元素lambda 提供了一个运行时动态创建函数的方法。我这里创建了 fn 函数。
#getmtime()返回文件列表中最新文件的时间（最新文件的时间最大，所以我们会得到一个最大时间）
#isdir()函数判断某一路径是否为目录。
list.sort(key=lambda fn:os.path.getmtime(file_path+"\\"+fn) if not os.path.isdir(file_path+"\\"+fn) else 0)
#-1 表示取文件列表中的最大值，也就是最新被创建的文件。
print("最新文件为;"+list[-1])
#join()方法用来连接字符串，通过路径与文件名的拼接，我们将得到目录下最新被创建的的文件名的完整路径。
file = os.path.join(file_path,list[-1])
print(file)






