__author__ = 'kamil'

import unittest
from foo import foo

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual([2, 6], foo(2, 4, 7))

    def test_2(self):
        self.assertEqual([5, 10, 15, 20, 25, 30],
        foo(5, 12, 35))



if __name__ == '__main__':
    unittest.main()
