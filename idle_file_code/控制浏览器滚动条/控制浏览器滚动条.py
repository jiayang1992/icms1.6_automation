#coding = utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

#将滚动条拖至最底下
js_bottom = "var drag_to_bottom = document.documentElement.scrollTop=10000 "
driver.execute_script(js_bottom)
time.sleep(2)

js_top = "var drag_to_top = document.documentElement.scrollTop=0 "
driver.execute_script(js_top)
time.sleep(3)

driver.quit()