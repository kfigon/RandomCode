import unittest
from binHeap import BinaryHeapArray, BinaryHeap

class TestHeap(unittest.TestCase):

#           41
#     39          33
#  18    27     12 

    def test1(self):
        b = BinaryHeapArray()
        b.tab = [41,39,33,18,27,12]
        b.insert(55)
        self.assertEqual(b.tab, [55,39,41,18,27,12,33])
        self.assertTrue(b.find(55))

    def test2(self):
        b = BinaryHeapArray()
        b.tab = [41,39,33,18,27,12]
        b.insert(40)
        self.assertEqual(b.tab, [41,39,40,18,27,12,33])
        self.assertFalse(b.find(55))

    def testExtract(self):
        b = BinaryHeapArray()
        b.tab = [41,39,33,18,27,12]
        
        self.assertEqual(b.extractMax(), 41)
        self.assertEqual(b.tab, [39,27,33,18,12])

    def testExtract2(self):
        b = BinaryHeapArray()
        b.tab = [41,39,33,18,27,32]
        
        self.assertEqual(b.extractMax(), 41)
        self.assertEqual(b.tab, [39, 32, 33, 18, 27])

    def testHeap1(self):
        b= BinaryHeap()
        b.insert(100)
        b.insert(50)
        b.insert(75)
        # 100
    # 75
#        50

        self.assertEqual(b.root.val,100)
        self.assertIsNone(b.root.parent)

        self.assertEqual(b.root.left.val, 75)
        self.assertIsNone(b.root.right)
        self.assertEqual(b.root.left.parent.val,100)
        
        self.assertEqual(b.root.left.right.val, 50)
        self.assertIsNone(b.root.left.left)
        self.assertEqual(b.root.left.right.parent.val, 75)

    def testHeap2(self):
        b: BinaryHeap = BinaryHeap()
        b.insert(100)
        b.insert(50)
        b.insert(75)
        b.insert(10)
        b.insert(120)
        b.insert(30)

        # 120
#      75        100
#  30     50
#    10 
        self.assertEqual(b.root.val, 120)
        self.assertEqual(b.root.left.val, 75)
        self.assertEqual(b.root.right.val, 100)
        
        self.assertEqual(b.root.left.left.val, 30)
        self.assertEqual(b.root.left.right.val, 50)

        self.assertEqual(b.root.left.left.right.val, 10)


        self.assertIsNone(b.root.parent)
        self.assertEqual(b.root.right.parent.val, 120)
        self.assertEqual(b.root.left.parent.val, 120)
        
        self.assertEqual(b.root.left.left.parent.val, 75)
        self.assertEqual(b.root.left.right.parent.val, 75)
        
        self.assertEqual(b.root.left.left.right.parent.val, 30)


        self.assertIsNone(b.root.right.left)
        self.assertIsNone(b.root.right.right)
        
        self.assertIsNone(b.root.left.left.left)
        self.assertIsNone(b.root.left.left.right.left)
        self.assertIsNone(b.root.left.left.right.right)
        
        self.assertIsNone(b.root.left.right.left)
        self.assertIsNone(b.root.left.right.right)

if __name__ == "__main__":
    unittest.main()