import unittest
# import method
import nomi as method
import graphcode
from common import configHttp
content=configHttp.ConfigHttp()
class TestTx(unittest.TestCase):
    def test1(self):
        for i in range(3):
            method.login('14711238651','123456',2)
            i+=1
        user1=graphcode.login3('14711238651', '111111', 2)
        self.assertEqual('00000000',user1['status'], msg="企业，图形验证码登录")
    def test2(self):
        i=0
        while i <3:
            method.login('14711231860','123456')
            i+=1
        user2=graphcode.login3('14711231860', '111111')
        self.assertEqual('00000000',user2['status'], msg="个人，图形验证码登录")
#
# if __name__=='__main__':
#     # 方法1：执行所有的测试
#     unittest.main()
