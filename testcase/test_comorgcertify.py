import unittest
# import method
import nomi as method
from common import generator
from common import configDB
person = configDB.MyDB()
class testzpg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("企业认证用例开始执行\n")
        # cls.qy = person.get_one("SELECT * FROM user_basic WHERE user_type=2 AND certificate_status=1 AND mobile LIKE '1471123%'")
    def setUp(self):
        print("单条用例执行开始")
    def test1(self):
        '''国有企业认证'''
        qy = person.get_one( "SELECT * FROM user_basic WHERE user_type=2 AND certificate_status=1 AND mobile LIKE '1471123%'")
        user=method.companycertify(qy['mobile'],'111111',generator.createidcard(),'联系人姓名','345@qq.com',
                                   '地址9号公寓楼8801德国大使馆的时光','city北京','pro北京','country中国',
                                   '法人真实姓名',generator.createidcard(),'机构名称',
                                   '100000000','经营范围：服装','社会统一信用码',2,'委托证书存储地址','营业执照存储地址')
        self.assertEqual('00000000',user['status'])

    def test2(self):
        '''非国有企业认证'''
        qy = person.get_one("SELECT * FROM user_basic WHERE user_type=2 AND certificate_status=1 AND mobile LIKE '1471123%'")
        user = method.companycertify(qy['mobile'], '111111', generator.createidcard(), '联系人姓名', '345@qq.com',
                                     '地址9号公寓楼8801德国大使馆的时光', 'city北京', 'pro北京', 'country中国',
                                     '法人真实姓名', generator.createidcard(), '机构名称',
                                     '100000000', '经营范围：服装', '社会统一信用码',3, '委托证书存储地址', '营业执照存储地址')
        self.assertEqual('00000000',user['status'])
    def test3(self):
        '''国有企业认证修改'''
        qy = person.get_one("SELECT * FROM user_basic WHERE user_type=2 AND certificate_status=3 AND mobile LIKE '1471123%'")
        user = method.companycermodi(qy['mobile'], '111111', generator.createidcard(), '联系人姓名', '345@qq.com',
                                     '地址9号公寓楼8801德国大使馆的时光', 'city北京', 'pro北京', 'country中国',
                                     '法人真实姓名', generator.createidcard(), '机构名称',
                                     '100000000', '经营范围：服装', '社会统一信用码', 2, '委托证书存储地址', '营业执照存储地址')
        self.assertEqual('00000000',user['status'])
    def test4(self):
        '''非国有企业认证修改'''
        qy = person.get_one("SELECT * FROM user_basic WHERE user_type=2 AND certificate_status=3 AND mobile LIKE '1471123%'")
        user = method.companycermodi(qy['mobile'], '111111', generator.createidcard(), '修改后联系人姓名', '修改后345@qq.com',
                                     '修改后地址9号公寓楼8801德国大使馆的时光', 'city北京', 'pro北京', 'country中国',
                                     '法人真实姓名', generator.createidcard(), '机构名称',
                                     '100000000', '修改后经营范围：服装', '社会统一信用码', 3, '委托证书存储地址', '营业执照存储地址')
        self.assertEqual('00000000',user['status'])
    def test5(self):
        '''政府机构认证'''
        qy = person.get_one( "SELECT * FROM user_basic WHERE user_type=2 AND certificate_status=1 AND mobile LIKE '1471123%'")
        user=method.orgcertify(qy['mobile'],'111111','法人','法人身份证号','机构名称','地址9号公寓楼8801德国大使馆的时光',
                               '北京','北京','中国','练练','345@qq.com')
        self.assertEqual('00000000',user['status'])
    def test6(self):
        '''政府机构认证修改'''
        qy = person.get_one("SELECT * FROM user_basic WHERE user_type=2 AND certificate_status=3 AND mobile LIKE '1471123%'")
        user = method.orgcermodi(qy['mobile'], '111111', '修改后法人', '修改后法人身份证号', '机构名称', '修改后地址9号公寓楼8801德国大使馆的时光',
                                 '北京', '北京', '中国', '练练', '345@qq.com')
        self.assertEqual('00000000',user['status'])
    def test7(self):
        '''查询企业用户认证信息'''
        qy = person.get_one("SELECT * FROM user_basic WHERE user_type=2 AND mobile LIKE '1471123%'")
        user=method.checkcomcertify(qy['mobile'],'111111')
        self.assertEqual('00000000', user['status'])
    def test8(self):
        '''查询认证结果'''
        qy = person.get_one("SELECT * FROM user_basic WHERE user_type=2 AND mobile LIKE '1471123%'")
        user=method.checkcetify(qy['mobile'],'111111')
        self.assertEqual('00000000', user['status'])
    def tearDown(self):
        # person.closeDB()
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        person.closeDB()
        print("企业认证用例执行结束")

if __name__=='__main__':
    unittest.main()

