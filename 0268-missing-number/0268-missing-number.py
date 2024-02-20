class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=len(nums)
        y=(x*(x+1))//2
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
        return y-sum
        
        