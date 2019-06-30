# -*- coding: utf-8 -*-
import unittest

import HtmlTestRunner
import time
from unittest import TestLoader, TestSuite
import basepage
from BSTestRunner import HTMLTestRunner


class MyTest(unittest.TestCase):
    # def tearDown(self):
    #     print('111')
    #
    # def setUp(self):
    #     print('22222')
    #
    # @classmethod
    # def tearDownClass(self):
    #     print('4444444')

    @classmethod
    def setUpClass(self):
        print('33333')

    def test_a_run(self):
        self.assertEqual(1, 1)

    def test_b_run(self):
        self.assertEqual(2, 2)


# 添加Suite
def Suite():
    # 定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    # 将测试用例加入到容器
    suiteTest.addTest(MyTest("test_b_run"))


    return suiteTest
if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(case_01)
    runer = HTMLTestRunner(
        title="带截图的测试报告",
        description="用例测试情况",
        tester='Shaofeng Wu',
        stream=basepage.get_report_path(),
        verbosity=2, retry=1, save_last_try=True)
    runer.run(Suite())