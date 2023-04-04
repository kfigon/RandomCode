__author__ = 'kamil'

import unittest
from foo import Stos

class MyTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.stos = Stos()

    def test_emptyPop(self):
        self.assertEqual(False, self.stos.pop())

    def test_push_1(self):
        self.assertEqual(True, self.stos.push(1))
        self.assertEqual(1, self.stos.pop())

    def test_push_3(self):
        self.assertEqual(True, self.stos.push(1))
        self.assertEqual(True, self.stos.push(2))
        self.assertEqual(True, self.stos.push(3))
        self.assertEqual(3, self.stos.pop())
        self.assertEqual(2, self.stos.pop())
        self.assertEqual(1, self.stos.pop())

if __name__ == '__main__':
    unittest.main()
