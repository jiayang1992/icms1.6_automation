# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://124.115.106.140:2121/manage/user/home "
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/manage/user/home")
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("1")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum0").click()
        driver.find_element_by_id("menu-sm0").click()
        # drophandle = driver.current_window_handle
        # allhandles=driver.window_handles
        # for droplisthandles in allhandles:
        #      if droplisthandles != drophandle:
        #          driver.switch_to_window(droplisthandles)
        #          driver.implicitly_wait(10)
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_name("town").click()
        driver.find_element_by_xpath("/html/body/form/div[1]/ul/li[1]/select/option[3]").click()
        driver.find_element_by_name("villageAttri").click()
        driver.find_element_by_xpath("/html/body/form/div[1]/ul/li[2]/select/option[2]").click()
        # select = Select(driver.find_element_by_name("town"))
        # select.select_by_visible_text(u"白泥井镇")
        # Select(driver.find_element_by_id("villageAttriId")).select_by_visible_text(u"贫困村")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        #
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
