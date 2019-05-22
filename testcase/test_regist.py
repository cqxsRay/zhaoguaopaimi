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
        print("注册用例开始执行\n")
    def setUp(self):
        # log.info("单条用例执行开始")
        print("单条用例执行开始")
    def test_regist1(self):
        user=method.regist('yuan3','14711234502','111111','111111')
        self.assertEqual(user['status'],'00000000',msg="正常用户注册")
    def test_regist2(self):
        user=method.regist('yuan3','14711234503','123456','111111')
        self.assertEqual(user['status'],'00000019',msg="两次密码不对注册")
    def test_regist3(self):
        user=method.regist('yuan3','14711234502','111111','111111')
        self.assertEqual(user['status'],'20002021',msg="已注册用户注册")
    def tearDown(self):
        # log.info("单条用例执行结束")
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        # log.info("登录用例执行结束")
        print("注册用例执行结束")

if __name__=='__main__':
    # 方法1：执行所有的测试
    unittest.main()

