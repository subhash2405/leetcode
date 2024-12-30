class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (high + 1)
        dp[0] = 1 

        for x in range(1, high + 1):
            if x >= zero:
                dp[x] += dp[x - zero]
            if x >= one:
                dp[x] += dp[x - one]
            dp[x] %= MOD

        total = sum(dp[low:high + 1]) % MOD
        return total
