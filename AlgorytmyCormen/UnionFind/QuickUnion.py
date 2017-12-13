__author__ = 'kamil'

import unittest
from AlgorytmyCormen.UnionFind.UnionFindBase import UnionFindBase

class RootClimberBase:
    def __init__(self,tab):
        self.__tab=tab

    def getEl(self, x):
        return self.__tab[x]

    def getRoot(self,x):
        pass

class RootClimberRecur(RootClimberBase):
    def __init__(self, tab):
        super().__init__(tab)

    def getRoot(self,x):
        if(x == self.getEl(x)):
            return x
        return self.getRoot(self.getEl(x))

class RootClimberIter(RootClimberBase):
    def __init__(self,tab):
        super().__init__(tab)

    def getRoot(self,x):
        root = x
        while(root != self.getEl(root)):
            root = self.getEl(root)

        return root

class QuickUnion(UnionFindBase):
    def __init__(self, rozmiarTablicy):
        super().__init__(rozmiarTablicy)

    def __getRoot(self, x):
        r = RootClimberIter(self._tab)
        return r.getRoot(x)

    def areConnected(self, p, q):
        return (self.__getRoot(p) == self.__getRoot(q))

    def union(self,p,q):
        rootP = self.__getRoot(p)
        rootQ = self.__getRoot(q)
        self._tab[rootP] = rootQ

    def getConnectedComponents(self):
        out = []
        uniqueRoots = []
        for i in range(len(self._tab)):
            root = self.__getRoot(i)
            if(root not in uniqueRoots):
                uniqueRoots.append(root)

        for root in uniqueRoots:
            toAdd=[]
            for i in range(len(self._tab)):
                elementsRoot = self.__getRoot(i)
                if(elementsRoot == root):
                    toAdd.append(i)

            out.append(tuple(toAdd))

        return out

class RootClimberTest(unittest.TestCase):
    def testIter1(self):
        r = RootClimberIter([0,1,9,4,9,6,6,7,8,9])
        self.checkAll1(r)

    def testRecur1(self):
        r = RootClimberRecur([0,1,9,4,9,6,6,7,8,9])
        self.checkAll1(r)

    def testIter2(self):
        r = RootClimberIter([0,1,1,8,3,0,5,1,8,8])
        self.checkAll2(r)

    def testRecur2(self):
        r = RootClimberRecur([0,1,1,8,3,0,5,1,8,8])
        self.checkAll2(r)

    def checkAll1(self, r):
        self.assertEqual(0, r.getRoot(0))
        self.assertEqual(1, r.getRoot(1))
        self.assertEqual(9, r.getRoot(2))
        self.assertEqual(9, r.getRoot(3))
        self.assertEqual(9, r.getRoot(4))
        self.assertEqual(6, r.getRoot(5))
        self.assertEqual(6, r.getRoot(6))
        self.assertEqual(7, r.getRoot(7))
        self.assertEqual(8, r.getRoot(8))
        self.assertEqual(9, r.getRoot(9))

    def checkAll2(self, r):
        self.assertEqual(0, r.getRoot(0))
        self.assertEqual(1, r.getRoot(1))
        self.assertEqual(1, r.getRoot(2))
        self.assertEqual(8, r.getRoot(3))
        self.assertEqual(8, r.getRoot(4))
        self.assertEqual(0, r.getRoot(5))
        self.assertEqual(0, r.getRoot(6))
        self.assertEqual(1, r.getRoot(7))
        self.assertEqual(8, r.getRoot(8))
        self.assertEqual(8, r.getRoot(9))

# moznaby podziedziczyc testy, ale sa problemy,
# odpalaja sie podwojnie ;<
class QuickUnionTest1(unittest.TestCase):
    def setUp(self):
        self.qf = QuickUnion(10)
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


class QuickUnionTest2(unittest.TestCase):
    def test(self):
        qf = QuickUnion(10)
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
