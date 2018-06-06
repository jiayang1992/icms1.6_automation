#coding=utf-8
from selenium import webdriver
import time
import os
#获取地址
driver = webdriver.Firefox()
path = 'file:///' + os.path.abspath('Document.html')
driver.get(path)

#定位上传按钮，上传文件
driver.find_element_by_name("file").click()
os.system("D:\Phyon\pycharm_code\idle_file_code\Document_upl\Document.exe")
driver.implicitly_wait(20)
driver.quit()
