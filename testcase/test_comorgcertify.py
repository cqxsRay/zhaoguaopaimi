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
    def setUp(self):
        print("单条用例执行开始")
    def test1(self):
        '''国有企业认证'''
        user=method.companycertify('14711234520','111111','city北京','country北京','pro北京','地址9号公寓楼8801德国大使馆的时光','100000000','经营范围：服装',
              '真实姓名练练',generator.createidcard(),'法人真实姓名',generator.createidcard(),'社会统一信用码',2,'htth://www.ddgdg.com',
               'url:degregrdg','机构名称','345@qq.com')
        self.assertEqual('00000000',user['status'])

    def test2(self):
        '''非国有企业认证'''
        user=method.companycertify('14711234520','111111','city北京','country北京','pro北京','地址9号公寓楼8801德国大使馆的时光','100000000','经营范围：服装',
              '真实姓名练练',generator.createidcard(),'法人真实姓名',generator.createidcard(),'社会统一信用码',3,'htth://www.ddgdg.com',
               'url:degregrdg','机构名称','345@qq.com')
        self.assertEqual('00000000',user['status'])
    def test3(self):
        '''国有企业认证修改'''
        # 需要从数据库里获取可以修改的数据
        user=method.companycermodi('14711234520','111111','北京','北京','北京','地址9号公寓楼8801德国大使馆的时光','100000000','经营范围：服装',
              '练练',generator.createidcard(),'法人','3451234336','社会统一信用码',2,'htth://www.ddgdg.com',
               'url:degregrdg','机构名称','345@qq.com')
        self.assertEqual('00000000',user['status'])
    def test4(self):
        '''非国有企业认证修改'''
        # 需要从数据库里获取可以修改的数据（SELECT * FROM user_basic WHERE certificate_status=1 AND user_type=2 AND mobile LIKE '1471123%'）
        user=method.companycermodi('14711234520','111111','北京','北京','北京','地址9号公寓楼8801德国大使馆的时光','100000000','经营范围：服装','练练',generator.createidcard(),'法人','3451234336','社会统一信用码',3,'htth://www.ddgdg.com','url:degregrdg','机构名称','345@qq.com')
        self.assertEqual('00000000',user['status'])
    def test5(self):
        '''政府机构认证'''
        user=method.orgcertify('14711234461','111111','北京','北京','北京','地址9号公寓楼8801德国大使馆的时光','练练','法人','3451234336','机构名称','345@qq.com',1)
        self.assertEqual('00000000',user['status'])
    def test6(self):
        '''政府机构认证修改'''
        # 需要从数据库里获取可以修改的数据
        user=method.orgcertify('14711234461','111111','北京','北京','北京','地址9号公寓楼8801德国大使馆的时光',
                               '练练啊','法人啊','33456765432','机构jigou','345344@qq.com',1)
        self.assertEqual('00000000',user['status'])
    # 以下举例从数据库取数
    # def test7(self):
    #     '''国有企业认证'''
    #     dd=person.get_one("SELECT * FROM user_basic WHERE certificate_status=1 AND user_type=2 AND mobile LIKE '1471123%'")
    #     user=method.companycertify(dd['mobile'],'111111','北京','北京','北京','地址9号公寓楼8801德国大使馆的时光','100000000',
    #                                '经营范围：服装','练练',generator.createidcard(),'法人','3451234336','社会统一信用码',
    #                                2,'htth://www.ddgdg.com','url:degregrdg','机构名称','345@qq.com')
    #     self.assertEqual('00000000',user['status'])
    # def tearDown(self):
        print("单条用例执行结束")
    @classmethod
    def tearDownClass(cls):
        print("企业认证用例执行结束")

if __name__=='__main__':
    # 方法1：执行所有的测试
    unittest.main()

