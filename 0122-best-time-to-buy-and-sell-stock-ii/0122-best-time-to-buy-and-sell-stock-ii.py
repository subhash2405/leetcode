class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[None for _ in range(2)] for _ in range(len(prices))]
        return max(-prices[0] + self.stock(prices,dp, 1, 0), self.stock(prices,dp, 0, 1))
    

    def stock(self,prices,dp,n,stat):
        if n == len(prices):
            return 0
        if dp[n][stat]!=None:
            return dp[n][stat]
        if stat == 1:
            dp[n][stat] = max(-prices[n]+self.stock(prices,dp,n+1,0), self.stock(prices, dp,n+1, 1))
            return dp[n][stat]
        dp[n][stat] = max(prices[n]+self.stock(prices, dp, n+1, 1), self.stock(prices, dp, n+1, 0))
        return dp[n][stat]