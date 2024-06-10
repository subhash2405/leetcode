# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        self.postord(root, res)
        return res
    def postord(self, root, res):
        if root == None:
            return
        self.postord(root.left, res)
        self.postord(root.right, res)
        res.append(root.val)