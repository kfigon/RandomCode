__author__ = 'kamil'

import unittest
from AlgorytmyCormen.UnionFind.UnionFindBase import UnionFindBase

class QuickFind(UnionFindBase):
    def __init__(self, rozmiarTablicy):
        super().__init__(rozmiarTablicy)

    def areConnected(self, p, q):
        return (self._tab[p] == self._tab[q])

    def union(self,p,q):
        toChange = self._tab[p]
        val = self._tab[q]
        for i in range(len(self._tab)):
            if(self._tab[i] == toChange):
                self._tab[i] = val

    def getConnectedComponents(self):
        out = []
        uniqueVals = []
        for el in self._tab:
            if(el not in uniqueVals):
                uniqueVals.append(el)

        for unique in uniqueVals:
            toAdd=[]
            for i in range(len(self._tab)):
                val = self._tab[i]
                if(val == unique):
                    toAdd.append(i)
            out.append(tuple(toAdd))

        return out

class QuickFindTest1(unittest.TestCase):
    def setUp(self):
        self.qf = QuickFind(10)
        self.qf.union(4,3)
        self.qf.union(3,8)
        self.qf.union(6,5)
        self.qf.union(9,4)
        self.qf.union(2,1)

    def test1(self):
        self.assertFalse(self.qf.areConnected(0,7))
        self.assertTrue(self.qf.areConnected(8,9))
        # 1 elementowe tuple tak wygladaja
        self.assertEqual([(0,), (1,2), (3,4,8,9), (5,6), (7,)], self.qf.getConnectedComponents())

    def test2(self):
        self.qf.union(5,0)
        self.qf.union(7,2)
        self.qf.union(6,1)
        self.qf.union(1,0)

        self.assertTrue(self.qf.areConnected(0,7))
        self.assertEqual([(0,1,2,5,6,7), (3,4,8,9)], self.qf.getConnectedComponents())


class QuickFindTest2(unittest.TestCase):
    def test(self):
        qf = QuickFind(10)
        qf.union(4,3)
        qf.union(3,8)
        qf.union(6,5)
        qf.union(9,4)
        qf.union(2,1)
        self.assertTrue(qf.areConnected(8,9))
        self.assertFalse(qf.areConnected(5,0))
        qf.union(5,0)
        qf.union(7,2)
        qf.union(6,1)

        expectedConnectedComponents = [(0,1,2,5,6,7), (3,4,8,9)]
        self.assertEqual(expectedConnectedComponents, qf.getConnectedComponents())

if __name__ == '__main__':
    unittest.main()
