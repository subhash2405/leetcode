class Solution:
    def numSquares(self, n: int) -> int:
        arr=[]
        for i in range(1,int(n**0.5)+1):
            arr.append(i**2)
        count=[float('inf')]*(n+1)
        count[0]=0
        for i in range(1,n+1):
            for j in arr:
                if j>i:
                    break
                count[i]=min(count[i],count[i-j]+1)
        return count[n]