# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def rec(n):
            if not n:
                return (0, float('-inf'))
            lp, lm = rec(n.left)
            rp, rm = rec(n.right)
            p = max(lp, rp, 0) + n.val
            return (p, max(lm, rm, p, max(lp+rp, 0) + n.val))
        rp, rm = rec(root)
        return max(rp, rm)
