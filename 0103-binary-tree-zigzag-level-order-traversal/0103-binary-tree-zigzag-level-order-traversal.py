# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        pq = [(root,0)]
        prev = 0
        val = []
        while pq:
            (temp,lvl) = pq.pop(0)
            if lvl==prev:
                val.append(temp.val)
            else:
                prev = lvl
                res.append(val)
                val = [temp.val]
            if temp.left:
                pq.append((temp.left,lvl+1))
            if temp.right:
                pq.append((temp.right, lvl+1))
        res.append(val)
        ans = []
        print(res)
        for i in range(len(res)):
            if i%2==0:
                ans.append(res[i])
            else:
                res[i].reverse()
                ans.append(res[i])
        return ans