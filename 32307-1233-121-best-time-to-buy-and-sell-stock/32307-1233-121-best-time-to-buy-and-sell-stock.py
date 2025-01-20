class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mina = prices[0]
        maxa = 0
        for i in range(1,len(prices)):
            maxa = max(maxa, prices[i]-mina)
            if prices[i]<mina:
                mina = prices[i]
        return maxa
