#coding = utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://124.115.106.140:8055/manage/user/home")
try:

    driver.find_element_by_id("userNameCopy").clear()
    driver.find_element_by_id("userNameCopy").send_keys("admin")
    driver.find_element_by_id("userPassword").clear()
    driver.find_element_by_id("userPassword").send_keys("1")
    driver.find_element_by_id("btnLogin1").click()
except:
    driver.get_screenshot_as_file("F:\工作总结\error.png")

    #driver.find_element_by_id("btnLogin").submit()
time.sleep(5)
driver.quit()
