import unittest
# import method
import nomi as method
from common import generator as g
from common import configHttp
content=configHttp.ConfigHttp()
class TestRegist(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("注册用例开始执行\n")
    def setUp(self):
        print("单条用例执行开始")
    def test01(self):
        '''个人用户注册'''
        user=method.regist(g.name(),g.createPhone(),'111111','111111')
        self.assertEqual('00000000',user['status'])
    def test02(self):
        '''企业用户注册'''
        user = method.regist(g.name(), g.createPhone(), '111111', '111111', 2)
        self.assertEqual('00000000',user['status'])
    def test03(self):
        '''两次密码不一致注册'''
        user=method.regist(g.name(),g.createPhone(),'123456','111111')
        self.assertEqual('00000019',user['status'])
    def test04(self):
        '''手机号已存在注册'''
        user=method.regist(g.name(),'14711234502','111111','111111')
        self.assertEqual('20002022',user['status'])
    def test05(self):
        '''用户名已存在注册'''
        user=method.regist('yuan',g.createPhone(),'111111','111111')
        self.assertEqual('20002021',user['status'])
    def test06(self):
        '''验证码不对注册'''
        user=method.regist(g.name(),g.createPhone(),'111111','111111',1,'989777')
        self.assertEqual('20002004',user['status'])
    def test07(self):
        '''手机号格式不正确注册'''
        user=method.regist(g.name(),'1471123450','111111','111111')
        self.assertEqual('00000009',user['status'])
    def test08(self):
        '''确认密码为空注册'''
        user=method.regist(g.name(),g.createPhone(),'111111','')
        self.assertEqual('00000009',user['status'])
    def test09(self):
        '''密码为空注册'''
        user=method.regist(g.name(),g.createPhone(),'','111111')
        self.assertEqual('00000009',user['status'])

    def tearDown(self):
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        print("注册用例执行结束")

# if __name__=='__main__':
#     # 方法1：执行所有的测试
#     unittest.main()

