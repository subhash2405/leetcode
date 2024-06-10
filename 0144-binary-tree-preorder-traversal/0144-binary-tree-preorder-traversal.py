# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        self.pre(root, res)
        return res
        
    def pre(self, root,res):
        if root==None:
            return 
        res.append(root.val)
        self.pre(root.left,res)
        self.pre(root.right,res)