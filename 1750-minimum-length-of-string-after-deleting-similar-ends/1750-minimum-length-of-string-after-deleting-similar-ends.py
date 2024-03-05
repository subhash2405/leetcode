class Solution:
    def minimumLength(self, s: str) -> int:
        start = 0
        end = len(s) - 1

        while start < end and s[start] == s[end]:
            char = s[start]
            while start <= end and s[start] == char:
                start += 1
            while end >= start and s[end] == char:
                end -= 1

        return end - start + 1
