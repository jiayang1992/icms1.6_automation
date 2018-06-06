#!D:\Phyon\pycharm_code\idle_file_code
#coding = utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮箱
sender = '15709277263@163.com'
#接收邮箱
receiver = '15709277263@163.com'
#发送邮件主题
subject = 'test the case'
#发送邮箱服务器
smtpserver = 'smtp.qq.com'
#发送邮箱账户和密码
username = '15709277263@163.com'
password = 'jiayang199213'
content = '您好'

#中文参数需要加'utf-8'
msg = MIMEText(content,'text','utf-8')
msg['Subject'] = Header(subject,'utf-8')
try:
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com',"25")
    smtp.starttls()  #启动安全传输模式
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print("邮件已发送")
except smtplib.SMTPException:
    print("发送邮件失败")


