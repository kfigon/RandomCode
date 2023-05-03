import unittest
from typing import List, Optional

class ListNode:
    def __init__(self, v):
        self.v = v
        self.next: Optional[ListNode] = None

def build(vals: List[int]) -> ListNode:
    start = None
    last = None
    for i,v in enumerate(vals):
        newNode = ListNode(v)
        if i == 0:
            start = newNode
            last = start
            continue
        last.next = newNode
        last = newNode

    return start

def collect(n: ListNode) -> List[int]:
    out = []
    while n:
        out.append(n.v)
        n = n.next
    return out

def merge(a: ListNode, b: ListNode) -> ListNode:
    start = ListNode(-1) # sentinel node
    ptr = start

    while a and b:
        if a.v < b.v:
            newNode = ListNode(a.v)
            a = a.next
            ptr.next = newNode
            ptr = ptr.next
        else:
            newNode = ListNode(b.v)
            b = b.next
            ptr.next = newNode
            ptr = ptr.next

    ptr.next = a or b  
    # while a:
    #     newNode = ListNode(a.v)
    #     a = a.next
    #     ptr.next = newNode
    #     ptr = ptr.next
    # while b:
    #     newNode = ListNode(b.v)
    #     b = b.next
    #     ptr.next = newNode
    #     ptr = ptr.next

    return start.next

def reverse(a: ListNode) -> ListNode:
    prev = None
    while a:
        newNext = a.next
        a.next = prev
        prev = a
        a = newNext
    return prev

# detect a node that references one of the previous nodes
# 2 iterators, regular and fast (jumps by 2). if they meet - we have a cycle
def cycle(n: Optional[ListNode]) -> Optional[int]:
    if not n or not n.next:
        return None
    slow = n.next
    fast = n.next.next
    while slow and fast and fast.next:
        if slow == fast:
            return slow.v
        slow = slow.next
        fast = fast.next.next
    return None

class TestList(unittest.TestCase):
    def testAdd(self):
        v = build([1,2,3,4])
        self.assertEqual([1,2,3,4], collect(v))
        
    def testMergeLists(self):
        a = build([2,5,7])
        b = build([3,11])
        self.assertEqual([2,3,5,7,11], collect(merge(a,b)))

    def testReverse(self):
        a = build([2,3,5,7,11])
        self.assertEqual([11,7,5,3,2], collect(reverse(a)))

    def testCycleNoCycle(self):
        a = build([2,3,5,7,11])
        self.assertIsNone(cycle(a))

    def testCycle(self):
        a = build([2,3,5,7,11])
        a.next.next.next.next.next = a.next
        self.assertEqual(11, cycle(a))

if __name__ == '__main__':
    unittest.main()