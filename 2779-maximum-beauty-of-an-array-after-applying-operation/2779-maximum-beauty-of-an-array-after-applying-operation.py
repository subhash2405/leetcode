class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxc = 0
        start = 0
        end = 0
        while end<len(nums):
            if nums[end]-nums[start]<=2*k:
                end+=1
            else:
                maxc = max(maxc, end-start)
                start+=1
        maxc = max(maxc, end-start)
        return maxc