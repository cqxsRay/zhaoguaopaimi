import uiautomator2 as u2
from time import sleep
from common.Log import Log
class user:
    log=Log()
    def __init__(self,phone,pwd):
        global d
        # 连接手机
        d = u2.connect("192.168.130.212")
        # # 启动app
        d.app_start("com.baofengpudgeapp")
        sleep(2)
        self.phone=phone
        self.password=pwd
    # 通过我的注册
    def regist(self,vericode):
        self.vericode=vericode
        d(text=u"我的").click()
        # 等待元素出现
        d(text=u"注册").wait(timeout=3)
        d(text=u"注册").click()
        d(text=u"请输入手机号码").wait(timeout=3)
        d(text=u"请输入手机号码").set_text(self.phone)
        d(text=u" 下一步 ").click()
        d(text=u"发送验证码").wait(timeout=3)
        try:
            assert d(text=u"发送验证码").exists
        except:
            print("手机号有误")
        else:
            d(text=u"发送验证码").click()
            d(text=u"请输入验证码").set_text(self.vericode)
            d(text=u"请输入登录密码").set_text(self.password)
            d(scrollable=True).scroll.to(text=u"完成")
            d(text=u" 完成 ").click()
            d(text=u"总资产(元)").wait(timeout=10)
            try:
                assert d(text=u"总资产(元)").exists
            except:
                print("注册失败")
                d.screenshot('regist.jpg')
            else:
                print("注册成功")


    # 通过我的登录
    def login(self):
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
            # 截屏
            d.screenshot('login.jpg')
        else:
            print("登录成功")
    # 通过充值去开户
    def openaccount(self,name,cardid,bankcardno,chargepass):
        self.name=name
        self.cardid=cardid
        self.bankcardno=bankcardno
        self.chargepass=chargepass
        d(text=u"充值").click()
        d(text=u"立即开通").click()
        d(text=u"请输入真实姓名").set_text(self.name)
        d(text=u"请输入身份证号").set_text(self.cardid)
        d(scrollable=True).scroll.to(text=u"下一步")
        d(text=u" 下一步 ").click()
        d(description=u"用户信息").wait(timeout=10)
        try:
            assert d(description=u"用户信息").exists
        except:
            self.log.error("已存在实名信息")
            d.screenshot('openaccount.jpg')
        else:
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
    # 通过我的去测评
    def ceping(self):
        # d(text=u"我的").click()
        # sleep(3)
        # # 点击输入手机号
        # d(text=u"请输入手机号码").set_text(self.phone)
        # d(text=u"请输入登录密码").set_text(self.password)
        # # 向上滑动
        # d(scrollable=True).scroll.to(text=u"登录")
        # d(text=u" 登录 ").click()
        # sleep(3)
        # try:
        #     assert d(text=u"总资产(元)").exists
        # except:
        #     print("登录失败")
        # else:
        d(text=u"立即测评").click()
        d(className="android.widget.CheckBox").click()
        d(className="android.widget.CheckBox", instance=5).click()
        d.swipe(0.5, 0.8, 0.5, 0.35)
        d(className="android.widget.CheckBox", instance=4).click()
        d(className="android.widget.CheckBox", instance=8).click()
        d.swipe(0.5, 0.8, 0.5, 0.35)
        d(className="android.widget.CheckBox",instance=2).click()
        d(className="android.widget.CheckBox", instance=6).click()
        d.swipe(0.5, 0.8, 0.5, 0.35)
        d(className="android.widget.CheckBox",instance=3).click()
        d(className="android.widget.CheckBox", instance=7).click()
        d.swipe(0.5, 0.8, 0.5, 0.35)
        d(className="android.widget.CheckBox",instance=3).click()
        d(className="android.widget.CheckBox", instance=7).click()
        d.swipe(0.5, 0.8, 0.5, 0.35)
        d(className="android.widget.CheckBox",instance=4).click()
        d(className="android.widget.CheckBox", instance=8).click()
        d(scrollable=True).scroll.to(description=u"提交")
        d(description=u"提交").click()
        assert d(description=u"完成").exists
    # 通过我的充值
    def recharge(self,amount,tradepass):
        self.amount=amount
        self.tradepass=tradepass
        # d(text=u"我的").click()
        # d(text=u"请输入手机号码").wait(timeout=3)
        # # 点击输入手机号
        # d(text=u"请输入手机号码").set_text(self.phone)
        # d(text=u"请输入登录密码").set_text(self.password)
        # # 向上滑动
        # d(scrollable=True).scroll.to(text=u"登录")
        # d(text=u" 登录 ").click()
        # d(text=u"总资产(元)").wait(timeout=3)
        # try:
        #     assert d(text=u"总资产(元)").exists
        # except:
        #     print("登录失败")
        # else:
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
    def withdraw(self,amount,tradepass):
        self.tradepass=tradepass
        self.amount = amount
        # d(text=u"我的").click()
        # d(text=u"请输入手机号码").wait(timeout=3)
        # # 点击输入手机号
        # d(text=u"请输入手机号码").set_text(self.phone)
        # d(text=u"请输入登录密码").set_text(self.password)
        # # 向上滑动
        # d(scrollable=True).scroll.to(text=u"登录")
        # d(text=u" 登录 ").click()
        # d(text=u"总资产(元)").wait(timeout=3)
        # try:
        #     assert d(text=u"总资产(元)").exists
        # except:
        #     print("登录失败")
        # else:
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
            print("提现金额有误")
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
            # 关闭app
    # 通过我的修改登录密码
    def modify_pass(self,newpass,renewpas):
        self.newpass=newpass
        self.renewpass=renewpas
        # d(text=u"我的").click()
        # d(text=u"请输入手机号码").wait(timeout=3)
        # # 点击输入手机号
        # d(text=u"请输入手机号码").set_text(self.phone)
        # d(text=u"请输入登录密码").set_text(self.password)
        # # 向上滑动
        # d(scrollable=True).scroll.to(text=u"登录")
        # d(text=u" 登录 ").click()
        # d(text=u"总资产(元)").wait(timeout=3)
        # try:
        #     assert d(text=u"总资产(元)").exists
        # except:
        #     print("登录失败")
        # else:
        # 点击设置按钮
        d.click(0.919, 0.085)
        d(text=u"密码管理").click()
        d(text=u"修改登录密码").click()
        d(text=u"请输入登录密码").set_text(self.password)
        d(text=u"请输入新登录密码").set_text(self.newpass)
        d(text=u"请再次输入新登录密码").set_text(self.renewpass)
        d(text=u"提交").click()
        try:
            d(text=u"好的").wait(timeout=3)
        except:
            print("重置失败")
        else:
            print("重置成功")
            d(text=u"好的").click()
    # 通过我的修改交易密码-记得原交易密码
    def modify_tradepass(self,oldtradepass,newtradepass,vericode):
        self.oldtradepass=oldtradepass
        self.newtradepass=newtradepass
        self.vericode=vericode
        # d(text=u"我的").click()
        # d(text=u"请输入手机号码").wait(timeout=3)
        # # 点击输入手机号
        # d(text=u"请输入手机号码").set_text(self.phone)
        # d(text=u"请输入登录密码").set_text(self.password)
        # # 向上滑动
        # d(scrollable=True).scroll.to(text=u"登录")
        # d(text=u" 登录 ").click()
        # d(text=u"总资产(元)").wait(timeout=3)
        # try:
        #     assert d(text=u"总资产(元)").exists
        # except:
        #     print("登录失败")
        # else:
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


    # 从我的页面退出登录
    def exitlogin(self):
        # 点击设置按钮
        d.click(0.919, 0.085)
        d(text=u"退出登录").click()
        d(text=u"退出").wait(timeout=3)
        d(text=u"退出").click()
        d(text=u"首页").wait(timeout=3)
        try:
            assert d(text=u"首页").exists
        except:
            self.log.error("退出失败")
            d.screenshot('exit.jpg')
        else:
            self.log.info("退出成功")

    # 关闭app
    def close(self):
        d.app_stop("com.baofengpudgeapp")
if __name__=='__main__':
    test=user('14711234517','bf1111')
    test.login()
    # test.regist('111111')
    # test.openaccount('阿花','640000198204150090','6228485883951848408','111111')
    # test.login()
    # test.exitlogin()
    # test.ceping()
    # test.modify_tradepass('123456','111111','111111')
    # test.recharge('1000','111111')
    # test.withdraw('100','111111')
    # test.close()
    # test.modify_pass('bf1111','bf1111')