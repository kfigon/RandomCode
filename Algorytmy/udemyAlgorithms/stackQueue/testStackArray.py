import unittest
from stackArray import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack[int]()

    def testEmpty(self):
        self.assertEqual(self.stack.length, 0)
        self.assertIsNone(self.stack.pop())

    def testStack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.length, 3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.length, 2)

        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.length, 1)

        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.length, 0)
        self.assertIsNone(self.stack.pop())
        self.assertEqual(self.stack.length, 0)

    def testStack2(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.pop()
        self.stack.push(123)

        self.assertEqual(self.stack.length, 3)

        self.assertEqual(self.stack.pop(), 123)
        self.assertEqual(self.stack.length, 2)

        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.length, 1)

        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.length, 0)
        self.assertIsNone(self.stack.pop())
        self.assertEqual(self.stack.length, 0)
        
if __name__ == "__main__":
    unittest.main()