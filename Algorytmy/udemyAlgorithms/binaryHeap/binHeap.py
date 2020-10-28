from typing import List, Optional, Tuple, Callable

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


# get child:
# x * 2 + 1 
# x * 2 + 2

# get parent:
# (n-1)//2

# 0 -> 1,2
# 1 -> 3,4
# 2 -> 5,6
# 3 -> 7,8
# 4 -> 9,10
# 5 -> 11,12
class BinaryHeapArray:
    def __init__(self):
        self.tab: List[int] = []

    def getChild(self, idx: int) -> Tuple[Optional[int], Optional[int]]:
        assert idx < len(self.tab) and idx >= 0, f'invalid idx: {idx}, len: {len(self.tab)}'
        
        adjust: Callable[[int],Optional[int]] = lambda x: x if x < len(self.tab) else None
        left = 2*idx + 1
        right = 2*idx + 2        
        return adjust(left), adjust(right)

    def getParent(self, idx: int) -> Optional[int]:
        assert idx < len(self.tab) and idx >= 0, f'invalid idx: {idx}, len: {len(self.tab)}'

        parentIdx = (idx-1)//2
        if parentIdx >= 0 and parentIdx < len(self.tab):
            return parentIdx
        return None