class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    
        adj_list = collections.defaultdict(list)
        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
    
        timer = 0
        visited = [False] * n
        discovery = [-1] * n  
        low = [-1] * n        
        res = []

        def dfs(node, parent):
            nonlocal timer
            
            visited[node] = True
            discovery[node] = low[node] = timer
            timer += 1
            
            for neighbor in adj_list[node]:
                if neighbor == parent: 
                    continue
                
                if not visited[neighbor]:
            
                    dfs(neighbor, node)
                    
                    low[node] = min(low[node], low[neighbor])
                
                    if low[neighbor] > discovery[node]:
                        res.append([node, neighbor])
                else:
                    low[node] = min(low[node], discovery[neighbor])

        dfs(0, -1)
        return res
