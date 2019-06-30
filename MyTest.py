# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import unittest


class MyTest(unittest.TestCase):
    def tearDown(self):

        print('111')

    def setUp(self):

        print('22222')

    @classmethod
    def tearDownClass(self):

        print('4444444')

    @classmethod
    def setUpClass(self):

        print('33333')

    def test_a_run(self):



        self.assertEqual(1, 1)

    def test_b_run(self):
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例