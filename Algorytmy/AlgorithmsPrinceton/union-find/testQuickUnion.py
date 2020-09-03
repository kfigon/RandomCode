import unittest
from quickUnion import QuickUnion

class TestQuickUnion(unittest.TestCase):
    def test1(self):
        qu = QuickUnion(5)
        qu.tab=[0,1,1,8,8,0,0,1,8,8]
        kejsy = [
            ((0,5), True),
            ((5,0), True),
            ((5,5), True),
            ((5,6), True),
            ((6,5), True),
            ((6,0), True),
            ((1,2), True),
            ((2,1), True),
            ((7,1), True),
            ((9,3), True),
            ((3,9), True),
            ((3,8), True),
            ((8,3), True),
            ((9,8), True),
            ((8,9), True),
            
            ((0,1), False),
            ((1,0), False),
            ((0,2), False),
            ((0,7), False),
            ((5,4), False),
            ((9,2), False),
            ((4,7), False),
            ((3,0), False)]
            
        for x, expectedResult in kejsy:
            nazwa = "when {} then {}".format(str(x), str(expectedResult))
            with self.subTest(name=nazwa):
                res = qu.connected(x[0],x[1])
                self.assertEqual(expectedResult, res)
        
        self.assertEqual(3, qu.getNumberOfConnectedComponents())

    def testUnions(self):
        qu = QuickUnion(10)
        qu.union(4,3)
        qu.union(3,8)
        qu.union(6,5)
        qu.union(9,4)
        qu.union(2,1)
        qu.union(8,9)
        qu.union(5,0)
        qu.union(7,2)
        qu.union(6,1)

        self.assertTrue(qu.connected(0,5))
        self.assertTrue(qu.connected(0,1))
        self.assertTrue(qu.connected(0,6))
        self.assertTrue(qu.connected(0,7))
        self.assertTrue(qu.connected(0,2))
        
        self.assertTrue(qu.connected(3,9))
        self.assertTrue(qu.connected(3,8))
        self.assertTrue(qu.connected(4,8))

        self.assertFalse(qu.connected(3,0))

        self.assertEqual(2, qu.getNumberOfConnectedComponents())
    

    def test2(self):
        qu = QuickUnion(5)
        qu.tab=[0,1,1,8,8,0,0,1,8,8]
        self.assertFalse(qu.connected(6,1))
        self.assertFalse(qu.connected(1,6))
        qu.union(6,1)
        self.assertTrue(qu.connected(6,1))
        self.assertTrue(qu.connected(1,6))
    
    def testVal(self):
        qu = QuickUnion(5)
        self.assertRaises(AssertionError, qu.connected, 5,1)
        self.assertRaises(AssertionError, qu.connected, 1,5)
        self.assertRaises(AssertionError, qu.connected, 20,10)

        # not raises
        qu.connected(4,4)

    
    def testRoots(self):
        qu = QuickUnion(5)
        qu.tab=[0,1,9,4,9,6,6,7,8,9]
        self.assertEqual(9, qu.getRoot(3))
        self.assertEqual(6, qu.getRoot(5))
        self.assertEqual(0, qu.getRoot(0))

if __name__ == "__main__":
    unittest.main()