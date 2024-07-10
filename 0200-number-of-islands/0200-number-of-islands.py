class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0]*n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and visited[i][j] == 0:
                    count+=1
                    st = [(i,j)]
                    while st:
                        (row,col) = st.pop()
                        if visited[row][col]==1 or grid[row][col] == "0":
                            continue
                        visited[row][col] = 1
                        x = [0, 0, 1, -1]
                        y = [1, -1, 0, 0]
                        for k in range(4):
                            y1 = row + y[k]
                            x1 = col + x[k]
                            if 0<=y1<m and 0<=x1<n and grid[row][col]=="1":
                                st.append((y1,x1))
                else:
                    continue
        return count