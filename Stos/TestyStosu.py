__author__ = 'kamil'

import unittest
from Stos import Stos

class TestyStosu(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.stos = Stos()

        self.assertEqual(True, self.stos.isEmpty())
        self.assertEqual(0, self.stos.getSize())

    def tearDown(self):
        super().tearDownClass()
        self.stos.clean()

        self.assertEqual(True, self.stos.isEmpty())
        self.assertEqual(0, self.stos.getSize())
        self.assertEqual(None, self.stos.pop())

    def testEmpty(self):
        self.assertEqual(True, self.stos.isEmpty())
        self.assertEqual(0, self.stos.getSize())

    def testPush(self):
        self.stos.push(800)
        self.assertEqual(False, self.stos.isEmpty())
        self.assertEqual(1, self.stos.getSize())

    def testMultiplePushPop(self):
        self.stos.push(1)
        self.stos.push(2)
        self.stos.push(3)

        self.assertEqual(3, self.stos.getSize())
        self.assertEqual(3, self.stos.pop())
        self.assertEqual(2, self.stos.pop())
        self.assertEqual(1, self.stos.pop())
        self.assertEqual(None, self.stos.pop())

    def testMultiPushMixOrder(self):
        self.stos.push(1)
        self.assertEqual(1, self.stos.pop())

        self.stos.push(2)
        self.stos.push(3)

        self.assertEqual(3, self.stos.pop())
        self.assertEqual(2, self.stos.pop())

    def testPop(self):
        self.stos.push(5)
        self.assertEqual(5, self.stos.pop())

    def testEmptyPop(self):
        self.assertEqual(None, self.stos.pop())

    def testDoublePop(self):
        self.stos.push(5)
        self.assertEqual(5, self.stos.pop())
        self.assertEqual(None, self.stos.pop())


if __name__ == '__main__':
    unittest.main()
