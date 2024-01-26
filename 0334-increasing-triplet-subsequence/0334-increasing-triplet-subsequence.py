from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        l = j = float('inf')

        for num in nums:
            if num <= l:
                l = num
            elif num <= j:
                j = num
            else:
                return True

        return False
