class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count1, count2 = 0, 0
        for i in range(len(s)//2):
            if s[i] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                count1 += 1
        
        for i in range(len(s)//2, len(s)):
            if s[i] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                count2 += 1
        
        return count1 == count2