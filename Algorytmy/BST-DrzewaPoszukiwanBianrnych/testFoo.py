__author__ = 'kamil'

import unittest
from foo import BST
from foo import Node

class testyDrzewa(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.d = BST()

        self.d.dodaj(5)
        self.d.dodaj(3)
        self.d.dodaj(2)
        self.d.dodaj(7)
        self.d.dodaj(5)
        self.d.dodaj(8)

    def testBasicInOrder(self):
        out = self.d.inOrder()
        self.assertEqual([2,3,5,5,7,8], out)

    def testSearchFound(self):
        node = self.d.search(3)
        self.assertIsNotNone(node)
        self.assertEqual(3, node.getKey())
        self.assertEqual(2, node.getLewy().getKey())
        self.assertEqual(5, node.getPrawy().getKey())

    def testSearchNotFound(self):
        node = self.d.search(900)
        self.assertIsNone(node)

    def testSearchFoundIter(self):
        node = self.d.searchIterative(3)
        self.assertIsNotNone(node)
        self.assertEqual(3, node.getKey())
        self.assertEqual(2, node.getLewy().getKey())
        self.assertEqual(5, node.getPrawy().getKey())

    def testSearchNotFoundIter(self):
        node = self.d.searchIterative(900)
        self.assertIsNone(node)

    def testGetMin(self):
        val = self.d.getMin()
        self.assertEqual(2, val)

    def testGetMax(self):
        val = self.d.getMax()
        self.assertEqual(8, val)

class testyPustegoDrzewa(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.d = BST()

    def testSearchFound(self):
        node = self.d.search(3)
        self.assertIsNone(node)

    def testSearchNotFound(self):
        node = self.d.search(900)
        self.assertIsNone(node)

    def testSearchFoundIter(self):
        node = self.d.searchIterative(3)
        self.assertIsNone(node)

    def testSearchNotFoundIter(self):
        node = self.d.searchIterative(900)
        self.assertIsNone(node)

    def testGetMin(self):
        val = self.d.getMin()
        self.assertIsNone(val)

    def testGetMax(self):
        val = self.d.getMax()
        self.assertIsNone(val)

if __name__ == '__main__':
    unittest.main()
