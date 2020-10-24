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
    
    def shift(self) -> Optional[T]:
        if self.head is None:
            return None
        
        v = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        
        self.length -= 1
        return v

    def unshift(self, val: T):
        if self.head is None:
            self.push(val)
        else:
            self.length+=1
            newHead = Node[T](val)
            newHead.next = self.head
            self.head = newHead
    
    def get(self, idx: int) -> Optional[T]:
        if idx < 0 or idx >= self.length:
            return None
        ptr = self.head
        i = 0
        while ptr:
            if i == idx:
                return ptr.val
            ptr = ptr.next
            i +=1
        return None

    def set(self, idx: int, val: T):
        if idx < 0 or idx >= self.length:
            raise Exception(f'Not valid idx {idx}, len: {self.length}')
    
        ptr = self.head
        i = 0
        while ptr:
            if i == idx:
                ptr.val = val
                return
            ptr = ptr.next
            i +=1