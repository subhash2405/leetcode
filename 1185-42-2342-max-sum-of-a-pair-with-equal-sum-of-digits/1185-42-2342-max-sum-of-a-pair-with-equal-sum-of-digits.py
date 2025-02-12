class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort()
        dic = {}
        keys = []
        for num in nums:
            var = str(num)
            a = 0
            for i in var:
                a+=int(i)
            if a in dic:
                dic[a].append(num)
            else:
                dic[a] = [num]
                keys.append(a)
        maxs = -1
        for key in keys:
            if len(dic[key])>1:
                maxs = max(maxs, dic[key][-1]+dic[key][-2])
        return maxs