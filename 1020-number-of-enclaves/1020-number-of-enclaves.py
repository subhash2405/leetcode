class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)]for _ in range(m)]
        st = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i==0 or j==0 or i==m-1 or j==n-1):
                    st.append((i,j))
        while st:
            (u,v) = st.pop()
            if visited[u][v] == 1:
                continue
            visited[u][v]=1
            if grid[u][v] == 1:
                nx = [-1,1,0,0]
                ny = [0,0,1,-1]
                for i in range(4):
                    if 0<=u+nx[i]<m and 0<=v+ny[i]<n:
                        st.append((u+nx[i],v+ny[i]))
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and visited[i][j]==0:
                    count+=1
        return count