import uiautomator2 as u2
from time import sleep
from common.Log import Log
class user:
    log = Log()
    def __init__(self,phone,pwd):
        global d
        # 连接手机
        d = u2.connect("192.168.131.109")
        self.phone=phone
        self.password=pwd
    # 通过我的登录
    def login(self):
        # 点击我的
        d(text=u"我的").click()
        d(text=u"请输入手机号码").wait(timeout=3)
        # 点击输入手机号
        d(text=u"请输入手机号码").set_text(self.phone)
        d(text=u"请输入登录密码").set_text(self.password)
        # 向上滑动
        d(scrollable=True).scroll.to(text=u"登录")
        d(text=u" 登录 ").click()
        d(text=u"总资产(元)").wait(timeout=3)
        try:
            assert d(text=u"总资产(元)").exists
        except:
            # 往log文件中写入日志，因为会打印到控制台，所以会在报告中体现
            self.log.info("登录失败")
            d.screenshot('login.jpg')
        else:
            self.log.info("登录成功")
    # 通过我的注册
    def regist(self, vericode):
        self.vericode = vericode
        d(text=u"我的").click()
        d(text=u"注册").wait(timeout=3)
        try:
            assert d(text=u"注册").exists
        except:
            print("手机号已登录")
        else:
            d(text=u"注册").click()
            sleep(2)
            d(text=u"请输入手机号码").set_text(self.phone)
            d(text=u" 下一步 ").click()
            sleep(3)
            try:
                assert d(text=u"发送验证码").exists
            except:
                print("手机号有误")
                d.screenshot('regist.jpg')
            else:
                d(text=u"发送验证码").click()
                d(text=u"请输入验证码").set_text(self.vericode)
                d(text=u"请输入登录密码").set_text(self.password)
                d(scrollable=True).scroll.to(text=u"完成")
                d(text=u" 完成 ").click()
                d(text=u"总资产(元)").wait(timeout=3)
                try:
                    assert d(text=u"总资产(元)").exists
                except:
                    self.log.error("密码有误")
                    d.screenshot('regist.jpg')
                else:
                    self.log.info("注册成功")

    # 通过我的充值
    def recharge(self, amount, tradepass):
        self.amount = amount
        self.tradepass = tradepass
        d(text=u"我的").click()
        d(text=u"请输入手机号码").wait(timeout=3)
        # 点击输入手机号
        d(text=u"请输入手机号码").set_text(self.phone)
        d(text=u"请输入登录密码").set_text(self.password)
        # 向上滑动
        d(scrollable=True).scroll.to(text=u"登录")
        d(text=u" 登录 ").click()
        d(text=u"总资产(元)").wait(timeout=3)
        try:
            assert d(text=u"总资产(元)").exists
        except:
            print("登录失败")
        else:
            d(text=u"充值").click()
            d.set_fastinput_ime(True)
            d.click(0.309, 0.427)
            d.send_keys(self.amount)
            d(text=u"下一步").click()
            d.set_fastinput_ime(False)
            d(resourceId="password").set_text(self.tradepass)
            d(resourceId="nextButton").click()
            d(text=u"查看充值记录").wait(timeout=15)
            # d(text=u"充值成功", instance=1).wait(timeout=10)
            try:
                assert d(text=u"查看充值记录").exists
            except:
                self.log.error("充值失败")
                d.screenshot('recharge.jpg')

            else:
                if d(text=u"充值处理中", instance=1).exists:
                    self.log.info("充值处理中")
                else:
                    self.log.info("充值成功")

    # 通过我的提现
    def withdraw(self, amount, tradepass):
        self.tradepass = tradepass
        self.amount = amount
        d(text=u"我的").click()
        d(text=u"请输入手机号码").wait(timeout=3)
        # 点击输入手机号
        d(text=u"请输入手机号码").set_text(self.phone)
        d(text=u"请输入登录密码").set_text(self.password)
        # 向上滑动
        d(scrollable=True).scroll.to(text=u"登录")
        d(text=u" 登录 ").click()
        d(text=u"总资产(元)").wait(timeout=3)
        try:
            assert d(text=u"总资产(元)").exists
        except:
            self.log.error('登录失败')
        else:
            d(text=u"提现").click()
            d.set_fastinput_ime(True)
            # 点击提现金额输入栏
            d.click(0.309, 0.427)
            d.send_keys(self.amount)
            d(text=u"下一步").click()
            d.set_fastinput_ime(False)
            d(resourceId="nextButton").wait(timeout=3)
            try:
                assert d(resourceId="nextButton").exists
            except:
                self.log.error("提现金额有误")
                d.screenshot('withdraw.jpg')
            else:
                d(resourceId="password").set_text(self.tradepass)
                d(resourceId="nextButton").click()
                d(text=u"查看提现记录").wait(timeout=15)
                try:
                    assert d(text=u"查看提现记录").exists
                except:
                    self.log.error("提现失败")
                    d.screenshot('withdraw.jpg')
                else:
                    if d(text=u"提现处理中", instance=1).exists:
                        self.log.info("提现处理中")
                    else:
                        self.log.info("提现成功")

    # 修改交易密码-记得原交易密码
    def modify_tradepass(self,oldtradepass,newtradepass,vericode):
        self.oldtradepass=oldtradepass
        self.newtradepass=newtradepass
        self.vericode=vericode
        d(text=u"我的").click()
        d(text=u"请输入手机号码").wait(timeout=3)
        # 点击输入手机号
        d(text=u"请输入手机号码").set_text(self.phone)
        d(text=u"请输入登录密码").set_text(self.password)
        # 向上滑动
        d(scrollable=True).scroll.to(text=u"登录")
        d(text=u" 登录 ").click()
        d(text=u"总资产(元)").wait(timeout=3)
        try:
            assert d(text=u"总资产(元)").exists
        except:
            print("登录失败")
        else:
            # 点击设置按钮
            d.click(0.919, 0.085)
            d(text=u"密码管理").click()
            d(text=u"修改交易密码").click()
            d(description=u"我记得原交易密码  ").click()
            d(resourceId="oldPassword").set_text(self.oldtradepass)
            d(resourceId="password").set_text(self.newtradepass)
            d(resourceId="sendSmsVerify").click()
            d(description=u"知道了").click()
            # 开启输入法
            d.set_fastinput_ime(True)
            d(resourceId="smsCode").click()
            d.send_keys(self.vericode)
            d.set_fastinput_ime(False)
            d(resourceId="nextButton").click()
            d(text=u"返回我的页面").wait(timeout=15)
            try:
                assert d(text=u"返回我的页面").exists
                self.log.info("修改交易密码成功")
            except:
                self.log.error("修改失败")
                d.screenshot('modify.jpg')

    # 通过充值去开户
    def openaccount(self,name,cardid,bankcardno,chargepass):
        self.name=name
        self.cardid=cardid
        self.bankcardno=bankcardno
        self.chargepass=chargepass
        # 点击我点
        d(text=u"我的").click()
        d(text=u"请输入手机号码").wait(timeout=3)
        # 点击输入手机号
        d(text=u"请输入手机号码").set_text(self.phone)
        d(text=u"请输入登录密码").set_text(self.password)
        # 向上滑动
        d(scrollable=True).scroll.to(text=u"登录")
        d(text=u" 登录 ").click()
        d(text=u"总资产(元)").wait(timeout=3)
        try:
            assert d(text=u"总资产(元)").exists
        except:
            self.log.info("登录失败")
        else:
            d(text=u"充值").click()
            d(text=u"立即开通").click()
            d(text=u"请输入真实姓名").set_text(self.name)
            d(text=u"请输入身份证号").set_text(self.cardid)
            d(scrollable=True).scroll.to(text=u"下一步")
            d(text=u" 下一步 ").click()
            sleep(3)
            # 输入银行卡号
            # send_keys不能显示发送的内容时，切换输入法
            d.set_fastinput_ime(True)
            d(resourceId="bankcardNo").click()
            d.send_keys(self.bankcardno)
            d(scrollable=True).scroll.to(resourceId="mobile")
            d(resourceId="mobile").click()
            # d(resourceId="mobile").set_text(self.phone)
            d.send_keys(self.phone)
            d(scrollable=True).scroll.to(resourceId="sendSmsVerify")
            d(resourceId="sendSmsVerify").click()
            d(description=u"知道了").click()
            sleep(2)
            d(resourceId="smsCode").click()
            d.send_keys("111111")
            # 用完后关闭输入法
            d.set_fastinput_ime(False)
            d(scrollable=True).scroll.to(resourceId="password")
            d(resourceId="password").set_text(self.chargepass)
            d(resourceId="confirmPassword").set_text(self.chargepass)
            d(scrollable=True).scroll.to(resourceId="nextButton")
            d(resourceId="nextButton").click()
            d(text=u"开户成功").wait(timeout=15)
            if d(text=u"开户成功").exists:
                self.log.info("开户成功")
            elif d(description=u"银行开户中").exists:
                self.log.warning("开户中")
            else:
                self.log.error("开户失败")
                d.screenshot('openaccount.jpg')