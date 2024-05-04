class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(1)==len(nums):
            return len(nums)-1
        res=[]
        cnt=0
        for i in nums:
            if i==1:
                cnt+=1
            else:
                res.append(cnt)
                cnt=0
        res.append(cnt)
        maxi=res[0]
        for i in range(1,len(res)):
            if res[i]+res[i-1]>maxi:
                maxi=res[i]+res[i-1]
        return maxi