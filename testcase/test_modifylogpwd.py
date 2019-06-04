import unittest
# import method
import nomi as method
class TestModifypwd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # log.info("登录用例执行开始")
        print("修改登录密码用例开始执行\n")
    def setUp(self):
        # log.info("单条用例执行开始")
        print("单条用例执行开始")
    def test1(self):
        user = method.modifypwd('14711234501','111111','111111')
        self.assertEqual('00000000',user['status'],  msg="所有信息均正确")
    def test2(self):
        user = method.modifypwd('14711234501','111111','123456','436436')
        self.assertEqual('20002014',user['status'], msg="短信验证码不对")
    def test3(self):
        user = method.modifypwd('14711234501','111111','123456','')
        self.assertEqual('00000009',user['status'], msg="短信验证码为空")
    def tearDown(self):
        # log.info("单条用例执行结束")
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        # log.info("登录用例执行结束")
        print("修改登录密码用例执行结束")

if __name__=='__main__':
    # 方法1：执行所有的测试
    unittest.main()

