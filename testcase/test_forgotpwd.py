import unittest
# import method
from common import configHttp
content=configHttp.ConfigHttp()
import graphcode as method

class TestForgotpwd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("忘记登录密码用例开始执行\n")
    def setUp(self):
        print("单条用例执行开始")
    def test01(self):
        user=method.forgotpwd('14711239056','111111','111111')
        self.assertEqual('00000000',user['status'],msg="个人用户所有信息均正确")
    def test02(self):
        user = method.forgotpwd('14711239056', '111111', '123456')
        self.assertEqual('20002018',user['status'],msg="两次密码不一样")
    def test04(self):
        user = method.forgotpwd('14711239056','111111','111111','000000', 1,'')
        self.assertEqual('20001001',user['status'], msg="图形验证码为空")
    def test05(self):
        user = method.forgotpwd('14711239056', '111111', '111111', '000000',1,'453465')
        self.assertEqual('20002014',user['status'],msg="图形验证码不对")
    def test06(self):
        user = method.forgotpwd('14711239056', '111111', '111111', '0768575')
        self.assertEqual('20002004',user['status'],msg="短信验证码不对")
    def test07(self):
        user = method.forgotpwd('14711239056', '111111', '111111', '')
        self.assertEqual('20001001',user['status'],msg="短信验证码为空")
    def test08(self):
        user = method.forgotpwd('14711239056', '111111', '')
        self.assertEqual('20001001',user['status'],msg="新密码为空")
    def test09(self):
        user=method.forgotpwd('14711239604','111111','111111','000000',2)
        self.assertEqual('00000000',user['status'],msg="企业所有信息均正确")
    def tearDown(self):
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        print("忘记登录密码用例执行结束")
if __name__=='__main__':
    # 方法1：执行所有的测试
    unittest.main()

