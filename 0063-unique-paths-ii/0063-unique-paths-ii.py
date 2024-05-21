class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m==1 and n==1:
            return 1 -(obstacleGrid[0][0])
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1- obstacleGrid[0][0]
        for i in range(1,m):
            if obstacleGrid[i][0] == 0 and grid[i-1][0] == 1 :
                grid[i][0] = 1
        for j in range(1,n):
            if obstacleGrid[0][j] == 0 and grid[0][j-1] == 1 :
                grid[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[-1][-1]

