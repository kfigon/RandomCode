from typing import List
import unittest

class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Node = None
        self.right: Node = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val: int):
        newNode = Node(val)
        if self.root is None:
            self.root = newNode
            return

        ptr = self.root
        while ptr:
            if val < ptr.val:
                if ptr.left is None:
                    ptr.left = newNode
                    return
                ptr = ptr.left
            else:
                if ptr.right is None:
                    ptr.right = newNode
                    return
                ptr = ptr.right

    def getLowestCommonAncestor(self, v1: int, v2: int) -> int:
        return -1

def testTree(vals: List[int], v1: int, v2: int) -> int:
    tree = Tree()
    for v in vals:
        tree.insert(v)
    return tree.getLowestCommonAncestor(v1,v2)

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, testTree([2,1,3,4,5,6], 4,6))
    def test2(self):
        self.assertEqual(4, testTree([4,2,3,1,7,6], 1,7))

if __name__ == '__main__':
    unittest.main()