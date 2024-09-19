class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        dp0 = [0] * n
        dp1 = [0] * n
        dp2 = [0] * n
        dp3 = [0] * n
        
        dp0[0] = a[0] * b[0]
        for i in range(1, n):
            dp0[i] = max(dp0[i - 1], a[0] * b[i])

        dp1[1] = dp0[0] + a[1] * b[1]
        for i in range(2, n):
            dp1[i] = max(dp1[i - 1], dp0[i - 1] + a[1] * b[i])

        dp2[2] = dp1[1] + a[2] * b[2]
        for i in range(3, n):
            dp2[i] = max(dp2[i - 1], dp1[i - 1] + a[2] * b[i])

        dp3[3] = dp2[2] + a[3] * b[3]
        maxScore = dp3[3]
        for i in range(4, n):
            dp3[i] = max(dp3[i - 1], dp2[i - 1] + a[3] * b[i])
            maxScore = max(maxScore, dp3[i])
        
        return maxScore