class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        sum_count = nums[0]
        min_len = float('inf')
        while r <= len(nums) - 1:
            if sum_count < target:
                r += 1
                if r <= len(nums) - 1:
                    sum_count += nums[r]
            else:
                min_len = min(min_len, r-l + 1)
                sum_count -= nums[l]
                l += 1
        if min_len == float('inf'):
            return 0
        return min_len


        