class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[[-float('inf') for _ in range(2)] for _ in range(3)] for _ in range(n)]
        return self.stock(prices, dp, 2, 0, 0)

    def stock(self, prices, dp, trans, day, bought):
        if trans < 0 or day >= len(prices):
            return 0
        if dp[day][trans][bought] != -float('inf'):
            return dp[day][trans][bought]

        if bought:  
            dp[day][trans][bought] = max(prices[day] + self.stock(prices, dp, trans, day + 1, 0),
                                         self.stock(prices, dp, trans, day + 1, 1))
        else: 
            if trans > 0:  
                dp[day][trans][bought] = max(-prices[day] + self.stock(prices, dp, trans - 1, day + 1, 1),
                                             self.stock(prices, dp, trans, day + 1, 0))
            else:  
                dp[day][trans][bought] = self.stock(prices, dp, trans, day + 1, 0)

        return dp[day][trans][bought]

