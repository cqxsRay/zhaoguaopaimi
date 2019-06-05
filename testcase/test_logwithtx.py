import unittest
# import method
import nomi as method
import graphcode
from common import configHttp
content=configHttp.ConfigHttp()
class TestTx(unittest.TestCase):
    def test1(self):
        '''企业用户图形验证码登录'''
        for i in range(3):
            method.login('14711238651','123456',2)
            i+=1
        user1=graphcode.login3('14711238651', '111111', 2)
        self.assertEqual('00000000',user1['status'])
    def test2(self):
        '''个人，图形验证码登录'''
        i=0
        while i <3:
            method.login('14711234505','123456')
            i+=1
        user2=graphcode.login3('14711234505', '111111')
        self.assertEqual('00000000',user2['status'])

# if __name__=='__main__':
#     # 方法1：执行所有的测试
#     unittest.main()
