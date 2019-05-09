from selenium import webdriver
from common import getexcel
import time
from common import configHttp
content=configHttp.ConfigHttp()
user=getexcel.read_xls("user.xlsx","register").dict_xls()
for i in range(len(user)):
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    regist_url = content.set_url("/pudge/register")
    driver.get(regist_url)
    time.sleep(3)
    element1 = driver.find_element_by_xpath("//input[@id='userAcc']")
    element1.send_keys(user[i]['phone'])
    element2 = driver.find_element_by_xpath("//input[@id='userPwd']")
    element2.send_keys(user[i]['password'])
    element3 = driver.find_element_by_xpath("//button[@type='button']")
    element3.click()
    element4 = driver.find_element_by_xpath("//input[@id='vericode']")
    element4.send_keys("111111")
    element5 = driver.find_element_by_xpath("//button[@type='submit']")
    element5.click()
    time.sleep(3)
    driver.close()
