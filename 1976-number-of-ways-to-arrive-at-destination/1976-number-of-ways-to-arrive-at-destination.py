class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj=[[] for i in range(n)]
        for u,v,t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))
        dist=[float('inf')]*n
        ways=[0]*n
        ways[0]=1
        dist[0]=0
        pq=[]
        heapify(pq)
        heappush(pq,(0,0))
        mod=10**9+7
        while pq:
            time,node=heappop(pq)
            for v,t in adj[node]:
                if dist[v]>t+time:
                    dist[v]=t+time
                    heappush(pq,(dist[v],v))
                    ways[v]=ways[node]
                elif dist[v]==t+time:
                    ways[v]=(ways[v]+ways[node])%mod
        return ways[n-1]%mod
