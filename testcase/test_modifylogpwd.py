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
        print("修改登录密码用例开始执行\n")
    def setUp(self):
        # log.info("单条用例执行开始")
        print("单条用例执行开始")
    def test_modify1(self):
        user = method.modifypwd('14711234500','111111','123456')
        self.assertEqual(user.json()['status'], '00000000', msg="手机号密码均正确，应该修改成功")
    # 其实这一条可以不需要，测试登录没有问题即可
    # def test_modify2(self):
    #     user = method.modifypwd('14711234500','123456','111111')
    #     self.assertEqual(user.json()['status'], '00000999', msg="登录密码不正确，应该修改失败")

    def test_modify2(self):
        user = method.modifypwd('14711234500', '123456', '123456')
        self.assertEqual(user.json()['status'], '00000000', msg="新密码同改之前的一样")
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

