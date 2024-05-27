class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nodes = len(grid)
        var = len(grid[0])
        minute = 0
        visited = [[0 for _ in range(var)]for _ in range(nodes)]
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        queue = []     
        for u in range(nodes):
            for v in range(var):
                if grid[u][v] == 2:
                    queue.append((u,v,0))
                    visited[u][v] = 2
        while queue:
            (u,v,minute) = queue.pop(0)
            for x in range(len(dx)):
                nx = u + dx[x]
                ny = v + dy[x]
                if(nx < 0 or ny < 0 or nx >= nodes or ny >= var or grid[nx][ny] != 1 or visited[nx][ny] == 2):
                    continue
                visited[nx][ny] = 2
                queue.append((nx,ny,minute+1))
        for u in range(nodes):
            for v in range(var):
                if grid[u][v] == 1 and visited[u][v] == 0:
                    return -1
        return minute







        