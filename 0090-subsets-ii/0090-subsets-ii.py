class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.rec(0,len(nums),[],nums, res)
        return res


    def rec(self, index, n, subset, nums, res):
        if index == n:
            subset.sort()
            if subset not in res:
                res.append(subset)
            return res
        sub1 = subset.copy()
        sub1.append(nums[index])
        self.rec(index+1, n, sub1,nums, res)
        self.rec(index +1, n, subset,nums, res)
        return res