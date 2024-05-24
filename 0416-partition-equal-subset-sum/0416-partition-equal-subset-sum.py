class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0:
            return False
        half = total/2
        sums = set()
        for n in nums:
            if n == half:
                return True
            for k in sums.copy():
                if k+n<half:
                    sums.add(k+n)
                if k+n == half:
                    return True
            sums.add(n)
        return False