class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=count=0
        for letter in s:
            if letter==' ' and count!=0:
                res=count
                count=0
            elif letter!=' ':
                count+=1
        return res if count==0 else count
        