from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.s: List[T] = []
        self.length = 0
    
    def push(self, val: T):
        self.s.append(val)
        self.length += 1

    def pop(self) -> Optional[T]:
        if len(self.s) == 0:
            return None
        
        v = self.s.pop()
        self.length -= 1
        return v