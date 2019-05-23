import unittest
import method
from common import generator
class testzpg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # log.info("登录用例执行开始")
        print("认证用例开始执行\n")
    def setUp(self):
        # log.info("单条用例执行开始")
        print("单条用例执行开始")
    def test_certify1(self):
        user=method.personcertify('14711234502','111111','详细地址达到噶收到哥哥3的爱国啊郭德纲',
              generator.createbankid(),'622609','招商银行','14711234502',generator.createidcard(),'北京','中国',
              '34354365465@qq.com','山东',generator.name())
        self.assertEqual(user['status'],'00000000',msg="所有信息均正确，应该认证成功")

    def tearDown(self):
        # log.info("单条用例执行结束")
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        # log.info("登录用例执行结束")
        print("认证用例执行结束")

if __name__=='__main__':
    # 方法1：执行所有的测试
    unittest.main()

