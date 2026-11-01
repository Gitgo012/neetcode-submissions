# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val: i for i, val in enumerate(inorder)}   # value -> inorder index
        self.pre = 0                                       # next root in preorder

        def build(lo, hi):                                 # inorder range [lo, hi]
            if lo > hi:
                return None
            root_val = preorder[self.pre]
            self.pre += 1
            root = TreeNode(root_val)
            mid = idx[root_val]
            root.left = build(lo, mid - 1)                 # left MUST be built first
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)