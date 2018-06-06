#coding = utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#获取所有cookie
cookie = driver.get_cookies()
print(cookie)
#向cookie的name和value添加会话信息
driver.add_cookie({'name':'key-aaaaaa','value':'value-bbbb'})
#遍历cookie中的name和value信息并打印
for cookie in driver.get_cookies():
    print("%s  - %s" %(cookie['name'],cookie['value']))

#删除部分cookie
dele_part_cookie = driver.delete_cookie("CookieName")
#删除所有cookie
dele_cookie = driver.delete_all_cookies()
print(cookie)

time.sleep(3)
