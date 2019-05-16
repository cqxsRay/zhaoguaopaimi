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
    driver.close()
