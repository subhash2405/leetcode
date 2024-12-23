class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums[0]-=k
        for i in range(1,len(nums)):
            if nums[i]-k>nums[i-1]:
                nums[i]-=k
            elif nums[i-1]+1<=nums[i]+k:
                nums[i]=nums[i-1]+1
            else:
                nums[i]=nums[i-1]
        return len(set(nums))