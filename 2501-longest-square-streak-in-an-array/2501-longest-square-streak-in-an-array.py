class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        temp = set(nums)
        maxcount = 0
        for var in nums:
            count = 1
            x = var
            while x**2 in temp: 
                x = x**2
                count+=1
            maxcount = max(maxcount, count)
        
        if maxcount == 1:
            return -1
        return maxcount