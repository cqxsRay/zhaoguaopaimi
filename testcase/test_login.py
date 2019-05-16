# 这个是接口自动化测试用例的模版
import unittest
from common import getexcel
from common import configHttp
from common import Log
content=configHttp.ConfigHttp()
log=Log.Log()
user=getexcel.read_xls("test.xlsx","Sheet1").dict_xls()
class testp2p(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # log.info("登录用例执行开始")
        print("登录用例开始执行\n")
    def setUp(self):
        # log.info("单条用例执行开始")
        print("单条用例执行开始")
    def test_login(self):
        content.set_url(user[0]['url'])
        content.set_data(user[0]['data'])
        self.assertEqual(str(content.post().json()), user[0]['message'])
    # def test_login2(self):
    #     content.set_url(user[1]['url'])
    #     content.set_data(user[1]['data'])
    #     self.assertEqual(str(content.post().json()), user[1]['message'])
    def tearDown(self):
        # log.info("单条用例执行结束")
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        # log.info("登录用例执行结束")
        print("登录用例执行结束")

# if __name__=='__main__':
#     # 方法1：执行所有的测试
#     unittest.main()

