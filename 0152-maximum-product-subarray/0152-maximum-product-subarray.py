class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = min_p = ans = nums[0]
        for i in range(1,len(nums)):
            a = nums[i]*max_p
            b = nums[i]*min_p
            max_p = max(a , b, nums[i])
            min_p = min(a, b, nums[i])
            ans = max(ans, max_p)
        return ans
            