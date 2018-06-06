#coding = utf-8
import smtplib
from email.mime.text import MIMEText

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
#定义邮件标题和内容
msg = MIMEText('</pre><h1>测试计划</h1><pre>','html','utf-8')
msg['subject'] = subject
try:
    #建立smtp对象
    smtp = smtplib.SMTP()
    #建立连接
    smtp.connect('smtp.qq.com',25)
    #启动安全传输模式
    smtp.starttls()
    #登录邮箱
    smtp.login(username,password)
    #发送邮件
    smtp.sendmail(sender,receive,msg.as_string())
    print("邮件发送成功")
    smtp.quit()
except smtplib.SMTPException:
    print("发送邮件失败")




