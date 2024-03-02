class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     nums[i]=nums[i]**2
        # nums.sort()
        # return nums
        start=0
        end=len(nums)-1
        res=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[start]**2>nums[end]**2:
                res[i]=nums[start]**2
                start+=1
            else:
                res[i]=nums[end]**2
                end-=1
        return res