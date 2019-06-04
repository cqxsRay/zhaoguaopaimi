import unittest
from common import HTMLTestReportCN
from testcase import test_login
from testcase.test_login import TestLogin
from testcase.test_regist import TestRegist
import os


if __name__=='__main__':
    suite=unittest.TestSuite()
    # suite1= unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    # suite2=unittest.TestLoader().loadTestsFromTestCase(TestRegist)
    # suite.addTest(unittest.TestLoader().loadTestsFromModule(test_login))

    runner=unittest.TextTestRunner(verbosity=2)
    # runner=HTMLTestReportCN.HTMLTestRunner(title='自动化测试报告',description='用例执行情况：',
    #                                          stream=open(newreport, 'wb'),verbosity=2)
    runner.run(suite)

