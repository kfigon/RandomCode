import unittest
from quickFind import QuickFind


class Tests(unittest.TestCase):
    def test1(self):
        uf = QuickFind(5)
        uf.tab=[0,1,1,8,8,0,0,1,8,8]
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
                res = uf.connected(x[0],x[1])
                self.assertEqual(expectedResult, res)
        
        self.assertEqual(3, uf.getNumberOfConnectedComponents())

    def testUnions(self):
        uf = QuickFind(10)
        uf.union(4,3)
        uf.union(3,8)
        uf.union(6,5)
        uf.union(9,4)
        uf.union(2,1)
        uf.union(8,9)
        uf.union(5,0)
        uf.union(7,2)
        uf.union(6,1)

        self.assertTrue(uf.connected(0,5))
        self.assertTrue(uf.connected(0,1))
        self.assertTrue(uf.connected(0,6))
        self.assertTrue(uf.connected(0,7))
        self.assertTrue(uf.connected(0,2))
        
        self.assertTrue(uf.connected(3,9))
        self.assertTrue(uf.connected(3,8))
        self.assertTrue(uf.connected(4,8))

        self.assertFalse(uf.connected(3,0))

        self.assertEqual(2, uf.getNumberOfConnectedComponents())
    

    def test2(self):
        uf = QuickFind(5)
        uf.tab=[0,1,1,8,8,0,0,1,8,8]
        self.assertFalse(uf.connected(6,1))
        self.assertFalse(uf.connected(1,6))
        uf.union(6,1)
        self.assertTrue(uf.connected(6,1))
        self.assertTrue(uf.connected(1,6))
        
if __name__ == "__main__":
    unittest.main()