from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [0] * n
        
        def dfs(node):
            if safe[node] != 0:
                return safe[node] == 2
            safe[node] = 1  
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            safe[node] = 2  
            return True
        
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        
        return res
