import unittest
# import method
import nomi as method
class TestModifymobile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # log.info("登录用例执行开始")
        print("修改绑定手机号用例开始执行\n")
    def setUp(self):
        # log.info("单条用例执行开始")
        print("单条用例执行开始")
    def test1(self):
        # 这个参数从库里区用户
        user = method.modifymobile('14711239056','111111','14711234507')
        self.assertEqual('00000000',user['status'],  msg="所哟信息均正确")
    def test2(self):
        user = method.modifymobile('14711234502','111111','14711234609','436436')
        self.assertEqual('20002014',user['status'], msg="短信验证码不对")
    def test3(self):
        user = method.modifymobile('14711234501','111111','14711234543','')
        self.assertEqual('00000009',user['status'], msg="短信验证码为空")
    def test4(self):
        user = method.modifymobile('14711234501','111111','147112345')
        self.assertEqual('00000009',user['status'], msg="新手机号格式不对")
    def test5(self):
        user = method.modifymobile('14711234501','111111','14711234502')
        self.assertEqual('00000009',user['status'], msg="新手机号为已注册手机号")
    def tearDown(self):
        # log.info("单条用例执行结束")
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        # log.info("登录用例执行结束")
        print("修改绑定手机号用例执行结束")

if __name__=='__main__':
    # 方法1：执行所有的测试
    unittest.main()

