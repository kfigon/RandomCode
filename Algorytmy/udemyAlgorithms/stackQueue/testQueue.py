import unittest
from queueArray import Queue

class TestQueue(unittest.TestCase):
    def testEmpty(self):
        q = Queue[int]()
        self.assertEqual(q.length, 0)
        self.assertIsNone(q.dequeue())
        self.assertEqual(q.length, 0)

    def testEnq(self):
        q = Queue[int]()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(q.length, 3)

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.length, 2)

        q.enqueue(0)
        self.assertEqual(q.length, 3)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.length, 2)

        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.length, 1)

        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.length, 0)

        self.assertIsNone(q.dequeue())
        self.assertEqual(q.length, 0)

if __name__ == "__main__":
    unittest.main()