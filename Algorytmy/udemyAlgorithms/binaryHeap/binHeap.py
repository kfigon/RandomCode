from typing import List, Optional

# BinaryHeap is kind of binarySearchTree (2 nodes)
# maxBinaryHeap - parent is always larger than children nodes
# minBinaryHeap - parent is always smaller than childen nodes

# BST moze byc jedna galezia, bardzo wysoka, bez rozgalezien
# Heap jest zbalansowany

class Node:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BinaryHeap:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, v: int):
        pass

    def find(self, v: int) -> bool:
        ptr: Optional[Node] = self.root

        while ptr:
            if ptr.val == v:
                return True
            ptr = ptr.left if v < ptr.val else ptr.right

        return False