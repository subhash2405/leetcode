class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxv = values[0]
        res = float('-inf')
        for i in range(1,len(values)):
            res = max(res, values[i]-i+maxv)
            maxv = max(maxv, values[i]+i)
        return res