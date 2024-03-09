class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # arr1=Counter(nums1)
        # arr2=Counter(nums2)
        # lis2=set(arr2.keys())
        # lis1=list(arr1.keys())
        # n=min(len(lis1),len(lis2))
        # for i in range(n):
        #     if lis1[i] in lis2:
        #         return lis1[i]
        # return -1
        a=b=0
        while a<len(nums1) and b<len(nums2):
            if nums1[a]==nums2[b]:
                return nums1[a]
            elif nums1[a]>nums2[b]:
                b+=1
            else:
                a+=1
        return -1
        