import HtmlTestRunner
import unittest


class StringMethodsTest(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')



    def test_fail(self):
        """ This test should fail. """
        self.assertEqual(1, 1)



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))