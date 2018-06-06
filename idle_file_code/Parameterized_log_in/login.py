#coding = utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time,os
import unittest
import userinfo
#通过变量来接收函数，获得用户名和密码
name,pwd=userinfo.fun()
print(name,pwd)

def login(self):
    driver = webdriver.Firefox()
    driver.find_element_by_class_name("tj_login").click()
    driver.find_element_by_id("user_name").clear()
    driver.find_element_by_id("user_name").send_keys(name)
    driver.find_element_by_id("user_pwd").clear()
    driver.find_element_by_id("user_pwd").send_keys(pwd)
    driver.find_element_by_id("dl_an_submit").click()

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
login()










