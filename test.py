from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://www.baidu.com")