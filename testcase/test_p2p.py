import unittest
from testfile.selenium import P2P
from common import getexcel
user=getexcel.read_xls("fortest.xlsx","fortest").dict_xls()
class testp2p(unittest.TestCase):
    def setUp(self):
        print("start")
    # def test_regist(self):
    #     per=P2P.user(user[0]['phone'],user[0]['password'])
    #     self.assertEqual(per.regist(),user[0]['msg'])
    # def test_regist2(self):
    #     per=P2P.user(user[1]['phone'],user[1]['password'])
    #     self.assertEqual(per.regist(),user[1]['msg'])
    #     per.close()
    # def test_regist3(self):
    #     per=P2P.user(user[2]['phone'],user[2]['password'])
    #     self.assertEqual(per.regist(),user[2]['msg'])
    #     per.close()
    def test_login(self):
        per = P2P.user(user[3]['phone'], user[3]['password'])
        self.assertEqual(per.login(), user[3]['msg'])
    def test_charge(self):
        per = P2P.user(user[4]['phone'], user[4]['password'])
        self.assertEqual(per.charge("100","123456"), user[4]['msg'])
    def tearDown(self):
        print("end")


if __name__=='__main__':
    # 方法1：执行所有的测试
    unittest.main()


