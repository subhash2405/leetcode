# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(root, other):
            if not root and not other:
                return True
            elif not root or not other:
                return False
            if root.val!=other.val:
                return False
            return check(root.right, other.left) and check(root.left, other.right)
        
        return check(root.right, root.left)