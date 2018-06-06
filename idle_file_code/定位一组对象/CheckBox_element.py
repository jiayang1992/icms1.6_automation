#coding=utf-8
from selenium import webdriver
import time
import os

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath("CheckBox.html")
driver.get(file_path)

#选择所有type为checkbox的元素并勾选
checkboxes = driver.find_elements_by_css_selector('input[type = checkbox]')
for checkbox in checkboxes:
    checkbox.click()

#打印当前页面上type为CheckBox的个数
print (len(driver.find_elements_by_css_selector('input[type=checkbox]')))

#把页面还是那个最后一个checkbox的勾去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
driver.quit()