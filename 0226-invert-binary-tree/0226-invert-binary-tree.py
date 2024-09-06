# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        head = root

        def change(root):
            if not root:
                return 
            temp = root.left
            root.left = root.right
            root.right = temp
            change(root.right)
            change(root.left)
            return root
        
        change(head)
        return head