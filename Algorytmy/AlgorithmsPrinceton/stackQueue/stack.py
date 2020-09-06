class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, val):
        new = Node(val)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.top is None:
            return
        newTop = self.top.next
        toReturn = self.top
        self.top = newTop

        val = toReturn.val
        toReturn = None
        return val

    def size(self) -> int:
        if self.top is None:
            return 0
        out = 1
        mark = self.top
        while mark.next is not None:
            out+=1
            mark = mark.next

        return out

    def clean(self):
        if self.top is None:
            return
        mark = self.top # for explicit nulling to ease GC
        while self.top is not None:
            mark = None
            self.top = self.top.next
            mark = self.top
