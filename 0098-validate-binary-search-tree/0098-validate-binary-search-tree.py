# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(temp, low, up):
            if not temp:
                return True
            
            return (low<temp.val<up) and check(temp.left, low, temp.val) and check(temp.right, temp.val, up)
        
        return check(root, float('-inf'), float('inf'))