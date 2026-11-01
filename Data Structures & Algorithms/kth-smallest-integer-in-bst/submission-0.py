# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            while curr:                  # go as far left as possible
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()           # visit the next smallest node
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right            # then explore its right subtree