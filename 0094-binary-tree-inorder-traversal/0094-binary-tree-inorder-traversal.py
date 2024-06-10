# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        self.inord(root, res)
        return res
    def inord(self, root, res):
        if root == None:
            return
        self.inord(root.left, res)
        res.append(root.val)
        self.inord(root.right, res)