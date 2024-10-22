# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        dic = {}

        def level(root, ht):
            if not root:
                return 
            if ht in dic:
                dic[ht]+=root.val
            else:
                dic[ht] = root.val
            
            level(root.left, ht+1)
            level(root.right, ht+1)
            return 
        
        level(root, 0)
        res = list(dic.values())

        if k>len(res):
            return -1
            
        res.sort(reverse = True)
    
        return res[k-1]