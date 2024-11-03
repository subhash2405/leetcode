class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            var = s[i:] + s[:i]
            if var == goal:
                return True

        return False