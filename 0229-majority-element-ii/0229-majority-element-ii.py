class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)/3
        arr = []
        nums1 = list(set(nums))
        for i in range(len(nums1)):
            if count[nums1[i]]>n:
                arr.append(nums1[i])
        return arr