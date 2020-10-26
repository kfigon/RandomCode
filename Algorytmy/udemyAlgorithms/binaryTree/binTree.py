from typing import Optional, List

class Node:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, v: int):
        newNode = Node(v)
        if not self.root:
            self.root = newNode
            return
        
        ptr = self.root
        while ptr:
            if v > ptr.val:
                if ptr.right:
                    ptr = ptr.right
                else:
                    ptr.right = newNode
                    return
            else:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = newNode
                    return
    
    def insertRec(self, v:int):
        newNode = Node(v)
        def go(ptr: Node) -> Node:
            if newNode.val > ptr.val:
                return go(ptr.right) if ptr.right else ptr
            else:
                return go(ptr.left) if ptr.left else ptr

        if not self.root:
            self.root = newNode
            return
                    
        ptr = go(self.root)
        if newNode.val > ptr.val:
            ptr.right = newNode
        else:
            ptr.left = newNode

    def find(self) -> Optional[int]:
        pass

    def traverse(self) -> List[int]:
        pass