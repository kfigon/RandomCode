from typing import TypeVar, Generic, Optional, List
T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, val: T):
        self.val = val
        self.left: Optional[Node[T]] = None
        self.right: Optional[Node[T]] = None


class BinarySearchTree(Generic[T]):
    def __init__(self):
        self.root: Optional[Node[T]] = None