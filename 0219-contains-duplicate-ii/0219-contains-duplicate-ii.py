class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index = {}  
        for i in range(len(nums)):
            num = nums[i]
            if num in num_index and i - num_index[num] <= k:
                return True
            num_index[num] = i

        return False
