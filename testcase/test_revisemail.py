import unittest
import method
from common import configHttp
content=configHttp.ConfigHttp()
class testzpg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # log.info("登录用例执行开始")
        print("修改绑定邮箱用例开始执行\n")
    def setUp(self):
        # log.info("单条用例执行开始")
        print("单条用例执行开始")
    def test_revisemail1(self):
        user=method.revisemail('14711234502','111111','65786@11.com','newmai1@139.com')
        self.assertEqual('00000000',user['status'],msg="所有信息均正确")
    # todo
    def test_revisemail2(self):
        user=method.revisemail('14711234502','111111','6657568@11.com','9998@139.com')
        self.assertEqual('00000001',user['status'],msg="原邮箱不对")
    def tearDown(self):
        # log.info("单条用例执行结束")
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        # log.info("登录用例执行结束")
        print("修改绑定邮箱用例执行结束\n")

if __name__=='__main__':
    # 方法1：执行所有的测试
    unittest.main()

