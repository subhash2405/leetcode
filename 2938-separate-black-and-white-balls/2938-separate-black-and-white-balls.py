class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        temp = 0
        for var in s:
            if var == "0" :
                res+=temp
            else:
                temp+=1
        return res
