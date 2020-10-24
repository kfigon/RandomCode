from typing import TypeVar, Generic, Optional, List
T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, val: T):
        self.val = val
        self.next: Optional[Node[T]] = None

class SingleLinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.length: int = 0
    
    def push(self, val: T):
        newNode = Node[T](val)
        self.length+=1
        if self.head is None:
            self.head = newNode
        else:
            assert self.tail, 'this shouldnt happen!' # just to satisfy mypy...
            self.tail.next = newNode
                
        self.tail = newNode
    
    def pop(self) -> Optional[T]:
        if self.head is None:
            return None
        elif self.head.next is None:
            self.length -=1
            v = self.head.val
            self.head = None
            self.tail = None
            return v

        newLast: Node = self.head
        while newLast.next != self.tail and newLast.next is not None:
            newLast = newLast.next
        
        assert self.tail # mypy
        v = self.tail.val
        
        newLast.next = None
        self.tail = newLast
        
        self.length -= 1
        return v