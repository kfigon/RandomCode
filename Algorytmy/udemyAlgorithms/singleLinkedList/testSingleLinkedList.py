import unittest
from singleLinkedList import SingleLinkedList

class Test(unittest.TestCase):
    def testPush(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.length, 3)
        self.assertEqual(s.head.val, 1)
        self.assertEqual(s.head.next.val, 2)
        self.assertEqual(s.head.next.next.val, 3)
        self.assertIsNone(s.head.next.next.next)
        self.assertEqual(s.tail.val, 3)
        self.assertIsNone(s.tail.next)

    def testPop3(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.push(2)
        s.push(3)

        v = s.pop()

        self.assertEqual(v, 3)
        self.assertEqual(s.length, 2)

        self.assertEqual(s.head.val, 1)
        self.assertEqual(s.head.next.val, 2)
        self.assertIsNone(s.head.next.next)
        self.assertIsNone(s.tail.next)
        self.assertEqual(s.tail.val, 2)

    def testPop2(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.push(2)

        v = s.pop()

        self.assertEqual(v, 2)
        self.assertEqual(s.length, 1)

        self.assertEqual(s.head.val, 1)
        self.assertEqual(s.tail.val, 1)

        self.assertIsNone(s.head.next)
        self.assertIsNone(s.tail.next)

    def testSinglePop(self):
        s = SingleLinkedList[int]()
        s.push(1)
        self.assertEqual(s.pop(), 1)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)
        self.assertEqual(s.length, 0)
        
    def testEmptyPop(self):
        s = SingleLinkedList[int]()
        self.assertIsNone(s.pop())
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)
        self.assertEqual(s.length, 0)

    def testShiftEmpty(self):
        s = SingleLinkedList[int]()
        self.assertIsNone(s.shift())
        self.assertEqual(s.length, 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)
    
    def testShiftSingle(self):
        s = SingleLinkedList[int]()
        s.push(2)
        self.assertEqual(s.shift(), 2)

        self.assertEqual(s.length, 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)
    
    def testShift2(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.push(2)
        self.assertEqual(s.shift(), 1)
        
        self.assertEqual(s.length, 1)
        self.assertEqual(s.head.val, 2)
        self.assertEqual(s.tail.val, 2)
        
        self.assertIsNone(s.head.next)
        self.assertIsNone(s.tail.next)

    def testShift3(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.shift(), 1)
        
        self.assertEqual(s.length, 2)
        self.assertEqual(s.head.val, 2)
        self.assertEqual(s.head.next.val, 3)
        self.assertEqual(s.tail.val, 3)
        self.assertIsNone(s.tail.next)
        self.assertIsNone(s.head.next.next)

    def testUnshiftEmpty(self):
        s = SingleLinkedList[int]()
        s.unshift(3)
        self.assertEqual(s.length, 1)
        self.assertEqual(s.head.val, 3)
        self.assertEqual(s.tail.val, 3)
        self.assertIsNone(s.tail.next)

    def testUnshiftSingle(self):
        s = SingleLinkedList[int]()
        s.push(3)
        s.push(5)
        s.unshift(1)
        self.assertEqual(s.length, 3)
        self.assertEqual(s.head.val, 1)
        self.assertEqual(s.head.next.val, 3)
        self.assertEqual(s.head.next.next.val, 5)
        
        self.assertIsNone(s.head.next.next.next)
        self.assertEqual(s.tail.val, 5)
        self.assertIsNone(s.tail.next)

    def testUnshift(self):
        s = SingleLinkedList[int]()
        s.push(5)
        s.unshift(3)
        self.assertEqual(s.length, 2)
        self.assertEqual(s.head.val, 3)
        self.assertEqual(s.head.next.val, 5)
        self.assertEqual(s.tail.val, 5)
        self.assertIsNone(s.tail.next)

    def testGetEmpty(self):
        s = SingleLinkedList[int]()
        self.assertIsNone(s.get(0))
        self.assertIsNone(s.get(1))
        self.assertIsNone(s.get(2))

    def testGet(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.push(2)
        self.assertEqual(s.get(0), 1)
        self.assertEqual(s.get(1), 2)
        self.assertEqual(s.get(2), None)
        self.assertEqual(s.get(3), None)
        self.assertEqual(s.get(-1), None)

    def testSetEmpty(self):
        s = SingleLinkedList[int]()
        self.assertRaises(Exception, s.setV, 0,123)
        self.assertRaises(Exception, s.setV, 1,123)
        self.assertRaises(Exception, s.setV, 2,123)
        self.assertRaises(Exception, s.setV, -1,123)

    def testSet(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.push(2)

        s.setV(0, 123)
        self.assertEqual(s.get(0),123)
        self.assertRaises(Exception, s.setV, 2,423)
        self.assertRaises(Exception, s.setV, -1,123)

    def testInsertEmpty(self):
        s = SingleLinkedList[int]()
        self.assertRaises(Exception, s.insert, -1,123)
        self.assertRaises(Exception, s.insert, 1,123)
        
        s.insert(0, 123)
        self.assertEqual(s.head.val, 123)
        self.assertIsNone(s.head.next)
        self.assertEqual(s.tail.val, 123)
        self.assertEqual(s.length, 1)

    def testInsertSingle_addAtEnd(self):
        s = SingleLinkedList[int]()
        s.push(1)

        s.insert(1, 123)
        self.assertEqual(s.head.val, 1)
        self.assertEqual(s.head.next.val, 123)
        self.assertEqual(s.tail.val, 123)
        self.assertEqual(s.length, 2)

    def testInsertSingle_addBeginning(self):
        s = SingleLinkedList[int]()
        s.push(1)

        s.insert(0, 123)
        self.assertEqual(s.head.val, 123)
        self.assertEqual(s.head.next.val, 1)
        self.assertEqual(s.tail.val, 1)
        self.assertEqual(s.length, 2)

    def testInsertMiddle(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.push(2)
        s.push(3)

        s.insert(1, 123)

        self.assertEqual(s.length, 4)
        self.assertEqual(s.head.val, 1)
        self.assertEqual(s.head.next.val, 123)
        self.assertEqual(s.head.next.next.val, 2)
        self.assertEqual(s.head.next.next.next.val, 3)
        self.assertEqual(s.tail.val, 3)

    def testInsert_End(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.push(2)
        s.push(3)

        s.insert(3, 123)

        self.assertEqual(s.length, 4)
        self.assertEqual(s.head.val, 1)
        self.assertEqual(s.head.next.val, 2)
        self.assertEqual(s.head.next.next.val, 3)
        self.assertEqual(s.head.next.next.next.val, 123)
        self.assertEqual(s.tail.val, 123)

    def testRemoveEmpty(self):
        s = SingleLinkedList[int]()
        self.assertRaises(Exception, s.remove, -1)
        self.assertRaises(Exception, s.remove, 0)
        self.assertRaises(Exception, s.remove, 1)

    def testRemoveSingle(self):
        s = SingleLinkedList[int]() 
        s.push(1)

        s.remove(0)

        self.assertEqual(s.length, 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)

    def testRemoveFirst(self):
        s = SingleLinkedList[int]() 
        s.push(1)
        s.push(2)

        s.remove(0)
        self.assertEqual(s.length, 1)
        self.assertEqual(s.head.val, 2)
        self.assertEqual(s.tail.val, 2)
        self.assertIsNone(s.head.next)

    def testRemoveLast(self):
        s = SingleLinkedList[int]() 
        s.push(1)
        s.push(2)

        s.remove(1)
        self.assertEqual(s.length, 1)
        self.assertEqual(s.head.val, 1)
        self.assertEqual(s.tail.val, 1)
        self.assertIsNone(s.head.next)

    def testRemoveMiddle(self):
        s = SingleLinkedList[int]() 
        s.push(1)
        s.push(2)
        s.push(3)

        s.remove(1)
        self.assertEqual(s.length, 2)
        self.assertEqual(s.head.val, 1)
        self.assertEqual(s.head.next.val, 3)
        self.assertEqual(s.tail.val, 3)
        self.assertIsNone(s.tail.next)

    def testReverseEmpty(self):
        s = SingleLinkedList[int]()
        s.reverse()
        self.assertEqual(s.length, 0)
        self.assertIsNone(s.head)
        self.assertIsNone(s.tail)

    def testReverseSingle(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.reverse()

        self.assertEqual(s.length, 1)
        self.assertEqual(s.head.val, 1)
        self.assertEqual(s.tail.val, 1)
        self.assertIsNone(s.tail.next)
        self.assertIsNone(s.head.next)

    def testReverse2(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.push(2)
        s.reverse()

        self.assertEqual(s.length, 2)
        self.assertEqual(s.head.val, 2)
        self.assertEqual(s.head.next.val, 1)

        self.assertEqual(s.tail.val, 1)
        
        self.assertIsNone(s.head.next.next)
        self.assertIsNone(s.tail.next)

    def testReverse3(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.push(2)
        s.push(3)
        s.reverse()

        self.assertEqual(s.length, 3)
        self.assertEqual(s.head.val, 3)
        self.assertEqual(s.head.next.val, 2)
        self.assertEqual(s.head.next.next.val, 1)
        self.assertEqual(s.tail.val, 1)
        
        self.assertIsNone(s.head.next.next.next)
        self.assertIsNone(s.tail.next)

    def testReverse4(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.reverse()

        self.assertEqual(s.length, 4)
        self.assertEqual(s.head.val, 4)
        self.assertEqual(s.head.next.val, 3)
        self.assertEqual(s.head.next.next.val, 2)
        self.assertEqual(s.head.next.next.next.val, 1)
        self.assertEqual(s.tail.val, 1)
        
        self.assertIsNone(s.head.next.next.next.next)
        self.assertIsNone(s.tail.next)

    def testReverse4_get(self):
        s = SingleLinkedList[int]()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.reverse()

        self.assertEqual(s.length, 4)
        self.assertEqual(s.get(0), 4)
        self.assertEqual(s.get(1), 3)
        self.assertEqual(s.get(2), 2)
        self.assertEqual(s.get(3), 1)
        self.assertIsNone(s.get(4))

if __name__ == "__main__":
    unittest.main()