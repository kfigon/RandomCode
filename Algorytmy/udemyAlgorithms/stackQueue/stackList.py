from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, val: T):
        self.val = val
        self.prev: Optional[Node[T]] = None

    def __repr__(self) -> str:
        return f'v: {self.val}'

class StackList(Generic[T]):
    def __init__(self):
        self.top: Optional[Node[T]] = None
        self.length = 0
    
    def push(self, val: T):
        newNode = Node[T](val)
        newNode.prev = self.top
        self.top = newNode
        self.length += 1

    def pop(self) -> Optional[T]:
        if self.isEmpty():
            return None

        assert self.top
        self.length -= 1
        v = self.top.val
        self.top = self.top.prev
        return v
    
    def isEmpty(self) -> bool:
        return self.top is None