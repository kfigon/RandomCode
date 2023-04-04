__author__ = 'kamil'

import unittest
from Flamaster import foo

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual("OPSS", foo("OPSS"))
    def test_2(self):
        self.assertEqual("ABCDEF", foo("ABCDEF"))
    def test_3(self):
        self.assertEqual("ABBC3D4E5FGGHIIJK3L", foo("ABBCCCDDDDEEEEEFGGHIIJKKKL"))
    def test_4(self):
        self.assertEqual("A10B16", foo("AAAAAAAAAABBBBBBBBBBBBBBBB"))
    def test_5(self):
        self.assertEqual("A3B", foo("AAAB"))

if __name__ == '__main__':
    unittest.main()
