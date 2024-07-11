class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res=0
        j=0
        i=0
        while i < len(g) and len(s)>j: 
            if s[j]>=g[i]:
                i+=1
                res+=1
            j+=1
        return res
            

        