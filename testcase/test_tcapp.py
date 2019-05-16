# 这个是app自动化测试的模版
import unittest
import os
import uiautomator2 as u2

class testapp(unittest.TestCase):
    # 定义存储照片的文件路径
    cur=os.path.dirname(os.path.realpath(__file__))
    photo=os.path.join(os.path.dirname(cur),'testdata/')
    @classmethod
    def setUpClass(cls):
        # 连接手机
        cls.d = u2.connect("192.168.130.212")
        # 解锁手机
        cls.d.unlock()
        # 启动app
        cls.d.app_start("com.baofengpudgeapp")
    def setUp(self):
        print("start")
    def test_login1(self):
        # 点击我的
        self.d(text=u"我的").click()
        self.d(text=u"请输入手机号码").wait(timeout=3)
        # 点击输入手机号
        self.d(text=u"请输入手机号码").set_text('14711119998')
        self.d(text=u"请输入登录密码").set_text('111111')
        # 向上滑动
        self.d(scrollable=True).scroll.to(text=u"登录")
        self.d(text=u" 登录 ").click()
        self.d(text=u"总资产(元)").wait(timeout=3)
        self.d.screenshot(self.photo+'login1.jpg')
        assert self.d(text=u"总资产(元)").exists
    def test_login2(self):
        # 点击我的
        self.d(text=u"我的").click()
        self.d(text=u"请输入手机号码").wait(timeout=3)
        # 点击输入手机号
        self.d(text=u"请输入手机号码").set_text('14711234500')
        self.d(text=u"请输入登录密码").set_text('bf1111')
        # 向上滑动
        self.d(scrollable=True).scroll.to(text=u"登录")
        self.d(text=u" 登录 ").click()
        self.d(text=u"总资产(元)").wait(timeout=3)
        self.d.screenshot(self.photo+'login2.jpg')
        assert self.d(text=u"总资产(元)").exists
    def tearDown(self):
        print("end")
    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop("com.baofengpudgeapp")
if __name__=='__main__':
    unittest.main()