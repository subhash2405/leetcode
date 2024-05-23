class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        path = float('inf')
        n = len(matrix)
        for i in range(n):
            path = min(path, self.minpath(dp, matrix, n-1,i))
        return path

    def minpath(self, dp, matrix, n, i):
        k = len(matrix)
        if i<0 or i>=k:
            return float('inf')

        if dp[n][i] != None:
            return dp[n][i]
        if n == 0:
            return matrix[n][i]

        maxp = float('inf')
        for j in range(i-1, i+2):
            maxp = min(maxp, self.minpath(dp,matrix,n-1,j) + matrix[n][i])
        dp[n][i] = maxp
        return maxp