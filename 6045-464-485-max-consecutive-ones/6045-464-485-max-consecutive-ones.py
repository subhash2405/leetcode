class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxv = 0
        count = 0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                maxv = max(count, maxv)
                count = 0
        return max(maxv, count)