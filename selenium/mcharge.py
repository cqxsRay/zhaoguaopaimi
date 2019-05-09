from selenium import webdriver
from common import getexcel
import time
from common import configHttp
content=configHttp.ConfigHttp()
user=getexcel.read_xls("user.xlsx","login").dict_xls()

for i in range(len(user)):
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    login_url = content.set_url("/pudge/login")
    driver.get(login_url)
    time.sleep(3)
    element1=driver.find_element_by_xpath("//input[@type='text']")
    element1.send_keys(user[i]['phone'])
    time.sleep(1)
    element2=driver.find_element_by_xpath("//input[@type='password']")
    element2.send_keys(user[i]['password'])
    element3=driver.find_element_by_xpath("//button[@type='submit']")
    element3.click()
    time.sleep(3)
    element4 = driver.find_element_by_link_text("我的账户")
    element4.click()
    time.sleep(3)
    # 点击充值按钮
    element5 = driver.find_element_by_xpath("//div/button[1]")
    element5.click()
    time.sleep(3)
    # 输入充值金额
    element6 = driver.find_element_by_xpath("//span/input[@type='text']")
    element6.send_keys(user[i]['charge'])
    # 点击确认充值按钮
    element7 = driver.find_element_by_xpath("//button[@type='button']")
    element7.click()
    time.sleep(3)
    # 输入交易密码
    element8 = driver.find_element_by_id("password")
    element8.send_keys(user[i]['chargeno'])
    # 点击同意协议并支付
    element9 = driver.find_element_by_id("nextButton")
    element9.click()
    time.sleep(10)
    driver.close()