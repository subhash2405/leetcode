# Good math intution that to find the longest distance in a simple undirected acyclic graph start from any node find the longest dist and from that node find the longest dist the dist b/w the 2nd and 3nd is the diameter

# Because the farthest nodes are always the farthest for any node in the graph so when we run bfs for the first time we get the first end and second time we reach the second end
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        adj_matrix1 = [[] for _ in range(len(edges1)+1)]
        adj_matrix2 = [[] for _ in range(len(edges2)+1)]

        for (u,v) in edges1:
            adj_matrix1[u].append(v)
            adj_matrix1[v].append(u)
        
        for (u,v) in edges2:
            adj_matrix2[u].append(v)
            adj_matrix2[v].append(u)
        

        def longest_dist(n, adj_matrix):
            pq = [(0,0)]
            visited = set()
            prev = 0
            while pq:
                x,dist = pq.pop(0)
                if x in visited:
                    continue
                prev = x
                visited.add(x)
                for i in adj_matrix[x]:
                    pq.append((i, dist+1))
            st = [(prev,0)]
            maxd = 0
            arr = set()
            while st:
                x,dist = st.pop(0)
                maxd = max(dist, maxd)
                if x in arr:
                    continue
                arr.add(x)
                for i in adj_matrix[x]:
                    st.append((i, dist+1))
            return maxd-1
        
        d1 = longest_dist(len(edges1)+1, adj_matrix1)
        d2 = longest_dist(len(edges2)+1, adj_matrix2)
        print(d1, d2)
        return max(d1, d2, ((d1+1)//2)+ ((d2+1)//2) +1 )
            