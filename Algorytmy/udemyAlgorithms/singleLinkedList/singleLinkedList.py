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

        newTail= self.head
        last = self.head
        while last.next:
            newTail = last
            last = last.next

        assert last        
        v = last.val
        
        newTail.next = None
        self.tail = newTail
        
        self.length -= 1
        return v