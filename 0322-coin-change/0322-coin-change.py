class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count=[float('inf')]*(amount+1)
        count[0]=0
        coins.sort()
        for i in range(1,amount+1):
            for j in coins:
                if j>i:
                    # if count[i]==float('inf'):
                    #     count[i]=-1
                    break
                if count[i-j]==-1:
                    continue
                else:    
                    count[i]=min(count[i],count[i-j]+1)
            if count[i]==float('inf'):
                count[i]=-1
        return count[amount]
            

        