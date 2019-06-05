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
        '''个人忘记登录密码'''
        user=method.forgotpwd('14711234501','111111','111111')
        self.assertEqual('00000000',user['status'])
    def test02(self):
        '''两次密码不一样'''
        user = method.forgotpwd('14711234501', '111111', '123456')
        self.assertEqual('20002018',user['status'],msg="两次密码不一样")
    def test04(self):
        '''图形验证码为空'''
        user = method.forgotpwd('14711234501','111111','111111','000000', 1,'')
        self.assertEqual('20001001',user['status'])
    def test05(self):
        '''图形验证码不对'''
        user = method.forgotpwd('14711234501', '111111', '111111', '000000',1,'453465')
        self.assertEqual('20002014',user['status'])
    def test06(self):
        '''短信验证码不对'''
        user = method.forgotpwd('14711234501', '111111', '111111', '0768575')
        self.assertEqual('20002004',user['status'])
    def test07(self):
        '''短信验证码为空'''
        user = method.forgotpwd('14711234501', '111111', '111111', '')
        self.assertEqual('20001001',user['status'])
    def test08(self):
        '''新密码为空'''
        user = method.forgotpwd('14711234501', '111111', '')
        self.assertEqual('20001001',user['status'])
    def test09(self):
        '''企业忘记登录密码'''
        user=method.forgotpwd('14711234520','111111','111111','000000',2)
        self.assertEqual('00000000',user['status'])
    def tearDown(self):
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        print("忘记登录密码用例执行结束")
if __name__=='__main__':
    # 方法1：执行所有的测试
    unittest.main()

