#coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://segmentfault.com/news")

# 获得所有分页的数量
# -2是因为要去掉上一个和下一个
total_pages = len(driver.find_element_by_class_name("pagination").find_elements_by_tag_name("li"))-2
print ("total_pages is %s" %(total_pages))

# 获取当前页面是第几页
current_page = driver.find_element_by_class_name("pagination").find_element_by_class_name("active")
print ("current page is %s" %(current_page.text))

#跳转到第二页
next_page = driver.find_element_by_class_name("pagination").find_element_by_link_text("2")
next_page.click()

pages = driver.find_element_by_class_name("pagination").find_elements_by_tag_name("li")
for page in pages:
   page.click()