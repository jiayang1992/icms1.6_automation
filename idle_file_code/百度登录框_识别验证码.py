# coding=UTF-8
from selenium import webdriver
import time
#PIL （Python Imaging Library）是 Python 中最常用的图像处理库
from PIL import Image
# python对图像的处理比较常见的是用pytesseract识别验证码，要安装pytesseract库，必须先安装其依赖的PIL及tesseract-ocr，其中PIL为图像处理库，而后面的tesseract-ocr则为google的ocr识别引擎
import pytesseract
# Python-tesseract 是光学字符识别Tesseract OCR引擎的Python封装类。能够读取任何常规的图片文件(JPG, GIF ,PNG , TIFF等)并解码成可读的语言。在OCR处理期间不会创建任何临文件
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle

#driver.find_element_by_link_text(u'登录').click()
# 点击登录链接
element0 = driver.find_elements_by_name("tj_login")
for ele0 in element0:
    if ele0.is_displayed():
        ele0.click()

#获取所有窗口句柄
all_handles = driver.window_handles
#转换到当前窗口句柄
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to_window(handle)
#输入账号和密码
driver.find_element_by_name("userName").send_keys("18220662738")
driver.find_element_by_name("password").send_keys("13772195973")
time.sleep(6)
#获取验证码
driver.save_screenshot('D://aa.png')
#定位验证码
imgelement = driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__verifyCodeImg']")
#获取验证码的x、y坐标
location = imgelement.location
#获取验证码的长宽
size = imgelement.size
driver.implicitly_wait(10)
#写成我们需要截取的位置坐标
rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))

#打开截图
openimage = Image.open('D://aa.png')
#使用Image的crop函数，从截图中再次截取我们需要的区域
frame3 = openimage.crop(rangle)
frame3.save('D://frame3.png')
qq=Image.open('D://frame3.png')
text =pytesseract.image_to_string(qq).strip()
print(text)

elem_code= driver.find_element_by_name("verifyCode")
elem_code.send_keys(text)
driver.implicitly_wait(10)
# 点击登录
driver.find_element_by_class_name("pass-button pass-button-submit")
driver.implicitly_wait(10)
driver.quit()
