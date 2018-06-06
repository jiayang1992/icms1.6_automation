# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os


class ICMS_WS(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        # 设置浏览器的默认下载路径及弹出窗口
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': 'E:\\WS自动化测试\\ICMS自动化测试\\ICMS_Automation_code\\Download_file\\'}
        option.add_experimental_option('prefs', prefs)
        # 指定chromediver的位置，如果在默认路径，这两行可以省略。
        executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        os.environ["webdriver.chrome.driver"] = executable_path
        option.add_argument("--user-data-dir=" + r"C:\Users\admin\AppData\Local\Google\Chrome\User Data")
        # 指定用户的配置地址，并加载至配置对象中。
        self.driver = webdriver.Chrome(executable_path, chrome_options=option)
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_设备数设置_添加测量位置_下发测量定义(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://192.168.40.211:2890/Home/Login")
        driver.implicitly_wait(3)
        driver.find_element_by_id("user").click()
        driver.find_element_by_id("user").clear()
        driver.find_element_by_id("user").send_keys("icmsadministrator  ")
        driver.find_element_by_id("pwd").click()
        driver.find_element_by_id("pwd").clear()
        driver.find_element_by_id("pwd").send_keys("ylicmsadministrator  ")
        driver.find_element_by_id("submit").click()
        # driver.find_element_by_xpath("//body/div/div[5]/div[2]/div").click()
        # 点击右侧树形图展开按钮
        driver.find_element_by_class_name("rightBtn").click()
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/ul/li[3]/h4").click()
        # driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/ul/li[3]/h4").click()
        # driver.find_element_by_xpath("//a[@id='LeftWS']/span").click()
        time.sleep(3)
        #点击设备树设置
        driver.find_element_by_xpath("//div[@id='Setting-Div']/div/ul/li[2]/a/span").click()
        driver.find_element_by_xpath("//body/div/div[5]/div[2]/div").click()
        menu = driver.find_element_by_xpath("//*[@id='DTList']/tbody/tr/td[9]")
        hidden_submenu = driver.find_element_by_xpath("//*[@id='DTList']/tbody/tr/td[9]/div/span[1]")
        time.sleep(5)
        addmenu = ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
        time.sleep(5)
        # driver.find_element_by_xpath("//span[@onclick='DevTreeSet.addMeasureSite(1)']").click()
        Select(driver.find_element_by_id("MSiteNameAdd")).select_by_value("7")
        Select(driver.find_element_by_id("WSIDAdd")).select_by_value("4")
        Select(driver.find_element_by_name("FactoryID_0")).select_by_value("NTN")
        # driver.find_element_by_xpath("//table[@id='MSAddBearingTable']/tbody/tr/td[2]/span/span/span/span[2]").click()
        driver.find_element_by_xpath("//form[@id='AddMSiteForm']/div[3]/div/label").click()
        driver.find_element_by_id("MSAddAlarmValue_0_0").click()
        driver.find_element_by_id("MSAddAlarmValue_0_0").clear()
        driver.find_element_by_id("MSAddAlarmValue_0_0").send_keys("0")
        driver.find_element_by_id("MSAddDangerValue_0_0").click()
        driver.find_element_by_id("MSAddDangerValue_0_0").clear()
        driver.find_element_by_id("MSAddDangerValue_0_0").send_keys("1")
        driver.find_element_by_id("MSAddAlarmValue_0_1").click()
        driver.find_element_by_id("MSAddAlarmValue_0_1").clear()
        driver.find_element_by_id("MSAddAlarmValue_0_1").send_keys("0")
        driver.find_element_by_id("MSAddDangerValue_0_1").click()
        driver.find_element_by_id("MSAddDangerValue_0_1").clear()
        driver.find_element_by_id("MSAddDangerValue_0_1").send_keys("1")
        driver.find_element_by_id("MSAddAlarmValue_0_2").click()
        driver.find_element_by_id("MSAddAlarmValue_0_2").clear()
        driver.find_element_by_id("MSAddAlarmValue_0_2").send_keys("0")
        driver.find_element_by_id("MSAddDangerValue_0_2").click()
        driver.find_element_by_id("MSAddDangerValue_0_2").clear()
        driver.find_element_by_id("MSAddDangerValue_0_2").send_keys("1")
        driver.find_element_by_xpath("//form[@id='AddMSiteForm']/div[4]/div/label").click()
        driver.find_element_by_id("MSAddAlarmValue_1_0").click()
        driver.find_element_by_id("MSAddAlarmValue_1_0").clear()
        driver.find_element_by_id("MSAddAlarmValue_1_0").send_keys("0")
        driver.find_element_by_id("MSAddDangerValue_1_0").click()
        driver.find_element_by_id("MSAddDangerValue_1_0").clear()
        driver.find_element_by_id("MSAddDangerValue_1_0").send_keys("1")
        driver.find_element_by_id("MSAddAlarmValue_1_1").click()
        driver.find_element_by_id("MSAddAlarmValue_1_1").clear()
        driver.find_element_by_id("MSAddAlarmValue_1_1").send_keys("0")
        driver.find_element_by_id("MSAddDangerValue_1_1").click()
        driver.find_element_by_id("MSAddDangerValue_1_1").clear()
        driver.find_element_by_id("MSAddDangerValue_1_1").send_keys("1")
        driver.find_element_by_id("MSAddAlarmValue_1_2").click()
        driver.find_element_by_id("MSAddAlarmValue_1_2").clear()
        driver.find_element_by_id("MSAddAlarmValue_1_2").send_keys("0")
        driver.find_element_by_id("MSAddDangerValue_1_2").click()
        driver.find_element_by_id("MSAddDangerValue_1_2").clear()
        driver.find_element_by_id("MSAddDangerValue_1_2").send_keys("1")
        driver.find_element_by_xpath("//form[@id='AddMSiteForm']/div[5]/div/label").click()
        driver.find_element_by_id("MSAddAlarmValue_2_0").click()
        driver.find_element_by_id("MSAddAlarmValue_2_0").clear()
        driver.find_element_by_id("MSAddAlarmValue_2_0").send_keys("0")
        driver.find_element_by_id("MSAddDangerValue_2_0").click()
        driver.find_element_by_id("MSAddDangerValue_2_0").clear()
        driver.find_element_by_id("MSAddDangerValue_2_0").send_keys("1")
        driver.find_element_by_id("MSAddAlarmValue_2_1").click()
        driver.find_element_by_id("MSAddAlarmValue_2_1").clear()
        driver.find_element_by_id("MSAddAlarmValue_2_1").send_keys("0")
        driver.find_element_by_id("MSAddDangerValue_2_1").click()
        driver.find_element_by_id("MSAddDangerValue_2_1").clear()
        driver.find_element_by_id("MSAddDangerValue_2_1").send_keys("1")
        driver.find_element_by_id("MSAddAlarmValue_2_2").click()
        driver.find_element_by_id("MSAddAlarmValue_2_2").clear()
        driver.find_element_by_id("MSAddAlarmValue_2_2").send_keys("0")
        driver.find_element_by_id("MSAddDangerValue_2_2").click()
        driver.find_element_by_id("MSAddDangerValue_2_2").clear()
        driver.find_element_by_id("MSAddDangerValue_2_2").send_keys("1")
        driver.find_element_by_xpath("//form[@id='AddMSiteForm']/div[6]/div/label").click()
        driver.find_element_by_id("MSAddAlarmValue_3_0").click()
        driver.find_element_by_id("MSAddAlarmValue_3_0").clear()
        driver.find_element_by_id("MSAddAlarmValue_3_0").send_keys("0")
        driver.find_element_by_id("MSAddDangerValue_3_0").click()
        driver.find_element_by_id("MSAddDangerValue_3_0").clear()
        driver.find_element_by_id("MSAddDangerValue_3_0").send_keys("1")
        driver.find_element_by_id("MSAddAlarmValue_3_1").click()
        driver.find_element_by_id("MSAddAlarmValue_3_1").clear()
        driver.find_element_by_id("MSAddAlarmValue_3_1").send_keys("0")
        driver.find_element_by_id("MSAddDangerValue_3_1").click()
        driver.find_element_by_id("MSAddDangerValue_3_1").clear()
        driver.find_element_by_id("MSAddDangerValue_3_1").send_keys("1")
        driver.find_element_by_xpath("//form[@id='AddMSiteForm']/div[7]/div/label").click()
        driver.find_element_by_id("MSAddAlarmValue_4_0").click()
        driver.find_element_by_id("MSAddAlarmValue_4_0").clear()
        driver.find_element_by_id("MSAddAlarmValue_4_0").send_keys("0")
        driver.find_element_by_id("MSAddDangerValue_4_0").click()
        driver.find_element_by_id("MSAddDangerValue_4_0").clear()
        driver.find_element_by_id("MSAddDangerValue_4_0").send_keys("1")
        driver.find_element_by_xpath("//form[@id='AddMSiteForm']/div[8]/div/label").click()
        driver.find_element_by_id("MSAddMTHighValue0").click()
        driver.find_element_by_id("MSAddMTHighValue0").clear()
        driver.find_element_by_id("MSAddMTHighValue0").send_keys("25")
        driver.find_element_by_id("MSAddMTHighHighValue0").click()
        driver.find_element_by_id("MSAddMTHighHighValue0").clear()
        driver.find_element_by_id("MSAddMTHighHighValue0").send_keys("35")
        driver.find_element_by_xpath("//form[@id='AddMSiteForm']/div[9]/div/label").click()
        driver.find_element_by_id("MSAddMTHighValue1").click()
        driver.find_element_by_id("MSAddMTHighValue1").clear()
        driver.find_element_by_id("MSAddMTHighValue1").send_keys("3.5")
        driver.find_element_by_id("MSAddMTHighHighValue1").click()
        driver.find_element_by_id("MSAddMTHighHighValue1").clear()
        driver.find_element_by_id("MSAddMTHighHighValue1").send_keys("2")
        driver.find_element_by_xpath("//form[@id='AddMSiteForm']/div[10]/div/label").click()
        driver.find_element_by_id("MSAddMTHighValue2").click()
        driver.find_element_by_id("MSAddMTHighValue2").clear()
        driver.find_element_by_id("MSAddMTHighValue2").send_keys("20")
        driver.find_element_by_id("MSAddMTHighHighValue2").click()
        driver.find_element_by_id("MSAddMTHighHighValue2").clear()
        driver.find_element_by_id("MSAddMTHighHighValue2").send_keys("35")
        driver.find_element_by_id("MeasureSiteAddFormButton").click()
        time.sleep(3)
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//table[@id='DTList']/tbody/tr[2]/td[2]/label").click()
        time.sleep(3)
        print("下发测量定义前的状态为:",driver.find_element_by_xpath("//*[@id='DTList']/tbody/tr[2]/td[8]").text)
        driver.find_element_by_xpath("//span[@onclick='DevTreeSet.opCmd()']").click()
        time.sleep(10)
        print("下发测量定义后的状态为:", driver.find_element_by_xpath("//*[@id='DTList']/tbody/tr[2]/td[8]").text)
        print("成功下发测量定义")
        # driver.find_element_by_class_name("views-oprate-item").click()
        # tooltip = driver.find_element_by_class_name("modal-content").find_element_by_class_name("message-content").text
        # print(tooltip)

    def test_设备树设置_刷新ws(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://192.168.40.211:2890/Home/Login")
        driver.implicitly_wait(3)
        driver.find_element_by_id("user").click()
        driver.find_element_by_id("user").clear()
        driver.find_element_by_id("user").send_keys("icmsadministrator  ")
        driver.find_element_by_id("pwd").click()
        driver.find_element_by_id("pwd").clear()
        driver.find_element_by_id("pwd").send_keys("ylicmsadministrator  ")
        driver.find_element_by_id("submit").click()
        # driver.find_element_by_xpath("//body/div/div[5]/div[2]/div").click()
        # 点击右侧树形图展开按钮
        driver.find_element_by_class_name("rightBtn").click()
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/ul/li[3]/h4").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='Setting-Div']/div/ul/li[2]/a/span").click()
        driver.find_element_by_class_name("rightBtn").click()
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='DevTreeSetArea']/div[1]/span[2]").click()
        time.sleep(5)
        try:
            content_driver = driver.find_element_by_class_name("tab-pane fade yltab-content active in")
            assert driver.refresh()# 刷新方法 refresh
            print('test pass: refresh successful')
        except Exception as e:
                print("Exception found", format(e))
                driver.quit()
#判断点击刷新WS后是否会对当前模块进行刷新
        try:
            num = 0
            if driver.find_element_by_class_name("views").click():
                num = 1
            else:
                num = 0
            assert driver.refresh()  # 刷新方法 refresh
            print('test pass: refresh successful')
        except Exception as e:
            print("Exception found", format(e))
            driver.quit()
    def test_传感器升级(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://192.168.40.211:2890/Home/Login")
        driver.implicitly_wait(3)
        driver.find_element_by_id("user").click()
        driver.find_element_by_id("user").clear()
        driver.find_element_by_id("user").send_keys("icmsadministrator")
        driver.find_element_by_id("pwd").click()
        driver.find_element_by_id("pwd").clear()
        driver.find_element_by_id("pwd").send_keys("ylicmsadministrator")
        driver.find_element_by_id("submit").click()
        # driver.find_element_by_xpath("//body/div/div[5]/div[2]/div").click()
        # 点击右侧树形图展开按钮
        driver.find_element_by_class_name("rightBtn").click()
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/ul/li[3]/h4").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='LeftWS']/span").click()
        driver.find_element_by_class_name("rightBtn").click()
        time.sleep(5)
        # try:
        #     element0 = driver.find_elements_by_name("ylicon-correctness_icon")
        #     for ele0 in element0:
        #         if ele0.is_displayed():
        #             state = "correctness"
        #     #         ele0.click()
        #     # driver.find_element_by_class_name("ylicon-correctness_icon")
        # except:
        #     state = "closemenu"
        #     if state == "correctness":
        #         print("该WS状态为连接状态！")  ylicon-closemenu_icon
        #         driver.find_element_by_class_name("table-selectbox").click()
        #     elif state == "closemenu":
        #         print("该WS状态为关闭状态！")
        driver.find_element_by_xpath("//*[@id='WSDataList']/tbody/tr/td[2]/label").click()
        time.sleep(3)
        driver.find_element_by_id("WSUpdateButton").click()
        time.sleep(5)
        # driver.find_element_by_id("WSUploadFileDetail").send_keys("")
        # path = 'file:///' + os.path.abspath('iWSNII.WS.Firmware.1.5.3.2.bin')
        # driver.get(path)
        # 定位上传按钮，上传文件
        element0 = driver.find_element_by_id("WSUploadFileDetail")
        for ele0 in element0:
            if ele0.is_displayed():
                ele0.click()
        #driver.find_element_by_id("WSUploadFileDetail").click()
        time.sleep(5)
        os.system("E:\WS自动化测试\iWSNII.WS.Firmware.1.5.3.2.exe")
        time.sleep(10)
        print("升级前的状态是：", driver.find_element_by_xpath("//*[@id='WSDataList']/tbody/tr[1]/td[10]").text)
        driver.find_element_by_class_name("btn-defaults btn-defaults-normal").click()
        time.sleep(10)
        print("升级后的状态是：", driver.find_element_by_xpath("//*[@id='WSDataList']/tbody/tr[1]/td[10]").text)
        print("升级后的版本号是:",driver.find_element_by_xpath("//*[@id='WSDataList']/tbody/tr[1]/td[9]").text)
        # print(driver.get_log())

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
