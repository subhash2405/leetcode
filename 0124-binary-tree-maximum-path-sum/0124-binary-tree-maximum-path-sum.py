# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxp = float('-inf')
        def check(root):
            if not root:
                return 0
            
            left = max(check(root.left),0)
            right =  max(check(root.right),0)
            self.maxp = max(self.maxp, root.val + left+right)
            return root.val + max(left, right) 
        check(root)
        return self.maxp