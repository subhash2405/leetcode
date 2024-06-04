class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n-1>len(connections):
            return -1
        visited = set()
        clusters = 0
        adj_list = [[]for _ in range(n)]
        for (u,v) in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
    
        for nodes in range(n):
            if nodes in visited:
                continue
            clusters+=1
            st = [nodes]
            while st:
                node = st.pop()
                if node in visited:
                    continue
                visited.add(node)
                for var in adj_list[node]:
                    st.append(var)
           
        clusters-=1
        return clusters
        