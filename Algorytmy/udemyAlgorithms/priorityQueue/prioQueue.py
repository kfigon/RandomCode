from typing import Tuple, Optional, Callable, List
# data structure where each element have priority
# higher priority elements are served before lower prio

# we can implement priority queue using BinaryHeap

class Node:
    def __init__(self, val: str, priority: int):
        self.val = val
        self.priority = priority

# insert/remove - O(logn)

# this time it's MinBinary Heap. lowest the value - higher the priority
class PriorityQueue:
    def __init__(self):
        self.tab: List[Node] = []

    def _getChild(self, idx: int) -> Tuple[Optional[int], Optional[int]]:
        adjust: Callable[[int],Optional[int]] = lambda x: x if x < len(self.tab) and x >= 0 else None
        left = 2*idx + 1
        right = 2*idx + 2        
        return adjust(left), adjust(right)

    def _getParent(self, idx: int) -> Optional[int]:
        if idx < 0 or idx >= len(self.tab):
            return None

        parentIdx = (idx-1)//2
        if parentIdx >= 0 and parentIdx < len(self.tab):
            return parentIdx
        return None
    
    # add to the end and bubble up
    def enqueue(self, val: str, priority: int):
        newValueIdx = len(self.tab)
        v = Node(val, priority)
        self.tab.append(v)

        parentIdx = self._getParent(newValueIdx)
        while (parentIdx is not None) and (v.priority < self.tab[parentIdx].priority):
            self.tab[newValueIdx],self.tab[parentIdx] = self.tab[parentIdx], self.tab[newValueIdx]
            newValueIdx = parentIdx
            parentIdx = self._getParent(newValueIdx)

    def dequeue(self) -> Optional[str]:
        if len(self.tab) == 0:
            return None
        elif len(self.tab) == 1:
            return self.tab.pop().val

        top = self.tab[0]
        self.tab = [self.tab[-1]] + self.tab[1:-1]
        
        newIdx = 0
        # kopcujemy
        while True:
            left,right = self._getChild(newIdx)
            minIdx = -1

            if left is None and right is not None:
                minIdx = right
            elif right is None and left is not None:
                minIdx = left
            elif right is not None and left is not None:
                minIdx = left if self.tab[left].priority < self.tab[right].priority else right
            else:
                break

            if self.tab[minIdx].priority < self.tab[newIdx].priority:
                self.tab[minIdx], self.tab[newIdx] = self.tab[newIdx], self.tab[minIdx]
                newIdx = minIdx
            else:
                break

        return top.val