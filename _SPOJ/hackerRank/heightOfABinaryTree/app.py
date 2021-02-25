from typing import List


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
        pass


def testTree(vals: List[int]) -> int:
    tree = Tree()
    for v in vals:
        tree.insert(v)
    return tree.getHeight()


assert testTree([]) == 0
assert testTree([431]) == 0
assert testTree([4,2]) == 1
assert testTree([4,2,6]) == 1
assert testTree([4,2,6, 5]) == 2
