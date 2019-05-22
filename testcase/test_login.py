import unittest
import method
from common import configHttp
content=configHttp.ConfigHttp()
# from common import getexcel
# user=getexcel.read_xls("test.xlsx","Sheet1").dict_xls()
class testzpg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # log.info("登录用例执行开始")
        print("登录用例开始执行\n")
    def setUp(self):
        # log.info("单条用例执行开始")
        print("单条用例执行开始")
    def test_login1(self):
        user = method.login('14711234500', '123456')
        self.assertEqual(user['status'], '00000000', msg="手机号密码均正确，应该登录成功")
    def test_login2(self):
        user=method.login('14711234500','111111')
        self.assertEqual(user['status'],'20002005',msg="登录密码错误，应该登录失败")
    def test_login3(self):
        user = method.login('14711234506', '111111')
        self.assertEqual(user['status'], '20002002', msg="未注册用户登录")
    def tearDown(self):
        # log.info("单条用例执行结束")
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        # log.info("登录用例执行结束")
        print("登录用例执行结束")

if __name__=='__main__':
    # 方法1：执行所有的测试
    unittest.main()

