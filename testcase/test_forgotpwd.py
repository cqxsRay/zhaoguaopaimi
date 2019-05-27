import unittest
import method
from common import configHttp
content=configHttp.ConfigHttp()
class testzgp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("注册用例开始执行\n")
    def setUp(self):
        print("单条用例执行开始")
    def test01(self):
        user=method.forgotpwd('14711234501','111111','111111')
        self.assertEqual('00000000',user['status'],msg="所有信息均正确，应该成功")
    def test02(self):
        user = method.forgotpwd('14711234501', '111111', '123456')
        self.assertEqual('20002018',user['status'],msg="两次密码不一样")
    def test03(self):
        user = method.forgotpwd('14711234506', '111111', '111111')
        self.assertEqual('20002019',user['status'],msg="未注册用户重置")
    def tearDown(self):
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        print("注册用例执行结束")

