# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dic = {}
        self.bfs(root, dic, 1)
        arr = dic.items()
        temp = sorted(arr, key = lambda x: x[1], reverse = True)
        return temp[0][0]

    def bfs(self, root, dic, level):
        if root:
            if level not in dic:
                dic[level] = root.val
            else:
                dic[level]+=root.val
        
            self.bfs(root.right, dic, level+1)
            self.bfs(root.left, dic, level+1)
        return dic