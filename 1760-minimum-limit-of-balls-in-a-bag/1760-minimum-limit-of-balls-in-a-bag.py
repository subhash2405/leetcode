class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low = 1
        high = max(nums)
        while low<=high:
            mid = (low+high)//2
            numop = 0
            for i in nums:
                numop+=((i-1)//mid)
            if numop>maxOperations:
                low = mid+1
            else:
                high = mid-1

        return low
