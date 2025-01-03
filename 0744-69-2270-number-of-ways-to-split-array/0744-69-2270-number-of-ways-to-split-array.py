class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        add = sum(nums)
        res = 0
        curr = 0
        for i in range(len(nums)-1):
            curr+=nums[i]
            if curr>=add-curr:
                res+=1
        return res