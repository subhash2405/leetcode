# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        maxh = [0]
        def check(root):
            if not root:
                return 0
            
            lhs = check(root.left)
            rhs = check(root.right)
            maxh[0] = max(maxh[0], lhs+rhs)
            return 1+max(lhs, rhs)
        check(root)
        return maxh[0]
