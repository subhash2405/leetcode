class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = ''.join(sorted(s)) 
        t = ''.join(sorted(t)) 
        for i in range(len(t)-1):
            if t[i]!=s[i]:
                return t[i]
        return t[-1]
        