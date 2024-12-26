from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(index,curr):
            if index==len(nums):
                return 1 if curr==target else 0

            if (index,curr) in memo:
                return memo[(index,curr)]

            add = dp(index+1, curr+nums[index])
            sub = dp(index+1, curr-nums[index])

            memo[(index, curr)] = add+sub

            return memo[(index,curr)]
        
        return dp(0,0)