class Solution:
    def maxScore(self, s: str) -> int:
        arr = [0]*len(s)
        arr[-1]=1 if s[-1]=='1' else 0
        for i in range(len(s)-2,0,-1):
            if s[i]=='1':
                # print(1)
                arr[i] = 1
            arr[i]+=arr[i+1]
        maxc = 0
        zero = 0
        for i in range(len(s)):
            maxc = max(maxc, arr[i]+zero)
            if s[i]=='0':
                zero+=1
        return maxc
        
            