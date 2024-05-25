from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if total_sum < abs(target):
            return 0
        
        dp = {}
        return self.oper(nums, dp, len(nums)-1, target)
    
    def oper(self, nums, dp, n, target):
        if n == -1:
            return 1 if target == 0 else 0
        
        if (n, target) in dp:
            return dp[(n, target)]
        
        positive = self.oper(nums, dp, n-1, target-nums[n])
        negative = self.oper(nums, dp, n-1, target+nums[n])
        
        dp[(n, target)] = positive + negative
        return dp[(n, target)]
