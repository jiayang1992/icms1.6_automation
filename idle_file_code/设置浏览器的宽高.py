#coding utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

print ("设置浏览器的宽高")
driver.set_window_size(480,800)
time.sleep(3)
driver.quit()
