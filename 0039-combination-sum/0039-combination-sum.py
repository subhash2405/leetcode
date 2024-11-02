class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def check(temp, add, index):
            if add == target:
                res.append(temp)
                return 
            elif add>target or index==len(candidates):
                return 
            var = temp.copy()
            var.append(candidates[index])
            check(var, add+candidates[index], index)
            check(temp, add, index+1)

        check([],0,0)
        return res
