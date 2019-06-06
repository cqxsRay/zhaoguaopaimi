import unittest
import time
# import method
import nomi as method
from common import generator
from common import configDB
person = configDB.MyDB()
class TestModifymobile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("修改绑定手机号用例开始执行\n")
        cls.gr = person.get_one("SELECT * FROM user_basic WHERE user_type=1 AND mobile LIKE '1471123%'")
        cls.qy= person.get_one("SELECT * FROM user_basic WHERE user_type=2 AND mobile LIKE '1471123%'")
    def setUp(self):
        print("单条用例执行开始")
    def test1(self):
        '''短信验证码不对'''
        user = method.modifymobile(self.gr['mobile'],'111111',generator.createPhone(),1,'436436')
        self.assertEqual('20002014',user['status'])
    def test2(self):
        '''短信验证码为空'''
        user = method.modifymobile(self.gr['mobile'],'111111',generator.createPhone(),1,'')
        self.assertEqual('00000009',user['status'])
    # 有bug，待修复
    # def test3(self):
    #     '''新手机号格式不对'''
    #     user = method.modifymobile(self.gr['mobile'],'111111','147112345')
    #     self.assertEqual('00000009',user['status'])
    # 有bug,待修复
    # def test4(self):
    #     '''新手机号为已注册手机号'''
    #     user = method.modifymobile(self.gr['mobile'],'111111','14711234502')
    #     self.assertEqual('00000009',user['status'])
    # tddo 仅审核过或者审核驳回的可以修改
    # def test5(self):
    #     '''企业用户修改手机号'''
    #     user = method.modifymobile(self.qy['mobile'],'111111',generator.createPhone(),2)
    #     self.assertEqual('00000000',user['status'])
    def test6(self):
        '''个人用户修改手机号'''
        user = method.modifymobile(self.gr['mobile'],'111111',generator.createPhone())
        self.assertEqual('00000000',user['status'])
    def tearDown(self):
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        print("修改绑定手机号用例执行结束")
        person.closeDB()
        time.sleep(10)


# if __name__=='__main__':
#     unittest.main()

