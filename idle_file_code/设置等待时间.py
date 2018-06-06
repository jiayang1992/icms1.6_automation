#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#webdriverWait方法的使用
element = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id("kw"))
element.send_keys("seleniium")

#添加智能等待
driver.implicitly_wait(30)
driver.find_element_by_id("su").click()
time.sleep(2)
driver.quit()

