class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        self.combine(nums, res, 0, sub)
        return res


    def combine(self, nums, res, index, sub):
        if index == len(nums):
            res.append(sub.copy())
            return 
        for i in range(len(nums)):
            if nums[i] not in sub:
                sub.append(nums[i])
                self.combine(nums, res, index+1, sub)
                sub.pop()
        return 