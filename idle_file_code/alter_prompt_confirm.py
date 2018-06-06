#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
url = "http://www.baidu.com"
driver.get(url)
driver.implicitly_wait(5)

#进入搜索设置项
#link = driver.find_element_by_link_text("设置")
element0 = driver.find_elements_by_name("tj_settingicon")
for ele0 in element0:
    if ele0.is_displayed():
        ele0.click()

driver.find_element_by_link_text("搜索设置").click()
time.sleep(2)

# 设置语言范围
choice = driver.find_element_by_name("SL")
choice.find_element_by_xpath("//*[@id='SL_1']").click()
time.sleep(2)

#保存设置
driver.find_element_by_xpath("//a[@class='prefpanelgo']").click()
time.sleep(3)

#弹框处理
#accept - 点击【确认】按钮
#dismiss - 点击【取消】按钮
alert=driver.switch_to_alert()
alert.accept()
print(alert.text())

#跳转到百度首页后，进行搜索表
driver.find_element_by_id('kw').send_keys("selenium")
driver.find_element_by_id('su').click()
time.sleep(3)

driver.quit()

'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

ele0 = driver.find_elements_by_name("tj_settingicon")
for element in ele0:
    if element.is_displayed():
        element.click()
driver.find_element_by_link_text("搜索设置").click()
time.sleep(2)

choice = driver.find_element_by_name("SL")
choice.find_element_by_xpath("//*[@id='SL_1']").click()
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[2]/div[7]/div/div/div/div[1]/form/div/table/tbody/tr[7]/td[2]/div[1]/a[1]").click()
time.sleep(2)
driver.switch_to_alert().accept()

driver.quit()
'''