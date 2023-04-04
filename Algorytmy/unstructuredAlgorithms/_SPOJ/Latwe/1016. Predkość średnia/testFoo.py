__author__ = 'kamil'

import unittest
from foo import foo

class MyTestCase(unittest.TestCase):
    def test_50(self):
        self.assertEqual(50, foo(50, 50))

    def test_48(self):
        self.assertEqual(48, foo(60, 40))


if __name__ == '__main__':
    unittest.main()
