# 这个是pc端ui自动话测试用例的模型
import unittest
import time
from selenium import webdriver
from common import getexcel
from common import configHttp
user=getexcel.read_xls("fortest.xlsx","fortest").dict_xls()
content=configHttp.ConfigHttp()
class testp2p(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()
    def setUp(self):
        print("start")
    def test_login1(self):
        login_url = content.set_url("/pudge/login")
        self.driver.get(login_url)
        time.sleep(3)
        # 输入手机号
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys('14711119998')
        # 输入密码
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys('111111')
        # 点击登录按钮
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        assert self.driver.current_url=="http://192.168.2.42/pudge/home"
    def test_login2(self):
        login_url = content.set_url("/pudge/login")
        self.driver.get(login_url)
        time.sleep(3)
        # 输入手机号
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys('18600660116')
        # 输入密码
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys('111111')
        # 点击登录按钮
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        assert self.driver.current_url=="http://192.168.2.42/pudge/home"

    def tearDown(self):
        print("end")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__=='__main__':
    # 方法1：执行所有的测试
    unittest.main()

