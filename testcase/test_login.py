import unittest
# import method
import nomi as method
from common import configHttp
content=configHttp.ConfigHttp()
# from common import getexcel
# user=getexcel.read_xls("test.xlsx","Sheet1").dict_xls()
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # log.info("登录用例执行开始")
        print("登录用例开始执行\n")
    def setUp(self):
        # log.info("单条用例执行开始")
        print("单条用例执行开始")

    def test1(self):
        ''' 手机号密码均正确，个人登录'''
        user = method.login('14711234500', '111111')
        self.assertEqual('00000000',user['status'], msg="手机号密码均正确，个人登录")
    def test2(self):
        ''' 登录密码错误，应该登录失败'''
        user=method.login('14711234500','11')
        self.assertEqual('20002005',user['status'],msg="登录密码错误，应该登录失败")
    def test3(self):
        '''手机号格式错误登录'''
        user = method.login('1471123450', '111111')
        self.assertEqual('20002002',user['status'], msg="手机号格式错误登录")
    def test4(self):
        '''未注册用户登录'''
        user = method.login('14711234587', '111111')
        self.assertEqual('20002002',user['status'], msg="未注册用户登录")
    def test5(self):
        '''密码为空登录'''
        user = method.login('14711234501', '')
        self.assertEqual('00000009',user['status'], msg="密码为空登录")
    def test6(self):
        '''手机号密码均正确，企业登录'''
        user = method.login('14711234560', '123456',2)
        self.assertEqual('00000000',user['status'],  msg="手机号密码均正确，企业登录")
    def test7(self):
        '''手机号用户名为空登录'''
        user = method.login('', '111111')
        self.assertEqual('00000009',user['status'], msg="手机号用户名为空登录")
    def test8(self):
        '''个人退出登录'''
        user = method.logout('14711234500', '111111')
        self.assertEqual('00000000', user['status'], msg="个人退出登录")
    def test9(self):
        '''企业退出登录'''
        user = method.logout('14711234560', '123456', 2)
        self.assertEqual('00000000', user['status'], msg="企业退出登录")
    def tearDown(self):
        # log.info("单条用例执行结束")
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        # log.info("登录用例执行结束")
        print("登录用例执行结束")

# if __name__=='__main__':
#     # 方法1：执行所有的测试
#     unittest.main()

