class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.dic = {}

        def check(start, curr):
            if curr==len(s):
                if s[start:curr] in wordDict:
                    return True
                return False
            
            if (start, curr) in self.dic:
                return self.dic[(start, curr)]
            
            a = False
            if s[start:curr] in wordDict:
                a = check(curr,curr+1)
            b = check(start, curr+1)

            self.dic[(start, curr)] = a or b

            return a or b
        
        return check(0,0)
