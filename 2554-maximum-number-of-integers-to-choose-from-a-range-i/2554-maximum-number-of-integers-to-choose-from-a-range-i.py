class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        nums = set(banned)
        count = 0
        add = 0
        for i in range(1, n+1):
            if i not in nums and add+i<=maxSum:
                count+=1
                add+=i
        return count