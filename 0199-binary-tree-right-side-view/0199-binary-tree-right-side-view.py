# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        self.right(root,0,res)
        return res
    def right(self, root, height,res):
        if root is not None:
            if height == len(res):
                res.append(root.val)
            self.right(root.right, height+1,res)
            self.right(root.left, height+1, res)
        return