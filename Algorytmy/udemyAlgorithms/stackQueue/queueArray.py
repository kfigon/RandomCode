from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')

#  we can also use linked list

class Queue(Generic[T]):
    def __init__(self):
        self.q: List[T]  = []
        self.length = 0

    def enqueue(self, v: T):
        self.q.insert(0, v)
        self.length += 1

    def dequeue(self) -> Optional[T]:
        if len(self.q) == 0:
            return None

        self.length -= 1
        return self.q.pop()