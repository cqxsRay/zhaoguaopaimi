import unittest
# import method
import nomi as method
from common import generator
from common import configDB
person = configDB.MyDB()
class TestPercerty(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("认证用例开始执行\n")
        cls.gr = person.get_one("SELECT * FROM user_basic WHERE user_type=1 AND certificate_status=1 AND mobile LIKE '1471123%'")
    def setUp(self):
        print("单条用例执行开始")
    def test6(self):
        '''个人认证所有信息均正确'''
        user=method.personcertify(self.gr['mobile'],'111111','622609',generator.createbankid(),'招商银行',self.gr['mobile'],
                                  generator.createidcard(),generator.realname(),'34354365465@qq.com',
                                  '详细地址达到噶收到哥哥3的爱国啊郭德纲','北京','北京','中国')
        self.assertEqual(user['status'],'00000000')

    def test2(self):
        '''银行卡号不符合规则'''
        user = method.personcertify(self.gr['mobile'],'111111','622609','456756789', '招商银行',
                                    self.gr['mobile'],generator.createidcard(), generator.realname(), '34354365465@qq.com',
                                    '详细地址达到噶收到哥哥3的爱国啊郭德纲', '北京', '北京', '中国')
        self.assertEqual('20002010',user['status'])

    def test3(self):
        '''真实姓名不符合规则'''
        user = method.personcertify(self.gr['mobile'], '111111', '622609', generator.createbankid(), '招商银行',
                                    self.gr['mobile'],generator.createidcard(),'retery1', '34354365465@qq.com',
                                    '详细地址达到噶收到哥哥3的爱国啊郭德纲', '北京', '北京', '中国')
        self.assertEqual('00000009', user['status'])
    def test4(self):
        '''身份证号不符合规则'''
        user = method.personcertify(self.gr['mobile'], '111111', '622609', generator.createbankid(), '招商银行',
                                    self.gr['mobile'], '345686787687', generator.realname(), '34354365465@qq.com',
                                    '详细地址达到噶收到哥哥3的爱国啊郭德纲', '北京', '北京', '中国')
        self.assertEqual('00000009', user['status'])
    def test5(self):
        '''邮箱不符合规则'''
        user = method.personcertify(self.gr['mobile'], '111111', '622609', generator.createbankid(), '招商银行',
                                    self.gr['mobile'],generator.createidcard(), generator.realname(), '34354365',
                                    '详细地址达到噶收到哥哥3的爱国啊郭德纲', '北京', '北京', '中国')
        self.assertEqual('00000009', user['status'])
    def tearDown(self):
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        person.closeDB()
        print("认证用例执行结束")

# if __name__=='__main__':
#     unittest.main()

