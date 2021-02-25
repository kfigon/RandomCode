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

    def getHeight(self) -> int:
        height = 0
        def traverse(n: Node):
            if n is None:
                return

            traverse(n.left)
            traverse(n.right)

        return height


def testTree(vals: List[int]) -> int:
    tree = Tree()
    for v in vals:
        tree.insert(v)
    return tree.getHeight()

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(testTree([]),0)
    def test2(self):
        self.assertEqual(testTree([431]), 0)
    def test3(self):
        self.assertEqual(testTree([4,2]), 1)
    def test4(self):
        self.assertEqual(testTree([4,2,6]), 1)
    def test5(self):
        self.assertEqual(testTree([4,2,6, 5]), 2)
    def test6(self):
        self.assertEqual(testTree([4,2,6, 5,1]), 2)
    def test7(self):
        self.assertEqual(testTree([4,2,6, 5,1,7]), 2)
    def test8(self):
        self.assertEqual(testTree([4,2,6, 5,1,7,8]), 3)

if __name__ == '__main__':
    unittest.main()