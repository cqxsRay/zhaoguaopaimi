import unittest
# import method
import nomi as method
from common import configHttp
content=configHttp.ConfigHttp()
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("登录用例开始执行\n")
    def setUp(self):
        print("单条用例执行开始")

    def test1(self):
        ''' 手机号密码均正确，个人登录'''
        user = method.login('14711234500', '111111')
        self.assertEqual('00000000',user['status'])
    def test2(self):
        ''' 登录密码错误，应该登录失败'''
        user=method.login('14711234500','11')
        self.assertEqual('20002005',user['status'])
    def test3(self):
        '''手机号格式错误登录'''
        user = method.login('1471123450', '111111')
        self.assertEqual('20002002',user['status'])
    def test4(self):
        '''未注册用户登录'''
        user = method.login('14711234587', '111111')
        self.assertEqual('20002002',user['status'])
    def test5(self):
        '''密码为空登录'''
        user = method.login('14711234501', '')
        self.assertEqual('00000009',user['status'])
    def test6(self):
        '''企业用户登录'''
        user = method.login('14711234560', '123456',2)
        self.assertEqual('00000000',user['status'])
    def test7(self):
        '''手机号用户名为空登录'''
        user = method.login('', '111111')
        self.assertEqual('00000009',user['status'])
    def test8(self):
        '''个人退出登录'''
        user = method.logout('14711234500', '111111')
        self.assertEqual('00000000', user['status'])
    def test9(self):
        '''企业退出登录'''
        user = method.logout('14711234560', '123456', 2)
        self.assertEqual('00000000', user['status'])
    def tearDown(self):
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        print("登录用例执行结束")

# if __name__=='__main__':
#     # 方法1：执行所有的测试
#     unittest.main()

