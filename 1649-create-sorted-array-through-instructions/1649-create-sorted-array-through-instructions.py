class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        count = 0
        nums = []

        def binsearch(nums, num):
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] < num:
                    low = mid + 1
                else:
                    high = mid
            return low

        for num in instructions:
            left = binsearch(nums, num)  # Number of elements smaller than `num`
            right = len(nums) - binsearch(nums, num + 1)  # Number of elements greater than `num`

            count = (count + min(left, right)) % MOD

            nums.insert(left, num)

        return count
