class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        print(sum(nums))
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                arr.append(current_sum)
        
        arr.sort()
        
        return (sum(arr[left-1:right]))%(10**9+7)