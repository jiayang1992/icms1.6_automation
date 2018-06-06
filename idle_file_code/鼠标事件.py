#右击鼠标
'''
#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("http://www.qq.com")

# 定位到需要右击的元素
right = driver.find_element_by_xpath("//*[@id='searchBtn']")

#对定位到的元素执行鼠标右击操作
ActionChains(driver).context_click(right)
'''
'''
#双击鼠标
#coding = utf-8
from selenium import webdriver
 #引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains

 #使用方法
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

 #定位到需要右击的元素并赋值给rigth_click
double= driver.find_element_by_xpath("//*[@id='su']")
 #对定位到的元素进行右击操作。
ActionChains(driver).double_click(double).perform()
'''
'''鼠标拖放
#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#定位元素的位置
element = driver.find_element_by_name("wd")
#定位元素要移动到的目标位置
target = driver.find_element_by_name("xxx")
#执行元素的移动操作
ActionChains(driver).drag_and_drop(element,target).perform()
'''
'''
#按下鼠标左键
#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.qq.com/")

#定位到鼠标按下左键的元素
left = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/strong/a")
#定位到的元素执行鼠标左键按下的操作
ActionChains(driver).click(left).perform()
'''
'''鼠标移动到元素上
#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#定位到鼠标移动到上面的元素
above = driver.find_element_by_xpath("//*[@id='su']")
#对定位到的元素执行鼠标移动到上面的操作
ActionChains(driver).move_to_element(above).perform()
'''
