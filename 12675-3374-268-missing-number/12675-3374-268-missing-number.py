class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        x = (n*(n+1))//2
        curr = sum(nums)
        return x - curr