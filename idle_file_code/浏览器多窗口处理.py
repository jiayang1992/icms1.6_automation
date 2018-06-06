#coding=utf-8
import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
#获取当前窗口
baiduhandle = driver.current_window_handle
#打开登录窗口
element0 = driver.find_elements_by_name("tj_login")
for ele0 in element0:
    if ele0.is_displayed():
        ele0.click()

#获得所有窗口
allhandles = driver.window_handles
for loginhandle in allhandles:
    if loginhandle!=baiduhandle:
        driver.switch_to_window(loginhandle)
        driver.implicitly_wait(10)

time.sleep(2)

driver.switch_to_window(baiduhandle)
driver.find_element_by_id("kw").send_keys("注册成功")
time.sleep(2)
driver.quit()


