class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        arr = Counter(nums)
        set1 = list(set(nums))
        res = [num for num in set1 if arr[num] == 1]
        return res
