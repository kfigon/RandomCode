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
        if self.root is None:
            return 0
        return self.traverseHeight(self.root)

    def traverseHeight(self, n: Node) -> int:
        if n is None:
            return -1
        left = self.traverseHeight(n.left)
        right = self.traverseHeight(n.right)
        return 1 + max(left,right)


def testTree(vals: List[int]) -> int:
    tree = Tree()
    for v in vals:
        tree.insert(v)
    return tree.getHeight()

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(0, testTree([]))
    def test2(self):
        self.assertEqual(0, testTree([431]))
    def test3(self):
        self.assertEqual(1, testTree([4,2]))
    def test4(self):
        self.assertEqual(1, testTree([4,2,6]))
    def test5(self):
        self.assertEqual(2, testTree([4,2,6, 5]))
    def test6(self):
        self.assertEqual(2, testTree([4,2,6, 5,1]))
    def test7(self):
        self.assertEqual(2, testTree([4,2,6, 5,1,7]))
    def test8(self):
        self.assertEqual(3, testTree([4,2,6, 5,1,7,8]))

if __name__ == '__main__':
    unittest.main()