#coding=utf-8
from selenium import webdriver
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
path = 'file:///' + os.path.abspath('下拉菜单.html')
driver.get(path)
time.sleep(2)

menu = driver.find_element_by_id("ShippingMethod")
menu.click()
ActionChains(driver).move_to_element(menu).perform()
dowenlist = driver.find_element_by_xpath("//*[@id='ShippingMethod']/option[2]")
time.sleep(3)
dowenlist.click()
time.sleep(3)

driver.quit()