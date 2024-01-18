class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        a = sum(nums[0:k])
        max_average = a / k
        pop = 0

        for i in range(k, len(nums)):
            a = a + nums[i] - nums[pop]
            max_average = max(max_average, a / k)
            pop += 1

        return max_average
