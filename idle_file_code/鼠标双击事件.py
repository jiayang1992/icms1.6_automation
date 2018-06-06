#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
brower = webdriver.Chrome()
brower.get("http://www.baidu.com")
 #定位到需要右击的元素并赋值给rigth_click
double = brower.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/form/span[2]/input")
 #对定位到的元素进行右击操作。
ActionChains(brower).double_click(double).perform()
