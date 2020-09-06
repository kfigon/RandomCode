import unittest
from stack import Stack

class Test(unittest.TestCase):
    def testPush(self):
        s = Stack()
        s.push(1)
        s.push(3)

        self.assertEqual(2, s.size())
        s.clean()
    
    def testClean(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.clean()

        self.assertEqual(0, s.size())
        self.assertIsNone(s.top)
    
    def testPushPop(self):
        s = Stack()
        s.push(1)
        s.push(3)
        
        self.assertEqual(3, s.pop())
        self.assertEqual(1, s.size())
        s.push(4)
        self.assertEqual(4, s.pop())
        self.assertEqual(1, s.pop())
        self.assertEqual(0, s.size())
        s.clean()

if __name__ == "__main__":
    unittest.main()