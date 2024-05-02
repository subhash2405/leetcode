class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        arr = s[0:k]
        count = 0
        for j in range(0, k):
            if arr[j]=='a' or arr[j]=='e' or arr[j]=='i' or arr[j]=='o' or arr[j]=='u':
                count += 1
        prev = count
        for i in range(1, len(s)-k+1):
            if s[i-1]=='a' or s[i-1]=='e' or s[i-1]=='i' or s[i-1]=='o' or s[i-1]=='u':
                count -= 1
            if s[i+k-1]=='a' or s[i+k-1]=='e' or s[i+k-1]=='i' or s[i+k-1]=='o' or s[i+k-1]=='u':
                count += 1
            prev = max(count, prev)
        return prev
