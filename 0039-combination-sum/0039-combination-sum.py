class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.rec(0,[],candidates, res, target)
        return res

    

    def rec(self, add, subset, candidates, res, target):
        if add == target:
            subset.sort()
            if subset not in res:
                res.append(subset)
            return res
        if (add>target) or (min(candidates)+add>target):
            return res
        for i in range(len(candidates)):
            sub1 = subset.copy()
            sub1.append(candidates[i])
            self.rec(add + candidates[i],sub1, candidates, res, target )
        return res
        
            