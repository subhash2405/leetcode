# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []      
        pq = [(root,0)]
        prev = 0
        maxv = float('-inf')
        res = []
        while pq:
            node, lvl = pq.pop(0)
            if lvl!=prev:
                prev = lvl
                res.append(maxv)
                maxv = node.val
            else:
                maxv = max(maxv, node.val)
            if node.left:
                pq.append((node.left, lvl+1))
            if node.right:
                pq.append((node.right, lvl+1))
        res.append(maxv)
        return res