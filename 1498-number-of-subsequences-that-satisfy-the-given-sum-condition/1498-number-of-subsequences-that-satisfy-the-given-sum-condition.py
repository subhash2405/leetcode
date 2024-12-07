from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        def binsearch(target, left):
            low, high = left, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return high
        
        count = 0
        for i in range(len(nums)):
            max_val = target - nums[i]
            j = binsearch(max_val, i)
            if j >= i:         
                count += (1 << (j - i))  

        return count % (10**9 + 7)  