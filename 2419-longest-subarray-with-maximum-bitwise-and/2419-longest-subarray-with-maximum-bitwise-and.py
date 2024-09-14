class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxnum = max(nums)
        count = 0
        maxc = 0
        for num in nums:
            if num == maxnum:
                count+=1
                maxc = max(maxc, count)
            else:
                count = 0
        return maxc