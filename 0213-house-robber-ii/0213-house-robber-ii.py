class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[-1]
        if len(nums)==2:
            return max(nums)
        dp1=[0]*(len(nums)-1)
        dp2=[0]*(len(nums))
        dp2[1]=nums[1]
        dp1[0]=nums[0]
        dp1[1]=max(nums[0],nums[1])
        for i in range(2,len(dp1)):
            dp1[i]=max(dp1[i-2]+nums[i],dp1[i-1])
        dp2[2]=max(nums[1],nums[2])
        for i in range(3,len(dp2)):
            dp2[i]=max(dp2[i-2]+nums[i],dp2[i-1])
        return max(dp1[-1],dp2[-1])