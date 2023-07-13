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

# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree
def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    ref = None
    def dfs(n1, n2):
        nonlocal ref
        if not n1:
            return
        if n1 == target:
            ref = n2
            return
        dfs(n1.left, n2.left)
        dfs(n1.right, n2.right)
    dfs(original, cloned)
    return ref

# https://leetcode.com/problems/range-sum-of-bst/
def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    sums = 0
    def dfs(n):
        nonlocal sums
        if not n:
            return
        dfs(n.left)
        if n.val >= low and n.val <= high:
            sums += n.val
        dfs(n.right)

    dfs(root)
    return sums

# or recursive with optimisation - we can exclude some branches based on value
# def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
#     if not root:
#         return 0
#     if root.val < low:
#         return self.rangeSumBST(root.right, low, high)
#     if root.val > high:
#         return self.rangeSumBST(root.left, low, high)
#     return root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)

# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree
def bstToGst(root: TreeNode) -> TreeNode:
    def dfs(n, sums):
        if not n:
            return sums
        n.val += dfs(n.right, sums)
        return dfs(n.left, n.val)

    dfs(root, 0)
    return root

# https://leetcode.com/problems/balanced-binary-tree
def isBalanced(root: Optional[TreeNode]) -> bool:
    def depth(n):
        if not n:
            return 0
        l = depth(n.left)
        r = depth(n.right)
        return 1 + max(l,r)

    def balanced(n):
        if not n:
            return True
        l = depth(n.left)
        r = depth(n.right)
        return abs(l-r) <= 1 and balanced(n.left) and balanced(n.right)
    
    return balanced(root)

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # find splitting node
    def dfs(n):
        if not n:
            return None
        elif p.val < n.val and q.val < n.val:
            return dfs(n.left)
        elif p.val > n.val and q.val > n.val:
            return dfs(n.right)
        return n
    
    return dfs(root)