# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        temp = root
        ht = 0
        return self.height(root, 0)
    def height(self, root, ht):
        if root == None:
            return ht
        return max(self.height(root.left,ht+1), self.height(root.right, ht+1))