import unittest
from prioQueue import PriorityQueue

class Test(unittest.TestCase):
    def test1(self):
        q: PriorityQueue = PriorityQueue()
        q.enqueue('walk dog', 2)
        q.enqueue('buy steak', 1)
        q.enqueue('pay bill', 0)
        q.enqueue('clean room', 1)
        
        self.assertEqual(q.dequeue(), 'pay bill')
        self.assertEqual(q.dequeue(), 'buy steak')
        self.assertEqual(q.dequeue(), 'clean room')
        self.assertEqual(q.dequeue(), 'walk dog')
        self.assertIsNone(q.dequeue())

if __name__ == "__main__":
    unittest.main()