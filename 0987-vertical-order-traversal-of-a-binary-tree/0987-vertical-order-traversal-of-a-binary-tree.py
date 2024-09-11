class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(lambda: [])
        
        def traverse(node, x, y):
            if not node:
                return
            mp[x].append((y, node.val))
            traverse(node.left, x-1, y+1)
            traverse(node.right, x+1, y+1)
        
        traverse(root, 0, 0)
        
        result = []
        # print(mp)
        for x in sorted(mp.keys()):
            mp[x].sort()
            # print(mp[x])
            result.append([val for _, val in mp[x]])
        
        return result