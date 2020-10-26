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
            elif v < ptr.val:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = newNode
                    return
            else:
                raise Exception(f'Duplicated value {v}')
    
    def insertRec(self, v:int):

        def create(ptr: Node):
            newNode = Node(v)
            if newNode.val > ptr.val:
                ptr.right = newNode
            else:
                ptr.left = newNode
            return ptr

        def go(ptr: Optional[Node]) -> Node:
            if not ptr:
                self.root = Node(v)
                return self.root
            
            if v > ptr.val:
                return go(ptr.right) if ptr.right else create(ptr)
            elif v < ptr.val:
                return go(ptr.left) if ptr.left else create(ptr)
            else:
                raise Exception(f'Duplicated value {v}')

        go(self.root)

    def find(self, v: int) -> bool:
        ptr: Optional[Node] = self.root

        while ptr:
            if v == ptr.val:
                return True
            elif v < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right
        
        return False

    def findRec(self, v: int) -> bool:
        def go(ptr: Optional[Node]) -> Optional[Node]:
            if not ptr:
                return None
            if v == ptr.val:
                return ptr
            elif v < ptr.val:
                return go(ptr.left)
            return go(ptr.right)

        return go(self.root) is not None

    def traverse(self) -> List[int]:
        pass