class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        majority_element = max(count, key=count.get)
        return majority_element
