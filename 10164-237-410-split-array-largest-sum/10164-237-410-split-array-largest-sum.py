class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)


        while low<=high:
            mid= (low+high)//2
            a, curr = 1,0
            for i in nums:
                curr+=i
                if curr>mid:
                    a+=1
                    curr = i
            if a>k:
                low = mid+1
            else:
                high = mid-1
        return low