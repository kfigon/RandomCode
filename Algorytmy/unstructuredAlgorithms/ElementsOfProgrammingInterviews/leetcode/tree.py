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

# https://leetcode.com/problems/increasing-order-search-tree/description/
def increasingBST(root: TreeNode) -> TreeNode:
    els = []
    def dfs(n):
        nonlocal els
        if not n:
            return
        dfs(n.left)
        els.append(n.val)
        dfs(n.right)

    dfs(root)
    v = root
    for i,val in enumerate(els):
        v.left = None
        v.val = val
        if not v.right and i != len(els)-1:
            v.right = TreeNode()
        v = v.right
    
    return root