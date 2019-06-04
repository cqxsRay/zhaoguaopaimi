import unittest
# import method
import nomi as method
from common import generator
class TestPercerty(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # log.info("登录用例执行开始")
        print("认证用例开始执行\n")
    def setUp(self):
        # log.info("单条用例执行开始")
        print("单条用例执行开始")
    def test1(self):
        '''所有信息均正确'''
        # 这个用户从库里取待认证待用户
        user=method.personcertify('14711234500','111111','详细地址达到噶收到哥哥3的爱国啊郭德纲',
              generator.createbankid(),'622609','招商银行','14711234500',generator.createidcard(),'北京','中国',
              '34354365465@qq.com','山东',generator.realname())
        self.assertEqual(user['status'],'00000000')

    def test2(self):
        '''银行卡号不符合规则'''
        # 这个用户从库里取待认证待用户
        user=method.personcertify('14711234500','111111','详细地址达到噶收到哥哥3的爱国啊郭德纲',
              '436456457','622609','招商银行','14711234502',generator.createidcard(),'北京','中国',
              '34354365465@qq.com','山东',generator.realname())
        self.assertEqual('20002010',user['status'])

    def test3(self):
        '''真实姓名不符合规则'''
        user = method.personcertify('14711234500', '111111', '详细地址达到噶收到哥哥3的爱国啊郭德纲',
                                    generator.createbankid(), '622609', '招商银行', '14711234502', generator.createidcard(), '北京', '中国',
                                    '34354365465@qq.com', '山东', '4354dd')
        self.assertEqual('00000009', user['status'])
    def test4(self):
        '''身份证号不符合规则'''
        user = method.personcertify('14711234500', '111111', '详细地址达到噶收到哥哥3的爱国啊郭德纲',
                                    generator.createbankid(), '622609', '招商银行', '14711234502', '32345678', '北京', '中国',
                                    '34354365465@qq.com', '山东', generator.realname())
        self.assertEqual('00000009', user['status'])
    def test5(self):
        '''邮箱不符合规则'''
        user = method.personcertify('14711234500', '111111', '详细地址达到噶收到哥哥3的爱国啊郭德纲',
                                    generator.createbankid(), '622609', '招商银行', '14711234502', generator.createidcard(), '北京', '中国',
                                    '34354', '山东', generator.realname())
        self.assertEqual('00000009', user['status'])
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

