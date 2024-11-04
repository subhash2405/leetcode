class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        flowers = [0]*n
        grid = [[] for _ in range(n)]
        for (u,v) in paths:
            grid[u-1].append(v-1)
            grid[v-1].append(u-1)
        
        def check(node, flower):
            for var in grid[node]:
                if flowers[var] == flower:
                    return False
            return True
        
        def recr(node):
            if node == n:
                return flowers

            for i in range(1,5):
                if check(node, i):
                    flowers[node] = i
                    if recr(node+1):
                        return flowers
                    flowers[node] = 0
        
        return recr(0)