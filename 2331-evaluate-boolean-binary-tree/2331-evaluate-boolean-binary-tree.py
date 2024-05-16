class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0  or root.val == 1:
            return root.val == 1
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
