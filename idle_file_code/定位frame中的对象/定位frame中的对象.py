#coding=utf-8
from selenium import webdriver
import time
import os

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('iframe.html')
driver.get(file_path)

driver.implicitly_wait(30)
#先找到iframe1的id等于f1的
driver.switch_to_frame("f1")
#在找到iframe2的id等于f2
driver.switch_to_frame("f2")

#操作元素
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(2)
driver.quit()

