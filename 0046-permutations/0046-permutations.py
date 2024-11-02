class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def check(temp):
            if len(temp) == len(nums):
                res.append(temp[:])
            
            for i in nums:
                if i not in temp:
                    temp.append(i)
                    check(temp)
                    temp.pop()
        
        for i in nums:
            check([i])
        return res