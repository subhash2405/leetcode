class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total=sum(nums)
        count=0
        for i in range(len(nums)):
            total-=nums[i]
            if total>nums[i] and len(nums)-count+1>3:
                return total+nums[i]
            count+=1
        return -1
