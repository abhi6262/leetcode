# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        colmin, colmax = 0, 0
        verMap = defaultdict(list)
        def dfs(node, column, depth):
            if not node:
                return
            verMap[column].append((depth, node.val))
            nonlocal colmin, colmax
            colmin = min(colmin, column)
            colmax = max(colmax, column)
            dfs(node.left, column - 1, depth + 1)
            dfs(node.right, column + 1, depth + 1)
        dfs(root, 0, 0)
        output = []
        for column in range(colmin, colmax + 1):
            curr = verMap[column]
            curr.sort()
            curr = [x[1] for x in curr]
            output.append(curr)
        return output
