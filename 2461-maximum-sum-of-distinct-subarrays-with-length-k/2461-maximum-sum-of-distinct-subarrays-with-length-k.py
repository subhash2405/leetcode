from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        dic = {}
        res = 0
        temp = 0
        
        for end in range(len(nums)):
            # Add current element to the window
            temp += nums[end]
            dic[nums[end]] = dic.get(nums[end], 0) + 1
            
            # Shrink window if size exceeds k
            if end - start + 1 > k:
                temp -= nums[start]
                dic[nums[start]] -= 1
                if dic[nums[start]] == 0:
                    del dic[nums[start]]
                start += 1
            
            # Check if current window is valid and update result
            if end - start + 1 == k and len(dic) == k:
                res = max(res, temp)
        
        return res
