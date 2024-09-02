class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        left = k%total
        for i in range(len(chalk)):
            if chalk[i]>left:
                return i
            left-=chalk[i]