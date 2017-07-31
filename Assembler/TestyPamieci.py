__author__ = 'kamil'

import unittest
from Procesor import Pamiec
from Procesor import Util

class MyTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.pamiec = Pamiec()
        for i in range(1024):
            self.assertEqual(0, self.pamiec.get(i))

    def testIleBajtow0(self):
        self.assertEqual(0, Util.ileBajtow(0))
    def testIleBajtow1(self):
        self.assertEqual(1, Util.ileBajtow(0x1))
    def testIleBajtow2(self):
        self.assertEqual(2, Util.ileBajtow(0x1234))
    def testIleBajtow3(self):
        self.assertEqual(3, Util.ileBajtow(0x123456))
    def testIleBajtow4(self):
        self.assertEqual(4, Util.ileBajtow(0x12345678))
    def testIleBajtow5(self):
        self.assertEqual(5, Util.ileBajtow(0x123456789a))
    def testIleBajtow6(self):
        self.assertEqual(6, Util.ileBajtow(0x123456789abc))
    def testIleBajtow7(self):
        self.assertEqual(7, Util.ileBajtow(0x123456789abcde))
    def testIleBajtow8(self):
        self.assertEqual(8, Util.ileBajtow(0x123456789abcdefa))

    def testWriteByte(self):
        self.pamiec.set(1, 0x12)
        self.assertEqual(0x12, self.pamiec.get(1))

    def testWrite2Bytes(self):
        self.pamiec.set(1, 0x1234)
        self.assertEqual(0x34, self.pamiec.get(1))
        self.assertEqual(0x12, self.pamiec.get(2))
        self.assertEqual(0, self.pamiec.get(3))

    def testWrite3Bytes(self):
        self.pamiec.set(1, 0x123456)
        self.assertEqual(0x56, self.pamiec.get(1))
        self.assertEqual(0x34, self.pamiec.get(2))
        self.assertEqual(0x12, self.pamiec.get(3))
        self.assertEqual(0, self.pamiec.get(4))

    def testWrite4Bytes(self):
        self.pamiec.set(1, 0x12345678)
        self.assertEqual(0x78, self.pamiec.get(1))
        self.assertEqual(0x56, self.pamiec.get(2))
        self.assertEqual(0x34, self.pamiec.get(3))
        self.assertEqual(0x12, self.pamiec.get(4))
        self.assertEqual(0, self.pamiec.get(5))

    def testWrite5Bytes(self):
        self.pamiec.set(1, 0x123456789a)
        self.assertEqual(0x9a, self.pamiec.get(1))
        self.assertEqual(0x78, self.pamiec.get(2))
        self.assertEqual(0x56, self.pamiec.get(3))
        self.assertEqual(0x34, self.pamiec.get(4))
        self.assertEqual(0x12, self.pamiec.get(5))
        self.assertEqual(0, self.pamiec.get(6))

    def testWrite6Bytes(self):
        self.pamiec.set(1, 0x123456789abc)
        self.assertEqual(0xbc, self.pamiec.get(1))
        self.assertEqual(0x9a, self.pamiec.get(2))
        self.assertEqual(0x78, self.pamiec.get(3))
        self.assertEqual(0x56, self.pamiec.get(4))
        self.assertEqual(0x34, self.pamiec.get(5))
        self.assertEqual(0x12, self.pamiec.get(6))
        self.assertEqual(0, self.pamiec.get(7))

    def testWrite7Bytes(self):
        self.pamiec.set(1, 0x123456789abcde)
        self.assertEqual(0xde, self.pamiec.get(1))
        self.assertEqual(0xbc, self.pamiec.get(2))
        self.assertEqual(0x9a, self.pamiec.get(3))
        self.assertEqual(0x78, self.pamiec.get(4))
        self.assertEqual(0x56, self.pamiec.get(5))
        self.assertEqual(0x34, self.pamiec.get(6))
        self.assertEqual(0x12, self.pamiec.get(7))
        self.assertEqual(0, self.pamiec.get(8))

    def testWrite8Bytes(self):
        self.pamiec.set(1, 0x123456789abcdefa)
        self.assertEqual(0xfa, self.pamiec.get(1))
        self.assertEqual(0xde, self.pamiec.get(2))
        self.assertEqual(0xbc, self.pamiec.get(3))
        self.assertEqual(0x9a, self.pamiec.get(4))
        self.assertEqual(0x78, self.pamiec.get(5))
        self.assertEqual(0x56, self.pamiec.get(6))
        self.assertEqual(0x34, self.pamiec.get(7))
        self.assertEqual(0x12, self.pamiec.get(8))
        self.assertEqual(0, self.pamiec.get(9))


if __name__ == '__main__':
    unittest.main()
