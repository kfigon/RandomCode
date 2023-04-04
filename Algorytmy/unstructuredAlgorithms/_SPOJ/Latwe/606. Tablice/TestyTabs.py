__author__ = 'kamil'

import unittest
from Tabs import foo

class TabsTest(unittest.TestCase):
    def test_321_123(self):
        self.assertEqual("1 2 3", foo("3 2 1"))

    def test_1323_321(self):
        self.assertEqual("3 2 1", foo("1 3 2 3"))

    def test_71234567_7654321(self):
        self.assertEqual("7 6 5 4 3 2 1", foo("7 1 2 3 4 5 6 7"))

if __name__ == '__main__':
    unittest.main()
