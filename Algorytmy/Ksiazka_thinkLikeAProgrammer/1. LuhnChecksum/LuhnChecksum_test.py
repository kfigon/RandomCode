__author__ = 'kamil'

import unittest
from LuhnChecksum import foo

class LuhnChecksumTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(False, foo(1))

    def test_176248(self):
        self.assertEqual(False, foo(176248))

if __name__ == '__main__':
    unittest.main()
