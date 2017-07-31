__author__ = 'kamil'
from Mult import mult

import unittest


class TestyMultiplikacji(unittest.TestCase):
    def testSimple_oneDigit(self):
        self.assertEqual("8", mult("4", "2"))

    def testHundredsTimesDigit(self):
        self.assertEqual("492", mult("123", "4"))

    def testHundredsTimesDigit_inverted(self):
        self.assertEqual("492", mult("4", "123"))

    def testHundredsTimesTens(self):
        self.assertEqual("5289", mult("123", "43"))

    def testHundredsTimesTens_inverted(self):
        self.assertEqual("5289", mult("43", "123"))

    def testHundredsHundreds(self):
        self.assertEqual("110808", mult("324", "342"))

    def testZeroMultiply(self):
        self.assertEqual("0", mult("0", "12"))

    def testBigNum(self):
        self.assertEqual("123437655", mult("9999", "12345"))

    def testBigNum_inv(self):
        self.assertEqual("123437655", mult("12345", "9999"))


if __name__ == '__main__':
    unittest.main()
