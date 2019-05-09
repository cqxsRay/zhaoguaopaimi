from selenium import webdriver
from common.Log import Log
from selenium.webdriver.common.keys import Keys
from common import configHttp
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time
import redis
from common import getexcel
log=Log()
person=getexcel.read_xls("userinfo.xls","sheet1").dict_xls()
content=configHttp.ConfigHttp()
# 连接redis
pool = redis.ConnectionPool(host='192.168.2.36', password='guohuaiGUO4056')  # 实现一个连接池
r = redis.Redis(connection_pool=pool)
# google
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# safari
# driver = webdriver.Safari()
# driver.maximize_window()
class user():
    def __init__(self,phone,pwd):
        self.phone=phone
        self.pwd=pwd
    # 天辰注册，无图形验证码
    def regist(self):
        regist_url=content.set_url("/pudge/register")
        driver.get(regist_url)
        time.sleep(3)
        # 输入手机号
        driver.find_element_by_xpath("//input[@id='userAcc']").send_keys(self.phone)
        # 输入密码
        driver.find_element_by_xpath("//input[@id='userPwd']").send_keys(self.pwd)
        # 点击获取验证码
        driver.find_element_by_xpath("//button[@type='button']").click()
        # 输入验证码
        driver.find_element_by_xpath("//input[@id='vericode']").send_keys("111111")
        # 点击提交按钮
        driver.find_element_by_xpath("//button[@type='submit']").click()
        # time.sleep(5)
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "ant-modal-body")))
        driver.find_element_by_class_name("ant-modal-close-x").click()
        return driver.current_url

    # 天辰新注册增加图形验证码
    def registx(self):
        regist_url = content.set_url("/pudge/register")
        driver.get(regist_url)
        # 获取session
        cookie = driver.get_cookies()[0]['value']
        # 获取图形验证码
        tuxing = r.get("user:captcha:%s" % cookie)
        # 将byte类型转换成字符串类型
        tx = str(tuxing, encoding='utf-8')
        time.sleep(3)
        # 输入手机号
        driver.find_element_by_xpath("//input[@id='userAcc']").send_keys(self.phone)
        # 输入图形验证码
        driver.find_element_by_xpath("//input[@id='captcha']").send_keys(tx)
        # 输入密码
        driver.find_element_by_xpath("//input[@id='userPwd']").send_keys(self.pwd)
        # 点击获取验证码
        driver.find_element_by_xpath("//button[@type='button']").click()
        # 输入验证码
        driver.find_element_by_xpath("//input[@id='vericode']").send_keys("111111")
        # 点击提交按钮
        driver.find_element_by_xpath("//button[@type='submit']").click()
        # time.sleep(5)
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "ant-modal-body")))
        driver.find_element_by_class_name("ant-modal-close-x").click()
        return driver.current_url
    # 开出借户
    def openaccount(self,idcard,bankcardno,tradeno,name):
        """

        :param idcard: 身份证号
        :param bankcardno: 银行卡号
        :param tradeno: 交易密码
        :param name: 姓名
        :return:
        """
        self.idcard=idcard
        self.bankcardno=bankcardno
        self.tradeno=tradeno
        self.name=name
        login_url = content.set_url("/pudge/login")
        driver.get(login_url)
        # time.sleep(3)
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, "//div/h3")))
        driver.find_element_by_xpath("//input[@type='text']").send_keys(self.phone)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(self.pwd)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.LINK_TEXT, "我的账户")))
        time.sleep(3)
        # 点击我的账户
        driver.find_element_by_link_text("我的账户").click()
        # time.sleep(3)
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.LINK_TEXT, "立即开户")))
        # 点击 立即开户
        driver.find_element_by_xpath("//div/div[1]/div[1]/a").click()
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.XPATH, "//div/h3")))
        # time.sleep(3)
        # 输入姓名
        driver.find_element_by_xpath("//input[@placeholder='请输入真实姓名']").send_keys(self.name)
        # 输入身份证
        driver.find_element_by_xpath("//input[@placeholder='请输入身份证号']").send_keys(self.idcard)
        time.sleep(3)
        # 点击下一步
        driver.find_element_by_xpath("//button[@type='submit']").click()
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "subtitle")))
        # 输入银行卡号
        driver.find_element_by_id('bankcardNo').send_keys(self.bankcardno)
        # 输入手机号
        driver.find_element_by_xpath("//input[@id='mobile']").send_keys(self.phone)
        # 点击获取验证码
        driver.find_element_by_xpath("//input[@id='sendSmsVerify']").click()
        time.sleep(3)
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "submitBtn-2")))
        # 点击弹框的我知道了
        driver.find_element_by_class_name("submitBtn-2").click()
        # time.sleep(2)
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "smsCode")))
        # 输入验证码
        driver.find_element_by_id("smsCode").send_keys("111111")
        # 输入交易密码
        driver.find_element_by_id("password").send_keys(self.tradeno)
        # 再次输入交易密码
        driver.find_element_by_id("confirmPassword").send_keys(self.tradeno)
        # 点击下一步
        driver.find_element_by_id("nextButton").click()
        # 等待结果出现
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "successs_h3___3gsQK")))

    # 个人借款开户
    def peropen(self,idcard,bankcardno,tradeno,name):
        """

        :param idcard: 身份证号
        :param bankcardno: 银行卡号
        :param tradeno: 交易密码
        :param name: 姓名
        :return:
        """
        self.idcard=idcard
        self.bankcardno=bankcardno
        self.tradeno=tradeno
        self.name=name
        login_url = content.set_url("/pudge/login")
        driver.get(login_url)
        # time.sleep(3)
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, "//div/h3")))
        driver.find_element_by_xpath("//input[@type='text']").send_keys(self.phone)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(self.pwd)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.LINK_TEXT, "我的账户")))
        time.sleep(3)
        # 点击我要借款
        driver.find_element_by_class_name("borrowTitle___3oPdp").click()
        # time.sleep(3)
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.LINK_TEXT, "立即开户")))
        # 点击 立即开户
        driver.find_element_by_xpath("//div/div[1]/div[1]/a").click()
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.XPATH, "//div/h3")))
        # time.sleep(3)
        # 输入姓名
        driver.find_element_by_xpath("//input[@placeholder='请输入真实姓名']").send_keys(self.name)
        # 输入身份证
        driver.find_element_by_xpath("//input[@placeholder='请输入身份证号']").send_keys(self.idcard)
        time.sleep(3)
        # 点击下一步
        driver.find_element_by_xpath("//button[@type='submit']").click()
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "subtitle")))
        # 输入银行卡号
        driver.find_element_by_id('bankcardNo').send_keys(self.bankcardno)
        # 输入手机号
        driver.find_element_by_xpath("//input[@id='mobile']").send_keys(self.phone)
        # 点击获取验证码
        driver.find_element_by_xpath("//input[@id='sendSmsVerify']").click()
        time.sleep(3)
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "submitBtn-2")))
        # 点击弹框的我知道了
        driver.find_element_by_class_name("submitBtn-2").click()
        # time.sleep(2)
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, "smsCode")))
        # 输入验证码
        driver.find_element_by_id("smsCode").send_keys("111111")
        # 输入交易密码
        driver.find_element_by_id("password").send_keys(self.tradeno)
        # 再次输入交易密码
        driver.find_element_by_id("confirmPassword").send_keys(self.tradeno)
        # 点击下一步
        driver.find_element_by_id("nextButton").click()
        # 等待结果出现
        time.sleep(10)
        if driver.find_element_by_class_name("successs_h3___2YdZh").is_displayed():
            print("开户成功")
        else:
            print("开户处理中或者失败")
    # 登录+测评
    def evaluation(self):
        login_url = content.set_url("/pudge/login")
        driver.get(login_url)
        # time.sleep(3)
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
        driver.find_element_by_xpath("//input[@type='text']").send_keys(self.phone)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(self.pwd)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        # time.sleep(3)
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.LINK_TEXT, "我的账户")))
        driver.find_element_by_link_text("我的账户").click()
        # time.sleep(3)
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.LINK_TEXT, "立即测评")))
        driver.find_element_by_link_text("立即测评").click()
        # time.sleep(3)
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='1']/div[2]//input")))
        # 每道题选最后一个选项
        # inputs = driver.find_elements_by_xpath("//input[@type='checkbox']")
        # for input in inputs:
        #     input.click()
        #     time.sleep(0.5)
        # 获取题数
        tishu = driver.find_elements_by_xpath("//div[@class='content___3phm_']/div")  # len:13
        # 获取每道题的选项数
        xuanxiang= driver.find_elements_by_xpath("//div[@id=1]/div")  # len:5
        # 每道题随机选
        for i in range(1, len(tishu)):  # id是从1开始，13是最后的声明。表示1-12的数字
            j = random.randint(2, len(xuanxiang))  # 1表示的题干，所以从2开始，表示2-5的数字，包含5
            xuanze = driver.find_element_by_xpath("//div[@id=%d]/div[%d]//input[@type='checkbox']" % (i, j))
            xuanze.click()
            time.sleep(1)
        # 提交
        driver.find_element_by_link_text("提交").click()
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, "完成")))
        # 点击结果页完成
        driver.find_element_by_link_text("完成").click()
        time.sleep(5)
    # 登录
    def login(self):
        login_url = content.set_url("/pudge/login")
        driver.get(login_url)
        time.sleep(3)
        # 输入手机号
        driver.find_element_by_xpath("//input[@type='text']").send_keys(self.phone)
        # 输入密码
        driver.find_element_by_xpath("//input[@type='password']").send_keys(self.pwd)
        # 点击登录按钮
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        return driver.current_url
    # 出借充值
    def charge(self,amount,tradeno):
        """

        :param amount: 充值金额
        :param tradeno: 交易密码
        :return:
        """
        self.amount=amount
        self.tradeno=tradeno
        login_url = content.set_url("/pudge/login")
        driver.get(login_url)
        time.sleep(3)
        driver.find_element_by_xpath("//input[@type='text']").send_keys(self.phone)
        time.sleep(1)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(self.pwd)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        # 点击我的账户
        driver.find_element_by_link_text("我的账户").click()
        time.sleep(3)
        # 点击充值按钮
        driver.find_element_by_xpath("//div/button[1]").click()
        time.sleep(3)
        # 输入充值金额
        driver.find_element_by_xpath("//span/input[@type='text']").send_keys(self.amount)
        # 点击确认充值按钮
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(3)
        # 输入交易密码
        driver.find_element_by_id("password").send_keys(self.tradeno)
        # 点击同意协议并支付
        driver.find_element_by_id("nextButton").click()
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "resContent___1w1Bw")))
        return driver.current_url
    # 个人借款充值
    def percharge(self,amount,tradeno):
        """

        :param amount: 充值金额
        :param tradeno: 交易密码
        :return:
        """
        self.amount=amount
        self.tradeno=tradeno
        login_url = content.set_url("/pudge/login")
        driver.get(login_url)
        time.sleep(3)
        driver.find_element_by_xpath("//input[@type='text']").send_keys(self.phone)
        time.sleep(1)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(self.pwd)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        # 点击我要借款
        driver.find_element_by_class_name("borrowTitle___3oPdp").click()
        time.sleep(3)
        # 点击充值按钮
        driver.find_element_by_class_name("ant-btn-primary").click()
        time.sleep(3)
        # 输入充值金额
        driver.find_element_by_xpath("//span/input[@type='text']").send_keys(self.amount)
        # 点击确认充值按钮
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(3)
        # 输入交易密码
        driver.find_element_by_id("password").send_keys(self.tradeno)
        # 点击同意协议并支付
        driver.find_element_by_id("nextButton").click()
        time.sleep(10)
        if driver.find_element_by_class_name('successs_h3___2YdZh').is_displayed():
            print("充值成功")
        else:
            log.info("充值非成功")
        return driver.current_url
    # 登录+购买
    def buy(self,buyamount):
        self.buyamount=buyamount
        login_url = content.set_url("/pudge/login")
        driver.get(login_url)
        time.sleep(3)
        driver.find_element_by_xpath("//input[@type='text']").send_keys(self.phone)
        time.sleep(1)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(self.pwd)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        # 找到第一个位置发售的产品
        driver.find_element_by_xpath("//div[1]/div/div/p[span='发售中']").click()
        time.sleep(3)
        # 输入购买金额
        driver.find_element_by_xpath("//input[@type='text']").send_keys(self.buyamount)
        # 找到购买按钮
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(3)
        return driver.current_url
    # 只是充值
    def chongzhi(self, amount, tradeno):
        """

        :param amount: 充值金额
        :param tradeno: 交易密码
        :return:
        """
        self.amount = amount
        self.tradeno = tradeno
        # 点击我的账户
        driver.find_element_by_link_text("我的账户").click()
        time.sleep(3)
        # 点击充值按钮
        driver.find_element_by_xpath("//div/button[1]").click()
        time.sleep(3)
        # 输入充值金额
        driver.find_element_by_xpath("//span/input[@type='text']").send_keys(self.amount)
        # 点击确认充值按钮
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(3)
        # 输入交易密码
        driver.find_element_by_id("password").send_keys(self.tradeno)
        # 点击同意协议并支付
        driver.find_element_by_id("nextButton").click()
        time.sleep(10)
    # 出借用户提现
    def withdraw(self,amount,tradno):
        self.amount=amount
        self.tradeno=tradno
        login_url = content.set_url("/pudge/login")
        driver.get(login_url)
        time.sleep(3)
        driver.find_element_by_xpath("//input[@type='text']").send_keys(self.phone)
        time.sleep(1)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(self.pwd)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        # 点击我的账户
        driver.find_element_by_link_text("我的账户").click()
        time.sleep(3)
        # 点击提现按钮
        driver.find_element_by_xpath("//div/button[2]").click()
        time.sleep(2)
        # 输入提现金额
        driver.find_element_by_xpath("//input[@type='text']").send_keys(self.amount)
        time.sleep(2)
        # 点击确认提现按钮
        driver.find_element_by_xpath("//button[@type='button']").click()
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "subtitle")))
        # 输入交易密码
        driver.find_element_by_id("password").send_keys(self.tradeno)
        # 点击确定按钮
        driver.find_element_by_id("nextButton").click()
    # 个人借款提现
    def perwithdraw(self,amount,tradno):
        self.amount=amount
        self.tradeno=tradno
        login_url = content.set_url("/pudge/login")
        driver.get(login_url)
        time.sleep(3)
        driver.find_element_by_xpath("//input[@type='text']").send_keys(self.phone)
        time.sleep(1)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(self.pwd)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        # 点击我要借款
        driver.find_element_by_class_name("borrowTitle___3oPdp").click()
        # time.sleep(3)
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.XPATH, "//div/div[2]/button")))
        # 点击提现按钮
        driver.find_element_by_xpath("//div/div[2]/button").click()
        time.sleep(2)
        # 输入提现金额
        driver.find_element_by_xpath("//input[@type='text']").send_keys(self.amount)
        time.sleep(2)
        # 点击确认提现按钮
        driver.find_element_by_xpath("//button[@type='button']").click()
        WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "subtitle")))
        # 输入交易密码
        driver.find_element_by_id("password").send_keys(self.tradeno)
        # 点击确定按钮
        driver.find_element_by_id("nextButton").click()
        # 等待结果出现
        time.sleep(10)
        # 判断结果
        if driver.find_element_by_class_name("waiting_h3___1UHc_").is_displayed():
            log.info("提现处理中")
        else:
            log.error("提现异常")

    # 关闭浏览器
    def close(self):
        time.sleep(3)
        driver.close()
if __name__=="__main__":
    for i in range(3,len(person)-1):
        a=user(person[i]['phone'],"a111111")
    # a=user("14711234599","bf1111")
    # a.perwithdraw("10","111111")
    # a=user("14711234599","bf1111")
    # a.registx()
        a.peropen(person[i]['cardid'],person[i]['bankid'],'111111',person[i]['name'])
    # a.evaluation()
    # a.withdraw("100","111111")
    # a.charge("2000","123456")
    # a.buy("100")