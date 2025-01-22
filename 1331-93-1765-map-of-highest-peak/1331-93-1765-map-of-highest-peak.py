class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        visited = [[-1 for _ in range(n)] for _ in range(m)]  
        res = [[float('inf') for _ in range(n)] for _ in range(m)]  
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    visited[i][j] = 1
                    res[i][j] = 0  
        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and visited[ni][nj] == -1:
                    res[ni][nj] = res[i][j] + 1
                    visited[ni][nj] = 1
                    queue.append((ni, nj))
        
        return res
