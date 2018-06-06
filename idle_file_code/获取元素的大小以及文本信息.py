#coding = utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("http://124.115.106.140:8055/manage/user/home")
text = driver.find_element_by_id("visitId").text
print (text)
time.sleep(5)

#driver.get("http://www.baidu.com")
#size = driver.find_element_by_id("kw").size
#print (size)
#time.sleep(4)
#返回元素的属性值，id、name、type或元素拥有的其它任意属性
attribute = driver.find_element_by_id("btnLogin").get_attribute('type')
print (attribute)

result = driver.find_element_by_id("btnLogin").is_displayed()
print (result)
