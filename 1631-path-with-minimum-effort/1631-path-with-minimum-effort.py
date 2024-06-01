class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        dist = [[float('inf')for _ in range(cols)]for _ in range(rows)]
        pq = [(0,0,0)]
        dist[0][0] = 0
        while pq:
            effort, u, v = heappop(pq)
            if u == rows-1 and v == cols -1:
                return effort
            for i in range(4):
                x = u + directions[i][0]
                y = v + directions[i][1]
                if 0<=x<rows and 0<=y<cols:
                    distance = max(effort, abs(heights[u][v] - heights[x][y]))
                    if distance < dist[x][y]:
                        dist[x][y] = distance
                        heappush(pq, (distance, x, y))
        
                    