#coding = utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#发送邮件
sender = '344810409@qq.com'
#接收邮件
receive = '15709277263@163.com'
#服务器
smtpserver = 'smtp.qq.com'
# #发送邮件主题
# subject = 'test the case'
#登录邮箱账号和密码
username = '344810409@qq.com'
password = 'tlkejbebcdhxbiba' #邮箱授权码

#多附件发送，创建MIMEMultipart对象，采用related定义内嵌资源的邮件体
msgRoot = MIMEMultipart('Related')
msgRoot['subject'] = 'test message'
# 创建一个MIMEText对象，HTML元素包括表格<table>及图片<img>
msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.'
                   '<img alt=""src="cid:image1"/>'
                   'good!','html','utf-8')
msgRoot.attach(msgText)
#读取图片信息
fp = open('D:\\Phyon\\pycharm_code\\idle_file_code\\Email\\1.png','rb')
# 创建MIMEImage对象，读取图片内容并作为参数
msgImage = MIMEImage(fp.read())
fp.close()
# 指定图片文件的Content-ID，imgid，<img>标签中的src用到
msgImage.add_header('Content-ID','')
#使用MIMEMultipart对象附加MIMEImage的内容
msgRoot.attach(msgImage)

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




