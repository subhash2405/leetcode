# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            nonlocal max_depth, leftmost_value
            if not root:
                return
            if depth > max_depth:
                max_depth = depth
                leftmost_value = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        max_depth = -1
        leftmost_value = -1
        dfs(root, 0)
        return leftmost_value
