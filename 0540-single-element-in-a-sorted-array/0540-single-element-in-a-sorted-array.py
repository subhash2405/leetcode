class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)
        while low<high:
            mid = (low+high)//2
            if mid==0 or mid == len(nums)-1:
                return nums[mid]
            if nums[mid-1] != nums[mid] != nums[mid+1]:
                return nums[mid]
            if nums[mid-1]==nums[mid]:
                if mid%2==0:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if mid%2==0:
                    low = mid+1
                else:
                    high = mid-1
        return nums[high]
        