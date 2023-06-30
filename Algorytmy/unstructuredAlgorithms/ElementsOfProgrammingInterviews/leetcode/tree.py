from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    #dfs
    def inv(node):
        if not node:
            return
        inv(node.left)
        inv(node.right)

        node.left,node.right = node.right,node.left

    inv(root)
    return root

def maxDepth(root: Optional[TreeNode]) -> int:
    # dfs
    def maks(node, maxD) -> int:
        if not node:
            return maxD
        l = maks(node.left, maxD + 1)
        r = maks(node.right, maxD + 1)
        return max(l, r)
        
    return maks(root, 0)

def maxDepth(root: Optional[TreeNode]) -> int:
    # dfs
    def maks(node) -> int:
        if not node:
            return 0
        return 1+ max(maks(node.left), maks(node.right))
        
    return maks(root)