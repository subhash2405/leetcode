# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=[root]
        ans=[]
        while q:
            n=len(q)
            lis=[]
            for i in range(n):
                a=q.pop(0)
                if a:
                    lis.append(a.val)
                    q.append(a.left)
                    q.append(a.right)
            if lis:
                ans.append(lis)
        return ans
