# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.add(root, 0)
        return root

    def add(self, node, count):
        if node is None:
            return count
        count = self.add(node.right, count)
        node.val += count
        count = node.val
        return self.add(node.left, count)
