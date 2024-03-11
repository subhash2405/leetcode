class Solution:
    def customSortString(self, order: str, s: str) -> str:
        arr=Counter(s)
        res=""
        for i in range(len(order)):
            if order[i] in arr:
                res+=order[i]*arr[order[i]]
                arr[order[i]]=0
        for i in range(len(s)):
            if arr[s[i]]!=0:
                res+=s[i]*arr[s[i]]
                arr[s[i]]=0
        return res
