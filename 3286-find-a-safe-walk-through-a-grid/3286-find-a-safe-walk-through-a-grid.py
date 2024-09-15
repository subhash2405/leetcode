class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        if grid[0][0]==1:
            pq = [(0,0,health-1)]
        else:
            pq = [(0,0, health)]
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)]for _ in range(m)]
        while pq:
            (x, y, remaining) = pq.pop()
            # print(x,y, remaining)
            if remaining == 0 or remaining<=visited[x][y]:
                continue
            visited[x][y] = remaining
            if (x,y) == (m-1, n-1) and remaining>0:
                # print(remaining)
                return True
            nx = [1,-1,0,0]
            ny = [0,0,1,-1]
            for i in range(4):
                if 0<=x + nx[i]<m and 0<=y + ny[i]<n:
                    a = x + nx[i]
                    b = y + ny[i]
                    if grid[a][b] == 1:
                        pq.append((a,b,remaining-1))
                    else:
                        pq.append((a,b,remaining))
        return False
            