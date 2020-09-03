import unittest
from quickFind import QuickFind

class TestQuickUnion(unittest.TestCase):
    def test1(self):
        qf = QuickFind(5)
        qf.tab=[0,1,1,8,8,0,0,1,8,8]
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
                res = qf.connected(x[0],x[1])
                self.assertEqual(expectedResult, res)
        
        self.assertEqual(3, qf.getNumberOfConnectedComponents())

    def testUnions(self):
        qf = QuickFind(10)
        qf.union(4,3)
        qf.union(3,8)
        qf.union(6,5)
        qf.union(9,4)
        qf.union(2,1)
        qf.union(8,9)
        qf.union(5,0)
        qf.union(7,2)
        qf.union(6,1)

        self.assertTrue(qf.connected(0,5))
        self.assertTrue(qf.connected(0,1))
        self.assertTrue(qf.connected(0,6))
        self.assertTrue(qf.connected(0,7))
        self.assertTrue(qf.connected(0,2))
        
        self.assertTrue(qf.connected(3,9))
        self.assertTrue(qf.connected(3,8))
        self.assertTrue(qf.connected(4,8))

        self.assertFalse(qf.connected(3,0))

        self.assertEqual(2, qf.getNumberOfConnectedComponents())
    

    def test2(self):
        qf = QuickFind(5)
        qf.tab=[0,1,1,8,8,0,0,1,8,8]
        self.assertFalse(qf.connected(6,1))
        self.assertFalse(qf.connected(1,6))
        qf.union(6,1)
        self.assertTrue(qf.connected(6,1))
        self.assertTrue(qf.connected(1,6))
    
    def testVal(self):
        qf = QuickFind(5)
        self.assertRaises(AssertionError, qf.connected, 5,1)
        self.assertRaises(AssertionError, qf.connected, 1,5)
        self.assertRaises(AssertionError, qf.connected, 20,10)

        # not raises
        qf.connected(4,4)

if __name__ == "__main__":
    unittest.main()