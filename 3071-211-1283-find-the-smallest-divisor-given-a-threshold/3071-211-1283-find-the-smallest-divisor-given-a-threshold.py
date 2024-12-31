class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        while low<=high:
            mid = (low+high)//2
            ans = sum(ceil(num/mid) for num in nums)
            if ans>threshold:
                low = mid+1
            
            if ans<=threshold:
                high = mid-1
        return low