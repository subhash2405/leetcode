class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        arr = Counter(nums)
        op = 0
        for num in nums:
            complement = k - num
            if complement in arr:
                if complement != num and arr[complement] > 0 and arr[num] > 0:
                    op += 1
                    arr[complement] -= 1
                    arr[num] -= 1
                elif complement == num and arr[num] > 1:  
                    op += 1
                    arr[num] -= 2
        return op