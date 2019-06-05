import unittest
# import method
import nomi as method
from common import configDB
person = configDB.MyDB()
class TestModifypwd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("修改登录密码用例开始执行\n")
        cls.gr = person.get_one("SELECT * FROM user_basic WHERE user_type=1 AND mobile LIKE '1471123%'")
        cls.qy = person.get_one("SELECT * FROM user_basic WHERE user_type=2 AND mobile LIKE '1471123%'")
    def setUp(self):
        print("单条用例执行开始")
    def test1(self):
        '''个人用户修改登录密码'''
        user = method.modifypwd(self.gr['mobile'],'111111','111111')
        self.assertEqual('00000000',user['status'])
    def test2(self):
        '''短信验证码不对'''
        user = method.modifypwd(self.gr['mobile'],'111111','123456',1,'436436')
        self.assertEqual('20002014',user['status'])
    def test3(self):
        '''短信验证码为空'''
        user = method.modifypwd(self.gr['mobile'],'111111','123456',1,'')
        self.assertEqual('00000009',user['status'])
    def test4(self):
        '''企业用户修改登录密码'''
        user = method.modifypwd(self.qy['mobile'],'111111','111111',2)
        self.assertEqual('00000000',user['status'])
    def tearDown(self):
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        print("修改登录密码用例执行结束")

if __name__=='__main__':
    # 方法1：执行所有的测试
    unittest.main()

