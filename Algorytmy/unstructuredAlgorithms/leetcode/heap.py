import heapq
from typing import List

# heapq is min heap in python
class MaxHeap:
    def __init__(self):
        self.tab = []
        heapq.heapify(self.tab)

    def push(self, v):
        heapq.heappush(self.tab, -v)

    def pop(self):
        return -heapq.heappop(self.tab)

    def len(self):
        return len(self.tab)
    
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array
def maxProduct(nums: List[int]) -> int:
    h = MaxHeap()
    for i in nums:
        h.push(i)

    return (h.pop()-1) * (h.pop()-1)

# https://leetcode.com/problems/kth-largest-element-in-an-array
def findKthLargest(nums: List[int], k: int) -> int:
    # solvable also with quickselect with pivot
    # or just sort and take kth el
    h = MaxHeap()
    [h.push(i) for i in nums]
    for i in range(k):
        v = h.pop()
        if i == k-1:
            return v
    return -1

# https://leetcode.com/problems/kth-largest-element-in-a-stream/
class KthLargest:
    # min heap with size K
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.tab = nums
        heapq.heapify(self.tab)

    def add(self, val: int) -> int:
        heapq.heappush(self.tab, val)
        while len(self.tab) != self.k:
            heapq.heappop(self.tab)
        return self.tab[0] # kth largest is the lowest in the minheap