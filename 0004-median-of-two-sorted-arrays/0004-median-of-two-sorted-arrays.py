class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        i, j = 0, 0
    
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        if len(merged) % 2 == 0:
            mid = len(merged) // 2
            return (merged[mid - 1] + merged[mid]) / 2.0
        
        return merged[len(merged)//2]