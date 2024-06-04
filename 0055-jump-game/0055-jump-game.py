class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        dp = [None]*len(nums)
        return self.jump(0, nums, dp)

    def jump(self, index,nums, dp):
        if index >= len(nums)-1:
            return True
        if dp[index]!=None:
            return dp[index]
        if  nums[index] == 0:
            dp[index] = False
            return False
        var = False
        for i in range(1,nums[index]+1):
            if index+i<len(nums) and dp[index+i]!=None :
                var+=dp[index+i]
            else:
                var += self.jump(index+i, nums, dp)
            if var == True:
                break
        dp[index] = var
        return var
        