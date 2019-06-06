import unittest
import time
# import method
import graphcode as method
from common import configDB
person = configDB.MyDB()
class TestTx(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("图形验证码登录用例开始执行\n")
        cls.gr = person.get_one("SELECT * FROM user_basic WHERE user_type=1 AND mobile LIKE '1471123%'")
        cls.qy = person.get_one("SELECT * FROM user_basic WHERE user_type=2 AND mobile LIKE '1471123%'")
    def setUp(self):
        print("单条用例执行开始")
    def test1(self):
        '''企业用户图形验证码登录'''
        user=method.login3(self.qy['mobile'], '111111', 2)
        self.assertEqual('00000000',user['status'])
    def test2(self):
        '''个人图形验证码登录'''
        user=method.login3(self.gr['mobile'], '111111')
        self.assertEqual('00000000',user['status'])
    def tearDown(self):
        print("单条用例执行结束")

    @classmethod
    def tearDownClass(cls):
        print("图形验证码登录用例执行结束")
        person.closeDB()
        time.sleep(10)

# if __name__=='__main__':
#     unittest.main()
