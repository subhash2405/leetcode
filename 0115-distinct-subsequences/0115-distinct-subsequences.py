class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def recr(temp, point, check, dic):
            if temp == t:
                return 1
            if point == len(s):
                return 0
            if (point, check) in dic:
                return dic[(point, check)]
            var = temp
            if s[point] == t[check]:
                var = temp + s[point]
                dic[(point, check)] = recr(var, point+1, check+1, dic) + recr(temp, point+1, check, dic) 
                return dic[(point, check)]
            else:
                dic[(point, check)] = recr(var, point+1, check, dic)
                return dic[(point, check)]
        return recr("", 0, 0, {})