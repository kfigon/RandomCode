__author__ = 'kamil'

import unittest
from foo import foo

class MyTestCase(unittest.TestCase):
    def test0(self):
        self.assertEqual(False, foo("4405140158"))
    def test1(self):
        self.assertEqual(True, foo("44051401458"))
    def test2(self):
        self.assertEqual(False, foo("12345678901"))

if __name__ == '__main__':
    unittest.main()
