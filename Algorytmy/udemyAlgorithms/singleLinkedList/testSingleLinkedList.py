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

if __name__ == "__main__":
    unittest.main()