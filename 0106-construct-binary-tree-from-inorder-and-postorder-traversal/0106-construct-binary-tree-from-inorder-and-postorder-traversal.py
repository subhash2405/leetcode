# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder or not postorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)

        ind = inorder.index(root_val)

        root.left = self.buildTree(inorder[:ind], postorder[:ind])
        root.right = self.buildTree(inorder[ind+1:], postorder[ind:-1])

        return root