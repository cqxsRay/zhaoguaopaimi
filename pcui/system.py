from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from common import configHttp
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time
from selenium.webdriver.support.select import Select
content=configHttp.ConfigHttp()
# global driver
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
class person:
    def login(self):
        login_url=content.set_url("/bfad/user/login")
        driver.get(login_url)
        time.sleep(3)
        action=ActionChains(driver)
        # 点击系统选择框
        action.click(driver.find_element_by_class_name("ant-select-lg")).perform()
        # 选择第几个系统就发送记几个按键
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(3)


if __name__=="__main__":
    b=person()
    b.login()
