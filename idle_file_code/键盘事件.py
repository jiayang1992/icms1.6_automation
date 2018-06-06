#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

#输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(2)

#删除多余的输入
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(2)

driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
time.sleep(2)

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(1)

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'c')
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
time.sleep(2)
driver.quit()


