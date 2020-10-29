from typing import List, Optional, Tuple, Callable

# BinaryHeap is kind of binarySearchTree (2 nodes)
# maxBinaryHeap - parent is always larger than children nodes
# minBinaryHeap - parent is always smaller than childen nodes

# BST moze byc jedna galezia, bardzo wysoka, bez rozgalezien
# Heap jest zbalansowany

class Node:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None

class BinaryHeap:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, v: int):
        newNode = Node(v)
        if not self.root:
            self.root = newNode
            return
        
        ptr = self.root
        while ptr:
            assert ptr.val != v

            if v < ptr.val:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = newNode
                    newNode.parent=ptr
                    break
            else:
                if ptr.right:
                    ptr = ptr.right
                else:
                    ptr.right = newNode
                    newNode.parent = ptr
                    break
        
        # bubble up:
        ptr = newNode
        parent = newNode.parent
        while parent and parent.val < v:
            ptr.val,parent.val = parent.val,ptr.val
            ptr = parent
            parent = parent.parent

    def extractMax(self) -> Optional[int]:
        if not self.root:
            return None

        
        toRet = self.root.val
        minimum = self.findMinimumNode()
        assert minimum
        assert minimum.parent

        self.root.val = minimum.val
        if minimum.parent.left and minimum.parent.left.val == minimum.val:
            minimum.parent.left = None
        elif minimum.parent.right and minimum.parent.right.val == minimum.val:
            minimum.parent.right = None
        minimum.parent = None

        minimum = self.root
        while minimum:
            maxNode = None
            left = minimum.left
            right = minimum.right
            if not right and not left:
                break
            elif not right and left:
                maxNode = left
            elif not left and right:
                maxNode = right
            else:
                assert right
                assert left
                maxNode = left if left.val > right.val else right
            
            assert maxNode

            if maxNode.val > minimum.val:
                minimum.val, maxNode.val = maxNode.val, minimum.val
                minimum = maxNode
                maxNode.parent = minimum.parent
            else:
                break


        return toRet

    def findMinimumNode(self) -> Optional[Node]:
        if not self.root:
            return None

        minV = self.root.val
        minNode = self.root

        while minNode:
            left = minNode.left
            right = minNode.right
            
            if not left and not right:
                break

            if left and left.val < minV:
                minV = left.val
                minNode = left

            if right and right.val < minV:
                minV = right.val
                minNode = right


        return minNode

    def find(self, v: int) -> bool:
        ptr: Optional[Node] = self.root

        while ptr:
            if ptr.val == v:
                return True
            ptr = ptr.left if v < ptr.val else ptr.right

        return False


# get child:
# x * 2 + 1 
# x * 2 + 2

# get parent:
# (n-1)//2

# 0 -> 1,2
# 1 -> 3,4
# 2 -> 5,6
# 3 -> 7,8
# 4 -> 9,10
# 5 -> 11,12
class BinaryHeapArray:
    def __init__(self):
        self.tab: List[int] = []

    def getChild(self, idx: int) -> Tuple[Optional[int], Optional[int]]:
        assert idx < len(self.tab) and idx >= 0, f'invalid idx: {idx}, len: {len(self.tab)}'
        
        adjust: Callable[[int],Optional[int]] = lambda x: x if x < len(self.tab) else None
        left = 2*idx + 1
        right = 2*idx + 2        
        return adjust(left), adjust(right)

    def getParent(self, idx: int) -> Optional[int]:
        if idx < 0 or idx >= len(self.tab):
            return None

        parentIdx = (idx-1)//2
        if parentIdx >= 0 and parentIdx < len(self.tab):
            return parentIdx
        return None
    
    # add to the end and bubble up
    def insert(self, v: int):
        newValueIdx = len(self.tab)
        self.tab.append(v)

        parentIdx = self.getParent(newValueIdx)
        while (parentIdx is not None) and (v > self.tab[parentIdx]):
            self.tab[newValueIdx],self.tab[parentIdx] = self.tab[parentIdx], self.tab[newValueIdx]
            newValueIdx = parentIdx
            parentIdx = self.getParent(newValueIdx)

    def find(self, v: int) -> bool:
        for i in self.tab:
            if i == v:
                return True
        return False

    # wyjac root, wsadzic tam ostatni element i 
    # kopcowac - wrzucic na dol, dobra wartosc wypaczkuje
    def extractMax(self) -> Optional[int]:
        if len(self.tab) == 0:
            return None
        
        top = self.tab[0]
        self.tab = [self.tab[-1]] + self.tab[1:-1]
        
        newIdx = 0
        # kopcujemy
        while True:
            left,right = self.getChild(newIdx)
            maxIdx = -1

            if left is None and right is not None:
                maxIdx = right
            elif right is None and left is not None:
                maxIdx = left
            elif right is not None and left is not None:
                maxIdx = left if self.tab[left] > self.tab[right] else right
            else:
                break

            if self.tab[maxIdx] > self.tab[newIdx]:
                self.tab[maxIdx], self.tab[newIdx] = self.tab[newIdx], self.tab[maxIdx]
                newIdx = maxIdx
            else:
                break

        return top
