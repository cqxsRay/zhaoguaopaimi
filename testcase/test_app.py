import unittest
import uiautomator2 as u2
from testfile.uiautomator import appfortest
from time import sleep

class testapp(unittest.TestCase):

    global d
    # 连接手机
    d = u2.connect("192.168.131.109")
    def setUp(self):
        # 启动app
        d.app_start("com.baofengpudgeapp")
        sleep(2)
        print("start")
    def test_regist1(self):
        regist1=appfortest.user('14711234500','bf1111')
        regist1.regist("111111")
        assert d(text=u"总资产(元)").exists
    # def test_login1(self):
    #     user1=appfortest.user('13456','bf1111')
    #     user1.login()
    #     # 用例的成功失败通过这个判断
    #     assert d(text=u"总资产(元)").exists
    def test_login2(self):
        user2=appfortest.user('14711234501','bf1111')
        user2.login()
        assert d(text=u"总资产(元)").exists
    def test_openaccount(self):
        open=appfortest.user('14711234501','bf1111')
        open.openaccount('name','cardid','bankcardno','chargepass')
        assert d(text=u"开户成功").exists
    def test_recharge(self):
        charge1=appfortest.user('14711234500','bf1111')
        charge1.recharge("1000","111111")
        assert d(text=u"查看充值记录").exists
    def test_widraw(self):
        withdraw1=appfortest.user('14711234500','bf1111')
        withdraw1.withdraw("1","111111")
        assert d(text=u"查看提现记录").exists
    def tearDown(self):
        d.app_stop("com.baofengpudgeapp")
        print("end")
if __name__=='__main__':
    unittest.main()