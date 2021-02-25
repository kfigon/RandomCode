
class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Node = None
        self.right: Node = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val: int):
        newNode = Node(val)
        if self.root is None:
            self.root = newNode
            return

        ptr = self.root
        while ptr:
            if val < ptr.val:
                if ptr.left is None:
                    ptr.left = newNode
                    return
                ptr = ptr.left
            else:
                if ptr.right is None:
                    ptr.right = newNode
                    return
                ptr = ptr.right

    def getHeight(self) -> int:
        pass