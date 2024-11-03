class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        st = [(0, 0, 0, 0)]  
        visited = [[float('inf')] * m for _ in range(n)]
        visited[0][0] = 0

        while st:
            time, x, y, index = heapq.heappop(st)
            if x == n - 1 and y == m - 1:
                return time

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                a, b = x + dx, y + dy
                if 0 <= a < n and 0 <= b < m:
                    next_time = time + (1 if index == 0 else 2)
                    if moveTime[a][b] > time:
                        next_time = moveTime[a][b] + (1 if index == 0 else 2)

                    if next_time < visited[a][b]:
                        visited[a][b] = next_time
                        heapq.heappush(st, (next_time, a, b, 1 - index))

        return visited[-1][-1]
