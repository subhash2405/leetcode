class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(i+1):
                substr = s[j:i+1]
                if substr == substr[::-1]:
                    count += 1
        return count
